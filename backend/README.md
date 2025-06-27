# Backend Application

## Virtual Environment

To activate the virtual environment for the backend application:

```bash
source backend/.venv/bin/activate
```

## Package Management

### Adding Packages

To add a new package to the backend application:

```bash
uv add <package_name>
```

### Exporting Requirements

To export the current dependencies to a requirements.txt file:

```bash
uv export --format requirements-txt --output-file requirements.txt
```
