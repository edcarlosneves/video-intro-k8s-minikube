#!/bin/bash

VERSION=$(cat VERSION)

if [ -z "$(docker images -q edcarlosneves/generate-order:$VERSION 2> /dev/null)" ]; then
    echo "Creating image."
    docker build -t edcarlosneves/generate-order:$VERSION .
    echo $(date) "->" $VERSION >> VERSION-HISTORY
else
    echo "Image with tag $VERSION already exists."
fi