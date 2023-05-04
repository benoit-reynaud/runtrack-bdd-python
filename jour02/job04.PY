import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chapy&Lapin",
  database="LaPlateforme"
)

# Récupération des données de la table "salles"
cursor = db.cursor()
query = "SELECT nom, capacite FROM salles"
cursor.execute(query)
result = cursor.fetchall()

# Affichage des résultats
for row in result:
  print("Nom :", row[0], ", Capacité :", row[1])

# Fermeture de la connexion à la base de données
db.close()