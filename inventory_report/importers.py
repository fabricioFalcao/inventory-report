import json
import csv
from typing import Dict, Type
from abc import ABC, abstractmethod

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            return [Product(**product) for product in json.load(file)]


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(
            self.path,
            "r",
        ) as file:
            return [Product(**product) for product in csv.DictReader(file)]


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
