from collections import defaultdict
from reports.base_report import Report

class AverageReport(Report):
    def generate(self, logs: list[dict]) -> list[list]:
        """Генерирует отчёт, поочередно запуская приватные функции"""

        stats = self._aggregate(logs)
        return self._build_table(stats)


    def _aggregate(self, logs: list[dict]) -> dict:
        """Формирует отчёт, собирая словарь формата "url":[response_time1, response_time2 ...]"""

        endpoint_stats = defaultdict(list)
        for log in logs:
            url = log.get("url")
            response_time = log.get("response_time", 0)
            if url:
                endpoint_stats[url].append(response_time)
        return endpoint_stats
    

    def _build_table(self, stats: dict) -> list[list]:
        """Собирает таблицу, вычисляет колличество вызовов для каждого эндпоинта и среднее время ответа этого эндпоинта [url, request_count, average_response_times]"""
        
        result = []
        for endpoint, response_times in stats.items():
            request_count = len(response_times)
            average_time = sum(response_times) / request_count if request_count else 0
            result.append([endpoint, request_count, round(average_time, 4)])
        return result