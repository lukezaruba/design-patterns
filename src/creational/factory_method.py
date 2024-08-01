from abc import ABC, abstractmethod


# Product Class
class DataSourceProduct(ABC):
    @abstractmethod
    def read_data(self):
        pass


# Concrete Product Classes
class ShapefileProduct(DataSourceProduct):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        return "Reading in Shapefile"


class GeoJSONProduct(DataSourceProduct):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        return "Reading in GeoJSON"


# Creator Class
class DataSourceCreator(ABC):
    @abstractmethod
    def factory_method(self) -> DataSourceProduct:
        pass

    def read_data(self):
        data_source = self.factory_method()
        return data_source.read_data()


# Concrete Creator Classes
class ShapefileCreator(DataSourceCreator):
    def __init__(self, file_path):
        self.file_path = file_path

    def factory_method(self) -> DataSourceProduct:
        return ShapefileProduct(self.file_path)


class GeoJSONCreator(DataSourceCreator):
    def __init__(self, file_path):
        self.file_path = file_path

    def factory_method(self) -> DataSourceProduct:
        return GeoJSONProduct(self.file_path)


# Client Code
def client_code(creator: DataSourceCreator) -> None:
    data = creator.read_data()
    print(f"Data: {data}")


if __name__ == "__main__":
    print("Using ShapefileCreator.")
    client_code(ShapefileCreator(file_path="path/to/shapefile.shp"))

    print("Using GeoJSONCreator.")
    client_code(GeoJSONCreator(file_path="path/to/data.geojson"))
