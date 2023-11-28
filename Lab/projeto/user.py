class User:
    def __init__(self, db):
        self.db = db

    def create(self, name, email, password, id):
        query = """
        CREATE (u:User {name: $name, email: $email, password: $password, id: $id})
        RETURN u
        """
        parameters = {
            'name': name,
            'email': email,
            'password': password,
            'id': id
        }
        return self.db.execute_query(query, parameters)

    def get(self, id):
        query = """
        MATCH (u:User)
        WHERE u.id = $id
        RETURN u
        """
        parameters = {
            'id': id
        }
        return self.db.execute_query(query, parameters)
    
    def get_user_by_email(self, email):
        query = """
        MATCH (u:User {email: $email})
        RETURN u
        """
        parameters = {
            'email': email
        }
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]['u']
        else:
            return None

    def update(self, id, name=None, email=None, password=None):
        query = """
        MATCH (u:User)
        WHERE u.id = $id
        SET u.name = coalesce($name, u.name),
            u.email = coalesce($email, u.email),
            u.password = coalesce($password, u.password)
        RETURN u
        """
        parameters = {
            'id': id,
            'name': name,
            'email': email,
            'password': password
        }
        return self.db.execute_query(query, parameters)

    def delete(self, id):
        query = """
        MATCH (u:User {id: $id})-[r:OWNS]-(p:Pokemon)
        DETACH DELETE u, r, p
        """
        parameters = {
            'id': id
        }
        return self.db.execute_query(query, parameters)