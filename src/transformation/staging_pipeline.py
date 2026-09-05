import pandas as pd

from src.transformation.transform import transform_events
from src.ingestion.storage import save_staging_data


def process_raw_to_staging(
    raw_path,
    staging_path,
):
    events = pd.read_csv(raw_path)

    transformed = transform_events(events)

    output_path = save_staging_data(
        transformed,
        staging_path,
    )

    return output_path