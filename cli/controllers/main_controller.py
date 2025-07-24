from utils.report_factory import get_report
from utils.logger import simple_logger

class MainController:
    def __init__(self, report_name, log_parser, table_formatter, logger):
        self.report_name = report_name
        self.log_parser = log_parser
        self.table_formatter = table_formatter
        self.logger = logger

    @simple_logger
    def run(self):
        logs = self.log_parser.parse()

        report = get_report(self.report_name)
        data = report.generate(logs)

        output = self.table_formatter.format(data, headers=["Endpoint", "Count", "Average Response Time"])
        print(output)