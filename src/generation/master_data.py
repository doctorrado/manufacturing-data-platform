import pandas as pd
def create_machines():   
   
    machines = [

    {
        "machine_id": "ASM-01",
        "machine_name": "CNC Machine 1",
        "machine_type": "CNC Machine",
        "production_stage": "Assembly",
        "ideal_cycle_time_seconds": 45,
        "rated_capacity_units_per_hour": 80,
        "max_temperature_celsius": 85,
        "max_pressure_bar": 8.0,
    },

    {
        "machine_id": "ASM-02",
        "machine_name": "CNC Machine 2",
        "machine_type": "CNC Machine",
        "production_stage": "Assembly",
        "ideal_cycle_time_seconds": 40,
        "rated_capacity_units_per_hour": 90,
        "max_temperature_celsius": 90,
        "max_pressure_bar": 8.0,
    },

    {
        "machine_id": "ASM-03",
        "machine_name": "Robotic Arm 1",
        "machine_type": "Robotic Arm",
        "production_stage": "Assembly",
        "ideal_cycle_time_seconds": 20,
        "rated_capacity_units_per_hour": 180,
        "max_temperature_celsius": 70,
        "max_pressure_bar": 6.0,
    },

    {
        "machine_id": "ASM-04",
        "machine_name": "Robotic Arm 2",
        "machine_type": "Robotic Arm",
        "production_stage": "Assembly",
        "ideal_cycle_time_seconds": 18,
        "rated_capacity_units_per_hour": 200,
        "max_temperature_celsius": 70,
        "max_pressure_bar": 6.0,
    },

    {
        "machine_id": "QA-01",
        "machine_name": "Vision System 1",
        "machine_type": "Vision System",
        "production_stage": "Quality",
        "ideal_cycle_time_seconds": 12,
        "rated_capacity_units_per_hour": 300,
        "max_temperature_celsius": 60,
        "max_pressure_bar": 3.0,
    },

    {
        "machine_id": "QA-02",
        "machine_name": "Vision System 2",
        "machine_type": "Vision System",
        "production_stage": "Quality",
        "ideal_cycle_time_seconds": 10,
        "rated_capacity_units_per_hour": 360,
        "max_temperature_celsius": 60,
        "max_pressure_bar": 3.0,
    },

    {
        "machine_id": "QA-03",
        "machine_name": "Measurement Station 1",
        "machine_type": "Measurement Station",
        "production_stage": "Quality",
        "ideal_cycle_time_seconds": 30,
        "rated_capacity_units_per_hour": 120,
        "max_temperature_celsius": 55,
        "max_pressure_bar": 4.0,
    },

    {
        "machine_id": "QA-04",
        "machine_name": "Functional Test Station 1",
        "machine_type": "Functional Test Station",
        "production_stage": "Quality",
        "ideal_cycle_time_seconds": 60,
        "rated_capacity_units_per_hour": 60,
        "max_temperature_celsius": 65,
        "max_pressure_bar": 5.0,
    },

    {
        "machine_id": "PKG-01",
        "machine_name": "Conveyor System 1",
        "machine_type": "Conveyor System",
        "production_stage": "Packaging",
        "ideal_cycle_time_seconds": 15,
        "rated_capacity_units_per_hour": 240,
        "max_temperature_celsius": 50,
        "max_pressure_bar": 2.0,
    },

    {
        "machine_id": "PKG-02",
        "machine_name": "Conveyor System 2",
        "machine_type": "Conveyor System",
        "production_stage": "Packaging",
        "ideal_cycle_time_seconds": 12,
        "rated_capacity_units_per_hour": 300,
        "max_temperature_celsius": 50,
        "max_pressure_bar": 2.0,
    },

    {
        "machine_id": "PKG-03",
        "machine_name": "Packaging Robotic Arm 1",
        "machine_type": "Robotic Arm",
        "production_stage": "Packaging",
        "ideal_cycle_time_seconds": 15,
        "rated_capacity_units_per_hour": 240,
        "max_temperature_celsius": 65,
        "max_pressure_bar": 6.0,
    },

    {
        "machine_id": "PKG-04",
        "machine_name": "Packaging Robotic Arm 2",
        "machine_type": "Robotic Arm",
        "production_stage": "Packaging",
        "ideal_cycle_time_seconds": 15,
        "rated_capacity_units_per_hour": 240,
        "max_temperature_celsius": 65,
        "max_pressure_bar": 6.0,
    },

    ]
    mc = pd.DataFrame(machines)
    return mc

