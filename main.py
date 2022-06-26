from ControladorProvincias import ControladorProvincias
from ObjectEncoder import ObjectEncoder
from ProvinciasView import ProvinciasView
from RepositorioProvincia import RespositorioProvincia
if __name__ == "__main__":
    conn=ObjectEncoder('datos.json')
    repo=RespositorioProvincia(conn)
    vista=ProvinciasView()
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()