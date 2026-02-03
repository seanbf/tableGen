# Table Generation

This tool is used to generate Idq (direct/quadrature currents) tables for PMAC (Permanant magnet Altneating Current Motors) .

## Configuration 

A YAML file is provided `<root>\config\config.yaml` . Although the tool is provided with “sensible” defaults, the user may wish to adjust these.

The file contains configurable fields for; defaults, min/max values, data headers.

## Inputs

The user will be prompted throughout the process to provide the following information:

### Motor Parameters

- Pole Pairs
- Kemf

### Measurement Data

A `.csv` file that includes the following headers , at a minimum:

- Torque Measured
- Speed Measured
- Direct-Axis Current (Id)
- Quadrature-Axis Current (Iq)
- Direct-Axis Voltage (Ud)
- Quadrature-Voltage (Uq)

## Process

### Data Pre Process

The measurement data will be formatted to an internal format for consistenancy.

Using the Motor Parameters and the measurement data extra values are calculated for Flux Linkages and Electromagentic Torque.

### Table Generation