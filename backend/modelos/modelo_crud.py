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
                print(f"Se setea el atributo {campo} con el valor {valor}")
                setattr(self,campo,valor)
        else:
            #Estoy creando la instancia en vez de leerla de una tabla!
            for campo,valor in zip(self.campos[1:],valores_atributos):
                print(f"Se setea el atributo {campo} con el valor {valor}")
                setattr(self,campo,valor)
    
    
    def insertar_en_tabla(self):
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
        
        
        
        cls.conexion.close()

        print("Objeto borrado")


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
    
    
    @classmethod
    def __convertir_registro_en_objeto(cls,resultado_consulta):
        return [cls(registro) for registro in resultado_consulta]