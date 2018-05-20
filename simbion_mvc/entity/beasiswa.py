from .entity import Entity

class skema_beasiswa(Entity):

    def __init__(self, kode, nama, jenis, deskripsi, nomor_identitas_donatur):
        super().__init__({'kode':kode, 'jenis': jenis, 'deskripsi': deskripsi, 'nomor_identitas_donatur': nomor_identitas_donatur})

    def getKode(self):
        return self.data['kode']

    def getJenis(self):
        return self.data['jenis']

    def getDeskripsi(self):
        return self.data['deskripsi']
    
    def getNomorIdentitasDonatur(self):
        return self.data['nomor_identitas_donatur']

    def __str__(self):
        return 'Skema Beasiswa: kode={}, jenis={}, deskripsi={}, nomor identitas donatur={}'.format(
                self.getKode(), self.getJenis(), self.getDeskripsi(), self.getNomorIdentitasDonatur()
            )
    def __repr__(self):
        return self.__str__()