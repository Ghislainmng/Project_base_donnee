
import xlrd
import os 
import sqlite3

def insert_into(liste):
  try:
    conn = sqlite3.connect('SQLite_Gh.db')
    cur = conn.cursor()
    print("Connexion réussie à SQLite")
    sql = "INSERT INTO secteur_activite(label, nbre_salarie) VALUES (?, ?)"
    cur.executemany(sql, liste)
    conn.commit()
    print("Enregistrements insérés avec succès dans la table secteur_activite")
    cur.close()
    print("Connexion SQLite est fermée")
  except sqlite3.Error as error:
    print("Erreur lors de l'insertion dans la table secteur_activite", error)


workbook = xlrd.open_workbook("JVS_Tableau1BE_FR_13AUG18-3.xls")
sheet = workbook.sheet_by_name("JVS_Tab_2_2021")
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(7,1))
print(sheet.cell_value(7,0))



A= []
B= []
for y in range (1, sheet.nrows):
    #A.append(sheet.cell_value(y,0))
    if y < 55:
        if y <=30:
            B.append((sheet.cell_value(y,1), "Au moins salaries"))
        else:
            B.append((sheet.cell_value(y,1), "Au moins salaries"))   

print(B)

insert_into(B)


#for i in range (B):
    

