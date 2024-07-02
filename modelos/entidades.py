from modelos.modelo_crud import ModeloBase
from conexion.configuracion_conexion_BD import conexion as con




class Excursion(ModeloBase):
    tabla = "excursion"
    campos =("id","titulo","descripcion","destino","precio_por_persona","url_imagen")
    conexion = con
    
    def __init__(self,valores_atributos):
        super().crear_instancia(valores_atributos)
        #print(vars(self))