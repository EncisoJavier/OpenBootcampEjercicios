import sqlite3

conn = sqlite3.connect("baseDatos1.db")
cursor = conn.cursor()
#cursor.execute("CREATE TABLE Alumnos(id integer, nombre text, apellido text)")
listaNombres = [
    (1, "Joel", "Gimenez"),
    (2, "Jose", "Lopez"),
    (3, "Roberto", "Gomez"),
    (4, "Julian", "Alvarez"),
    (5, "Javier", "Enciso"),
    (6, "Pedro", "Baez"),
    (7, "Airton", "Nichel"),
    (8, "Kiko", "Federico")
]

#cursor.executemany("INSERT INTO Alumnos values (?,?,?)", listaNombres)

cursor.execute("SELECT * FROM Alumnos WHERE nombre='Airton'")
buscar = cursor.fetchone()
print(buscar)

conn.commit()
conn.close()

