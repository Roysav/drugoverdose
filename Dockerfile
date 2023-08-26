FROM ubuntu:latest
LABEL authors="roysa"

ENTRYPOINT ["top", "-b"]