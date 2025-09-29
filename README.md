# CPU-Scheduler-using-tkinter

A Python GUI application for simulating CPU scheduling algorithms with Gantt chart visualization.

## Features

- Graphical User Interface (Tkinter)
- Supports multiple scheduling algorithms:
  - First-Come-First-Serve (FCFS)
  - Shortest Job First (SJF) *(in progress)*
  - Priority Scheduling *(in progress)*
  - Round Robin *(in progress)*
- Generate random process data for testing
- Import and display CSV files with process data
- Visualize scheduling results in tables and Gantt charts (using Matplotlib and Plotly)

## File Structure

- `algos.py` — Scheduling algorithms (FCFS implemented, SJF in progress)
- `application_file.py` — Main Tkinter GUI application
- `datagen.py` — Random data generation for processes
- `gantt.py` — Gantt chart visualization using Plotly
- `Random_data/` — Folder for generated CSV files
    - `test.csv` — Example process data
- `README.md` — Project documentation

## Getting Started

### Prerequisites

- Python 3.x
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - plotly
  - pandastable
  - tkinter (usually included with Python)

Install dependencies with pip:

```sh
pip install pandas numpy matplotlib plotly pandastable
```

### Running the Application

```sh
python application_file.py
```

### Generating Random Data

Use the "New" option in the GUI to generate random process data, or run:

```sh
python datagen.py
```

### Visualizing Gantt Charts

You can visualize a Gantt chart for a CSV file using:

```sh
python gantt.py
```

## Example

Sample process data format (`Random_data/test.csv`):

```
process_number,arrival_time,cpu_burst_time,priority
0,10,34,3
1,15,75,8
...
```

## Notes

- Only FCFS is fully implemented; other algorithms are under development.
- The GUI allows you to open, view, and schedule processes from CSV files.

## License

This project is for educational purposes.
