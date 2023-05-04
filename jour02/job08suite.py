import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Chapy&Lapin",
  database="laplateforme"
)
cursor = db.cursor()

# Fonction pour afficher les animaux présents dans le zoo
def afficher_animaux():
  cursor.execute("SELECT * FROM animal")
  result = cursor.fetchall()
  for animal in result:
    print(animal)

# Fonction pour afficher les animaux présents dans chaque cage
def animaux_dans_cages():
  cursor.execute("SELECT cage.id, cage.superficie, cage.capacite, animal.nom FROM cage LEFT JOIN animal ON cage.id = animal.id_cage")
  result = cursor.fetchall()
  cages = {}
  for row in result:
    cage_id = row[0]
    cage_superficie = row[1]
    cage_capacite = row[2]
    animal_nom = row[3]
    if cage_id not in cages:
      cages[cage_id] = {
        "superficie": cage_superficie,
        "capacite": cage_capacite,
        "animaux": []
      }
    if animal_nom:
      cages[cage_id]["animaux"].append(animal_nom)
  for cage_id, cage in cages.items():
    print("Cage " + str(cage_id) + " :")
    print("Superficie : " + str(cage["superficie"]) + "m2")
    print("Capacité : " + str(cage["capacite"]) + " animaux")
    print("Animaux : " + ", ".join(cage["animaux"]))

# Fonction pour calculer la superficie totale de toutes les cages
def superficie_totale():
  cursor.execute("SELECT SUM(superficie) FROM cage")
  result = cursor.fetchone()
  superficie_totale = result[0]
  print("La superficie totale de toutes les cages est de " + str(superficie_totale) + "m2")

# Menu principal
while True:
  print()
  print("=== MENU ===")
  print("1 - Ajouter un animal")
  print("2 - Modifier un animal")
  print("3 - Supprimer un animal")
  print("4 - Ajouter une cage")
  print("5 - Modifier une cage")
  print("6 - Supprimer une cage")
  print("7 - Afficher la liste des animaux")
  print("8 - Afficher la liste des animaux par cage")
  print("9 - Calculer la superficie totale de toutes les cages")
  print("0 - Quitter")
  choix = input("Entrez votre choix : ")


  # Ajouter un animal
  if choix == "1":
    nom = input("Entrez le nom de l'animal : ")
    race = input("Entrez la race de l'animal : ")
    id_cage = input("Entrez l'ID de la cage : ")
    date_naissance = input("Entrez la date de naissance de l'animal (format YYYY-MM-DD) : ")
    pays_origine = input("Entrez le pays d'origine de l'animal : ")
    cursor.execute("INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)", (nom, race, id_cage, date_naissance, pays_origine))
    db.commit
    