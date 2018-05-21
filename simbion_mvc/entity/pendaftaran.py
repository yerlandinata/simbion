from .entity import Entity

class Pendaftaran(Entity):
    def __init__(self,skema_beasiswa_aktif,mahasiswa,waktu_daftar,status_daftar,status_terima):
        super().__init__({
            'skema_beasiswa_aktif':skema_beasiswa_aktif.data,
            'mahasiswa':mahasiswa.data,
            'waktu_daftar':waktu_daftar,
            'status_daftar':status_daftar,
            'status_terima':status_terima
    })
        self.__skema_beasiswa_aktif = skema_beasiswa_aktif
        self.__mahasiswa = mahasiswa

    def getNoUrut(self):
        return self.__skema_beasiswa_aktif.getNoUrut()

    def getKodeSkemaBeasiswa(self):
        return self.__skema_beasiswa_aktif.getSkemaBeasiswa().getKode()

    def getNPM(self):
        return self.__mahasiswa.getNpm()

    def getWaktuDaftar(self):
        return self.data['waktu_daftar']

    def getStatusDaftar(self):
        return self.data['status_daftar']

    def getStatusTerima(self):
        return self.data['status_terima']

    def getMahasiswa(self):
        return self.__mahasiswa

    def __repr__(self) :
        return 'Pendaftaran : nomor urut = {}, kode skema beasiswa = {} ,NPM Mahasiswa = {}, \
          waktu daftar = {} , status daftar = {} , status_terima = {}'.format(self.getNoUrut(),self.getKodeSkemaBeasiswa(),
                                                                               self.getNPM(),self.getWaktuDaftar(),
                                                                               self.getStatusDaftar(),self.getStatusTerima())

    def __str__(self) :
        return self.__repr__()

