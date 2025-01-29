from flask import request, session
import json
import decimal
from __main__ import app
import controlador_salas

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/salas",methods=["GET"])
def salas():
    salas,code= controlador_salas.obtener_salas()
    return json.dumps(salas, cls = Encoder),code

@app.route("/salas/<id>",methods=["GET"])
def sala_por_id(id):
    sala,code = controlador_salas.obtener_sala_por_id(id)
    return json.dumps(sala, cls = Encoder),code

@app.route("/salas",methods=["POST"])
def guardar_sala():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        sala_json = request.json
        ret,code=controlador_salas.insertar_sala(sala_json["nombre"], sala_json["descripcion"], float(sala_json["precio"]), sala_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/salas/<id>", methods=["DELETE"])
def eliminar_sala(id):
    ret,code=controlador_salas.eliminar_sala(id)
    return json.dumps(ret), code

@app.route("/salas", methods=["PUT"])
def actualizar_sala():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        sala_json = request.json
        ret,code=controlador_salas.actualizar_salas(sala_json["id"],sala_json["nombre"], sala_json["descripcion"], float(sala_json["precio"]),sala_json["foto"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code