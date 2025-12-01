import pandas as pd
import numpy as np

def check_missing_values(df):
    return df.isnull().sum().to_dict()

def check_duplicates(df):
    return int(df.duplicated().sum())

def check_schema(df, expected_schema):
    details = {}
    match = True

    for col, expected_type in expected_schema.items():
        if col not in df.columns:
            details[col] = "Missing Column"
            match = False
        else:
            actual = str(df[col].dtype)
            if actual != expected_type:
                details[col] = f"Datatype Mismatch (Expected {expected_type}, Got {actual})"
                match = False
            else:
                details[col] = "OK"

    return match, details

def check_outliers_iqr(df):
    outliers = {}

    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        count = int(((df[col] < lower) | (df[col] > upper)).sum())

        if count > 0:
            outliers[col] = count

    return outliers

def check_value_ranges(df, ranges):
    issues = []

    for col, (min_val, max_val) in ranges.items():
        if col not in df.columns:
            issues.append(f"{col}: column missing")
            continue

        if min_val is not None and (df[col] < min_val).any():
            issues.append(f"{col}: values below {min_val}")

        if max_val is not None and (df[col] > max_val).any():
            issues.append(f"{col}: values above {max_val}")

    return issues
