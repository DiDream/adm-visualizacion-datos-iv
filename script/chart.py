import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd


class ADMChart:
    def __init__(self, x_axis_name, y_axis_name, data):
        self.x_axis_name = x_axis_name if len(x_axis_name) > 1 else x_axis_name[0]
        if isinstance(y_axis_name, list) and len(y_axis_name) > 0:
            self.y_axis_name = y_axis_name if len(y_axis_name) > 1 else y_axis_name[0]
        self.data = data

    def get_axis_size(self):
        if isinstance(self.x_axis_name, list):
            return len(self.x_axis_name)
        else:
            return len(self.data[self.x_axis_name])

    def get_figure_width(self):
        x_axis_size = self.get_axis_size()
        figure_width = x_axis_size * 0.15
        if figure_width < 5:
            figure_width = 5
        elif figure_width > 25:
            figure_width = 25
        return figure_width

    def generate_chart(self, chart_name):
        x_axis_size = self.get_axis_size()
        figure_width = self.get_figure_width()

        chart = plt.figure(figsize=(figure_width, 5))

        # Ancho adaptable al contenido -> https://stackoverflow.com/a/54756766
        axes_left = 1 / figure_width
        axes = chart.add_axes([axes_left, 0.15, 0.98 - axes_left, 0.75])
        axes.set_title(chart_name)
        axes.grid()
        axes.tick_params(axis='x', which='major', labelsize=8.5)
        axes.tick_params(axis='x', labelrotation=90)
        axes.margins(x=(1 / x_axis_size))

        self.set_type_chart(axes)

        if isinstance(self.x_axis_name, list) or isinstance(self.y_axis_name, list):
            chart.legend()

        return chart

    def set_type_chart(self, axes):
        pass


class LineChart(ADMChart):
    def set_type_chart(self, axes):
        if isinstance(self.x_axis_name, list):
            for index, row in self.data.iterrows():
                axes.plot(row[self.x_axis_name], label=row[self.y_axis_name])
        elif isinstance(self.y_axis_name, list):
            axes.set_xlabel(self.x_axis_name)
            for name in self.y_axis_name:
                axes.plot(self.data[self.x_axis_name], self.data[name], label=name)
        else:
            axes.set_xlabel(self.x_axis_name)
            axes.set_ylabel(self.y_axis_name)
            axes.plot(self.data[self.x_axis_name], self.data[self.y_axis_name])


class BarChart(ADMChart):

    def generate_chart(self, chart_name):
        figure_width = self.get_figure_width()
        fig = plt.figure(figsize=(figure_width, 5))
        fig.suptitle(chart_name)

        # https://stackoverflow.com/a/49505519
        if isinstance(self.x_axis_name, list):
            data = self.data.melt(self.y_axis_name, value_vars=self.x_axis_name, var_name='__a', value_name='__b')
            ax = sns.barplot(x='__a', y='__b', hue=self.y_axis_name, data=data)
            ax.set_ylabel('')
            ax.set_xlabel('')
        elif isinstance(self.y_axis_name, list):
            data = self.data.melt(self.x_axis_name, value_vars=self.y_axis_name, var_name='__a', value_name='__b')
            ax = sns.barplot(x=self.x_axis_name, y='__b', hue='__a', data=data)
            ax.legend().set_title('')
            ax.set_ylabel('')
        else:
            ax = sns.barplot(x=self.x_axis_name, y=self.y_axis_name, data=self.data)

        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=8.5)
        return fig


class ScatterChart(ADMChart):
    def __init__(self, x_axis_name, y_axis_name, data):
        super().__init__(x_axis_name, y_axis_name, data)
        self.x_axis_name = self.x_axis_name[0] if isinstance(self.x_axis_name, list) else self.x_axis_name
        self.y_axis_name = self.y_axis_name[0] if isinstance(self.y_axis_name, list) else self.y_axis_name

    def set_type_chart(self, axes):
        axes.set_xlabel(self.x_axis_name)
        axes.set_ylabel(self.y_axis_name)
        axes.scatter(self.data[self.x_axis_name], self.data[self.y_axis_name])

    def get_axis_size(self):
        return 5/0.15


class ViolinChart(ADMChart):
    def __init__(self, x_axis_name, y_axis_name, data):
        super().__init__(x_axis_name, y_axis_name, data)
        self.x_axis_name = self.x_axis_name[0] if isinstance(self.x_axis_name, list) else self.x_axis_name
        self.y_axis_name = self.y_axis_name[0] if isinstance(self.y_axis_name, list) else self.y_axis_name

    def generate_chart(self, chart_name):
        fig = plt.figure()
        fig.suptitle(chart_name)

        ax = sns.violinplot(x=self.data[self.x_axis_name], y=self.data[self.y_axis_name])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
        return fig


# No es necesario --y-axis
class HistogramChart(ADMChart):
    def generate_chart(self, chart_name):
        fig = plt.figure()

        fig.suptitle(chart_name)

        # Disable Kernel density estimation -> https://stackoverflow.com/a/57802471
        sns.distplot(self.data[self.x_axis_name], kde=True)

        return fig


class BoxPlotChart(ADMChart):
    def __init__(self, x_axis_name, y_axis_name, data):
        super().__init__(x_axis_name, y_axis_name, data)
        self.x_axis_name = self.x_axis_name[0] if isinstance(self.x_axis_name, list) else self.x_axis_name
        self.y_axis_name = self.y_axis_name[0] if isinstance(self.y_axis_name, list) else self.y_axis_name

    def generate_chart(self, chart_name):
        fig = plt.figure()
        fig.suptitle(chart_name)

        ax = sns.boxplot(x=self.data[self.x_axis_name], y=self.data[self.y_axis_name])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
        return fig


class MapChart(ADMChart):
    def __init__(self, x_axis_name, y_axis_name, data):
        super().__init__(x_axis_name, y_axis_name, data)
        self.x_axis_name = self.x_axis_name[0] if isinstance(self.x_axis_name, list) else self.x_axis_name

    # Ejemplo de http://www.geomapik.com/desarrollo-programacion-gis/mapas-con-python-geopandas-matplotlib/
    def generate_chart(self, chart_name):
        map_data = self.data

        # Control del tamaño de la figura del mapa
        fig, ax = plt.subplots(figsize=(10, 10))

        # Control del encuadre (área geográfica) del mapa
        # ax.axis([-12, 5, 32, 48])

        # Control del título y los ejes
        ax.set_title(chart_name, pad=20, fontdict={'fontsize': 20, 'color': '#4873ab'})

        ax.set_xlabel('Lon')
        ax.set_ylabel('Lat')

        # Añadir la leyenda separada del mapa
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.2)

        # Generar y cargar el mapa
        map_data.plot(column=self.x_axis_name, cmap='plasma', ax=ax, legend=True, cax=cax, zorder=5)

        # Cargar un mapa base con contornos de países
        # https://www.naturalearthdata.com/downloads/50m-physical-vectors/50m-ocean/
        # map_ocean = gpd.read_file('./assets/ne_50m_ocean.shp')
        # map_ocean.plot(ax=ax, color='#89c0e8', zorder=0)

        return fig


chart_constructors = {
    'bar': BarChart,
    'line': LineChart,
    'scatter': ScatterChart,
    'violin': ViolinChart,
    'histogram': HistogramChart,
    'box': BoxPlotChart,
    'map': MapChart
}