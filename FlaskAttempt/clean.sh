##NOTE: This will remove all running containers. Proceed with caution
##You can manually remove the `flask-attempt` containers if needed
docker rm -vf $(docker ps -a -q)
deactivate
rm -rf venv
