import pandas as pd

from src.analytics.oee import (
    calculate_oee_by_machine,
    calculate_oee_by_shift,
    calculate_downtime_by_machine,
    calculate_rejects_by_machine,
    calculate_defects_by_type,
)
from src.generation.master_data import create_machines


def process_warehouse_to_analytics(
    warehouse_path,
    output_dir="data/analytics",
):
    events = pd.read_csv(warehouse_path)

    machines = create_machines()

    machine_oee = calculate_oee_by_machine(
        events,
        machines,
    )

    shift_oee = calculate_oee_by_shift(
        events,
        machines,
    )

    downtime = calculate_downtime_by_machine(events)

    rejects = calculate_rejects_by_machine(events)

    defects = calculate_defects_by_type(events)

    machine_performance = machine_oee.merge(
        downtime,
        on="machine_id",
        how="left",
    ).merge(
        rejects,
        on="machine_id",
        how="left",
    )

    machine_performance.to_csv(
        f"{output_dir}/machine_performance.csv",
        index=False,
    )

    shift_oee.to_csv(
        f"{output_dir}/shift_performance.csv",
        index=False,
    )

    defects.to_csv(
        f"{output_dir}/defect_summary.csv",
        index=False,
    )

    return {
        "machine_performance": machine_performance,
        "shift_performance": shift_oee,
        "defect_summary": defects,
    }
