To run the clustertest, start the redis container using
```commandline
docker compose -f ../docker-compose.yml up redis
```
then
```commandline
uv run pytest -v
```