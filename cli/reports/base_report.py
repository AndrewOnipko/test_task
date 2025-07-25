from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self, logs: list[dict]) -> list[list]:
        """Принимает список логов, возвращает данные для таблиц."""
        
        ...


    @abstractmethod
    def headers(self) -> list[str]:
        """Заголовки для таблицы"""
        
        ...