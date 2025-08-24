# Log Report Generator

A script for processing log files in JSON format and generating a report by endpoints: number of requests and average response time.

---

## 🚀 Example Run

```bash
python main.py --file sample.log --report average
```

You can pass multiple files:

```bash
python main.py --file logs/api1.log logs/api2.log --report average
```

---

## 📊 Example Output

```
+---------------------+----------------+----------------+
| Endpoint            | Request Count  | Average Time   |
+---------------------+----------------+----------------+
| /api/v1/users       | 125            | 198.36         |
| /api/v1/orders      | 80             | 240.75         |
+---------------------+----------------+----------------+
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📂 Project Structure

```
log_report/
├── main.py              # Entry point
├── log_parser.py        # Log parsing
├── report.py            # Report generation
├── tests/
│   ├── test_parser.py   # Tests for parser
│   └── test_report.py   # Tests for report
└── sample.log           # Example log file
```

---

## 📎 Requirements

* Python 3.8+
* `tabulate` (for table display)
* `pytest` (for tests)

Installation:

```bash
pip install -r requirements.txt
```

---

## 🛠 Features

* ✅ Support for multiple files via `--file`
* ✅ Output as a formatted table
* ✅ Covered with tests
* ⚠️ Only `average` report type is implemented (others not yet)

---