def create_defects():
    defects = [
            {
                "defect_id": "DEF-001",
                "defect_name": "Dimensional Deviation",
                "defect_category": "Dimensional",
                "severity": "Major",
                "production_stage": "Assembly",
            },
            {
                "defect_id": "DEF-002",
                "defect_name": "Surface Defect",
                "defect_category": "Cosmetic",
                "severity": "Minor",
                "production_stage": "Assembly",
            },
            {
                "defect_id": "DEF-003",
                "defect_name": "Assembly Misalignment",
                "defect_category": "Assembly",
                "severity": "Major",
                "production_stage": "Assembly",
            },
            {
                "defect_id": "DEF-004",
                "defect_name": "Measurement Out of Specification",
                "defect_category": "Dimensional",
                "severity": "Major",
                "production_stage": "Quality",
            },
            {
                "defect_id": "DEF-005",
                "defect_name": "Vision Inspection Failure",
                "defect_category": "Quality",
                "severity": "Major",
                "production_stage": "Quality",
            },
            {
                "defect_id": "DEF-006",
                "defect_name": "Functional Test Failure",
                "defect_category": "Functional",
                "severity": "Major",
                "production_stage": "Quality",
            },
            {
                "defect_id": "DEF-007",
                "defect_name": "Damaged Packaging",
                "defect_category": "Packaging",
                "severity": "Minor",
                "production_stage": "Packaging",
            },
            {
                "defect_id": "DEF-008",
                "defect_name": "Incorrect Label",
                "defect_category": "Labeling",
                "severity": "Major",
                "production_stage": "Packaging",
            },
            {
                "defect_id": "DEF-009",
                "defect_name": "Missing Component",
                "defect_category": "Packaging",
                "severity": "Major",
                "production_stage": "Packaging",
            },
        ]

    dim_defect = pd.DataFrame(defects)
    return dim_defect

def create_products():
    products = [
        {
            "product_id": "PRD-001",
            "product_name": "Product A",
            "product_category": "Finished Good",
            "description": "Primary manufactured product",
        }
    ]

    dim_product = pd.DataFrame(products)

    return dim_product

def create_shifts():
    shifts = [
        {
            "shift_id": "SHIFT-001",
            "shift_name": "Day Shift",
            "start_time": "06:00",
            "end_time": "18:00",
        },
        {
            "shift_id": "SHIFT-002",
            "shift_name": "Night Shift",
            "start_time": "18:00",
            "end_time": "06:00",
        },
    ]

    dim_shift = pd.DataFrame(shifts)

    return dim_shift

def create_operators():
    operators = [
        {"operator_id": "OP-001", "operator_name": "Operator 001", "team": "Assembly"},
        {"operator_id": "OP-002", "operator_name": "Operator 002", "team": "Assembly"},
        {"operator_id": "OP-003", "operator_name": "Operator 003", "team": "Assembly"},
        {"operator_id": "OP-004", "operator_name": "Operator 004", "team": "Assembly"},
        {"operator_id": "OP-005", "operator_name": "Operator 005", "team": "Assembly"},
        {"operator_id": "OP-006", "operator_name": "Operator 006", "team": "Assembly"},

        {"operator_id": "OP-007", "operator_name": "Operator 007", "team": "Quality"},
        {"operator_id": "OP-008", "operator_name": "Operator 008", "team": "Quality"},
        {"operator_id": "OP-009", "operator_name": "Operator 009", "team": "Quality"},
        {"operator_id": "OP-010", "operator_name": "Operator 010", "team": "Quality"},
        {"operator_id": "OP-011", "operator_name": "Operator 011", "team": "Quality"},

        {"operator_id": "OP-012", "operator_name": "Operator 012", "team": "Packaging"},
        {"operator_id": "OP-013", "operator_name": "Operator 013", "team": "Packaging"},
        {"operator_id": "OP-014", "operator_name": "Operator 014", "team": "Packaging"},
        {"operator_id": "OP-015", "operator_name": "Operator 015", "team": "Packaging"},
    ]

    dim_operator = pd.DataFrame(operators)

    return dim_operator