from modelos.entidades import Cliente


clientes = Cliente.obtener_todos_de_tabla()
for cliente in clientes:
    print(cliente.__dict__)

#Se busca el objeto con el id 4

cliente_4 = Cliente.obtener_objeto_de_tabla(4)
print("-----------------------------------------------------------------")
print("Datos del cliente 4")
print(cliente_4.__dict__)

#print(f"El cliente con el id {cliente_4.id} se llama {cliente_4.nombre} {cliente_4.apellido}")

#Intento borrar el ciente 3
#Cliente.eliminar_de_tabla(3)



#SI NO GUARDO LOS DATOS PARA PASAR AL CONSTRUCTOR EN UNA TUPLA, AL MOMENTO DE GUARDAR LA INSTANCIA EXPLOTA COMO EL VOLCAN DE KRAKATOA !!!!
""" datos_nuevo_cliente = ("Elita","One","1133331111","elita@cybertron.com")


nuevo_cliente = Cliente(datos_nuevo_cliente)


nuevo_cliente.insertar_en_tabla() """

