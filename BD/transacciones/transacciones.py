import psycopg2 as bd

conexion = bd.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)"
    valores = ("Maria", "Esperanza", "mesperanza@yopmail.com")
    cursor.execute(sentencia, valores)

    conexion.commit()
    print(f"Se afectaron: {cursor.rowcount}")


except Exception as e:
    conexion.rollback()
    print("Se hizo rollback")
    print(f"ERROR: {e}")
finally:
    conexion.close()