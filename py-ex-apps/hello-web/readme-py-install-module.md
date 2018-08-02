#Install python modules

* docker-py-requirements.txt
```
Flask
Redis
```

* install modules
```
C:\_dev\python\Python36-32\Scripts\pip install --trusted-host pypi.python.org -r docker-py-requirements.txt
Collecting Flask (from -r docker-py-requirements.txt (line 1))
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 382kB/s
Collecting Redis (from -r docker-py-requirements.txt (line 2))
  Downloading redis-2.10.6-py2.py3-none-any.whl (64kB)
    100% |████████████████████████████████| 71kB 1.8MB/s
Collecting Werkzeug>=0.7 (from Flask->-r docker-py-requirements.txt (line 1))
  Downloading Werkzeug-0.12.2-py2.py3-none-any.whl (312kB)
    100% |████████████████████████████████| 317kB 1.5MB/s
Collecting itsdangerous>=0.21 (from Flask->-r docker-py-requirements.txt (line 1))
  Downloading itsdangerous-0.24.tar.gz (46kB)
    100% |████████████████████████████████| 51kB 1.4MB/s
Collecting click>=2.0 (from Flask->-r docker-py-requirements.txt (line 1))
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 1.5MB/s
Collecting Jinja2>=2.4 (from Flask->-r docker-py-requirements.txt (line 1))
  Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 1.3MB/s
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->Flask->-r docker-py-requirements.txt (line 1))
  Downloading MarkupSafe-1.0.tar.gz
Installing collected packages: Werkzeug, itsdangerous, click, MarkupSafe, Jinja2, Flask, Redis
  Running setup.py install for itsdangerous ... done
  Running setup.py install for MarkupSafe ... done
Successfully installed Flask-0.12.2 Jinja2-2.10 MarkupSafe-1.0 Redis-2.10.6 Werkzeug-0.12.2 click-6.7 itsdangerous-0.24
```