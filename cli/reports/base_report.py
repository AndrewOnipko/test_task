from abc import ABC, abstractmethod
from typing import List

class Report(ABC):

    @abstractmethod
    def generate(self, logs: List[dict]) -> List[List]:
        """Принимает список логов, возвращает данные для таблиц."""
        
        ...