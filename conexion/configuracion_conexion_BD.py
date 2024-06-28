from mysql import connector


parametros_conexion_desarrollo={
    'user': 'root',
    'password': '0pt1mu5Pr1m3',
    'host': 'localhost',
    'database': 'hotel'
}

#Sólo para pruebas:
parametros_conexion_desarrollo_dummy={
    'user': 'root',
    'password': '0pt1mu5Pr1m3',
    'host': 'localhost',
    'database': 'dummy'
}

#Conectar con la BD 

#se ponen ** antes del diccionario pasado como parámetro para que lo tome como **kwargs
conexion =connector.connect(**parametros_conexion_desarrollo)