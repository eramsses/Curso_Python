import psycopg2 as bd

conexion = bd.connect(
    user="postgres",
    password="michelle",
    host="127.0.0.1",
    port="5432",
    database="test_db")

try:
    cursor = conexion.cursor()
    sentencia = "INSERT"