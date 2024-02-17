#!/bin/bash

# Define variables
DOCKER_USERNAME="shoryasngh"
DOCKER_PASSWORD="Shorya@_1104"
DOCKER_REGISTRY="docker.io" # Or specify your Docker registry address if different

# Login to Docker registry
echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin "$DOCKER_REGISTRY"

# Check if login was successful
if [ $? -eq 0 ]; then
    echo "Login to Docker registry successful"
else
    echo "Failed to login to Docker registry"
fi
