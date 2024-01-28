# Como base usaremos Alpine
FROM alpine:latest

# instalamos las dependencias
RUN apk update
RUN apk add python3 py3-pip bash
RUN apk add hug logging

# hacemos el entorno virtual para invoke y lo instalamos
RUN python3 -m venv /venv
RUN /venv/bin/pip install invoke

# copiamos los ficheros
COPY src /sonder/src

# establecemos el directorio de trabajo
WORKDIR /sonder/src

# ejecutamos los test
CMD ["/venv/bin/invoke", "test"]