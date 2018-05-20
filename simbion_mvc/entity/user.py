from .entity import Entity

class User(Entity):

    def __init__(self, username, password, role):
        super().__init__({'username': username, 'password': password, 'role': role})

    def getUsername(self):
        return self.data['username']

    def getPassword(self):
        return self.data['password']

    def getRole(self):
        return self.data['role']

    def __str__(self):
        return 'Pengguna: username={}, password={}, role={}'.format(
                self.getUsername(), self.getPassword(), self.getRole()
            )
    def __repr__(self):
        return self.__str__()
        