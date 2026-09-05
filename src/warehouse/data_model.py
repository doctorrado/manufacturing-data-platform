def create_fact_machine_events(events):
    fact_columns = [
        "timestamp",
        "event_date",
        "event_hour",
        "machine_id",
        "product_id",
        "shift_id",
        "operator_id",
        "defect_id",
        "temperature",
        "pressure",
        "cycle_time",
        "production_count",
        "downtime_minutes",
        "reject_count",
        "energy_consumption",
    ]

    fact_events = events[fact_columns].copy()

    return fact_events

from src.generation.master_data import (
    create_machines,
    create_products,
    create_shifts,
    create_operators,
    create_defects,
)


def create_dimensions():
    dimensions = {
        "dim_machine": create_machines(),
        "dim_product": create_products(),
        "dim_shift": create_shifts(),
        "dim_operator": create_operators(),
        "dim_defect": create_defects(),
    }

    return dimensions