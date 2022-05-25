import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    cursor = conexion.cursor()
    #sentencia = "SELECT * FROM personas WHERE id_persona IN (1,2)"
    #dinamico
    sentencia = "SELECT * FROM personas WHERE id_persona IN (1,2)"
    llaves_primarias = input("Ingrese el valor id_persona: ")
    #llaves_primarias = ((1,2),)
    cursor.execute(sentencia, (llaves_primarias,))
    #cursor.execute(sentencia)

    registros = cursor.fetchall()
    #registros = cursor.fetchone()
    for r in registros:
        print(r)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conexion.close()



