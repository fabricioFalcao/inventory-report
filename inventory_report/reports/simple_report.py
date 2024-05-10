from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport(Report):
    def __init__(self) -> None:
        self._inventories = []
        self._oldest_manufacturing_date = None
        self._closest_expiration_date = None
        self._stocked_products_by_company = None
        self._largest_company_inventory = None

    def add_inventory(self, inventory: Inventory) -> None:
        self._inventories.append(inventory)

    def report_data(self) -> None:
        today = datetime.today().date()
        oldest_manufacturing_date = today
        closest_expiration_date = datetime(year=3000, month=1, day=1).date()
        company_inventory = {}

        for inventory in self._inventories:
            for product in inventory.data:
                manufacturing_date = datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                ).date()
                expiration_date = datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                ).date()

                if product.company_name not in company_inventory:
                    company_inventory[product.company_name] = 1
                else:
                    company_inventory[product.company_name] += 1

                if manufacturing_date < oldest_manufacturing_date:
                    oldest_manufacturing_date = manufacturing_date

                if (
                    expiration_date > today
                    and expiration_date < closest_expiration_date
                ):
                    closest_expiration_date = expiration_date

        self._oldest_manufacturing_date = oldest_manufacturing_date.strftime(
            "%Y-%m-%d"
        )
        self._closest_expiration_date = closest_expiration_date.strftime(
            "%Y-%m-%d"
        )
        self._stocked_products_by_company = company_inventory
        self._largest_company_inventory = max(
            company_inventory.items(), key=lambda x: x[1]
        )[0]

    def generate(self) -> str:
        self.report_data()
        return (
            f"Oldest manufacturing date: {self._oldest_manufacturing_date}\n"
            f"Closest expiration date: {self._closest_expiration_date}\n"
            f"Company with the largest inventory: {self._largest_company_inventory}\n"
        )
