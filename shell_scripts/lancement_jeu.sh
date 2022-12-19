#!/bin/bash

case $1 in
    "mario")
        eval docker rm -f mario
        eval dokcer run --name mario -d -p 8600:8080 pengbai/docker-supermario
    ;;
    "2048")
        eval docker rm -f 2048
        eval docker run --name 2048 --rm -it -d -p 8080:80 inglebard/retroarch-web
    ;;
    *)
        echo jeu indisponible
    ;;
esac