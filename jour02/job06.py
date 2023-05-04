import mysql.connector

# Se connecter à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chapy&Lapin",
  database="laplateforme"
)

# Exécuter la requête SQL pour calculer la somme des capacités des salles
cursor = db.cursor()
query = "SELECT SUM(capacite) FROM salles"
cursor.execute(query)
result = cursor.fetchone()[0]

# Afficher le résultat en console
print("La somme des capacités des salles est de", result)