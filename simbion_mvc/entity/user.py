from .entity import Entity

class User(Entity):

    valid_role = ('mahasiswa', 'admin',  'donatur')

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
        
    def isValid(self):
        return 0 < len(self.getUsername()) <= 20 and 8 <= len(self.getPassword()) <= 20 and self.getRole() in User.valid_role
