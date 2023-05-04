import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chapy&Lapin",
    database="laplateforme"
)

# Création d'un curseur pour exécuter les requêtes SQL
cursor = db.cursor()

# Exécution de la requête SQL pour calculer la superficie de l'ensemble des étages
query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)
result = cursor.fetchone()[0]

# Affichage du résultat
print(f"La superficie de La Plateforme est de {result} m2")

# Fermeture de la connexion à la base de données
db.close()