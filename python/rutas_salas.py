from flask import request, session, make_response
import json
from __main__ import app
import controlador_salas
from funciones_auxiliares import Encoder, sanitize_input, prepare_response_extra_headers,validar_session_admin,validar_session_normal

@app.route("/salas",methods=["GET"])
def salas():
    if (validar_session_normal()):
        respuesta,code= controlador_salas.obtener_salas()
    else:
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/salas/<id>",methods=["GET"])
def sala_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            respuesta,code = controlador_salas.obtener_sala_por_id(id)
        else:
            respuesta={"status":"Forbidden"}
            code=403
    else:
        respuesta={"status":"Bad parameters"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/salas",methods=["POST"])
def guardar_sala():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        sala_json = request.json
        if "nombre" in sala_json and "descripcion" in sala_json and "foto" in sala_json:
            nombre = sanitize_input(sala_json["nombre"])
            descripcion = sanitize_input(sala_json["descripcion"])
            precio = sala_json["precio"]
            foto = sanitize_input(sala_json["foto"])
            if isinstance(nombre, str) and isinstance(descripcion, str) and isinstance(foto, str) and len(nombre)<128 and len(descripcion)<512 and len(foto)<128:
                if (validar_session_admin()):
                    precio = float(precio)
                    respuesta,code=controlador_salas.insertar_sala(nombre,descripcion,precio,foto)
                else: 
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request 1"}
                code=401
        else:
            respuesta={"status":"Bad request 2"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder),code)  
    return response

@app.route("/salas/<int:id>", methods=["DELETE"])
def eliminar_sala(id):
    if (validar_session_admin()):
        respuesta,code=controlador_salas.eliminar_sala(id)
    else: 
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/salas", methods=["PUT"])
def actualizar_sala():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        sala_json = request.json
        if "id" in sala_json and "nombre" in sala_json and "descripcion" in sala_json and "foto" in sala_json:
            id = request.json["id"]
            nombre = sanitize_input(sala_json["nombre"])
            descripcion = sanitize_input(sala_json["descripcion"])
            precio = sala_json["precio"]
            foto = sanitize_input(sala_json["foto"])
            if id.isnumeric() and isinstance(nombre, str) and isinstance(descripcion, str) and precio.isnumeric() and isinstance(foto, str) and len(id)<8 and len(nombre)<128 and len(descripcion)<512 and len(foto)<128:
                id=int(id)
                precio=float(precio)
                if (validar_session_normal()):
                    respuesta,code=controlador_salas.actualizar_sala(id,nombre,descripcion,precio,foto)
                else: 
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response