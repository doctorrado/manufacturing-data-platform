import pandas as pd
import numpy as np

def calculate_availability(events):
    total_time = len(events)

    downtime = events["downtime_minutes"].sum()

    availability = (
        (total_time - downtime) / total_time
    )

    return availability

def calculate_performance(events, machines):
    if events.empty:
        return 0

    machine_data = machines[
        ["machine_id", "ideal_cycle_time_seconds"]
    ]

    events_with_machine = events.merge(
        machine_data,
        on="machine_id",
        how="left",
    )

    ideal_production_time = (
        events_with_machine["ideal_cycle_time_seconds"]
        * events_with_machine["production_count"]
    ).sum()

    actual_production_time = (
        events_with_machine["cycle_time"]
        * events_with_machine["production_count"]
    ).sum()

    if actual_production_time == 0:
        return 0

    performance = (
        ideal_production_time
        / actual_production_time
    )

    return min(performance, 1.0)

def calculate_quality(events):
    total_production = events["production_count"].sum()
    total_rejects = events["reject_count"].sum()

    if total_production == 0:
        return 0

    good_production = total_production - total_rejects

    quality = good_production / total_production

    return min(quality, 1.0)

def calculate_oee(availability, performance, quality):
    oee = availability * performance * quality

    return min(oee, 1.0)

def calculate_oee_by_machine(events, machines):
    results = []

    for machine_id in machines["machine_id"]:
        machine_events = events[
            events["machine_id"] == machine_id
        ]

        availability = calculate_availability(machine_events)
        performance = calculate_performance(
            machine_events,
            machines,
        )
        quality = calculate_quality(machine_events)

        oee = calculate_oee(
            availability,
            performance,
            quality,
        )

        results.append({
            "machine_id": machine_id,
            "availability": availability,
            "performance": performance,
            "quality": quality,
            "oee": oee,
        })

    return pd.DataFrame(results)

def calculate_oee_by_shift(events, machines):
    results = []

    for shift_id in events["shift_id"].unique():
        shift_events = events[
            events["shift_id"] == shift_id
        ]

        availability = calculate_availability(shift_events)
        performance = calculate_performance(
            shift_events,
            machines,
        )
        quality = calculate_quality(shift_events)

        oee = calculate_oee(
            availability,
            performance,
            quality,
        )

        results.append({
            "shift_id": shift_id,
            "availability": availability,
            "performance": performance,
            "quality": quality,
            "oee": oee,
        })

    return pd.DataFrame(results)

def calculate_oee_by_shift(events, machines):
    results = []

    for shift_id in events["shift_id"].unique():
        shift_events = events[
            events["shift_id"] == shift_id
        ]

        availability = calculate_availability(shift_events)
        performance = calculate_performance(
            shift_events,
            machines,
        )
        quality = calculate_quality(shift_events)

        oee = calculate_oee(
            availability,
            performance,
            quality,
        )

        results.append({
            "shift_id": shift_id,
            "availability": availability,
            "performance": performance,
            "quality": quality,
            "oee": oee,
        })

    return pd.DataFrame(results)

def calculate_downtime_by_machine(events):
    downtime = (
        events.groupby("machine_id")["downtime_minutes"]
        .sum()
        .reset_index()
    )

    return downtime

def calculate_rejects_by_machine(events):
    rejects = (
        events.groupby("machine_id")["reject_count"]
        .sum()
        .reset_index()
    )

    return rejects

def calculate_defects_by_type(events):
    defects = (
        events.dropna(subset=["defect_id"])
        .groupby("defect_id")["reject_count"]
        .sum()
        .reset_index()
        .sort_values("reject_count", ascending=False)
    )

    return defects

