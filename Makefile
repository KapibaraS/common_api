.PHONY: run exec


run:
	@docker-compose up

run-db:
	@docker-compose up mongodb

down:
	@docker-compose down

build:
	@docker-compose build

exec:
	@docker-compose exec mongodb mongo

kill-user:
	@sudo fuser -k 27017/tcp

stop-docker:
	@docker stop $(docker ps -aq)

remove-docker:
	@docker rm $(docker ps -aq)
	@docker rmi $(docker images -q)

ps:
	docker ps -a
