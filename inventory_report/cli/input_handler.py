from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    data = []
    for file_path in file_paths:
        if file_path.endswith(".json"):
            data.extend(JsonImporter(file_path).import_data())
        elif file_path.endswith(".csv"):
            data.extend(CsvImporter(file_path).import_data())

    inventory = Inventory(data)

    if report_type == "simple":
        report = SimpleReport()
        report.add_inventory(inventory)
        return report.generate()
    elif report_type == "complete":
        report = CompleteReport()
        report.add_inventory(inventory)
        return report.generate()
    else:
        raise ValueError("Report type is invalid.")
