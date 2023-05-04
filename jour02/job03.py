import mysql.connector

# se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Chapy&Lapin',
                              host='localhost', database='laplateforme')
cursor = cnx.cursor()

# ajouter les données dans la table "etage"
add_etage = ("INSERT INTO etage "
             "(nom, numero, superficie) "
             "VALUES (%s, %s, %s)")
data_etage = [
    ('RDC', 0, 500),
    ('R+1', 1, 500)
]
cursor.executemany(add_etage, data_etage)

# ajouter les données dans la table "salles"
add_salles = ("INSERT INTO salles "
              "(nom, id_etage, capacite) "
              "VALUES (%s, %s, %s)")
data_salles = [
    ('Lounge', 1, 100),
    ('Studio son', 1, 5),
    ('Broadcasting', 2, 50),
    ('Bocal pPeda', 2, 4),
    ('Coworking', 2, 80),
    ('Studio Video', 2, 5)
]
cursor.executemany(add_salles, data_salles)

# valider les modifications et fermer la connexion
cnx.commit()
cursor.close()
cnx.close()