## Requerimientos
* python >=3.7

## Ejecución
1. Instalar dependencias mediante `pip3 install -r requirements.txt`.
2. Ejecutar programa mediante `python3 main.py <ARGUMENTOS>`.

```bash
$ python3 main.py --help
usage: main.py [-h] --x-axis X_AXIS [X_AXIS ...] --y-axis Y_AXIS [Y_AXIS ...] [--x-select [X_SELECT [X_SELECT ...]]]
               [--y-select [Y_SELECT [Y_SELECT ...]]] [--data DATA] [--chart-type {bar,line,scatter,violin,histogram,box}]
               [--chart-name CHART_NAME] [--chart-file-name CHART_FILE_NAME] [--as-json] [--group-by GROUP_BY]
               [--group-by-func {sum,max,min,prod,first,last}]

optional arguments:
  -h, --help                                            show this help message and exit
  --x-axis X_AXIS [X_AXIS ...]                          Chart X axis
  --y-axis Y_AXIS [Y_AXIS ...]                          Chart Y axis
  --x-select [X_SELECT [X_SELECT ...]]                  x axis data values ​​selected for rendering
  --y-select [Y_SELECT [Y_SELECT ...]]                  y axis data values ​​selected for rendering
  --data DATA                                           Url or path of file with data. Only formats csv and json
  --chart-type {bar,line,scatter,violin,histogram,box}  Chart type
  --chart-name CHART_NAME                               Chart name
  --chart-file-name CHART_FILE_NAME                     Chart file name
  --as-json                                             Print result as json
  --group-by GROUP_BY                                   Print result as json
  --group-by-func {sum,max,min,prod,first,last}         Grouping function
```

Ejemplo:
```
$ python3 main.py --url http://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-06-2020.csv --x-axis Province_State --y-axis Confirmed --chart-type line
```