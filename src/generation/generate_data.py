from src.generation.master_data import (
    create_machines,
    create_operators,
    create_defects,
)

from src.generation.event_generator import (
    generate_timestamps,
    create_operator_assignments,
    generate_machine_events,
)

from src.validation.data_validation import validate_events


def generate_dataset(
    start_date,
    end_date,
    frequency_minutes=1,
):
    machines = create_machines()
    operators = create_operators()
    defects = create_defects()

    timestamps = generate_timestamps(
        start_date,
        end_date,
        frequency_minutes,
    )

    assignments = create_operator_assignments(
        machines,
        operators,
    )

    events = generate_machine_events(
        timestamps,
        machines,
        "PRD-001",
        assignments,
        defects,
    )

    errors = validate_events(events)

    if errors:
        raise ValueError(
            f"Data validation failed: {errors}"
        )

    return events