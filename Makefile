run-docker:
	@docker run --rm -e REDIS_URL="redis://redis" --cpus="1.0" --memory="1000M" -p 5050:5050 --network fastapi-redis-flashes-messages_flashes-network --name flashes flashes:dev