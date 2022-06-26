import json
from urllib.request import urlopen
from urllib.error import URLError,HTTPError
class Provincia(object):
    __nombre=None
    __capital=None
    __cantidadHabitantes=None
    __cantidadDepartamentos=None
    def __init__(self,nombre,capital,cantidadHabitantes,cantidadDepartamentos):
        self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__capital = self.requerido(capital, 'Capital es un valor requerido')
        self.__cantidadHabitantes = self.tipoValido(cantidadHabitantes, 'Cantidad de habitantes no tiene un valor numérico correcto.')
        self.__cantidadDepartamentos = self.tipoValido(cantidadDepartamentos, 'Cantidad de departamentos/partidos no tiene un valor numérico correcto.')
    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getCantidadHabitantes(self):
        return self.__cantidadHabitantes
    def getCantidadDepartamentos(self):
        return self.__cantidadDepartamentos
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def tipoValido(self,valor,mensaje):
        try:
            valor=int(valor)
        except ValueError:
            raise ValueError(mensaje)
        return valor
    def consultaApi(self):
        dJson=None
        url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c53e9413b476ed4e52be057ceb6034bf'.format(self.__capital.replace(' ','%20'))
        try:
            respuesta=urlopen(url)
        except HTTPError as e:
            mensaje=''
            if e.code==404:
                mensaje='ERROR 404 no se encontro la ciudad.'
            else:
                mensaje='ERROR {} en la consulta.'.format(e.code)
            raise Exception(mensaje)
        except:
            raise Exception('Fallo la conexión a la API, no se obtuvieron datos.')
        else:
            dJson=json.loads(respuesta.read())['main']
        return dJson
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
            nombre=self.__nombre,
            capital=self.__capital,
            cantidadHabitantes=self.__cantidadHabitantes,
            cantidadDepartamentos=self.__cantidadDepartamentos
            ))
        return d