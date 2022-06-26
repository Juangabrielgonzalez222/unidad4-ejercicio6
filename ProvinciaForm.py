import tkinter as tk
from tkinter import messagebox
from Provincia import Provincia

class ProvinciaForm(tk.LabelFrame):
    __fields = ('Nombre','Capital','Cantidad de habitantes','Cantidad de departamentos/partidos')
    __frame=None
    def __init__(self, master, **kwargs):
        super().__init__(master, text='Provincia', padx=10, pady=10, **kwargs)
        self.__frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.__fields)))
        self.__frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.__frame, text=text)
        entry = tk.Entry(self.__frame, width=50)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        # a partir de un paciente, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (provincia.getNombre(),provincia.getCapital(),provincia.getCantidadHabitantes(),provincia.getCantidadDepartamentos())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearProvinciaDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear una nueva provincia
        values = [e.get() for e in self.entries]
        provincia=None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
    def getFrame(self):
        return self.__frame