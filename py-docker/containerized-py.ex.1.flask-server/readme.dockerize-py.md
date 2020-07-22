# dockerize an python app

```
docker build -t my-py-flask-image .
```

```
docker run -d -p 5000:5000 my-py-flask-image
```

```
curl http://localhost:5000
```
