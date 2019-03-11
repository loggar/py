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
```
