import tempfile
import pytest
import logging
import os
from parser.log_parser import LogParser

@pytest.fixture
def logger():
    return logging.getLogger("test")


@pytest.fixture
def sample_log_file():
    content = """
{"@timestamp": "2025-06-22T10:00:00+00:00", "url": "/api/test", "response_time": 0.1}
{"@timestamp": "2025-06-22T11:00:00+00:00", "url": "/api/test", "response_time": 0.2}
{"@timestamp": "2025-06-23T12:00:00+00:00", "url": "/api/skip", "response_time": 0.3}
"""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".log", delete=False) as f:
        f.write(content.strip())
        f.flush()
        yield f.name
    os.remove(f.name)


@pytest.fixture
def temp_log_file():
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".log", delete=False) as f:
        yield f.name
    os.remove(f.name)



def test_log_parser_filters_by_date(logger, sample_log_file):
    """Проверяет корректность обработки логов с фильтром по дате, на выходе ожидаются две строки"""

    parser = LogParser(logger, [sample_log_file], date="2025-06-22")
    result = parser.parse()

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(log["url"] == "/api/test" for log in result)


def test_log_parser_without_date(logger, sample_log_file):
    """Проверяет корректность обработки без фильтра по дате, на выходе ожидаются три строки"""

    parser = LogParser(logger, [sample_log_file])
    result = parser.parse()

    assert len(result) == 3


def test_log_parser_skips_invalid_json(temp_log_file, logger):
    """Проверяет корректность except на JSONDecodeError"""

    with open(temp_log_file, "w", encoding="utf-8") as f:
        f.write('{"url": "/valid", "response_time": 0.1}\n')
        f.write('INVALID_JSON_LINE\n')  

    parser = LogParser(logger, [temp_log_file])
    logs = parser.parse()

    assert len(logs) == 1
    assert logs[0]["url"] == "/valid"


def test_log_parser_handles_invalid_timestamp(temp_log_file, logger):
    """Проверяет корректность отработки except Exception в _matches_date"""

    with open(temp_log_file, "w", encoding="utf-8") as f:
        f.write('{"@timestamp": null, "url": "/broken", "response_time": 0.1}\n')

    parser = LogParser(logger, [temp_log_file], date="2025-01-01")
    logs = parser.parse()

    assert logs == [] 