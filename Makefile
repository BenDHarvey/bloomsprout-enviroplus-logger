# import config.
GIT_SHORT_SHA=$(shell git rev-parse --short HEAD)
GIT_BRANCH=$(shell git rev-parse --symbolic-full-name --abbrev-ref HEAD)
VERSION=$(GIT_BRANCH)_$(GIT_SHORT_SHA)

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

SHELL := /bin/bash

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

dev: ## Run locally using variables in the config-local file
	echo "Doing the thing"

install: ## Install the service
	cp ./service.tmpl /etc/systemd/system/enviroplus.service
	sudo systemctl enable enviroplus.service
	sudo systemctl start enviroplus.service
