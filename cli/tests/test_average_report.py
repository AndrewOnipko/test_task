import pytest
from reports.average_report import AverageReport

@pytest.fixture
def sample_logs():
    return [
        {"url": "/api/test", "response_time": 0.1},
        {"url": "/api/test", "response_time": 0.2},
        {"url": "/api/test", "response_time": 0.3},
        {"url": "/api/other", "response_time": 0.4},
    ]


def test_average_report_basic(sample_logs):
    """Проверяет корректность подсчета числа вызовов эндпоинта и среднее время"""
    report = AverageReport()
    result = report.generate(sample_logs)
    report_dict = {row[0]: (row[1], row[2]) for row in result}

    assert report_dict["/api/test"] == (3, 0.2)
    assert report_dict["/api/other"] == (1, 0.4)


def test_average_report_with_empty_logs():
    """Проверяет, что при пустом отчете скрипт не вылетит"""

    report = AverageReport()
    result = report.generate([])
    assert result == []


def test_average_report_with_missing_response_time():
    """Проверяет, что при отсутствующем response_time скрипт не вылетит и добавит только одну строку"""

    logs = [
        {"url": "/api/test"},
        {"url": "/api/test", "response_time": 0.3},
    ]
    report = AverageReport()
    result = report.generate(logs)
    assert result == [['/api/test', 2, 0.15]]
