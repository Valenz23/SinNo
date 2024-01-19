import hug
import logging

# COPIUM https://github.com/Nastard/F1Department/blob/main/f1department/f1department_api.py
# COPIUM https://github.com/Nastard/F1Department/blob/main/tests/test_f1department_api.py

logging.basicConfig(filename='./app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)



@hug.get('/status')
def status():
    logging.info("Checking status")
    return{"status":"OK"}

