# Como base usaremos Alpine
FROM alpine:latest

# instalamos las dependencias
RUN apk update
RUN apk add python3 py3-pip bash
RUN python3 -m venv /venv

# instalamos invoke sobre el entorno virtual
RUN /venv/bin/pip install invoke

# copiamos los ficheros
COPY src /sonder/src

# establecemos el directorio de trabajo
WORKDIR /sonder/src

# Establecemos el usuario como root
USER root

# ejecutamos los test
CMD ["/venv/bin/invoke", "test"]

#docker build -t sonder .
#docker run sonder