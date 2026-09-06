# Manufacturing Data Platform

An end-to-end data engineering and analytics platform that simulates a manufacturing environment and processes machine events from synthetic data generation through data validation, transformation, dimensional modeling, PostgreSQL warehousing, and operational analytics.

The project is designed to demonstrate practical data engineering skills in a manufacturing context, with a focus on data quality, warehouse design, and Overall Equipment Effectiveness (OEE).

<img width="1884" height="952" alt="Screenshot From 2026-09-06 12-36-00" src="https://github.com/user-attachments/assets/745012cd-7398-4eeb-baf7-9550c5e67d41" />
<img width="1864" height="963" alt="Screenshot From 2026-09-06 12-36-28" src="https://github.com/user-attachments/assets/430dfbda-e056-440b-b213-1f51e4360e73" />
<img width="1864" height="963" alt="Screenshot From 2026-09-06 12-36-38" src="https://github.com/user-attachments/assets/301d5dae-ac70-4920-b844-9029e9cdc252" />
<img width="1864" height="963" alt="Screenshot From 2026-09-06 12-36-42" src="https://github.com/user-attachments/assets/8dddc549-271c-484b-8342-5394c9397e54" />




---

## Project Overview

The platform simulates a manufacturing facility with:

- 12 machines
- 15 operators
- 2 production shifts
- 1 product
- 9 defect types
- Machine events generated at one-minute intervals

The generated data contains operational measurements such as temperature, pressure, cycle time, production counts, downtime, rejects, defects, and energy consumption.

The complete pipeline follows:

```text
Synthetic Data Generation
          ↓
       Validation
          ↓
          RAW
          ↓
       STAGING
          ↓
      WAREHOUSE
          ↓
      PostgreSQL
          ↓
       ANALYTICS
          ↓
        Metabase
```

---

## Architecture

```text
┌─────────────────────────┐
│   Synthetic Data        │
│      Generation         │
│                         │
│ Python + Pandas + NumPy │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Data Validation   │
│                         │
│ Quality rules and       │
│ duplicate detection     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│          RAW            │
│                         │
│ Original generated      │
│ machine events          │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        STAGING          │
│                         │
│ Cleaning and basic      │
│ transformations         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       WAREHOUSE         │
│                         │
│ Fact + Dimension Tables │
│                         │
│ PostgreSQL              │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        ANALYTICS        │
│                         │
│ OEE and operational     │
│ performance metrics     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│        METABASE         │
│                         │
│ Manufacturing           │
│ Performance Dashboard   │
└─────────────────────────┘
```

---

## Data Generation

Synthetic manufacturing events are generated using Python, Pandas, and NumPy.

Each machine produces an event every minute containing operational and production measurements.

Generated event fields include:

```text
timestamp
event_date
event_hour
machine_id
product_id
shift_id
operator_id
defect_id
temperature
pressure
cycle_time
production_count
downtime_minutes
reject_count
energy_consumption
```

Supporting master data is generated for:

- Machines
- Operators
- Products
- Shifts
- Defects

The simulation contains three production areas:

```text
Assembly
Quality
Packaging
```

---

## Data Validation

Data validation is performed immediately after data generation and before the data enters the RAW layer.

The validation layer checks for data quality issues including:

- Missing timestamps
- Missing machine IDs
- Negative production counts
- Negative reject counts
- Reject counts greater than production
- Production during downtime
- Defect IDs without rejects
- Negative temperature values
- Negative pressure values
- Negative energy consumption
- Duplicate machine events

Duplicate events are identified using:

```text
timestamp + machine_id
```

If validation errors are detected, the pipeline stops before the data is written to the subsequent processing layers.

Validation logic is implemented in:

```text
src/validation/data_validation.py
```

---

## Data Pipeline

The complete pipeline is orchestrated through:

```text
src/pipeline.py
```

The pipeline performs the following operations:

1. Generate manufacturing events
2. Validate generated data
3. Write the RAW dataset
4. Transform RAW data into STAGING
5. Build warehouse fact and dimension tables
6. Load warehouse tables into PostgreSQL

The pipeline can be executed from the command line:

```bash
python -m src.pipeline     --start-date 2026-01-01     --end-date 2026-02-01
```

The end date is exclusive.

---

## RAW Layer

The RAW layer contains the generated manufacturing events before staging transformations.

Example:

```text
data/raw/
├── manufacturing_events_2026-01.csv
├── manufacturing_events_2026-02.csv
├── ...
└── manufacturing_events_2026-12.csv
```

The project contains synthetic manufacturing data covering 2026.

January alone contains:

```text
535,680 events
13 columns
```

The full-year dataset contains approximately:

```text
6.3 million machine events
365 days
```

---

## STAGING Layer

The staging layer prepares the raw events for warehouse processing.

Current transformations include:

- Timestamp conversion
- Creation of `event_date`
- Creation of `event_hour`
- Preservation of operational measurements

Staging files are stored under:

```text
data/staging/
```

The staging pipeline is implemented in:

```text
src/transformation/staging_pipeline.py
```

---

## Warehouse Layer

The warehouse uses a dimensional modeling approach based on a star schema.

### Fact Table

```text
fact_machine_events
```

The fact table contains machine-level operational events and measurements.

### Dimension Tables

```text
dim_machine
dim_product
dim_shift
dim_operator
dim_defect
```

The logical warehouse model is:

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

Warehouse datasets are also stored under:

```text
data/warehouse/
```

