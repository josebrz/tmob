# Constants
API_NAME = server

# Commands
compose_cmd = docker-compose -f ./docker-compose.yml
down_cmd = $(compose_cmd) down --remove-orphans
exec_cmd = docker exec -it $(API_NAME)

# Targets

down:
	@echo "Removing containers and orphans..."
	@$(down_cmd)

down_all:
	@echo "Removing containers with their volumes and images..."
	@$(down_cmd) --volumes

exec:
	@$(exec_cmd) bash

logs:
	@$(compose_cmd) logs --tail=all -f | grep $(API_NAME)

start:
	@$(compose_cmd) start

test:
	@$(exec_cmd) pytest

up:
	@$(compose_cmd) up -d
