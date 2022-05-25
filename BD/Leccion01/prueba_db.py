import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    cursor = conexion.cursor()
    sentencia = "INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)"
    valores = ("Alejandra", "Rodriguez", "arodriguez@yopmail.com")
    cursor.execute(sentencia, valores)
    conexion.commit()

    registros_insertados = cursor.rowcount
    print(f"Registros insertados: {registros_insertados}")

except Exception as e:
    print(e)
finally:
    cursor.close()
    conexion.close()



