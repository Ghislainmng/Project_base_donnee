import sqlite3 
connBDD = sqlite3.connect('/Users/clay_jnr/Desktop/test_sql.db') 
cursor = connBDD.cursor()
print("hello ")
for g in cursor.execute("select id_region,nom_region from region"):
    print(g)