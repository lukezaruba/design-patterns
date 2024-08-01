from __future__ import annotations
from abc import ABC, abstractmethod


# Builder Class
class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_layer(self, layer_name: str) -> None:
        pass

    @abstractmethod
    def add_tag(self, tag: str) -> None:
        pass

    @abstractmethod
    def set_title(self, title: str) -> None:
        pass


# Concrete Builder Class
class ConcreteMapBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Map()

    @property
    def product(self) -> Map:
        product = self._product
        self.reset()
        return product

    def add_layer(self, layer_name: str) -> Builder:
        self._product.add_layer(layer_name)
        return self

    def add_tag(self, tag: str) -> Builder:
        self._product.add_tag(tag)
        return self

    def set_title(self, title: str) -> Builder:
        self._product.set_title(title)
        return self


# Map Class
class Map:
    def __init__(self) -> None:
        self.layers = []
        self.tags = []
        self.title = ""

    def add_layer(self, layer_name: str) -> None:
        self.layers.append(layer_name)

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)

    def set_title(self, title: str) -> None:
        self.title = title

    def list_config(self) -> None:
        print(f"Title: {self.title}, Layers: {self.layers}, Tags: {self.tags}")


# Director Class
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_basic_map(self) -> None:
        self.builder.add_layer("US_Roads")
        self.builder.add_layer("US_Buildings")
        self.builder.add_tag("infrastructure")
        self.builder.add_tag("united states")
        self.builder.set_title("U.S. Infrastructure Map")


# Examples
if __name__ == "__main__":
    # First example uses the director
    director = Director()
    builder = ConcreteMapBuilder()
    director.builder = builder

    print("Basic Map: ")
    director.build_basic_map()
    builder.product.list_config()

    # Second example uses the concrete builder itself
    print("Custom Map:")
    new_builder = ConcreteMapBuilder()

    # We can use method chaining
    new_builder.set_title("Minneapolis Parks & Census Tracts") \
        .add_layer("Minneapolis_Parks") \
        .add_layer("Minneapolis_Census_Tracts") \
        .add_tag("minneapolis")

    new_builder.product.list_config()
