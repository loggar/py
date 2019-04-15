# `setup.py`

## install modules via `setup.py`

```
python setup.py build

python setup.py install
```

## uninstall packages/modules via `setup.py`

if you use pip to install packages,

```
pip install package-name

pip uninstall package-name
```

but if you use `setup.py`

```
sudo python setup.py install --record files.txt

sudo cat files.txt | sudo xargs rm -rf
```
