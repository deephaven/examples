#docker build --tag flask/local ./flask-local
#docker run -d -p 5000:5000 flask/local
docker-compose up -d
python flask-app/server.py
