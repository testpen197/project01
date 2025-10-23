import csv

# Étape 1 : lire le fichier CSV et stocker les arêtes
edges = []
with open("parcours_explorateurs.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        edges.append({
            "from": row["noeud_amont"],
            "to": row["noeud_aval"],
            "type": row["type_aretes"],
            "distance": float(row["distance"])
        })

# Étape 2 : identifier tous les départs
departures = [e for e in edges if e["type"] == "depart"]

# Étape 3 : reconstruire les trajets
def build_trajet(start_node):
    trajet = []
    current_node = start_node
    total_distance = 0
    while True:
        # Trouver l'arête qui commence depuis le noeud courant
        edge = next((e for e in edges if e["from"] == current_node), None)
        if edge is None:
            break
        trajet.append(edge)
        total_distance += edge["distance"]
        current_node = edge["to"]
        if edge["type"] == "arrivee":
            break
    return trajet, total_distance

# Étape 4 : calculer les distances et trouver le plus long trajet
trajets = []
for dep in departures:
    trajet, distance = build_trajet(dep["from"])
    trajets.append({
        "trajet": trajet,
        "distance": distance
    })

# Trouver le trajet le plus long
trajet_max = max(trajets, key=lambda x: x["distance"])

print("Le trajet le plus long a une distance totale de :", trajet_max["distance"])
print("Voici le trajet (noeud_amont -> noeud_aval) :")
for e in trajet_max["trajet"]:
    print(f"{e['from']} -> {e['to']} ({e['distance']:.2f})")
