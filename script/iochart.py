#!/usr/bin/env python3

import argparse
import sys

import urllib

import lib.data_source as data_sources
from lib.chart import chart_constructors
from lib.learning import learning_constructors
from lib.custom_error import CustomError

group_by_functions = {
    'sum': lambda series_group_by: series_group_by.sum(),
    'max': lambda series_group_by: series_group_by.max(numeric_only=True),
    'min': lambda series_group_by: series_group_by.min(numeric_only=True),
    'prod': lambda series_group_by: series_group_by.prod(),
    'first': lambda series_group_by: series_group_by.first(),
    'last': lambda series_group_by: series_group_by.last(),
}


# multilevel argparse -> https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html
class IOChart:
    def __init__(self):
        parser = argparse.ArgumentParser(
            formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=130)
        )
        parser.add_argument('command', help='Subcommand to run', choices=['chart', 'learn'])

        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def get_data(self, args):
        if args.data is not None:
            data_source_input = data_sources.UrlDataSourceInput(args.data)
        elif not sys.stdin.isatty():
            data_source_input = data_sources.StdinDataSourceInput(sys.stdin.read())
        else:
            raise CustomError('Especifique el contenido de los datos mediante el argumento --data o < NOMBRE FICHERO')

        try:
            data_source = data_sources.DataSource.get_instance(data_source_input)
            return data_source.get_data()
        except FileNotFoundError:
            raise CustomError('No se ha encontrado el fichero especificado')
        except urllib.error.HTTPError:
            raise CustomError('Datos no encontrados mediante URL')

    def get_subprog(self):
        return '{} {}'.format(sys.argv[0], sys.argv[1])

    def chart(self):
        parser = argparse.ArgumentParser(
            prog=self.get_subprog(),
            description='Generate chart',
            formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=130)
        )

        parser.add_argument('-x', '--x-axis', help='Chart X axis', nargs='+', type=str, required=True)
        parser.add_argument('-y', '--y-axis', help='Chart Y axis', nargs='*', type=str, default=[])
        parser.add_argument(
            '--x-select',
            help='x axis data values ​​selected for rendering',
            nargs='*',
            type=str
        )
        parser.add_argument(
            '--y-select',
            help='y axis data values ​​selected for rendering',
            nargs='*',
            type=str
        )
        parser.add_argument('--data', help='Url or path of file with data. Formats csv and json supported')
        parser.add_argument('--chart-type', help='Chart type', choices=list(chart_constructors.keys()))
        parser.add_argument('--chart-name', help='Chart name')
        parser.add_argument('--chart-file-name', help='Chart file name', default='chart')
        parser.add_argument('--group-by', help='Field name to group')
        parser.add_argument('--group-by-func', help='Grouping function', choices=list(group_by_functions.keys()),
                            default="sum")

        parser.add_argument('--as-json', default=False, action='store_true', help='Print result as json')

        args = parser.parse_args(sys.argv[2:])

        if args.chart_type is not None and args.chart_type != 'histogram' and args.chart_type != 'map' and args.y_axis is None:
            raise CustomError('Debe especificar al menos un campo asociado al eje Y')

        data = self.get_data(args)

        # Se comprueba si los campos seleccionados para los ejes están presentes en el header del csv
        x_axis_name = args.x_axis
        y_axis_name = args.y_axis

        if len(x_axis_name) > 1 and len(y_axis_name) > 1:
            raise CustomError('Sólo puede especificar múltiples campos para un eje')

        for name in x_axis_name:
            if name not in data.columns:
                raise CustomError('Seleccione un valor del listado para X axis: {}'.format(data.columns.to_list()))

        for name in y_axis_name:
            if name not in data.columns:
                raise CustomError('Seleccione un valor del listado para Y axis: {}'.format(data.columns.to_list()))

        # BEGIN Agrupación de los datos
        group_by = None
        if args.chart_type == 'scatter':
            group_by = args.group_by
        elif args.chart_type == 'line' or args.chart_type == 'bar':
            group_by = x_axis_name[0]
            if len(x_axis_name) > 1:
                group_by = y_axis_name[0]

        if group_by is not None:
            data = group_by_functions[args.group_by_func](data.groupby(group_by, as_index=False))
        # END Agrupación de los datos

        # BEGIN select specific values
        if args.x_select is not None:
            data = data[data[x_axis_name[0]].isin(args.x_select)]

        if args.y_select is not None:
            data = data[data[y_axis_name[0]].isin(args.y_select)]
        # END select specific values

        chart_constructor = chart_constructors.get(args.chart_type)
        chart = chart_constructor(x_axis_name, y_axis_name, data)
        chart.output(args)

    def learn(self):
        parser = argparse.ArgumentParser(
            prog=self.get_subprog(),
            description='Apply learning algorithms',
            formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=130)
        )
        parser.add_argument('-x', help='x data', nargs='*', type=str)
        parser.add_argument('-y', help='y data', type=str)
        parser.add_argument('-d', '--data', help='Url or path of file with data. Formats csv and json supported')
        parser.add_argument(
            '-a',
            '--algorithm',
            help='Learning algorithm',
            choices=list(learning_constructors.keys()),
            required=True
        )
        parser.add_argument('--n-clusters', help='Number of clusters', type=int, default=2)
        parser.add_argument('--test-size', help='Test size from data. Ex: 0.2', type=float, default=0.2)
        parser.add_argument('--max-depth', help='Max depth for tree algorithms', type=int, default=4)
        parser.add_argument('--as-json', default=False, action='store_true', help='Print result as json')

        args = parser.parse_args(sys.argv[2:])
        data = self.get_data(args)

        learning_constructor = learning_constructors.get(args.algorithm)
        algorithm = learning_constructor(data=data, x=args.x, y=args.y, args=args)
        algorithm.run()


try:
    IOChart()
except CustomError as e:
    print(e, file=sys.stderr, end='')
