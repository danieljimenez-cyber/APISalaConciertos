from bd import obtener_conexion
from __main__ import app
from funciones_auxiliares import sanitize_input
import sys

# CRUD : CREATE
def insertar_sala(nombre, descripcion, precio,foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO salas(nombre, descripcion, precio,foto) VALUES (%s, %s, %s,%s)",
                       (nombre, descripcion, precio,foto))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        app.logger.info("Excepcion al insertar una sala de conciertos")
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_sala_a_json(sala):
    d = {}
    d['id'] = sala[0]
    d['nombre'] = sanitize_input(sala[1])
    d['descripcion'] = sanitize_input(sala[2])
    d['precio'] = sala[3]
    d['foto'] = sanitize_input(sala[4])
    return d

#  CRUD : READ 
def obtener_salas(): 
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM salas")
            salas = cursor.fetchall()
            salasjson=[]
            if salas:
                for sala in salas:
                    salasjson.append(convertir_sala_a_json(sala))
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al obtener las salas de concierto")
        salasjson=[]
        code=500
    return salasjson,code

def obtener_sala_por_id(id):
    salajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM salas WHERE id = %s", (id,))
            sala = cursor.fetchone()
            if sala is not None:
                salajson = convertir_sala_a_json(sala)
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al recuperar una sala de concierto")
        code=500
    return salajson,code

# CRUD : DELETE
def eliminar_sala(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM salas WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al eliminar una sala de conciertos")
        ret = {"status": "Failure" }
        code=500
    return ret,code

# CRUD : UPDATE
def actualizar_sala(id, nombre, descripcion, precio, foto):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE salas SET nombre = %s, descripcion = %s, precio = %s, foto=%s WHERE id = %s",
                       (nombre, descripcion, precio, foto,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al eliminar una sala")
        ret = {"status": "Failure" }
        code=500
    return ret,code
