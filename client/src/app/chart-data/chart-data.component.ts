import { Component, ChangeDetectionStrategy, Input, ChangeDetectorRef, Directive, HostBinding, ViewChild } from "@angular/core";
import { IChartImportedData, IChartArguments } from '../core/chart.model';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';

@Directive({
    selector: '[selectedByAxis]'
})
export class SelectedByAxisDirective {
    @Input()
    public selectedByAxis: string;

    @HostBinding('class.x-axis-selected')
    protected xAxisSelected: boolean = false;

    @HostBinding('class.y-axis-selected')
    protected yAxisSelected: boolean = false;
    
    @Input()
    public set chartArguments(chartArguments: IChartArguments) {
        if (chartArguments) {
            this.xAxisSelected = chartArguments.xAxis.some(axisName => axisName == this.selectedByAxis);
            if (chartArguments.yAxis) {
                this.yAxisSelected = chartArguments.yAxis.some(axisName => axisName == this.selectedByAxis);
            }
        }
    }
}


@Component({
    selector: 'app-chart-data',
    templateUrl: './chart-data.component.html',
    styleUrls: ['./chart-data.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class ChartDataComponent {
    public arguments: IChartArguments;

    public displayedColumns: string[] = [];

    public dataSource: MatTableDataSource<any> = new MatTableDataSource();

    @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;
    @ViewChild(MatSort, {static: true}) sort: MatSort;

    @Input()
    public set chartArguments(chartArguments: IChartArguments) {
        this.arguments = chartArguments;
        this.cd.detectChanges();
    }

    constructor(private cd: ChangeDetectorRef) {}

    public renderData(data: IChartImportedData) {
        this.displayedColumns = data.headers;
        this.dataSource.data = data.rows;

        this.chartArguments = null;
        this.cd.detectChanges();
    }

    ngOnInit() {
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
    }
}