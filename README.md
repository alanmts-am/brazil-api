# BRAZIL API 

[README, PT-BR](docs/README-PT-BR.md)

 This idea encompasses a more direct way of dealing with data from Brazil.

## How to Run

The project uses Poetry to manage all dependencies. It should be installed depending on the machine.

Ubuntu/Debian

```Shell
pip install poetry
```

To install all dependencies

```Shell
poetry install
```

To run the API locally
```Shell
poetry run uvicorn app.main:app --host 0.0.0.0 --port {PORTA}
```
## Virtual Environment

For better project performance on your machine, it is recommended to start it in a virtual environment. In this case, you can use Python's virtualenv.

```Shell
pip install virtualenv
```
Then, specify the folder for the Python modules

```Shell
python3 -m venv {NOME_PASTA}
```

To activate the virtual environment, run the following command

```Shell
source {NOME_PASTA}/bin/activate
```

While in the virtual environment, to deactivate it, run

```Shell
deactivate
```

## Data Loaded by the API

- [X] Countries (/countries)
- [X] States (/states)
- [X] Regions (/regions)
- [X] Cities (/cities)

All endpoints will be the same depending on your base URL

* /{base} - lists all data about the entity
* /{base}/{id} - lists data of a specific entity
* /{base}/names - returns only the names of each entity