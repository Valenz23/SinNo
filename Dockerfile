# Como base usaremos Alpine
FROM alpine:latest

# etiquetas
LABEL version="0.3.1"
LABEL description="Contenedor de la imagen de SONDER"
LABEL maintainer="Pablo Valenzuela Álvarez --> <valenbetis@gmail.com>"

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

# ejecutamos los test
CMD ["/venv/bin/invoke", "test"]