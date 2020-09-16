import pandas as pd
from io import StringIO
import ssl
import geopandas as gpd


class DataSourceInput:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data


class UrlDataSourceInput(DataSourceInput):
    def __init__(self, url):
        # ERROR urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]
        #   certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)
        # SOLUCION https://stackoverflow.com/a/52172355
        ssl._create_default_https_context = ssl._create_unverified_context

        # Obtener csv directamente desde url -> https://stackoverflow.com/a/41880513
        super().__init__(url)


class StdinDataSourceInput(DataSourceInput):
    def __init__(self, stdin_read):
        super().__init__(StringIO(stdin_read))

    def get_data(self):
        self.data.seek(0)
        return self.data


class DataSource:
    def __init__(self, data_source_input: DataSourceInput):
        self.data_source_input = data_source_input

    @staticmethod
    def get_instance(data_source_input: DataSourceInput):
        data = data_source_input.get_data()

        if isinstance(data_source_input, UrlDataSourceInput):
            if data.endswith('.csv'):
                return CsvDataSource(data_source_input)
            elif data.endswith('.json'):
                return JsonDataSource(data_source_input)
            elif data.endswith('.geojson'):
                return GeojsonDataSource(data_source_input)
        try:
            pd.read_json(data)
            return JsonDataSource(data_source_input)
        except ValueError:
            pass

        try:
            pd.read_csv(data_source_input.get_data())
            return CsvDataSource(data_source_input)
        except (pd.errors.ParserError, pd.errors.EmptyDataError) as e:
            return GeojsonDataSource(data_source_input)


class JsonDataSource(DataSource):
    def get_data(self):
        data = self.data_source_input.get_data()
        return pd.read_json(data)


class CsvDataSource(DataSource):
    def get_data(self):
        data = self.data_source_input.get_data()
        return pd.read_csv(data)


class GeojsonDataSource(DataSource):
    def get_data(self):
        data = self.data_source_input.get_data()
        return gpd.read_file(data)
