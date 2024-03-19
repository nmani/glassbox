ARG PYTHON_VER=3.12-slim
FROM docker.io/library/python:$PYTHON_VER

LABEL org.opencontainers.image.authors  = "Naveen Manivannan <naveen.manivannan@gmail.com>" \
      org.opencontainers.image.source   = "https://github.com/nmani/glassbox" \
      org.opencontainers.image.licenses = "MIT"

FROM apt-get update \
    && apt-get upgrade -qqy \
    && pip install poetry \
    && apt-get autoremove -qqy \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/list/*
