# src/validators.py
import pandas as pd
import numpy as np

def check_missing_values(df: pd.DataFrame) -> dict:
    """Return dict of missing counts per column."""
    return df.isnull().sum().to_dict()

def check_duplicates(df: pd.DataFrame) -> int:
    """Return number of duplicated rows."""
    return int(df.duplicated().sum())

def check_schema(df: pd.DataFrame, expected_schema: dict) -> (bool, dict):
    """
    expected_schema: {column: dtype_str}
    Returns (match_bool, details_dict)
    """
    details = {}
    match = True
    for col, expected_type in expected_schema.items():
        if col not in df.columns:
            details[col] = "Missing Column"
            match = False
            continue
        actual = str(df[col].dtype)
        if actual != expected_type:
            details[col] = f"Datatype Mismatch (Expected {expected_type}, Got {actual})"
            match = False
        else:
            details[col] = "OK"
    return match, details

def check_outliers_iqr(df: pd.DataFrame) -> dict:
    """
    Return dict {col: outlier_count} for numeric columns using IQR rule.
    """
    outliers = {}
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in numeric_cols:
        series = df[col].dropna()
        if series.empty:
            continue
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        count = int(((series < lower) | (series > upper)).sum())
        if count > 0:
            outliers[col] = count
    return outliers

def check_value_ranges(df, ranges):
    """
    ranges: {column: [min, max]}
    Handles mixed types by converting to numeric safely.
    """
    issues = []

    for col, r in ranges.items():
        if col not in df.columns:
            issues.append(f"{col}: column missing")
            continue

        min_val, max_val = r

        # Convert column to numeric, coerce errors → NaN
        numeric_series = pd.to_numeric(df[col], errors="coerce")

        # Identify rows that couldn't be converted to numeric
        if numeric_series.isnull().sum() > 0:
            issues.append(f"{col}: contains non-numeric values")
        
        # Drop NaNs for comparison
        clean_series = numeric_series.dropna()

        # Check min
        if min_val is not None and (clean_series < min_val).any():
            issues.append(f"{col}: values below {min_val}")

        # Check max
        if max_val is not None and (clean_series > max_val).any():
            issues.append(f"{col}: values above {max_val}")

    return issues

