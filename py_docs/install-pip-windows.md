# python environments

## install pip on windows system

Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py. This will install pip.

```
λ python get-pip.py
```

```
λ pip --version
pip 10.0.1 from c:\_dev\python\python37-32\lib\site-packages\pip (python 3.7)
```

## Update pip

```
python -m pip install --upgrade pip
```

## pip list

```
$ pip search "query"

$ pip show package-name

$ pip list

$ pip list --outdated
```

## pip install

```
$ pip install package-name

$ pip install package-name==1.0.0

$ pip install package-name --upgrade

$ pip install package-name --upgrade --force-reinstall

$ pip uninstall package-name
```
