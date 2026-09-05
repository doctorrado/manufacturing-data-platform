import pandas as pd


def calculate_production_metrics(events):
    return {
        "total_production": events["production_count"].sum(),
        "total_rejects": events["reject_count"].sum(),
        "total_downtime": events["downtime_minutes"].sum(),
        "total_energy": events["energy_consumption"].sum(),
        "reject_rate": (
            events["reject_count"].sum()
            / events["production_count"].sum()
            )
    }

def calculate_production_by_machine(events):
    production = (
        events
        .groupby("machine_id")
        .agg(
            total_production=("production_count", "sum"),
            total_rejects=("reject_count", "sum"),
            total_downtime=("downtime_minutes", "sum"),
            total_energy=("energy_consumption", "sum"),
        )
        .reset_index()
    )

    production["reject_rate"] = (
        production["total_rejects"]
        / production["total_production"]
    )

    return production

def calculate_production_by_shift(events):
    production = (
        events
        .groupby("shift_id")
        .agg(
            total_production=("production_count", "sum"),
            total_rejects=("reject_count", "sum"),
            total_downtime=("downtime_minutes", "sum"),
            total_energy=("energy_consumption", "sum"),
        )
        .reset_index()
    )

    production["reject_rate"] = (
        production["total_rejects"]
        / production["total_production"]
    )

    return production

def calculate_production_by_date(events):
    production = (
        events
        .groupby("event_date")
        .agg(
            total_production=("production_count", "sum"),
            total_rejects=("reject_count", "sum"),
            total_downtime=("downtime_minutes", "sum"),
            total_energy=("energy_consumption", "sum"),
        )
        .reset_index()
    )

    production["reject_rate"] = (
        production["total_rejects"]
        / production["total_production"]
    )

    return production