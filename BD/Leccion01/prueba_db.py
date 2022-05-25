import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    with conexion.cursor() as cursor:
        sentencia = "INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)"
        valores = (
            ("Marco", "Flores", "mflores@yopmail.com"),
            ("Angel", "Martinez", "amartinez@yopmail.com"),
            ("Maria", "Gonzalez", "arodriguez@yopmail.com")
        )

        #cursor.execute(sentencia, valores)
        cursor.executemany(sentencia, valores)
        conexion.commit() #no se usa si está dentro del with

        registros_insertados = cursor.rowcount
        print(f"Registros insertados: {registros_insertados}")

except Exception as e:
    print(e)
finally:
    #cursor.close() #se cierra por el with
    conexion.close()



