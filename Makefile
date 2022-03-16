TAG=$(shell git describe --always --tags)
IMAGE=odahub/oda-metrics:$(TAG)

up: build
	helm upgrade --install oda-metrics . \
		--set image.tag=$(TAG)

               #USER_ID=$(shell id -u) && \

build:
	docker build . -t $(IMAGE)
	docker push $(IMAGE)
