import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { IChartOutput, IChartArguments } from './chart.model';

@Injectable({
    providedIn: 'root'
})
export class ChartService {
    constructor(
        private http: HttpClient
    ) {}

    getChart(chartArguments: IChartArguments): Observable<{data: IChartOutput}> {
        return this.http.post<{data: IChartOutput}>('api/chart', chartArguments)
            .pipe(
                catchError((err: HttpErrorResponse) => throwError(err.error))
            )
    }
}