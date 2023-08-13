VM=alpine

build:
	docker pull ${VM}
	docker container run --rm -t -d --name ${VM} ${VM}

run:
	docker exec -it -u root ${VM} sh
