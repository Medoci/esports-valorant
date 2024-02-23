# Template
A repository formatting the standard template of a project

*Please replace this description with the purpose of this repository*

## Developer Guidance

This package uses `poetry` as a dependancy manager please refer to the documentation [poetry-docs](https://python-poetry.org).
It creates a package specifc `venv` to handle and resolve dependancies. By default the venv is established in 
...\AppData\Local\pypoetry\Cache\virtualenvs\template-aoXx48YX-py3.11\Scripts\python.exe

To get started and create a `venv` run the following...

``` sh
poetry install
```

To modify dependant packages 
``` sh
poetry add pandas
poetry remove pandas
```

For packages used in development
``` sh
poetry add flake8 --dev
poetry remove flake8
```

For debugging and to check versioning without relying on the kernel you can launch Visual Studio code from the shell
``` sh
poetry shell
code .
```

## Running guidance

*Please replace this description with how to run and navigate the project