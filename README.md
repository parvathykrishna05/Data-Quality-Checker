# 📊 Data Quality Checker  
A professional, modular, and extensible **data validation toolkit** with both **CLI** and **Streamlit UI** for analyzing dataset quality, detecting issues, and generating structured reports.  
This project is designed for **Data Engineers, ML Engineers, and Data Scientists** who need to ensure data integrity before ingestion, modeling, or deployment.

---

## 🚀 Features

### 🔍 Automated Data Validation  
- Missing value detection  
- Duplicate row detection  
- Schema validation  
- Outlier detection (IQR method)  
- Range validation  
- Detection of non-numeric values in numeric fields  
- Extra or unexpected column detection  

### 📈 Streamlit Dashboard (UI)  
- Upload CSV files interactively  
- Dataset preview  
- Summary metrics  
- Color-coded **Data Quality Score**  
- Expandable detailed insights  
- Downloadable JSON report  

### 🖥 Command-Line Interface (CLI)  
For engineers and pipeline integration:

python main.py --file data/sample.csv --config config/config.yaml --out reports/report.json


### 📄 Structured JSON Reports  
All validation results are exported in an easy-to-read JSON format.

### 🧱 Modular Architecture  
Validator modules are cleanly separated and easy to extend.  
Configuration is handled via YAML for flexibility.

---

## 📁 Project Structure

data-quality-checker/
│
├── ui/
│ └── app.py # Streamlit dashboard
│
├── src/
│ ├── init.py
│ ├── validators.py # Validation logic
│ └── utils.py # Config & logging utilities
│
├── config/
│ └── config.yaml # Schema & range rules
│
├── data/
│ └── sample.csv # Sample dataset
│
├── reports/
│ └── validation_report.json # Generated output
│
├── logs/
│ └── run.log # CLI logs
│
├── main.py # CLI entrypoint
├── requirements.txt
└── README.md


---

## ▶️ Run the Streamlit App

Launch the dashboard:

streamlit run ui/app.py


The browser will open automatically and display:

- Dataset preview  
- Summary metrics  
- Missing values  
- Duplicates  
- Schema issues  
- Outliers  
- Range violations  
- Data quality score  
- Download JSON button  

---

## 🖥 Running via CLI

Execute from the project root:

python main.py
--file data/sample.csv
--config config/config.yaml
--out reports/validation_report.json


The CLI generates:

- JSON report  
- Log file  
- Summary validation output  

---

## ⚙️ Configuration (YAML)

Located at: `config/config.yaml`

```yaml
expected_schema:
  age: int64
  salary: float64
  department: object

value_ranges:
  age: [0, 120]
  salary: [0, null]

logging:
  level: INFO

You can easily update:
Column names
Expected datatypes
Value ranges
Logging settings

##🧪 Testing With Messy Data

This tool has been validated using real messy datasets from Kaggle, including:

Adult Census Income

Titanic (raw)

Medical Appointments No-Show

House Prices

These datasets contain:

Missing values

Incorrect datatypes

Inconsistent formatting

Outliers

Extra columns

Range violations

Duplicates

Perfect for testing data quality pipelines.

📦 Installation

Clone the repository:
git clone https://github.com/your-username/data-quality-checker.git
cd data-quality-checker
Install dependencies:
pip install -r requirements.txt
🧰 Technologies Used

Python 3

Pandas

NumPy

PyYAML

Streamlit

Logging

## 🌐 Deployment

Compatible with:

- **Local execution**
- **Streamlit Cloud**
- **Docker**
- **HuggingFace Spaces**
- **Heroku** (Streamlit buildpack)

The project structure is optimized for smooth deployment across platforms.

---

## 🎯 Use Cases

This tool is suitable for:

- **Data validation in ML pipelines**
- **Pre-ingestion checks in ETL workflows**
- **Business data quality assessments**
- **Dashboard-based dataset audits**
- **Reproducible data integrity analysis**

---

## 👩‍💻 Author

**Parvathy**  
Data Science • AI • Machine Learning  

This project was built to demonstrate practical data-engineering and validation skills.
