

# Transformer Efficiency Calculator

## Overview

This project provides tools for calculating the efficiency of transformers. It includes two implementations:
1. **Command-Line Version**: A simple Python script for calculating transformer efficiency via terminal input.
2. **GUI Version**: A graphical user interface (GUI) version using `tkinter` for a more interactive experience.

## Features

- **Command-Line Version**: 
  - Calculate transformer efficiency with user-provided input values for output power, core losses, and copper losses.
  - Easy to run and use directly from the command line.

- **GUI Version**:
  - Interactive interface to input values and calculate efficiency.
  - User-friendly design with real-time feedback and error handling.

## Requirements

- Python 3.x
- `tkinter` (included with Python standard library)

## Usage

### Command-Line Version

1. Save the file as `transformer_efficiency_calculator.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using:
   ```bash
   python transformer_efficiency_calculator.py
   ```
5. Follow the prompts to enter output power, core losses, and copper losses. The efficiency will be calculated and displayed.

### GUI Version

1. Save the file as `transformer_efficiency_calculator_gui.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script using:
   ```bash
   python transformer_efficiency_calculator_gui.py
   ```
5. A graphical user interface will open. Enter the output power, core losses, and copper losses in the provided fields, and click "Calculate Efficiency" to see the result.

## Example

**Command-Line Output:**
```
Enter the output power (in watts): 500
Enter the core losses (in watts): 50
Enter the copper losses (in watts): 25

Transformer Efficiency: 85.71%
```

**GUI Example:**
- Input fields for output power, core losses, and copper losses.
- Display of efficiency in a user-friendly format.



---
