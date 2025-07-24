import json
from utils.logger import simple_logger

class LogParser:
    def __init__(self, logger, files: list[str], date: str | None = None):
        self.logger = logger
        self.files = files
        self.date = date


    @simple_logger
    def parse(self) -> list[dict]:
        """Читает все логи и возвращает список словарей, отфильтрованных по дате(если указана)"""

        logs = []
        for file_path in self.files:
            with open(file_path, 'r') as f:
                for line in f:
                    try:
                        entry = json.loads(line)
                        if self._matches_date(entry):
                            logs.append(entry)
                    except json.JSONDecodeError:
                        continue  
        return logs


    @simple_logger
    def _matches_date(self, entry: dict) -> bool:
        """Проверяет, совпадает ли дата"""

        if not self.date:
            return True
        try:
            ts = entry.get("@timestamp", "")
            return ts.startswith(self.date)
        except Exception:
            return False