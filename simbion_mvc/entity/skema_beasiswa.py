from .entity import Entity
from simbion_mvc.dao import donatur_dao
class SkemaBeasiswa(Entity):

    def __init__(self, donatur, kode, nama, jenis, deskripsi):
        super().__init__({
                'kode': kode, 
                'nama': nama,
                'jenis': jenis, 
                'deskripsi': deskripsi, 
                'donatur': donatur
            })
        self.__donatur = donatur

    def getKode(self):
        return self.data['kode']

    def getNama(self):
        return self.data['nama']

    def getJenis(self):
        return self.data['jenis']

    def getDeskripsi(self):
        return self.data['deskripsi']
    
    def getDonatur(self):
        return self.__donatur

    def __repr__(self):
        return 'Skema Beasiswa: kode={}, jenis={}, deskripsi={}, [{}]'.format(
                self.getKode(), self.getJenis(), self.getDeskripsi(), str(self.getDonatur())
            )

    def __str__(self):
        return self.__repr__()
