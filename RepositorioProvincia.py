from ManejadorProvincia import ManejadorProvincia
from ObjectEncoder import ObjectEncoder
from Provincia import Provincia
class RespositorioProvincia(object):
    __conn=None
    __manejador=None
    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        generarManejador=False
        if diccionario!=-1:
            resultado=self.__conn.decodificarDiccionario(diccionario)
            if isinstance(resultado,ManejadorProvincia):
                self.__manejador=resultado
            else:
                generarManejador=True
        else:
            generarManejador=True
        if generarManejador:
            self.__manejador=ManejadorProvincia()
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())