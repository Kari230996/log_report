import argparse
from tabulate import tabulate

from log_parser import parse_log_file
from report import generate_avg_report


def main():
    parser = argparse.ArgumentParser(description="Log Report Generator")
    parser.add_argument("--file", nargs="+", required=True,
                        help="Path(s) to log file(s)")
    parser.add_argument("--report", required=True,
                        choices=["average"], help="Report type")

    args = parser.parse_args()

    logs = []

    for file_path in args.file:
        logs.extend(parse_log_file(file_path))

    if args.report == "average":
        report = generate_avg_report(logs)
        print(tabulate(report, headers=[
              "Endpoint", "Request Count", "Average Time"], tablefmt="pretty"))


if __name__ == "__main__":
    main()
