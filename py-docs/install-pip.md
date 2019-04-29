# python environments, install pip

## install pip on windows system

Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py. This will install pip.

```
λ python get-pip.py
```

```
λ pip --version
pip 10.0.1 from c:\_dev\python\python37-32\lib\site-packages\pip (python 3.7)
```

## install pip on linux system

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

$ python get-pip.py

$ python3 -m pip --version
```

## Update pip

```
python -m pip install --upgrade pip

# or

python3 -m pip install --user --upgrade pip
```

