# Code Insight – Python Static Code Analyzer

Code Insight is a command-line tool that analyzes Python source files and provides structural insights about the code.

## Overview

This project was built to understand how source code can be programmatically inspected and evaluated.  
It performs structural analysis on Python files and provides basic complexity estimation.

## Features

- Counts total lines of code
- Detects blank lines
- Counts comment lines
- Identifies number of functions
- Identifies number of classes
- Provides rule-based complexity evaluation (Low / Medium / High)

## Technical Design

The project follows a modular architecture:

- `analyzer.py` handles command-line input and formatted output
- `utils.py` contains the core analysis logic
- Clear separation of concerns improves maintainability

## How to Run

1. Clone the repository:

   git clone https://github.com/05khushipatel/code-insight.git

2. Navigate into the folder:

   cd code-insight

3. Run the analyzer:

   python analyzer.py sample.py

## Example Output

Analysis of: sample.py  
Total Lines: 8  
Blank Lines: 2  
Comment Lines: 1  
Functions: 2  
Classes: 1  
Complexity Level: Low  

## Future Improvements

- AST-based parsing for more accurate analysis
- Cyclomatic complexity calculation
- Directory-wide analysis
- Support for additional programming languages