import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chapy&Lapin",
    database="LaPlateforme"
)

# Récupération des données des étudiants
cursor = conn.cursor()
cursor.execute("SELECT * FROM etudiants")
etudiants = cursor.fetchall()

# Affichage des résultats
for etudiant in etudiants:
    print(etudiant)

# Fermeture de la connexion
conn.close()