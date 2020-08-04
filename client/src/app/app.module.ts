import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { ChartViewComponent } from './chart-view/chart-view.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NbThemeModule, NbLayoutModule, NbInputModule, NbButtonModule, NbSelectModule, NbSidebarModule, NbTabsetModule, NbSpinnerModule, NbCardModule, NbToastrModule, NbIconModule, NbAlertModule, NbCheckboxModule } from '@nebular/theme';
import { NbEvaIconsModule } from '@nebular/eva-icons';
import { ReactiveFormsModule } from '@angular/forms';
import { ChartFormComponent } from './chart-form/chart-form.component';
import { ChartDataComponent, SelectedByAxisDirective } from './chart-data/chart-data.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';

@NgModule({
    declarations: [
        AppComponent,
        ChartFormComponent,
        ChartViewComponent,
        ChartDataComponent,
        SelectedByAxisDirective
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        BrowserAnimationsModule,
        ReactiveFormsModule,


        NbThemeModule.forRoot({ name: 'default' }),
        NbLayoutModule,
        NbEvaIconsModule,
        NbIconModule,
        NbInputModule,
        NbButtonModule,
        NbSelectModule,
        NbSidebarModule.forRoot(),
        NbTabsetModule,
        NbSpinnerModule,
        NbCardModule,
        NbToastrModule.forRoot(),
        NbAlertModule,
        MatTableModule,
        MatPaginatorModule,
        MatSortModule,
        NbCheckboxModule,
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
