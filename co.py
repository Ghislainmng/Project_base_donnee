import sqlite3

#création d'une base de la base SQLite 
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = '''
        CREATE TABLE secteur_activite (
            id INTEGER PRIMARY KEY,
            label VARCHAR(255) NOT NULL,
            nbre_salarie VARCHAR(255) NOT NULL
        );
        CREATE TABLE postes_emploi (
            id_emploi INTEGER PRIMARY KEY, 
            label VARCHAR(255) NOT NULL
        );
        CREATE TABLE region (
            id_region INTEGER PRIMARY KEY,
            label VARCHAR(255) NOT NULL
        );
        '''
    
    cursor = sqliteConnection.cursor()
    cursor.executescript(sqlite_create_table_query)
    print("Database created and Successfully Connected to SQLite")

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")