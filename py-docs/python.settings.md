# Python settings

## make default `python` command from other version installed

```
sudo ln -s /opt/homebrew/bin/python3.11 /opt/homebrew/bin/python

~  $ where python
/opt/homebrew/bin/python
~  $ python --version
Python 3.11.2
```

## run python unbuffered mode

allows the print() statements to be immediately displayed in the console:

```
python -u your_server_script.py
```
