export interface IChartImportedData {
    headers: string[];
    rows: {[key: string]: string}[];
}

export enum ChartTypeEnum {
    LINE = 'line',
    BAR = 'bar',
    SCATTER = 'scatter',
    VIOLIN = 'violin',
    HISTOGRAM = 'histogram',
    BOX = 'box',
}

export const CHART_TYPES: {key: ChartTypeEnum, label: string}[] = [
    {
        key: ChartTypeEnum.LINE,
        label: 'Líneas'
    },
    {
        key: ChartTypeEnum.BAR,
        label: 'Barras'
    },
    {
        key: ChartTypeEnum.SCATTER,
        label: 'Dispersión'
    },
    {
        key: ChartTypeEnum.VIOLIN,
        label: 'Violin',
    },
    {
        key: ChartTypeEnum.HISTOGRAM,
        label: 'Histograma',
    },
    {
        key: ChartTypeEnum.BOX,
        label: 'Cajas y bigotes',
    },
];

export enum GroupByFunctionEnum {
    SUM = 'sum',
    MAX = 'max',
    MIN = 'min',
    PROD = 'prod',
    FIRST = 'first',
    LAST = 'last',
}

export const GROUP_BY_FUNCTIONS = [
    {
        key: GroupByFunctionEnum.SUM,
        label: 'Suma'
    },
    {
        key: GroupByFunctionEnum.MAX,
        label: 'Máximo'
    },
    {
        key: GroupByFunctionEnum.MIN,
        label: 'Mínimo'
    },
    {
        key: GroupByFunctionEnum.PROD,
        label: 'Producto'
    },
    {
        key: GroupByFunctionEnum.FIRST,
        label: 'Primera ocurrencia'
    },
    {
        key: GroupByFunctionEnum.LAST,
        label: 'Última ocurrencia'
    },
]




export interface IChartArguments {
    chartType: string,
    url: string,
    xAxis: string[],
    xSelect: string[],
    yAxis: string[],
    ySelect: string[],
    groupByFunction: string,
    dataBase64: {
        filename: string,
        filetype: string
        value: string
    }
}

export interface IChartOutput {
    imageBase64: string;
    sourceData: {
        data: {[key: string]: any}[],
        schema: {
            fields: string[],
            pandas_version: string,
            primaryKey: string[]
        }
    }
}