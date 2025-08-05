from log_parser import parse_log_file


def test_parse_log_file(tmp_path):
    """
    Проверяем, что parse_log_file возвращает словари из валидных JSON‑строк и
    игнорирует пустые и некорректные строки.
    """
    content = "\n".join([
        '{"endpoint": "/a", "response_time": 100}',
        "invalid json",
        '{"endpoint": "/b", "response_time": 200}',
        ""  # пустая строка игнорируется
    ])
    file_path = tmp_path / "sample.log"
    file_path.write_text(content, encoding="utf-8")

    logs = list(parse_log_file(file_path))
    assert logs == [
        {"endpoint": "/a", "response_time": 100},
        {"endpoint": "/b", "response_time": 200},
    ]
