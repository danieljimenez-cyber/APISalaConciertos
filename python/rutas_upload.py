from __future__ import print_function
from __main__ import app
from flask import request, make_response
import os
import json
import sys

@app.route ('/upload', methods=['POST']) 
def upload():
    try:
        if (validar_session_normal()):
            f= request.files['fichero']
            user_input = request.form.get("nombre")
            basepath = os.path.dirname(__file__) # ruta del archivo actual
            upload_path = os.path.join (basepath,'static',user_input) 
            print('lugar' +  upload_path, file=sys.stdout)
            f.save(upload_path)
            respuesta={"status": "OK"}
            code=200
        else:
            respuesta={"status":"Forbidden"}
            code=403
    except:
        respuesta={"status": "ERROR"}
        code=500
    response=make_response(json.dumps(respuesta),code)
    return response