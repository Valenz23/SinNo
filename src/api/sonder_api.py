import hug # desde .. huf -f api/sonder_api.py
import logging
import random


from clases.user import *
from clases.cancion import *

# COPIUM https://github.com/Nastard/F1Department/blob/main/f1department/f1department_api.py
# COPIUM https://github.com/Nastard/F1Department/blob/main/tests/test_f1department_api.py

# configuracion de logging
logging.basicConfig(filename='./logs/app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)

@hug.get('/status')
def status():
	mensaje = "Servicio disponible"
	status = "OK"
	logging.info(mensaje)
	return {
		"mensaje":mensaje,
		"status":status
    }

@hug.not_found()
def not_found_handler():
	mensaje = "Servicio no encontrado"
	status = "Not Found"
	logging.error(mensaje)
	return {
		"mensaje":mensaje,
		"status":status
    }

@hug.get('/buscar')
def api_buscar_cancion(atributo:str, valor:str):
   
    busqueda = buscarCancion(atributo,valor)
    cancion = ""
    status = ""

    if busqueda:
        mensaje = f"Encontrada cancion: campo: {atributo} | valor: {valor}"
        logging.info(mensaje)
        cancion = busqueda[0]
        status = "OK"
    else:
        mensaje = f"No se encontro ninguna cancion: campo: {atributo} | valor: {valor}"
        logging.error(mensaje)
        status = "Not Found"

    return{
        "message":mensaje,
        "song":cancion,
        "status":status
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

