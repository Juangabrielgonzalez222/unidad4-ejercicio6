import tkinter as tk
from ProvinciaList import ProvinciaList
from UpdateProvinciaForm import UpdateProvinciaForm
class ProvinciasView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de provincias")
        self.list = ProvinciaList(self, height=15)
        self.form = UpdateProvinciaForm(self)
        self.btn_new = tk.Button(self, text="Agregar provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)
    #obtiene los valores del formulario y crea una nueva provincia
    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()
    #Ver estado de Provincia en formulario de provincia
    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)