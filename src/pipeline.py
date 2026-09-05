import argparse

from src.generation.generate_data import generate_dataset
from src.transformation.staging_pipeline import process_raw_to_staging
from src.warehouse.warehouse_pipeline import process_staging_to_warehouse
from src.warehouse.postgres_loader import load_warehouse_to_postgres
from src.validation.data_validation import validate_events


def run_pipeline(start_date, end_date):
    raw_events = generate_dataset(
        start_date,
        end_date,
    )

    validation_errors = validate_events(raw_events)

    if validation_errors:
        raise ValueError(
            f"Data validation failed: {validation_errors}"
        )

    raw_path = (
        f"data/raw/manufacturing_events_"
        f"{start_date[:7]}.csv"
    )

    raw_events.to_csv(
        raw_path,
        index=False,
    )

    staging_path = (
        f"data/staging/manufacturing_events_"
        f"{start_date[:7]}.csv"
    )

    process_raw_to_staging(
        raw_path,
        staging_path,
    )

    warehouse_tables = process_staging_to_warehouse(
        staging_path,
    )

    load_warehouse_to_postgres(
        warehouse_tables,
    )

    return {
        "raw_path": raw_path,
        "staging_path": staging_path,
        "warehouse_tables": warehouse_tables,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the manufacturing data pipeline."
    )

    parser.add_argument(
        "--start-date",
        required=True,
        help="Pipeline start date in YYYY-MM-DD format.",
    )

    parser.add_argument(
        "--end-date",
        required=True,
        help="Pipeline end date in YYYY-MM-DD format.",
    )

    args = parser.parse_args()

    run_pipeline(
        args.start_date,
        args.end_date,
    )