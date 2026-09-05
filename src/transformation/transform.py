import pandas as pd


def transform_events(events):
    transformed = events.copy()

    transformed["timestamp"] = pd.to_datetime(
        transformed["timestamp"]
    )

    transformed["event_date"] = (
        transformed["timestamp"].dt.date
    )

    transformed["event_hour"] = (
        transformed["timestamp"].dt.hour
    )

    return transformed