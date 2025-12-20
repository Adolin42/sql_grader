# SQL Autograder - References

This document lists all external sources and references used in this project.

## Python Standard Library

- **Error Handling (try/except)**: https://docs.python.org/3/tutorial/errors.html
  - Used for exception handling in config parser and database module

- **Context Managers (with statement)**: https://docs.python.org/3/reference/compound_stmts.html#with
  - Used in DatabaseConnection class to ensure resources are properly closed

- **Classes and Objects**: https://docs.python.org/3/tutorial/classes.html
  - Used for DatabaseConnection class definition

- **JSON Module**: https://docs.python.org/3/library/json.html
  - Used for parsing configuration JSON files

- **sys Module**: https://docs.python.org/3/library/sys.html
  - Used for sys.exit() in config validation errors

## Third-Party Libraries

- **PyMySQL**: https://pymysql.readthedocs.io/
  - MySQL database driver for Python
  - Used for executing queries and connecting to MySQL databases
  - DictCursor documentation: https://pymysql.readthedocs.io/en/latest/modules/cursors.html

## Project Components

- `config_parser.py`: Validates configuration JSON structure
- `database.py`: Handles MySQL connections and query execution
- `test_config.json`: Sample configuration file for testing

## Notes

Add new references here as new components are developed.
