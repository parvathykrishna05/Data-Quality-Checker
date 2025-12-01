import json
import pandas as pd
from src.data_quality_checker import (
    check_missing_values,
    check_duplicates,
    check_schema,
    check_outliers_iqr,
    check_value_ranges
)

# Load dataset
df = pd.read_csv("data/sample.csv")

# Define expected schema: column: dtype
expected_schema = {
    "age": "int64",
    "salary": "float64",
    "department": "object"
}

# Define value ranges for validation
ranges = {
    "age": (0, 120),
    "salary": (0, None)
}

report = {}

report["missing_values"] = check_missing_values(df)
report["duplicates"] = check_duplicates(df)
report["schema_match"], report["schema_details"] = check_schema(df, expected_schema)
report["outliers"] = check_outliers_iqr(df)
report["range_issues"] = check_value_ranges(df, ranges)

# Save report
with open("reports/validation_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("✔ Data quality report generated successfully in reports/validation_report.json")
