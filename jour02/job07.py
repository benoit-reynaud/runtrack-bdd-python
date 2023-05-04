import mysql.connector

# Création de la connexion à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chapy&Lapin",
  database="laplateforme"
)

# Création de la table "employes"
cursor = db.cursor()
cursor.execute("CREATE TABLE employes (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL(10, 2), id_service INT)")

# Insertion des employés dans la table "employes"
sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
values = [
  ("Dupont", "Jean", 3200.50, 1),
  ("Durand", "Marie", 2800.00, 2),
  ("Martin", "Pierre", 3500.00, 1),
  ("Lefevre", "Sophie", 2900.00, 3),
  ("Leclerc", "Luc", 4000.00, 2)
]
cursor.executemany(sql, values)
db.commit()

# Requête pour récupérer les employés dont le salaire est supérieur à 3000€
cursor.execute("SELECT * FROM employes WHERE salaire > 3000")
result = cursor.fetchall()
print("Les employés dont le salaire est supérieur à 3000€ :")
for row in result:
    print(row)

# Création de la table "services"
cursor.execute("CREATE TABLE services (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")

# Insertion des services dans la table "services"
sql = "INSERT INTO services (nom) VALUES (%s)"
values = [
  ("Informatique"),
  ("Comptabilité"),
  ("Marketing")
]
cursor.executemany(sql, values)
db.commit()

# Requête pour récupérer les employés et leur service respectif
cursor.execute("SELECT employes.nom, employes.prenom, services.nom FROM employes INNER JOIN services ON employes.id_service = services.id")
result = cursor.fetchall()
print("Les employés et leur service respectif :")
for row in result:
    print(row)

# Classe pour effectuer des opérations CRUD sur la table "employes"
class Employe:
  def __init__(self, nom, prenom, salaire, id_service):
    self.nom = nom
    self.prenom = prenom
    self.salaire = salaire
    self.id_service = id_service

  # Méthode pour insérer un employé dans la table "employes"
  def create(self):
    cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)", (self.nom, self.prenom, self.salaire, self.id_service))
    db.commit()
    print(cursor.rowcount, "employé ajouté.")

 # Méthode pour récupérer un employé de la table "employes"
  def read(self):
    cursor.execute("SELECT * FROM employes WHERE nom = %s AND prenom = %s", (self.nom, self.prenom))
    result = cursor.fetchone()
    if result == None:
      print("Aucun employé trouvé")
    else:
      print(result)

# Connexion à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

# Création d'un objet "Employe"
employe = Employe("Doe", "John", 3500, 1)

# Ajout de l'employé à la table "employes"
employe.create()

# Mise à jour du salaire de l'employé
employe.update(4000)

# Suppression de l'employé de la table "employes"
employe.delete()

# Récupération d'un employé de la table "employes"
employe = Employe("Doe", "John", None, None)
employe.read()

# Fermeture de la connexion à la base de données
db.close()