The PostgreSQL loader is implemented in:

```text
src/warehouse/postgres_loader.py
```

The warehouse pipeline is implemented in:

```text
src/warehouse/warehouse_pipeline.py
```

---

## PostgreSQL Warehouse

The warehouse tables are loaded into PostgreSQL for analytical querying.

The main fact table contains:

```text
timestamp
event_date
event_hour
machine_id
product_id
shift_id
operator_id
defect_id
temperature
pressure
cycle_time
production_count
downtime_minutes
reject_count
energy_consumption
```

PostgreSQL provides the relational warehouse layer consumed by the analytics and BI layer.

---

## Analytics

The project includes Python-based analytics modules as well as SQL-based analytical queries.

Analytics include:

- Overall Equipment Effectiveness (OEE)
- Availability
- Performance
- Quality
- Production
- Downtime
- Rejects
- Defects
- Energy consumption

### Overall Equipment Effectiveness

OEE is calculated as:

```text
OEE = Availability × Performance × Quality
```

The project calculates OEE at multiple levels:

- Plant
- Machine
- Production stage
- Shift
- Day

This allows operational performance to be analyzed at different levels of the manufacturing process.

---

## Analytics Outputs

The project also contains analytical datasets under:

```text
data/analytics/
```

Current outputs include:

```text
machine_performance.csv
shift_performance.csv
defect_summary.csv
```

The analytics implementation is located in:

```text
src/analytics/
├── analytics_pipeline.py
├── oee.py
└── production.py
```

---

## Metabase Dashboard

The PostgreSQL warehouse is connected to Metabase through Docker.

The current dashboard is:

```text
Manufacturing Performance Dashboard
```

The dashboard provides operational monitoring through:

### Plant KPIs

- Availability
- Performance
- Quality
- OEE

### OEE Analysis

- OEE by machine
- OEE by shift
- OEE by production stage
- OEE by day

### Production Analysis

- Production by day
- Production by machine
- Rejections by day
- Rejections by machine

### Quality Analysis

- Defects by type
- Reject rate by machine

### Downtime Analysis

- Downtime by machine
- Downtime by production stage

### Energy Analysis

- Energy consumption by day
- Energy consumption by machine

The dashboard includes a date filter that can be used to analyze the operational metrics across different time periods.

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
│   ├── __init__.py
│   ├── pipeline.py
│   │
│   ├── config/
│   │   └── loader.py
│   │
│   ├── generation/
│   │   ├── event_generator.py
│   │   ├── generate_data.py
│   │   └── master_data.py
│   │
│   ├── ingestion/
│   │   └── storage.py
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
│   │   ├── postgres_loader.py
│   │   ├── storage.py
│   │   └── warehouse_pipeline.py
│   │
│   └── analytics/
│       ├── analytics_pipeline.py
│       ├── oee.py
│       └── production.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies

### Programming & Data

- Python
- Pandas
- NumPy

### Data Engineering

- ETL pipelines
- Data validation
- Data transformation
- Dimensional modeling
- Star schema
- Fact and dimension tables
- Analytical SQL

### Data Storage

- CSV
- DuckDB
- PostgreSQL

DuckDB is included as a local analytical storage artifact in the project. The current Metabase dashboard uses PostgreSQL as its data source.

### Analytics & BI

- SQL
- Metabase

### Development

- Git
- GitHub
- Linux
- Python virtual environments
- Docker

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
cd manufacturing-data-platform
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the pipeline

```bash
python -m src.pipeline     --start-date 2026-01-01     --end-date 2026-02-01
```

The pipeline will:

```text
Generate
   ↓
Validate
   ↓
RAW
   ↓
STAGING
   ↓
WAREHOUSE
   ↓
PostgreSQL
```

---

## Current Results

The current implementation demonstrates a complete end-to-end manufacturing data workflow.

The generated 2026 dataset contains approximately:

```text
6.3 million machine events
365 days
12 machines
15 operators
2 shifts
1 product
9 defect types
```

The analytical layer supports:

```text
Plant OEE
Machine OEE
Shift OEE
Stage OEE
Daily OEE
Availability
Performance
Quality
Production
Downtime
Rejects
Defects
Energy Consumption
```

Pressure and temperature are generated as operational telemetry and retained in the warehouse. Current dashboard analysis focuses primarily on production, quality, downtime, energy consumption, and OEE rather than dedicated pressure analysis.

The PostgreSQL warehouse provides the analytical data source for the Metabase dashboard.

---

## Future Improvements

Potential future development includes:

- Loading the warehouse into Google BigQuery
- Adding Apache Airflow orchestration
- Expanding cloud-based storage
- Adding additional manufacturing KPIs
- Improving pipeline observability and logging
- Adding automated data-quality tests
- Containerizing additional pipeline components
- Expanding the synthetic manufacturing simulation

These are future enhancements and are not required for the current end-to-end implementation.

---

## Project Objective

The objective of this project is to demonstrate practical end-to-end data engineering capabilities through a realistic manufacturing use case.

The platform covers:

```text
Data Generation
       ↓
Data Validation
       ↓
Data Transformation
       ↓
Dimensional Modeling
       ↓
PostgreSQL Warehouse
       ↓
Analytics
       ↓
Business Intelligence
```

The project demonstrates skills applicable to:

- Data Engineering
- Data Analytics
- Business Intelligence
- Manufacturing Analytics
- ETL Development
- Data Quality
- Data Warehousing
