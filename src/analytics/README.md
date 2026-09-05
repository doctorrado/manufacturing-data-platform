# Manufacturing Data Platform

A professional data engineering and analytics project that simulates a manufacturing environment and builds an end-to-end data pipeline from raw machine events to analytical datasets.

The project demonstrates data generation, validation, transformation, warehouse modeling, and operational analytics using Python, Pandas, SQL-oriented data modeling concepts, and CSV-based data storage.

The final analytical outputs are designed to be consumed by a BI tool such as Power BI.

---

## Project Overview

The Manufacturing Data Platform simulates a manufacturing facility with multiple production areas, machines, operators, shifts, products, and defect types.

Synthetic machine events are generated at one-minute intervals and processed through several data pipeline layers.

The main objective is to demonstrate an end-to-end data engineering workflow:

```text
Data Generation
      ↓
     RAW
      ↓
   STAGING
      ↓
  WAREHOUSE
      ↓
  ANALYTICS
      ↓
   BI / Power BI
```

The dataset currently contains:

* 12 machines
* 15 operators
* 2 shifts
* 1 product
* 9 defect types
* 535,680 machine events for January 2026

---

## Architecture

```text
┌──────────────────────┐
│   Synthetic Data     │
│      Generation      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│         RAW          │
│   Original Events    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       STAGING        │
│ Cleaning & Basic     │
│ Transformations      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      WAREHOUSE       │
│ Fact & Dimension     │
│ Tables               │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      ANALYTICS       │
│ OEE & Operational    │
│ KPIs                 │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   BI / Visualization │
│      Power BI        │
└──────────────────────┘
```

---

## Data Generation

Synthetic manufacturing events are generated using Python.

Each machine produces one event per minute containing operational telemetry and production information.

Generated fields include:

* `timestamp`
* `machine_id`
* `product_id`
* `shift_id`
* `operator_id`
* `temperature`
* `pressure`
* `cycle_time`
* `production_count`
* `downtime_minutes`
* `reject_count`
* `defect_id`
* `energy_consumption`

The generator also creates supporting master data for:

* Machines
* Operators
* Products
* Shifts
* Defects

---

## RAW Layer

The RAW layer contains the generated manufacturing events before analytical processing.

Example:

```text
data/raw/
└── manufacturing_events_2026-01.csv
```

The January dataset contains:

```text
535,680 rows
13 columns
```

The RAW layer represents the source data entering the platform.

---

## STAGING Layer

The staging layer prepares the raw data for the warehouse.

Transformations currently include:

* Timestamp conversion
* Creation of `event_date`
* Creation of `event_hour`
* Preservation of the original operational measurements

Example:

```text
data/staging/
└── manufacturing_events_2026-01.csv
```

The staging pipeline is implemented in:

```text
src/transformation/staging_pipeline.py
```

---

## Warehouse Layer

The warehouse organizes the staging data into a dimensional model.

The project uses a star-schema approach.

### Fact Table

```text
fact_machine_events
```

Contains the machine event measurements and foreign-key-style identifiers.

### Dimension Tables

```text
dim_machine
dim_product
dim_shift
dim_operator
dim_defect
```

Current warehouse structure:

```text
                 dim_machine
                      │
                      │
dim_product ─── fact_machine_events ─── dim_shift
                      │
                      │
                dim_operator
                      │
                      │
                  dim_defect
```

Warehouse outputs are stored in:

```text
data/warehouse/
```

The warehouse pipeline is implemented in:

```text
src/warehouse/warehouse_pipeline.py
```

---

## Data Validation

Data validation is performed before the dataset is finalized.

The validation layer checks the generated event data and returns validation errors when data quality rules are violated.

Example:

```text
Validation errors: []
Validation passed successfully
```

Validation logic is located in:

```text
src/validation/
```

---

## Analytics Layer

The analytics layer converts warehouse data into business-oriented metrics.

Current analytics include:

### OEE

Overall Equipment Effectiveness is calculated using:

```text
OEE = Availability × Performance × Quality
```

Current overall results from the generated dataset are approximately:

```text
Availability: 98.02%
Performance: 100.00%
Quality:      99.01%
OEE:          97.04%
```

### OEE by Machine

OEE is also calculated individually for each machine.

