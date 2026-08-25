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