import sqlite3

#création d'une base de la base SQLite 
try:
    sqliteConnection = sqlite3.connect('SQLite_GH.db')
    sqlite_create_table_query = '''
        CREATE TABLE IF NOT EXISTS secteur_activite (
            id_sect_act INTEGER PRIMARY KEY,
            label VARCHAR(255) NOT NULL,
            nbre_salarie VARCHAR(255) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS postes_emploi (
            id_emploi INTEGER PRIMARY KEY, 
            label VARCHAR(255) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS region (
            id_region INTEGER PRIMARY KEY,
            label VARCHAR(255) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS entrprise (
            fixe REAL NOT NULL,
            interim REAL NULL,
            id_sect INTEGER, 
            id_emp INTEGER, 
            id_reg INTEGER,

            FOREIGN KEY(id_reg)  REFERENCES region (id_region),
            FOREIGN KEY(id_emp)  REFERENCES postes_emploi (id_emploi),
            FOREIGN KEY(id_sect)  REFERENCES secteur_activite (id_sect_act)
        )
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