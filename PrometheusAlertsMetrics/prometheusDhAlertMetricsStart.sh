docker build --tag prometheus-deephaven/grpc-api .
docker build --tag flask/prometheus-webhook-alerts flask-app
docker-compose up
