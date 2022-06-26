import tkinter as tk
from ProvinciaForm import ProvinciaForm
class NewProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.title('Nueva Provincia')
        self.form = ProvinciaForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia