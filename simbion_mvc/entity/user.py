from .entity import Entity

class User(Entity):

    def __init__(self, username, password):
        super().__init__({'username': username, 'password': password})
