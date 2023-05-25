#!/bin/bash

# Setup default fail steps
fail_build() {
    clean_up
    if [ -n "$1" ]; then
        echo "Failing Integration Build at : $1"
    else
        echo "Failing Integration Build"
    fi
    exit 1  # stop building
}

clean_up() {
    # Stop and remove all containers and images
    docker compose -f docker-compose.yml down -v --rmi all
}

wait_for() {
    echo "Waiting for $1 ready ... "
    while [[ $(docker inspect -f '{{.State.Health.Status}}' $1) != 'healthy' ]]
    do
        sleep 1
        echo "."
    done
    echo "$1 is healthy!"
}

echo "Start Integration Build ..."

# Build the environment
docker compose -f docker-compose.yml build || fail_build "Build"

# Start the environment
docker compose -f docker-compose.yml up -d || fail_build "Deployment"

# Use health check to make sure the container is ready
wait_for "seedcase_webapp"

echo "Run unit test"
# Run unit tests in app container
docker compose -f docker-compose.yml exec -T web pytest || fail_build "Unit
Tests"

echo "Seedcase is ready to use!"