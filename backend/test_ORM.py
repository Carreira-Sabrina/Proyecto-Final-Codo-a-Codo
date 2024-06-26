from modelos.entidades import Cliente


""" clientes = Cliente.obtener_todos_de_tabla()

    
cliente_seleccionado = clientes[0] """



#SI NO GUARDO LOS DATOS PARA PASAR AL CONSTRUCTOR EN UNA TUPLA, AL MOMENTO DE GUARDAR LA INSTANCIA EXPLOTA COMO EL VOLCAN DE KRAKATOA !!!!
datos_nuevo_cliente = ("Thunder","Cracker","1178369911","thundercrcker@decepticon.com")


nuevo_cliente = Cliente(datos_nuevo_cliente)


nuevo_cliente.insertar_en_tabla()


""" los_campos = ["nombre","apellido","celular","email"]


placeholders = f"({'%s,'*(len(los_campos)-1)}%s)"

print(placeholders) """