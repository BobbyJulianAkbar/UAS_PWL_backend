# UAS_PWL_backend

## Getting Started

Change directory into your newly created project if not already there. Your
current directory should be the same as this README.txt file and setup.py.

```
cd inventory
```

Create a Python virtual environment, if not already created.

```
python -m venv venv
```

or

```
python3 -m venv venv
```

Activate virtual environment.

```
venv\Scripts\activate #for Windows OS
```

Upgrade packaging tools, if necessary.

```
install --upgrade pip setuptools
```

Install the project in editable mode with its testing requirements.

```
pip install -e ".[testing]"
```

Initialize and upgrade the database using Alembic.

- Generate your revision.
  
  ```
  alembic -c development.ini revision --autogenerate -m "Migrate to my db"
  ```
  
- Upgrade to that revision.

  ```
  alembic -c development.ini upgrade head
  ```

Load default data into the database using a script.

```
initialize_inventory_db development.ini
```

Run your project's tests.

```
pytest
```
Run your project.

```
pserve development.ini
```

## Dependencies

List of dependencies:
- pyramid
- cookiecutter
- alembic
- sqlalchemy
- mysql-connector-python
- mysqlclient
