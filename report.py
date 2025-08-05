from collections import defaultdict


def generate_avg_report(logs):
    stats = defaultdict(list)

    for log in logs:
        endpoint = log.get("endpoint")
        response_time = log.get("response_time")
        if endpoint and isinstance(response_time, (int, float)):
            stats[endpoint].append(response_time)

    report = []

    for endpoint, times in stats.items():
        avg_time = sum(times) / len(times)
        report.append([endpoint, len(times), round(avg_time, 2)])

    return sorted(report, key=lambda x: x[1], reverse=True)
