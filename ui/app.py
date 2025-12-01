import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import json

from src.validators import (
    check_missing_values,
    check_duplicates,
    check_schema,
    check_outliers_iqr,
    check_value_ranges
)
from src.utils import load_config


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Data Quality Checker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Using configuration from:")
    st.code("config/config.yaml")
    st.write("Upload a CSV file and review its data-quality profile.")
    st.markdown("---")
    st.caption("Developed by Parvathy • Data Quality Checker v1.0")


# -----------------------------
# MAIN TITLE
# -----------------------------
st.title("📊 Data Quality Checker")
st.subheader("Upload a CSV file to generate a structured data-quality assessment.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
config = load_config("config/config.yaml")

expected_schema = config.get("expected_schema", {})
ranges = config.get("value_ranges", {})


# -----------------------------
# DATA PROCESSING
# -----------------------------
if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.markdown("### 📁 Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Run validators
    missing = check_missing_values(df)
    duplicates = check_duplicates(df)
    schema_match, schema_details = check_schema(df, expected_schema)
    outliers = check_outliers_iqr(df)
    range_issues = check_value_ranges(df, ranges)

    # -----------------------------
    # SCORE CALCULATION
    # -----------------------------
    score = 100

    score -= min(sum(missing.values()), 20)   
    score -= min(duplicates, 10)
    score -= min(len(outliers) * 5, 15)
    score -= min(len(range_issues) * 5, 20)
    if not schema_match:
        score -= 15

    score = max(0, min(score, 100))

    if score >= 85:
        score_status = "🟢 Excellent"
    elif score >= 60:
        score_status = "🟡 Moderate"
    else:
        score_status = "🔴 Poor"

    # -----------------------------
    # METRIC CARDS
    # -----------------------------
    st.markdown("### 📌 Summary Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Missing Values", sum(missing.values()))
    col2.metric("Duplicate Rows", duplicates)
    col3.metric("Outlier Columns", len(outliers))

    col4, col5, col6 = st.columns(3)
    col4.metric("Range Violations", len(range_issues))
    col5.metric("Schema Match", "Yes" if schema_match else "No")
    col6.metric("Data Quality Score", f"{score} / 100", score_status)


    # -----------------------------
    # DETAILED SECTIONS
    # -----------------------------
    st.markdown("### 🔍 Detailed Insights")

    with st.expander("📌 Missing Values"):
        st.json(missing)

    with st.expander("📌 Duplicate Records"):
        st.write(f"{duplicates} duplicate rows detected.")

    with st.expander("📌 Schema Validation"):
        st.write(f"Schema Match: **{schema_match}**")
        st.json(schema_details)

    with st.expander("📌 Outlier Detection (IQR Method)"):
        if outliers:
            st.json(outliers)
        else:
            st.success("No outliers detected.")

    with st.expander("📌 Range Validation Issues"):
        if range_issues:
            st.write(range_issues)
        else:
            st.success("No range violations detected.")


    # -----------------------------
    # DOWNLOAD REPORT
    # -----------------------------
    st.markdown("### 📄 Download JSON Report")

    full_report = {
        "missing_values": missing,
        "duplicates": duplicates,
        "schema_match": schema_match,
        "schema_details": schema_details,
        "outliers": outliers,
        "range_issues": range_issues,
        "quality_score": score,
        "status": score_status
    }

    st.download_button(
        label="⬇️ Download Report",
        data=json.dumps(full_report, indent=4),
        file_name="validation_report.json",
        mime="application/json"
    )

