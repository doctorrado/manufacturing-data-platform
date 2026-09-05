import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = (
    "postgresql+psycopg://"
    "manufacturing:manufacturing@localhost:5432/manufacturing"
)


def create_postgres_engine():
    """Create a connection to the PostgreSQL warehouse."""
    return create_engine(DATABASE_URL)


def load_table(dataframe, table_name, engine):
    """Load a Pandas DataFrame into a PostgreSQL table."""

    if_exists = "append" if table_name == "fact_machine_events" else "replace"

    dataframe.to_sql(
        table_name,
        engine,
        if_exists=if_exists,
        index=False,
    )


def load_warehouse_to_postgres(tables):
    """Load all warehouse tables into PostgreSQL."""

    engine = create_postgres_engine()

    for table_name, dataframe in tables.items():
        load_table(
            dataframe,
            table_name,
            engine,
        )

    engine.dispose()