This allows identification of machines with comparatively lower operational performance.

### OEE by Shift

OEE is calculated for each production shift.

### Downtime by Machine

Total downtime is aggregated by machine to identify machines experiencing more production interruptions.

### Rejects by Machine

Total rejected production is aggregated by machine.

### Defects by Type

Rejects are grouped by defect type to identify the most frequent quality issues.

---

## Analytics Outputs

The analytics pipeline produces:

```text
data/analytics/
├── machine_performance.csv
├── shift_performance.csv
└── defect_summary.csv
```

### `machine_performance.csv`

Contains:

```text
machine_id
availability
performance
quality
oee
downtime_minutes
reject_count
```

### `shift_performance.csv`

Contains:

```text
shift_id
availability
performance
quality
oee
```

### `defect_summary.csv`

Contains:

```text
defect_id
reject_count
```

These datasets are designed to provide a clean interface between the data engineering pipeline and future BI/reporting tools.

---

## Project Structure

```text
manufacturing-data-platform/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── staging/
│   ├── warehouse/
│   └── analytics/
│
├── src/
│   ├── generation/
│   │   ├── event_generator.py
│   │   ├── generate_data.py
│   │   └── master_data.py
│   │
│   ├── transformation/
│   │   ├── transform.py
│   │   └── staging_pipeline.py
│   │
│   ├── validation/
│   │   └── data_validation.py
│   │
│   ├── warehouse/
│   │   ├── data_model.py
│   │   └── warehouse_pipeline.py
│   │
│   └── analytics/
│       ├── oee.py
│       └── analytics_pipeline.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies

### Programming & Data

* Python
* Pandas
* NumPy

### Data Engineering

* ETL / ELT concepts
* Data validation
* Data transformation
* Dimensional modeling
* Star schema
* Fact and dimension tables

### Development

* Git
* GitHub
* Linux
* Virtual environments

### Planned / Future

* SQL
* Google Cloud Platform
* BigQuery
* Apache Airflow
* Docker
* Power BI
* DAX

---

## How to Run

Create the Python virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the manufacturing dataset:

```python
from src.generation.generate_data import generate_dataset

events = generate_dataset(
    "2026-01-01",
    "2026-02-01",
)
```

The generated dataset can then be processed through the staging and warehouse pipelines.

Run the staging pipeline:

```python
from src.transformation.staging_pipeline import process_raw_to_staging

process_raw_to_staging(
    "data/raw/manufacturing_events_2026-01.csv",
    "data/staging/manufacturing_events_2026-01.csv",
)
```

Run the warehouse pipeline:

```python
from src.warehouse.warehouse_pipeline import process_staging_to_warehouse

process_staging_to_warehouse(
    "data/staging/manufacturing_events_2026-01.csv"
)
```

Run the analytics pipeline:

```python
from src.analytics.analytics_pipeline import process_warehouse_to_analytics

process_warehouse_to_analytics(
    "data/warehouse/fact_machine_events.csv"
)
```

---

## Current Results

The current generated dataset demonstrates a complete flow from synthetic machine events to analytical outputs.

Example analytical results:

```text
Overall OEE              ≈ 97%
Overall Availability     ≈ 98%
Overall Performance      = 100%
Overall Quality          ≈ 99%
```

Machine-level analysis provides additional operational detail, including:

* OEE by machine
* Downtime by machine
* Rejects by machine
* OEE by shift
* Defect frequency

---

## Future Development

The next stage of the project will focus on BI consumption and cloud-oriented data engineering.

Planned improvements include:

* Building a Power BI dashboard
* Creating DAX measures
* Adding SQL transformations
* Loading warehouse data into BigQuery
* Orchestrating pipelines with Apache Airflow
* Containerizing the application with Docker
* Expanding the synthetic manufacturing dataset
* Adding additional production and quality KPIs

---

## Project Objective

This project demonstrates the ability to design and implement a complete data pipeline rather than simply perform isolated data analysis.

The platform covers:

```text
Generation
    ↓
Validation
    ↓
Transformation
    ↓
Data Modeling
    ↓
Warehouse
    ↓
Analytics
    ↓
Business Intelligence
```

The goal is to demonstrate practical skills applicable to Data Engineering, Data Analytics, and Manufacturing Analytics roles.
