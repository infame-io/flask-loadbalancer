#docker build -t nginx8080 . --no-cache
#docker build -t nginx8081 . --no-cache
#docker build -t nginx8082 . --no-cache

docker run -d --name nginx8080 -it -p 8080:8080 nginx8080
docker run -d --name nginx8081 -it -p 8081:8081 nginx8081
docker run -d --name nginx8082 -it -p 8082:8082 nginx8082
