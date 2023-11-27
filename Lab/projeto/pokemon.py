class Pokemon:
    def __init__(self, db):
        self.db = db

    def create(self, id, name, pokedexid):
        query = """
        MATCH (u:User)
        WHERE u.id = $id
        CREATE (d:Pokemon {name: $name, pokedexid: $pokedexid})
        CREATE (u)-[:OWNS]->(d)
        RETURN d
        """
        parameters = {
            'id': id,
            'name': name,
            'pokedexid': pokedexid
        }
        return self.db.execute_query(query, parameters)

    def get(self, pokedexid):
        query = """
        MATCH (d:Pokemon)
        WHERE d.pokedexid = $pokedexid
        RETURN d
        """
        parameters = {
            'pokedexid': pokedexid
        }
        return self.db.execute_query(query, parameters)

    def update(self, pokedexid, name=None):
        query = """
        MATCH (d:Pokemon)
        WHERE d.pokedexid = $pokedexid
        SET d.name = coalesce($name, d.name),
            d.mac = coalesce($pokedexid, d.pokedexid)
        RETURN d
        """
        parameters = {
            'pokedexid': pokedexid,
            'name': name,
        }
        return self.db.execute_query(query, parameters)

    def delete(self, pokedexid):
        query = """
        MATCH (d:Pokemon)
        WHERE d.pokedexid = $pokedexid
        DELETE d
        """
        parameters = {
            'pokedexid': pokedexid
        }
        return self.db.execute_query(query, parameters)
    
    def get_pokemons_from_user(self, id):
        query = """
        MATCH (u:User {id: $id})-[:OWNS]->(d:Pokemon)
        RETURN d
        UNION
        MATCH (u:User {id: $id})-[:SHARES]->(d:Pokemon)
        RETURN d
        UNION
        MATCH (u)-[:SHARED_WTH]->(d:Pokemon)
        RETURN d
        """
        parameters = {
            'id': id
        }
        return self.db.execute_query(query, parameters)