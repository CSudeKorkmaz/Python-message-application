all: build
DOCKER_IMAGE = Dockerfile
build:
	@echo "building docker image"
	docker build -t $(DOCKER_IMAGE) .

push:
	@echo "Setting minikube docker environment"
	@minikube start
	@& minikube -p minikube docker-env --shell powershell | Invoke-Expression
	docker build -t $(DOCKER_IMAGE) .

deploy:
	kubectl apply -f $(KUBERNETES_DEPLOYMENT)
	kubectl apply -f $(KUBERNETES_SERVICE)

url:
	minikube service fastapi-service --url
