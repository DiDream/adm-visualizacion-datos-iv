import { Component, ViewChild, ElementRef } from '@angular/core';
import { ChartConstructors, ADMChart } from '../core/chart.lib';
import { IChartOutput, IChartArguments } from '../core/chart.model';

@Component({
    selector: 'app-chart-view',
    templateUrl: './chart-view.component.html'
})
export class ChartViewComponent {
    @ViewChild('chartCanvasRef', { read: ElementRef }) chartCanvasRef: ElementRef<HTMLCanvasElement>;

    private readonly base64Prefix: string = 'data:image/png;base64,';

    public chartBase64: string;

    public data: any;
    public csvFields: string[] = [];

    private chart: Chart;
    private chartContext: CanvasRenderingContext2D;

    ngAfterViewInit() {
        this.chartContext = this.chartCanvasRef.nativeElement.getContext('2d');
    }

    public renderChart({response, chartArguments}: {response: {data: IChartOutput}, chartArguments: IChartArguments}) {
        this.chartBase64 = `${this.base64Prefix}${response.data.imageBase64}`;

        // Initialize chart with chart.js
        const { chartType } = chartArguments;
        
        if (this.chart) {
            this.chart.clear();
            this.chart.destroy();
        }

        if (chartType in ChartConstructors) {
            const admChart: ADMChart = new ChartConstructors[chartType](this.chartContext, chartArguments, response.data);
            this.chart = admChart.build();
        }
    }
}