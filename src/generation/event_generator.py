import pandas as pd
import numpy as np


def generate_timestamps(start_date, end_date, frequency_minutes):
    timestamps = pd.date_range(
        start=start_date,
        end=end_date,
        freq=f"{frequency_minutes}min",
        inclusive="left",
    )

    return timestamps


def get_shift(timestamp):
    hour = timestamp.hour

    if 6 <= hour < 18:
        return "SHIFT-001"

    return "SHIFT-002"


def create_operator_assignments(machines, operators):
    assignments = []

    for stage in machines["production_stage"].unique():

        stage_machines = machines[
            machines["production_stage"] == stage
        ]

        stage_operators = operators[
            operators["team"] == stage
        ].reset_index(drop=True)

        for shift_id in ["SHIFT-001", "SHIFT-002"]:

            if len(stage_operators) >= len(stage_machines):
                selected_operators = stage_operators.iloc[
                    :len(stage_machines)
                ]

            else:
                selected_operators = stage_operators.sample(
                    n=len(stage_machines),
                    replace=True,
                    random_state=42
                )

            for (_, machine), (_, operator) in zip(
                stage_machines.iterrows(),
                selected_operators.iterrows()
            ):
                assignments.append({
                    "machine_id": machine["machine_id"],
                    "shift_id": shift_id,
                    "operator_id": operator["operator_id"],
                })

    return pd.DataFrame(assignments)


def generate_machine_telemetry(machine):
    ideal_cycle_time = machine["ideal_cycle_time_seconds"]
    max_temperature = machine["max_temperature_celsius"]
    max_pressure = machine["max_pressure_bar"]

    temperature = np.random.normal(
        loc=max_temperature * 0.75,
        scale=max_temperature * 0.08
    )

    pressure = np.random.normal(
        loc=max_pressure * 0.75,
        scale=max_pressure * 0.08
    )

    cycle_time = np.random.normal(
        loc=ideal_cycle_time,
        scale=ideal_cycle_time * 0.10
    )

    return {
        "temperature": round(temperature, 2),
        "pressure": round(pressure, 2),
        "cycle_time": round(cycle_time, 2),
    }

def generate_production_metrics(cycle_time):
    if np.random.random() < 0.02:
        downtime_minutes = 1
        production_count = 0
    else:
        expected_production = 60 / cycle_time

        production_count = int(expected_production)

        if np.random.random() < (expected_production - production_count):
            production_count += 1

        downtime_minutes = 0

    return {
        "production_count": production_count,
        "downtime_minutes": downtime_minutes,
    }

def generate_quality_metrics(machine, production_count, defects):
    reject_count = 0
    defect_id = None

    if production_count > 0 and np.random.random() < 0.03:
        stage_defects = defects[
            defects["production_stage"] == machine["production_stage"]
        ]

        defect = stage_defects.sample(n=1).iloc[0]

        reject_count = 1
        defect_id = defect["defect_id"]

    return {
        "reject_count": reject_count,
        "defect_id": defect_id,
    }

def generate_energy_consumption(machine, production_count, downtime_minutes):
    base_consumption = (
        machine["rated_capacity_units_per_hour"] / 100
    )

    if downtime_minutes > 0:
        energy_consumption = np.random.normal(
            loc=base_consumption * 0.25,
            scale=base_consumption * 0.05
        )
    else:
        energy_consumption = np.random.normal(
            loc=base_consumption,
            scale=base_consumption * 0.10
        )

    return round(max(0, energy_consumption), 2)

def generate_machine_events(timestamps, machines, product_id, assignments, defects):
    events = []

    assignment_lookup = {
        (row["machine_id"], row["shift_id"]): row["operator_id"]
        for _, row in assignments.iterrows()
    }

    for timestamp in timestamps:
        shift_id = get_shift(timestamp)

        for _, machine in machines.iterrows():

            operator_id = assignment_lookup[
                (machine["machine_id"], shift_id)
            ]

            telemetry = generate_machine_telemetry(machine)

            production = generate_production_metrics(
                telemetry["cycle_time"]
            )

            quality = generate_quality_metrics(
                machine,
                production["production_count"],
                defects
            )

            energy_consumption = generate_energy_consumption(
                machine,
                production["production_count"],
                production["downtime_minutes"]
            )

            events.append({
                "timestamp": timestamp,
                "machine_id": machine["machine_id"],
                "product_id": product_id,
                "shift_id": shift_id,
                "operator_id": operator_id,
                "temperature": telemetry["temperature"],
                "pressure": telemetry["pressure"],
                "cycle_time": telemetry["cycle_time"],
                "production_count": production["production_count"],
                "downtime_minutes": production["downtime_minutes"],
                "reject_count": quality["reject_count"],
                "defect_id": quality["defect_id"],
                "energy_consumption": energy_consumption
            })

    return pd.DataFrame(events)