from typing import Optional, List
from inventory_report.product import Product

class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        self.__data = [] if data is None else data

    @property
    def data(self) -> List[Product]:
        return self.__data
    
    def add_data (self, data: List[Product]) -> None:
        self.__data.extend(data)