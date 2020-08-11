## Requerimientos
* python >=3.7

## Consideraciones previas
* Instalar dependencias mediante `pip3 install -r requirements.txt`.

## Ejecución
El programa `iochart.py` tiene dos subcomandos asociados, los cuales se pueden listar mediante:

```bash
$ python3 iochart.py --help
usage: iochart.py [-h] {chart,learn}

positional arguments:
  {chart,learn}  Subcommand to run

optional arguments:
  -h, --help     show this help message and exit

```

#### Generación de gráficas

```bash
$ python3 iochart.py chart --help
usage: ./iochart.py chart [-h] -x X_AXIS [X_AXIS ...] [-y [Y_AXIS [Y_AXIS ...]]] [--x-select [X_SELECT [X_SELECT ...]]]
                          [--y-select [Y_SELECT [Y_SELECT ...]]] [--data DATA]
                          [--chart-type {bar,line,scatter,violin,histogram,box,map}] [--chart-name CHART_NAME]
                          [--chart-file-name CHART_FILE_NAME] [--group-by GROUP_BY]
                          [--group-by-func {sum,max,min,prod,first,last}] [--as-json]

Generate chart

optional arguments:
  -h, --help                                                show this help message and exit
  -x X_AXIS [X_AXIS ...], --x-axis X_AXIS [X_AXIS ...]      Chart X axis
  -y [Y_AXIS [Y_AXIS ...]], --y-axis [Y_AXIS [Y_AXIS ...]]  Chart Y axis
  --x-select [X_SELECT [X_SELECT ...]]                      x axis data values ​​selected for rendering
  --y-select [Y_SELECT [Y_SELECT ...]]                      y axis data values ​​selected for rendering
  --data DATA                                               Url or path of file with data. Formats csv and json supported
  --chart-type {bar,line,scatter,violin,histogram,box,map}  Chart type
  --chart-name CHART_NAME                                   Chart name
  --chart-file-name CHART_FILE_NAME                         Chart file name
  --group-by GROUP_BY                                       Field name to group
  --group-by-func {sum,max,min,prod,first,last}             Grouping function
  --as-json                                                 Print result as json
```

Ejemplo:

```
$ python3 iochart.py chart --url http://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-06-2020.csv --x-axis Province_State --y-axis Confirmed --chart-type line
```

#### Aplicar algoritmos de aprendizaje

```bash
$ python3 iochart.py learn --help
usage: iochart.py learn [-h] [-x [X [X ...]]] [-y Y] [-d DATA] -a {naive-bayes,tree-classifier,tree-regression,k-means}
                        [--n-clusters N_CLUSTERS] [--test-size TEST_SIZE] [--max-depth MAX_DEPTH] [--as-json]

Apply learning algorithms

optional arguments:
  -h, --help                                                                    show this help message and exit
  -x [X [X ...]]                                                                x data
  -y Y                                                                          y data
  -d DATA, --data DATA                                                          Url or path of file with data. Formats csv and
                                                                                json supported
  -a {naive-bayes,tree-classifier,tree-regression,k-means}, --algorithm {naive-bayes,tree-classifier,tree-regression,k-means}
                                                                                Learning algorithm
  --n-clusters N_CLUSTERS                                                       Number of clusters
  --test-size TEST_SIZE                                                         Test size from data. Ex: 0.2
  --max-depth MAX_DEPTH                                                         Max depth for tree algorithms
  --as-json                                                                     Print result as json
```