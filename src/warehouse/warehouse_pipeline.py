import pandas as pd

from src.warehouse.data_model import (
    create_fact_machine_events,
    create_dimensions,
)
from src.warehouse.storage import save_table


def process_staging_to_warehouse(input_path):
    events = pd.read_csv(
    input_path,
    parse_dates=["timestamp"],
    )

    fact_events = create_fact_machine_events(events)

    dimensions = create_dimensions()

    warehouse_tables = {
        "fact_machine_events": fact_events,
        **dimensions,
    }

    for table_name, dataframe in warehouse_tables.items():
        output_path = f"data/warehouse/{table_name}.csv"

        save_table(
            dataframe,
            output_path,
        )

    return warehouse_tables