from modelos.modelo_crud import ModeloBase
from conexion.configuracion_conexion_BD import conexion as con


class Cliente(ModeloBase):
    tabla = "cliente"
    campos = ("id","nombre","apellido","celular","email")
    conexion = con
    
    
    def __init__(self,valores_atributos):
        super().crear_instancia(valores_atributos)
        #print(vars(self))
        


class Habitacion(ModeloBase):
    tabla = "habitacion"
    campos =("id","nombre","categoria","precio_por_dia")



class Reserva(ModeloBase):
    tabla = "reserva"
    campos =("id","id_habitacion","id_cliente","fecha_ingreso","fecha_egreso")
