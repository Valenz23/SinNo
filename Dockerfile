# Utilizo una imagen de Python slim como base
FROM python:3.8-slim

# Instalo las dependencias necesarias
RUN apt-get update

# Instalo las dependencias de la aplicación
RUN pip install hug invoke pandas

# Configuro el directorio de trabajo
WORKDIR /sonder/src

# Copio los archivos de tu aplicación
COPY src /sonder/src

# Establezco el comando por defecto para ejecutar los tests y activar la API
# CMD ["sh", "-c", "invoke test && hug -f api/sonder_api.py"]
CMD ["sh", "-c", "invoke test"]