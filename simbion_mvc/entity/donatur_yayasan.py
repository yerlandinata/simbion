from . import Entity

class DonaturYayasan(Entity):

    def __init__(self, donatur, no_sk, email, nama, no_telp='-'):
        super().__init__({
            'donatur': donatur.data, # ACTUAL OBJECT, NOT JUST FOREIGN KEY
            'no_sk': no_sk,
            'email': email,
            'nama': nama,
            'no_telp': no_telp
        })
        self.__donatur = donatur

    def getNoSk(self):
        return self.data['no_sk']

    def getEmail(self):
        return self.data['email']

    def getNama(self):
        return self.data['nama']

    def getNoTelp(self):
        return self.data['no_telp']

    def getDonatur(self):
        return self.__donatur

    def __repr__(self):
        return 'Donatur Yayasan: no_sk={}, email={}, nama={}, no_telp={}, [{}]'.format(
                self.getNoSk(), self.getEmail(), self.getNama(), self.getNoTelp(), str(self.getDonatur())
            )

    def __str__(self):
        return self.__repr__()

