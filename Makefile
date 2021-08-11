# import config.
cnf-dev ?= config-dev.env
include $(cnf-dev)

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

run-dev: ## Run locally using variables in the config-local file
	echo "==================================="
	echo "Setting local environment variables"
	echo "==================================="
	cat ./config-dev.env
	source ./config-dev.env
	NATS_SERVER=$(NATS_SERVER) NATS_SUBJECT=$(NATS_SUBJECT) python3 main.py

git-submodule-update: ## Update all the submodules for this project
	git submodule update --init --recursive
	git submodule update --recursive --remote
