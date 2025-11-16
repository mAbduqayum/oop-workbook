# Python Workbook Project

This is a structured collection of Python programming exercises,
designed for learning and practice.

## Project Structure

```txt
│oop-workbook
├── chapter
│ ├── chapter_docs
│ ├── chapter_question
│ │ ├── chapter_question.md
│ │ ├── chapter_question.py
│ │ └── test_chapter_question.py
│ ├── ...
│ ├── chapter_question
```

## Question Creation

- First create the question in `*.md` format
- Then create the test file - `test_*.py` file
- Then solve it in `*.py` file
- Use `uv run pytest` command to run pytest for the question
- make sure the examples section in the Markdown question has the right outputs shown.  

### Question Refactoring

- update all three files if necessary

## Commands

- `uv run filename.py` to run python files
- `git mv` to move files around
