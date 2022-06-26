from NewProvincia import NewProvincia

class ControladorProvincias(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())
    # comandos que se ejecutan a través de la vista
    def crearProvincia(self):
        nuevaProvincia = NewProvincia(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.agregarProvincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)
    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)
    def start(self):
        for p in self.provincias:
            self.vista.agregarProvincia(p)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()