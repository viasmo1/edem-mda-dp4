# edem-mda-dp4
Deploy a Flask application with Docker:
---
1. Clone repo
2. Build docker image:
```
  $ docker build -t flask_prueba .
```

3. Build docker container
```
  $ docker run -p 5000:5000 flask_prueba
```
4. Visit the website: http://0.0.0.0:5000
