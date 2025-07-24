import subprocess
import sys
import os
import tempfile

def test_main_smoke():
    """Проверяет, что скрипт в целом запуститься и не вылетит при корректных аргументах"""

    content = """{"@timestamp": "2025-06-22T10:00:00+00:00", "url": "/api/test", "response_time": 0.1}"""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".log", delete=False) as f:
        f.write(content)
        f.flush()
        log_file_path = f.name

    result = subprocess.run(
        [sys.executable, "main.py", "--file", log_file_path, "--report", "average", "--date", "2025-06-22"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    os.remove(log_file_path)

    assert result.returncode == 0
    assert "/api/test" in result.stdout
    assert "Average Response Time" in result.stdout
