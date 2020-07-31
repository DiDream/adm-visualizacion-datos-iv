import { Injectable } from '@nestjs/common';
import { spawn } from 'child_process';
import { ConfigService } from '@nestjs/config';

export interface IChartArguments {
    url: string,
    xAxis: string[],
    xSelect: string[],
    yAxis: string[],
    ySelect: string[],
    chartType: string,
    groupByFunction: string,
    groupBy: string,
    dataBase64: {
        filename: string,
        filetype: string
        value: string
    }
}

export interface IChartOutput {
    imageBase64: string,
    sourceData: {
        data: { [key: string]: any }[],
        schema: {
            fields: string[],
            pandas_version: string,
            primaryKey: string[]
        }
    }
}

const UTF_8 = 'utf-8';

@Injectable()
export class ChartService {
    constructor(
        private readonly configService: ConfigService
    ) { }

    public async getChart(chartArguments: IChartArguments) {
        const programArguments = [
            this.configService.get('SCRIPT_PATH'),
            '--as-json',
            '--x-axis', ...chartArguments.xAxis,
            '--y-axis', ...chartArguments.yAxis,
            '--chart-type', chartArguments.chartType,
            ...(chartArguments.url ? ['--data', chartArguments.url] : []),
            ...(chartArguments.groupByFunction ? ['--group-by-func', chartArguments.groupByFunction] : []),
            ...(chartArguments.groupBy ? ['--group-by', chartArguments.groupBy] : []),
            ...(chartArguments.xSelect ? ['--x-select', ...chartArguments.xSelect ] : []),
            ...(chartArguments.ySelect ? ['--y-select', ...chartArguments.ySelect ] : []),
        ];

        return new Promise((resolve, reject) => {
            const chartGenerator = spawn(this.configService.get('PYTHON_COMMAND') || 'python3', programArguments);

            if (chartArguments.dataBase64) {
                const buffer = Buffer.from(chartArguments.dataBase64.value, 'base64');
                chartGenerator.stdin.setDefaultEncoding(UTF_8)
                chartGenerator.stdin.write(buffer.toString(UTF_8));
                chartGenerator.stdin.end();
            }

            let dataResultBuffer = '';
            let errorBuffer = '';

            chartGenerator.stdout.on('data', data => {
                dataResultBuffer += data.toString();
            })

            chartGenerator.on('close', (code) => {
                if (code != 0) {
                    return reject(new Error(errorBuffer || 'Error durante la ejecución del script'));
                }
                try {
                    const dataResult: IChartOutput = JSON.parse(dataResultBuffer)
                    resolve(dataResult);
                }
                catch (err) {
                    reject(err)
                }
            });

            chartGenerator.stderr.on('data', (data) => {
                errorBuffer += data.toString();
            });

            chartGenerator.on('error', (err) => {
                reject(err);
            });
        })
        .catch(err => {
            console.log(`Program arguments ${new Date().toISOString()}:`, programArguments.join(' '));
            console.log(`Program error:`, err);
            throw err;
        })

    }
}