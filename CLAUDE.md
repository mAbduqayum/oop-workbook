# Python Workbook Project

This is a structured collection of Python programming exercises,
designed for learning and practice.

## Project Structure

- Each exercise is in a numbered directory
  - `0**` class basics
  - `1**` oop inheritance
  - `2**` oop encapsulation
- Exercise directories contain:
  - `*.md` file with problem description, examples, and formulas.
- Reference materials are in `x0_*/` directories

## Exercise Categories

- **Basic I/O**: Hello world, user input/output
- **Computer Science**: Arithmetic, geometry, area/perimeter calculations
- **Mathematics**: Arithmetic, geometry, area/perimeter calculations
- **Physics**: Free fall, ideal gas law, pressure conversions
- **Chemistry**: Free fall, ideal gas law, pressure conversions
- **Biology**: Free fall, ideal gas law, pressure conversions
- **Finance**: Interest calculations, tip calculators, banking
- **Time/Date**: Time conversions, date calculations
- **Utilities**: Sorting, string manipulation, unit conversions

## Exercise Workflow

1. Read the `.md` file to understand requirements
2. Create `*.py` and solve the question 
3. Create `test_*.py` and unit test the solution
4. Don't write comments/docs in solutions/tests.
5. Don't create python files and tests for docs or appendix sections

## Commands
- `uv run filename.py` to run python files
- `uv run pytest dir/` to run pytest in specific directory
- `git mv` to reorder files. don't use temp dirs, the dirs are unique even without enumeration
