# debug py code with docker compose

## Applying Code Updates

docker volume:

`docker-compose.yaml`

```
  app:
    build: app
    restart: always
    volumes:
      - ./app/src:/code
```

`server.py`

```py
server.run(debug=True, host='0.0.0.0', port=5000)
```

If we check the logs of the app container we see that the flask server is running in debugging mode.

```
$ docker-compose logs app
Attaching to project_app_1
app_1 | * Serving Flask app "server" (lazy loading)
app_1 | * Environment: production
app_1 | WARNING: This is a development server. Do not use it in a production deployment.
app_1 | Use a production WSGI server instead.
app_1 | * Debug mode: on
app_1 | * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
app_1 | * Restarting with stat
app_1 | * Debugger is active!
app_1 | * Debugger PIN: 315-974-099
```

Once we update the source code and save, we should see the notification in the logs and reload.

```
$ docker-compose logs app
Attaching to project_app_1
app_1 | * Serving Flask app "server" (lazy loading)
...
app_1 | * Debugger PIN: 315-974-099
app_1 | * Detected change in '/code/server.py', reloading
app_1 | * Restarting with stat
app_1 | * Debugger is active!
app_1 | * Debugger PIN: 315-974-099
```

## Debuggin Code

Export port

`docker-compose.yaml`

```
  app:
    build: app
    restart: always
    volumes:
      - ./app/src:/code
    ports:
      - 5678:5678
```

`server.py`

```
import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 5678))
```

`requirements.txt`

```
Flask==1.1.1
mysql-connector==2.2.9

ptvsd==4.3.2
```

vscode `launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Remote Attach",
      "type": "python",
      "request": "attach",
      "port": 5678,
      "host": "localhost",
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}/app/src",
          "remoteRoot": "/code"
        }
      ]
    }
  ]
}
```

We need to make sure we update the path map locally and in the container.

Once we do this, we can easily place breakpoints in the IDE, start the debugging mode based on the configuration we created and, finally, trigger the code to reach the breakpoint.
