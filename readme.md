# Python

## virtualenv

```
# Windows cmd
λ .venv\Scripts\activate

# Windows powershell
$ .venv\Scripts\Activate.ps1

(.venv) λ where python
C:\Users\webnl\Documents\_workspace\loggar-py\.venv\Scripts\python.exe
C:\_dev\python\Python37-32\python.exe


# MacOS
$ . ./venv/activate

(.venv) λ which python
/c/Users/webnl/Documents/_workspace/loggar-py/.venv/Scripts/python
```

## requirements

```
(.venv) λ pip install -r requirements.txt

(.venv) λ pip list
```

## pytest

```
pytest
```

## pytest-cov

code-coverage with pytest

```
pytest --cov=my_project_name

python -m pytest --cov --cov-report=html:_pytest-report/html_dir --cov-report=xml:_pytest-report/coverage.xml lib-being-tested.module
```

## pytype

> does not work on Windows (v2019.3.15)

generating a sample config file:

```
$ pytype --generate-config pytype.cfg
```

`pytype.cfg`

```cfg
[pytype]

exclude =
    **/*_test.py
    **/test_*.py
    **/*_test_*.py
    
inputs =
    py-dev/pytype

output = _pytype_output

python_version = 3.7

pythonpath =
    .venv/Scripts
```

run pytype:

```
$ pytype --config=pytype.cfg
```
