import hug
# huf -f sonder_api.py
import logging

# COPIUM https://github.com/Nastard/F1Department/blob/main/f1department/f1department_api.py
# COPIUM https://github.com/Nastard/F1Department/blob/main/tests/test_f1department_api.py

# configuracion de logging
logging.basicConfig(filename='./app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)

# from ..clases.user import *

@hug.get('/status')
def status():
    logging.info("Servicio disponible")
    return{"status":"Vale"}

@hug.not_found()
def not_found_handler():
	logging.error("API no encontrada")
	return {"status": "No encontrada"}

@hug.get('/buscar?{atributo}&{buscar}', output=hug.output_format.text)
def buscar_cancion(buscar:str, atributo:str):

    busca = buscar_cancion(buscar=buscar,atributo=atributo)

    if busca:
        print(busca)
        msg = "Canción encontrada"
        
    else:
        msg = "Canción no encontrada"
         

    logging.info(msg)             
    return{f"status": "{}".format(msg)}
    
        
      
      

