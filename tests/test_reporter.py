from report import generate_avg_report

def test_generate_avg_report():
    logs = [
        {"endpoint": "/a", "response_time": 100},
        {"endpoint": "/a", "response_time": 200},
        {"endpoint": "/b", "response_time": 300},
    ]
    report = generate_avg_report(logs)
    assert report == [
        ['/a', 2, 150.0],
        ['/b', 1, 300.0],
    ]