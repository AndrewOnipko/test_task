# from collections import Counter
# from typing import List
# from reports.base_report import Report

# class UserAgentReport(Report):
#     def generate(self, logs: List[dict]) -> List[List]:
#         agents = [log.get("http_user_agent", "Unknown") for log in logs]
#         counter = Counter(agents)
#         return [[agent, count] for agent, count in counter.most_common()]