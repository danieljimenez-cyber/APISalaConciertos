from __future__ import print_function
from bd import obtener_conexion
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
        print("Excepcion al insertar una sala de conciertos", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_sala_a_json(juego):
    d = {}
    d['id'] = juego[0]
    d['nombre'] = juego[1]
    d['descripcion'] = juego[2]
    d['precio'] = juego[3]
    d['foto'] = juego[4]
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
        print("Excepcion al obtener las salas de concierto", file=sys.stdout)
        salasjson=[]
        code=500
    return salasjson,code

def obtener_sala_por_id(id):
    salajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM salas WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM salas WHERE id =" + id)
            sala = cursor.fetchone()
            if sala is not None:
                salajson = convertir_sala_a_json(sala)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar una sala de concierto", file=sys.stdout)
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
        print("Excepcion al eliminar una sala de conciertos", file=sys.stdout)
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
        print("Excepcion al eliminar una sala", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
