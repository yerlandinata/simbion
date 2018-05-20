from .entity import Entity

class SkemaBeasiswaAktif(Entity):

    def __init__(
            self, 
            skema_beasiswa,  
            no_urut, 
            tgl_mulai_pendaftaran, 
            tgl_tutup_pendaftaran, 
            periode_penerimaan,
            status,
            jumlah_pendaftar
        ):
        super().__init__({
                    'no_urut': no_urut, 
                    'tgl_mulai_pendaftaran': tgl_mulai_pendaftaran, 
                    'tgl_tutup_pendaftaran': tgl_tutup_pendaftaran,
                    'periode_penerimaan':periode_penerimaan,
                    'status':status,
                    'jumlah_pendaftar': jumlah_pendaftar,
                    #store actual data of skema_beasiswa
                    'skema_beasiswa':skema_beasiswa.data
                })
        self.__skema_beasiswa = skema_beasiswa

    def getNoUrut(self):
        return self.data['no_urut']

    def getTglMulaiPendaftaran(self):
        return self.data['tgl_mulai_pendaftaran']
    
    def getTglTutupPendaftaran(self):
        return self.data['tgl_tutup_pendaftaran']
    
    def getPeriodePenerimaan(self):
        return self.data['periode_penerimaan']
    
    def getStatus(self):
        return self.data['status']

    def getJumlahPendaftar(self):
        return self.data['jumlah_pendaftar']
    
    def getSkemaBeasiswa(self):
        return self.__skema_beasiswa

    def __repr__(self):
        return 'Skema Beasiswa Aktif:  nomor urut={}, Tanggal mulai pendaftaran={}, Tanggal tutup pendaftaran={}, \
                Status={}, periode_penerimaan={}, jumlah_pendaftar{}, [{}]'.format(
                self.getNoUrut(), self.getTglMulaiPendaftaran(), self.getTglTutupPendaftaran(),
                self.getStatus(), self.getPeriodePenerimaan(), self.getJumlahPendaftar(),
                self.getSkemaBeasiswa()
            )

    def __str__(self):
        return self.__repr__()
