# pytype

pytype can:

- Lint plain Python code, flagging common mistakes such as mispelled attribute names, incorrect function calls, and much more, even across file boundaries.
- Enforce user-provided type annotations. While annotations are optional for pytype, it will check and apply them where present.
- Generate type annotations in standalone files ("pyi files"), which can be merged back into the Python source with a provided merge-pyi tool.

## settins and run

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
