IMAGE_NAME := quiz
VERSION := $(shell git describe --tags --always --dirty)
PORT := 9090
CONTAINER_PORT := 8000

.PHONY: help build run daemonize push

default: build daemonize

help:
	@echo "Makefile commands:"
	@echo "  make		    - Runs build and daemonize"
	@echo "  make build     - Build Docker image with tag $(VERSION)"
	@echo "  make run       - Run Docker container"
	@echo "  make daemonize - Run Docker container as daemon"

build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

run:
	docker run --rm -it -p $(PORT):$(CONTAINER_PORT) $(IMAGE_NAME):$(VERSION)

daemonize:
	docker run -d -p $(PORT):$(CONTAINER_PORT) $(IMAGE_NAME):$(VERSION)