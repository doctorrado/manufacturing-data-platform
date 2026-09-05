import pandas as pd


def validate_events(events):
    errors = []

    duplicates = events.duplicated(
    subset=["timestamp", "machine_id"]
    )

    if duplicates.any():
        duplicate_dates = (
            events.loc[duplicates, "timestamp"]
            .dt.date
            .astype(str)
            .value_counts()
            .sort_index()
        )

        duplicate_details = ", ".join(
        f"{date}: {count}"
        for date, count in duplicate_dates.items()
        )

        errors.append(
        f"Duplicate machine events detected: {duplicate_details}"
        )

    if events["timestamp"].isna().any():
        errors.append("Missing timestamps detected")

    if events["machine_id"].isna().any():
        errors.append("Missing machine IDs detected")

    if (events["production_count"] < 0).any():
        errors.append("Negative production counts detected")

    if (events["reject_count"] < 0).any():
        errors.append("Negative reject counts detected")

    if (events["reject_count"] > events["production_count"]).any():
        errors.append(
            "Reject count exceeds production count"
        )

    downtime_events = events["downtime_minutes"] > 0

    if (
        events.loc[downtime_events, "production_count"] > 0
    ).any():
        errors.append(
            "Production detected during downtime"
        )

    if (
        (events["defect_id"].notna())
        & (events["reject_count"] == 0)
    ).any():
        errors.append(
            "Defect ID detected without a reject"
        )

    if (events["temperature"] < 0).any():
        errors.append("Negative temperature detected")

    if (events["pressure"] < 0).any():
        errors.append("Negative pressure detected")

    if (events["energy_consumption"] < 0).any():
        errors.append(
            "Negative energy consumption detected"
        )

    return errors