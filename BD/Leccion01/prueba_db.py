import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM personas WHERE id_persona = %s"
    id_persona = input("Ingrese el valor id_persona: ")
    cursor.execute(sentencia, (id_persona,))

    #registros = cursor.fetchall()
    registros = cursor.fetchone()

    print(registros)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conexion.close()



