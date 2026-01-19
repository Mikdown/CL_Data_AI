# Copilot Instructions for CL_Data_AI

## Project Context
This is the **Code Louisville 2026 AI class** repository. It's in early stages and will grow to include AI/machine learning and data science projects and coursework.

## Architecture & Structure
- **Purpose**: Educational AI/Data Science project for Code Louisville 2026 class
- **Likely structure** (to be established):
  - `src/` or `notebooks/` - Main project code/analysis
  - `data/` - Datasets and data-related files
  - `docs/` - Documentation and guides
  - `tests/` - Unit and integration tests
  - `requirements.txt` or `pyproject.toml` - Python dependencies (if Python-based)

## Key Conventions to Follow

### Python Projects (if applicable)
- Use meaningful variable and function names that reflect data science terminology
- Document assumptions about data shapes and types in docstrings
- Include type hints for better clarity in data processing functions
- Place data loading logic separately from analysis/modeling logic

### Documentation
- Update README.md with project goals and setup instructions as features are added
- Include clear examples in documentation for any custom utilities
- Document data source schemas and any preprocessing steps

### Development Workflow
- Create feature branches for new assignments or features
- Keep commits focused and descriptive
- Test code locally before pushing
- Update documentation alongside code changes

## When Adding Code
- If creating a new Jupyter notebook, include markdown cells explaining the analysis goal
- If creating classes/modules, include docstrings with usage examples
- If working with data, document the source, format, and any transformations
- Consider reproducibility - include seeds for random operations if applicable

## Current Status
This is an initial repository with only README.md. As code is added, revisit and update this file with project-specific patterns discovered during development.
