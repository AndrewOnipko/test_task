import logging
from utils.table_formatter import TableFormatter

def test_table_formatter_output_contains_expected_text():
    """Передает фиктивные данные и заголовки, проверяет, что результат содержит необходимые данные в нужном формате"""

    data = [
        ["/api/test", 3, 0.2],
        ["/api/other", 1, 0.4],
    ]
    headers = ["Endpoint", "Count", "Average Response Time"]
    logger = logging.getLogger("test")

    formatter = TableFormatter(logger)
    output = formatter.format(data, headers)

    assert "Endpoint" in output
    assert "/api/test" in output
    assert "0.4" in output
    assert "+" in output  
