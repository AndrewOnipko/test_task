# import argparse 
# from controllers.main_controller import MainController
# from parser.log_parser import LogParser
# from utils.table_formatter import TableFormatter
# import logging
# import os
# import sys

# script_name = os.path.basename(__file__)
# script_path = os.path.abspath(sys.argv[0])
# file_directory = os.path.dirname(script_path)
# log_file = os.path.join(file_directory, 'logs.log')


# formatter = logging.Formatter('%(asctime)s - %(message)s')

# logging.basicConfig(level=logging.INFO,
#                     handlers=[
#                         logging.FileHandler(log_file, encoding='utf-8', mode='w'),
#                         logging.StreamHandler()
#                     ])

# for handler in logging.getLogger().handlers:
#     handler.setFormatter(formatter)

# def main():
#     logger = logging.getLogger()
#     parser = argparse.ArgumentParser(description="Log report generator")
#     parser.add_argument('--file', nargs='+', required=True, help='Path to log file(s)')
#     parser.add_argument('--report', choices=['average'], required=True, help='Report type')
#     parser.add_argument('--date', required=False, help='Filter logs by date (YYYY-MM-DD)')
#     args = parser.parse_args()
#     log_parser = LogParser(logger, args.file, args.date, )
#     table_formattet = TableFormatter(logger)
#     controller = MainController(args.report, log_parser, table_formattet, logger)
#     controller.run()

# if __name__ == '__main__':
#     main()

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst


print(append_to_list(2))
print(append_to_list(3))