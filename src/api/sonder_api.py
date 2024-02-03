import hug # desde .. huf -f api/sonder_api.py
import logging

from clases.user import * 
from clases.cancion import *

import mysql.connector

# configuracion de logging
logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)

def conectarDB():
    conf = {
        'host': 'mysql',
        'user': 'myuser',
        'password': 'secret',
        'database': 'sonder'
    }
    conexion = mysql.connector.connect(**conf)
    return conexion

# se prueba si la conexion a la base de datos es correcta
@hug.get('/status')
def status():

    mensaje = ''

    try:     
        conexion_db = conectarDB()
        mensaje = "Conexión a la base de datos establecida"    
        logging.info(mensaje)
        status = "OK"
    except mysql.connector.Error as err:
        mensaje = f"Error de conexión a la base de datos: {err}"    
        logging.error(mensaje)
        status = "Error"

    return { 
		"mensaje":mensaje,
		"status":status
    }

# busca la cancion
@hug.get('/buscar')
def api_buscar_cancion(atributo: str, valor: str):

    consulta = f'SELECT * FROM cancion WHERE {atributo} LIKE "%{valor}%"'
    mensaje = ''
    status = ''
    resultado = ''

    try:
        conexion_db = conectarDB()
        with conexion_db.cursor() as cursor:            
            mensaje = 'Consulta: {}'.format(consulta)
            cursor.execute(consulta)
            resultado = cursor.fetchall()
        status = "OK"
        logging.info(mensaje)

    except Exception as e:
        mensaje = f'Error en la consulta: {str(e)}'
        resultado = None
        status = "Error"
        logging.error(mensaje)

    return {
        "mensaje": mensaje,
        "resultado": resultado,
        "status": status
    }


@hug.put('/add')
def api_add_cancion(artista:str, titulo:str, letra:str):
    u = usuario()
    c = cancion(artista, titulo, letra)

    u.anadirCancion(c)

    mensaje = f"ADD cancion: artista: {artista} | titulo: {titulo} |letra: {letra}"
    status = "OK"
    
    logging.info(mensaje)
    return {
		  "mensaje":mensaje,
		  "status":status
    }

@hug.delete('/del')
def api_delete_cancion(id:str):
     
    a = admin()
    a.borrarCancion(id)
    
    mensaje = f"DELETE cancion: id: {id}"
    status = "OK"
    
    logging.info(mensaje)
    return {
		  "mensaje":mensaje,
		  "status":status
    }

@hug.put('/lote')
def api_add_lote(path:str):
     
    a = admin()
    a.anadirLote(path)     

    mensaje = f"ADD lote: path: {path}"
    status = "OK"
    
    logging.info(mensaje)
    return {
		  "mensaje":mensaje,
		  "status":status
    }

@hug.get('/lista')
def api_listar_canciones():
     
    lista = listarCanciones()
    lista = lista.to_numpy()

    mensaje = "Listando canciones por popularidad"
    status = "OK"

    logging.info(mensaje)
    return {
		  "mensaje":mensaje,
      "lista":lista,
		  "status":status
    }

@hug.put('/mod')
def api_modificar_letra(id:int, letra:str):
    u = usuario()
    mensaje = f"Modificando cancion: id: {id} | letra: {letra}"
    status = "OK"

    u.modificarLetra(id, letra)
    
    logging.info(mensaje)
    return {
		  "mensaje":mensaje,
		  "status":status
    }

