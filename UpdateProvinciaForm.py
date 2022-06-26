import tkinter as tk
from tkinter import messagebox
from ProvinciaForm import ProvinciaForm

class UpdateProvinciaForm(ProvinciaForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label1 = tk.Label(super().getFrame(), text='Temperatura')
        self.entryTemperatura=tk.Entry(super().getFrame(),width=50)
        self.label2=tk.Label(super().getFrame(),text='Sensación térmica')
        self.entrySensacion=tk.Entry(super().getFrame(),width=50)
        self.label3=tk.Label(super().getFrame(),text='Humedad')
        self.entryHumedad=tk.Entry(super().getFrame(),width=50)
        self.label1.grid(row=4,column=0,pady=5)
        self.entryTemperatura.grid(row=4,column=1,pady=5)
        self.label2.grid(row=5,column=0,pady=5)
        self.entrySensacion.grid(row=5,column=1,pady=5)
        self.label3.grid(row=6,column=0,pady=5)
        self.entryHumedad.grid(row=6,column=1,pady=5)
    def mostrarEstadoProvinciaEnFormulario(self,provincia):
        super().mostrarEstadoProvinciaEnFormulario(provincia)
        try:
            variables=provincia.consultaApi()
        except Exception as e:
            messagebox.showerror("Error de consulta", str(e), parent=self)
        else:
            self.entryTemperatura.delete(0, tk.END)
            self.entrySensacion.delete(0, tk.END)
            self.entryHumedad.delete(0, tk.END)
            self.entryTemperatura.insert(0,variables['temp'])
            self.entrySensacion.insert(0,variables['feels_like'])
            self.entryHumedad.insert(0,variables['humidity'])
    