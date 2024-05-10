from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport(Report):
    def __init__(self) -> None:
        self.__inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.__inventories.append(inventory)

    def generate(self) -> str:
        today = datetime.today().date()
        oldest_manufacturing_date = today
        closest_expiration_date = datetime(year=3000, month=1, day=1).date()
        largest_company_inventory = {}

        for inventory in self.__inventories:
            for product in inventory.data:
                manufacturing_date = datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                ).date()
                expiration_date = datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                ).date()

                if product.company_name not in largest_company_inventory:
                    largest_company_inventory[product.company_name] = 1
                else:
                    largest_company_inventory[product.company_name] += 1

                if manufacturing_date < oldest_manufacturing_date:
                    oldest_manufacturing_date = manufacturing_date

                if (
                    expiration_date > today
                    and expiration_date < closest_expiration_date
                ):
                    closest_expiration_date = expiration_date

        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date.strftime('%Y-%m-%d')}\n"
            f"Closest expiration date: {closest_expiration_date.strftime('%Y-%m-%d')}\n"
            f"Company with the largest inventory: {max(largest_company_inventory.items(), key=lambda x: x[1])[0]}\n"
        )
