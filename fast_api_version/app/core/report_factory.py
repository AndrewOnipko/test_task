from app.reports.average_report import AverageReport
from app.reports.base_report import Report

report_registry = {
    "average": AverageReport
}


def get_report(name: str) -> Report:
    report_class = report_registry.get(name)
    if not report_class:
        raise ValueError(f"Неизвестный тип отчета: {name}")
    return report_class()