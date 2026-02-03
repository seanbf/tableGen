# Style Guide

## Code Formatting

- Use [PEP 8](https://www.python.org/dev/peps/pep-0008/) as the standard
- Line length: 88 characters (Black formatter compatible)
- Use 4 spaces for indentation

## Naming Conventions

- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private members**: prefix with `_`

## Documentation

- Write docstrings for all public functions and classes
- Use triple quotes: `"""`
- Follow Google or NumPy docstring format

## Imports

- Group imports: standard library, third-party, local
- One import per line for modules
- Use `import x` or `from x import y`

## Type Hints

- Use type hints for function signatures
- Example: `def function(param: str) -> bool:`

## Testing

- Write tests for all public functions
- Use `pytest` for test framework
- Test file naming: `test_*.py`

## Tools

- Package management with **uv**
- Lint and format with **uv ruff**
  - Run checks: `uv ruff check`
  - Auto-format: `uv ruff format`
