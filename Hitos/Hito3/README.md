# Hito 3: Creación de un contenedor para pruebas.
 
## Elección del contenedor base

Alpine porque es una imagen de Alpine Linux que solo pesa 7.38 MB. Después nosotros tenemos que instalar todos los paquetes necesarios para que nuestro proyecto funcione.






# miau
- docker pull alpine
- docker run --name alpinito -it alpine 
- apk get update
- apk add python3
- apk add py3-pip
- python3 -m venv /venv
- source /venv/bin/activate
- (venv) :: pip install invoke



# lista
- from alpine
- instalar: python invoke
- copiar ficheros
- realizar tests


# completer
Se llevará a cabo en las siguientes rúbricas:

    2 puntos: elección correcta y justificada del contenedor base.
    4 puntos: Dockerfile correcto, siguiendo buenas prácticas, y adaptado de forma correcta a las clases o módulos que se están testeando, incluyendo optimización del tamaño del mismo durante su construcción o a continuación.
    2 puntos: contenedor subido correctamente a Docker Hub y documentación de la actualización automática.
    2 puntos: uso de registros alternativos y públicos de contenedores (como GitHub Container Registry), con la correspondiente justificación como es natural.
