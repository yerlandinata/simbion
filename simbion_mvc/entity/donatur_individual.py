from . import Entity

class DonaturIndividual(Entity):

    def __init__(self, donatur, nik):
        super().__init__({
            'donatur': donatur.data, # ACTUAL OBJECT, NOT JUST FOREIGN KEY
            'nik': nik
        })
        self.__donatur = donatur
    
    def getNik(self):
        return self.data['nik']

    def getDonatur(self):
        return self.__donatur

    def __repr__(self):
        return 'Donatur Individual: nik={}, [{}]'.format(self.getNik(), str(self.getDonatur()))

    def __str__(self):
        return self.__repr__()
        