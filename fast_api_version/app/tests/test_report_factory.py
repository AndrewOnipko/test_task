import pytest
from app.core.report_factory import get_report
from app.reports.average_report import AverageReport


def test_get_report_returns_correct_class():
    """Проверяет, что get_report("average") вернёт нужный класс"""

    report = get_report("average")

    assert isinstance(report, AverageReport)


def test_get_report_raises_for_unknown():
    """Проверяет, что при неправильном ключе - вылетает ValueError"""

    with pytest.raises(ValueError) as excinfo:
        get_report("unknown")

    assert "Неизвестный тип отчета" in str(excinfo.value)
