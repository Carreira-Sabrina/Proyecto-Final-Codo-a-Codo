from conexion.configuracion_conexion_BD import conexion as con

#Representa una tabla en la base de datos
class ModeloBase():
    #Constructor
    def __init__(self,tabla,campos,conexion):
        self.tabla = tabla
        self.campos = campos
        self.conexion = con #Mmmmm
        

    #Opera dentro del constructor de las subclases      
    def crear_instancia(self,valores_atributos):
        # LAS INSTANCIAS NO TIENEN LA MISMA CANTIDAD DE ATRIBUTOS CUANDO SE CREAN O CUANDO SE LEEN DE LAS TABLAS, CUANDO SE LEEN DE LAS TABLAS
        # TIENEN ID !
        if len(valores_atributos) == len(self.campos):
            #Aca vino un id...
            for campo,valor in zip(self.campos,valores_atributos):
                #print(f"Se setea el atributo {campo} con el valor {valor}")
                setattr(self,campo,valor)
        else:
            #Estoy creando la instancia en vez de leerla de una tabla!
            for campo,valor in zip(self.campos[1:],valores_atributos):
                #print(f"Se setea el atributo {campo} con el valor {valor}")
                setattr(self,campo,valor)
    
    
    def insertar_en_tabla(self):
        #Este método toma un objeto, lee sus variables y las inserta en la tabla que le corresponde
        #Obtengo los nombres de las columnas a insertar (no paso el id !)
        campos_a_insertar = str(self.campos[1:]).replace("'","`").replace('"','`')
        
        #Voy a insertar un campo menos, porque el id no se inserta
        cantidad_campos_a_insertar = len(self.campos[1:])
        
        #Los placeholders son los %s que se ponen en VALUES de la consulta, son parámetros para evitar inyecciones SQL
        placeholders_values = f"({'%s,'*(cantidad_campos_a_insertar-1)} %s)"
        
        #Obtengo una tupla por comprehension de los valores de los atributos de la clase  
        valores_a_insertar = tuple(getattr(self,valor) for valor in vars(self).keys())
    
        consulta_insertar = f'INSERT INTO {self.tabla} {campos_a_insertar} VALUES {placeholders_values};'
        
        #Conexion
        conexion = con
        conexion.connect()
        cursor = conexion.cursor()
        cursor.execute(consulta_insertar,valores_a_insertar)
        
        conexion.commit()
        
        conexion.close()

    
    @classmethod
    def obtener_todos_de_tabla(cls):
        consulta_sql = f"SELECT * FROM {cls.tabla}"
        return cls.__conectar_y_ejecutar_consulta(consulta_sql)
        
    
    #Metodo sólo accesible dentro de la clase y sus subclases
    @classmethod 
    def __conectar_y_ejecutar_consulta(cls,consulta):
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()

        cursor.execute(consulta)
        resultado_consulta = cursor.fetchall() # Esto trae tuplas
        cls.conexion.close()
        return cls.__convertir_registros_en_objetos(resultado_consulta) #Ahora si devuelve una lista de objetos !

        
    @classmethod
    def obtener_objeto_de_tabla(cls,id):
        consulta_sql= f"SELECT * FROM {cls.tabla} WHERE id= %s"
        parametros_consulta = (id,) #se convierte en tupla 
        
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()

        cursor.execute(consulta_sql,parametros_consulta)
        resultado_consulta = cursor.fetchone()
        cls.conexion.close()
        
        #Devuelvo el objeto 
        
        objeto_a_retornar = cls(resultado_consulta)
        return objeto_a_retornar


    @classmethod
    def eliminar_de_tabla(cls,id):
        #primero se obtiene el objeto de la tabla y luego se elimina
        objeto_a_eliminar = cls.obtener_objeto_de_tabla(id)
        consulta_eliminar = f"DELETE FROM {cls.tabla} WHERE id=%s"
        parametros_consulta = (id,)#Siempre como tupla
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()

        cursor.execute(consulta_eliminar,parametros_consulta)
        cls.conexion.commit()
        cls.conexion.close()
        print("Objeto borrado")
    
    
    @classmethod
    def __convertir_registros_en_objetos(cls,resultado_consulta):
        return [cls(registro) for registro in resultado_consulta]
    
    
    @classmethod
    def actualizar_registro_tabla(cls,registro):
        
        
        
        #UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
        
        # ME TIENE QUE LLEGAR UNA TUPLA CON LO QUE DICE EL FORM 
        # TIPO tupla("1","Viñedos la Patoneta", "tomate un vinito",Mendoza","10000","url de imagen")
        
        #De la tupla que recibo del form tengo que discriminar el id porque no se actualiza ! (y lo tengo que pasar a tupla para pasarlo como parametro a la consulta)
        id = (registro[0],)
        
        #Elimino a "id" de la lista de campos
        campos_sin_id = cls.campos[1:]
        
        #También elimino el valor del id porque NO SE PUEDE REEMPLAZAR
        valores_del_form_sin_id = registro[1:] #Se asume por ahora que el id va a venir en la tupla enviada por el form
        
        #Le tome el gustito al list comprehension
        #Qué  es esa linea tan fea como la conciencia de Megatron?
        # Primero convierte el contenido de la tupla de lo que viene del form con str()
        # Luego hago una lista de pares variable = valor con zip
        #Cambio las comillas dobles por backticks que es como las toma la consulta SQL
        # Como todo eso quedó entre [] por ser un list comprehension, quité las llaves
        
        set_string = str([f"`{variable}` = '{valor}'" for variable,valor in zip(campos_sin_id,valores_del_form_sin_id)]).replace('"',"").replace("[","").replace("]","")
        
        #Se arma dinámicamente el string de la consulta SQL
        consulta_update = f"UPDATE {cls.tabla} SET {set_string} WHERE ID = %s"
        
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()

        cursor.execute(consulta_update,id)
        
        
        cls.conexion.commit()
        
        cls.conexion.close()
        
        print(f"Se actualizo el registro con id {id} !")