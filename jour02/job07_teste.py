import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chapy&Lapin",
    database="laplateforme"
)
cursor = db.cursor()

# Récupération de tous les employés
cursor.execute("SELECT * FROM employes")
result = cursor.fetchall()

# Affichage des employés
for employe in result:
    print(employe)
    
    
# Récupération des employés dont le salaire est supérieur à 3000 euros
cursor.execute("SELECT * FROM employes WHERE salaire > 3000")
result = cursor.fetchall()

# Affichage des employés
for employe in result:
    print(employe)