from database import Database
from helper.writeAJson import writeAJson

def __init__(self, db: Database):
        db = Database(database="pokedex", collection="pokemons")
        db.resetDatabase()

pokemons = db.collection.find() #todos pokemons

def getPokemonByName(name: str): #pokemons por nome
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

def getPokemonsByType(types: list): #pokemons por tipo
    return db.collection.find({"type": {"$in": types}})

types = ["Fighting"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type")

tipos = ["Grass", "Poison"] #pokemons tipo grama OU veneno que tem evolução
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

pokemons = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}}) #pokemons que tem chance de spawn ENTRE 0.3 e 0.6