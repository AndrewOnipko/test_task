from app.core.report_factory import get_report
from app.core.logger import simple_logger

class MainController:
    def __init__(self, report_name, log_parser, logger):
        self.report_name = report_name
        self.log_parser = log_parser
        self.logger = logger

    @simple_logger
    def run(self):
        logs = self.log_parser.parse()
        report = get_report(self.report_name)
        data = report.generate(logs)
        return data