from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        self.report_data()

        stocked_products_output = "\n".join(
            f"- {company}: {quantity}"
            for company, quantity in self._stocked_products_by_company.items()
        )

        return (
            f"Oldest manufacturing date: {self._oldest_manufacturing_date}\n"
            f"Closest expiration date: {self._closest_expiration_date}\n"
            f"Company with the largest inventory: {self._largest_company_inventory}\n"
            f"Stocked products by company:\n"
            f"{stocked_products_output}\n"
        )
