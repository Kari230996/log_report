import json


def parse_log_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue
