IMAGE=odahub/oda-metrics:$(shell git describe --always --tags)

build:
	docker build . -t $(IMAGE)
