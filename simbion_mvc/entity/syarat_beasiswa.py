from .entity import Entity

class SyaratBeasiswa(Entity):

    def __init__(self, skema_beasiswa, syarat):
        super().__init__({
                'skema_beasiswa': skema_beasiswa.data, 
                'syarat': syarat
                })
        self.__skema_beasiswa = skema_beasiswa

    def getSkemaBeasiswa(self):
        return self.__skema_beasiswa

    def getSyarat(self):
        return self.data['syarat']

    def __repr__(self):
        return self.getSyarat()

    def __str__(self):
        return self.__repr__()
