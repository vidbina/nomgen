# This Makefile assists in creating and managing the container. Make you life
# easer and use it :wink:
#
# Run `make image` to build the image
# Run `make list-containers` to list the project containers
# Run `make list-images` to list the project images
# Run `make clean-containers`
# Run `make clean-image`
# Run `make shell` to drop in at the shell of the container
SHELL=/bin/sh
DOCKER=docker
GIT=git

CONTAINER_RUNS=${DOCKER} run \
		--rm \
		-it \
		-v "${PWD}:/src" \
		-w "/src" \
		python:3.3-alpine

repl:
	${CONTAINER_RUNS} python

shell:
	${CONTAINER_RUNS} /bin/sh

.PHONY: \
  repl mech
