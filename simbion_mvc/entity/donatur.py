from . import Entity

class Donatur(Entity):

    def __init__(self, user, no_id, email, nama, npwp, alamat, no_telp='-'):
        super().__init__({
            'id': no_id,
            'email': email,
            'nama': nama,
            'no_telp': no_telp,
            'npwp': npwp,
            'alamat': alamat,
            'user': user.data # STORE ACTUAL OBJECT, NOT JUST FOREIGN KEY
        })
        self.__user = user

    def getNama(self):
        return self.data['nama']

    def getId(self):
        return self.data['id']

    def getEmail(self):
        return self.data['email']

    def getNpwp(self):
        return self.data['npwp']

    def getNoTelp(self):
        return self.data['no_telp']

    def getAlamat(self):
        return self.data['alamat']

    def getUser(self):
        return self.__user

    def __repr__(self):
        return 'Donatur: nama={}, no_id={}, email={}, no_telp={}, npwp={}, alamat={},\
                [{}]'.format(self.getNama(), self.getId(), self.getEmail(), self.getNoTelp(), 
                                self.getNpwp(), self.getAlamat(), str(self.getUser()))
    
    def __str__(self):
        return self.__repr__()

    def isValid(self):
        return (
                0 < len(self.getNama()) <= 50 
                and 0 < len(self.getId()) < 20 
                and 0 <= len(self.getEmail()) <= 50 
                and len(self.getNpwp()) == 20
                and 0 < len(self.getNoTelp()) <= 50
                and 0 < len(self.getAlamat()) <= 50
                and self.getUser().isValid()
            )
