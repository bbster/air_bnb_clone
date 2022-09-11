#!/usr/bin/env bash

--- docker images
--- docker 이미지로 컨테이너 생성
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD="1r2r3r4r" --name PostgreSQL postgres

docker exec -it PostgreSQL /bin/bash