import mysql.connector

def connexion(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user='root',
        password='Chapy&Lapin',
        database='laplateforme'
    )
    
    
    
def ajouter_animal(conn, nom, race, id_cage, date_naissance, pays_origine):
    cursor = conn.cursor()
    sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, race, id_cage, date_naissance, pays_origine)
    cursor.execute(sql, val)
    conn.commit()
    
def supprimer_animal(conn, id_animal):
    cursor = conn.cursor()
    sql = "DELETE FROM animal WHERE id_animal = %s"
    val = (id_animal,)
    cursor.execute(sql, val)
    conn.commit()
    
def modifier_animal(conn, id_animal, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
    cursor = conn.cursor()
    ql = "UPDATE animal SET "
    val = []
    if nom is not None:
        sql += "nom = %s, "
        val.append(nom)
    if race is not None:
        sql += "race = %s, "
        val.append(race)