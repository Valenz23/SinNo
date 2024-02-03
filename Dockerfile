# Utilizo una imagen de Python slim como base
FROM python:3.8-slim

# Instalo las dependencias necesarias
RUN apt-get update

# Copio el archivo requirements.txt
COPY requirements.txt requirements.txt

# Instalo las dependencias desde requirements.txt
RUN pip install -r requirements.txt

# Configuro el directorio de trabajo
WORKDIR /sonder/src

# Copio los archivos de tu aplicación
COPY src /sonder/src

# Establezco el comando por defecto para ejecutar los tests y activar la API
# CMD ["sh", "-c", "invoke test && hug -f api/sonder_api.py"]
# CMD ["sh", "-c", "invoke test"]
CMD ["sh", "-c", "hug -f api/sonder_api.py"]