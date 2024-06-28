from abc import ABC, abstractmethod


# Abstract Base Factory
class GeometryFactory(ABC):
    """Abstract factory for creating geometries."""

    @abstractmethod
    def create_point(self):
        pass

    @abstractmethod
    def create_line(self):
        pass

    @abstractmethod
    def create_polygon(self):
        pass


# Concrete Factories - 2D and 3D
class TwoDimensionalFactory(GeometryFactory):

    def create_point(self):
        return TwoDimensionalPoint()

    def create_line(self):
        return TwoDimensionalLine()

    def create_polygon(self):
        return TwoDimensionalPolygon()


class ThreeDimensionalFactory(GeometryFactory):

    def create_point(self):
        return ThreeDimensionalPoint()

    def create_line(self):
        return ThreeDimensionalLine()

    def create_polygon(self):
        return ThreeDimensionalPolygon()


# Abstract Products
class AbstractPoint(ABC):
    """Abstract product for points"""

    @abstractmethod
    def wkt(self):
        pass


class AbstractLine(ABC):
    """Abstract product for lines"""

    @abstractmethod
    def wkt(self):
        pass

    @abstractmethod
    def length(self):
        pass


class AbstractPolygon(ABC):
    """Abstract product for polygons"""

    @abstractmethod
    def wkt(self):
        pass

    @abstractmethod
    def area(self):
        pass


# Concrete Products
class TwoDimensionalPoint(AbstractPoint):
    def wkt(self):
        print("WKT method for 2D Point.")


class TwoDimensionalLine(AbstractLine):
    def wkt(self):
        print("WKT method for 2D Line.")

    def length(self):
        print("Length method for 2D Line.")


class TwoDimensionalPolygon(AbstractPolygon):
    def wkt(self):
        print("WKT method for 2D Polygon.")

    def area(self):
        print("Area method for 2D Polygon.")


class ThreeDimensionalPoint(AbstractPoint):
    def wkt(self):
        print("WKT method for 3D Point.")


class ThreeDimensionalLine(AbstractLine):
    def wkt(self):
        print("WKT method for 3D Line.")

    def length(self):
        print("Length method for 3D Line.")


class ThreeDimensionalPolygon(AbstractPolygon):
    def wkt(self):
        print("WKT method for 3D Polygon.")

    def area(self):
        print("Area method for 3D Polygon.")


# Factory Mapping
factory_mapping = {
    "2D": TwoDimensionalFactory(),
    "3D": ThreeDimensionalFactory(),
}


# Factory Selection
def select_shape_dimensionality(dimensionality):
    # Retrieve factory
    factory = factory_mapping.get(dimensionality)

    # Handle invalid factory
    if factory is None:
        raise ValueError("Invalid provider")

    return factory


# Example usage
if __name__ == "__main__":
    # 2D Factory
    two_dimensional = select_shape_dimensionality("2D")

    print("Created 2D Factory")

    # Creating 2D Geometries
    point_2d = two_dimensional.create_point()
    line_2d = two_dimensional.create_line()
    polygon_2d = two_dimensional.create_polygon()

    print("Created 2D Geometries")

    # Running 2D Geometry Methods
    point_2d.wkt()

    line_2d.wkt()
    line_2d.length()

    polygon_2d.wkt()
    polygon_2d.area()

    print("Used 2D Geometry Methods\n")

    # 3D Factory
    three_dimensional = select_shape_dimensionality("3D")

    print("Created 3D Factory")

    # Creating 3D Geometries
    point_3d = three_dimensional.create_point()
    line_3d = three_dimensional.create_line()
    polygon_3d = three_dimensional.create_polygon()

    print("Created 3D Geometries")

    # Running 3D Geometry Methods
    point_3d.wkt()

    line_3d.wkt()
    line_3d.length()

    polygon_3d.wkt()
    polygon_3d.area()

    print("Used 3D Geometry Methods")
