from .entity import Entity

class SkemaBeasiswaAktif(Entity):

    def __init__(self, kode_skema_beasiswa, 
                no_urut, 
                tgl_mulai_pendaftaran, 
                tgl_tutup_pendaftaran, 
                nomor_identitas_donatur):
        super().__init__({'kode_skema_beasiswa':kode_skema_beasiswa, 
                        'no_urut': no_urut, 
                        'tgl_mulai_pendaftaran': tgl_mulai_pendaftaran, 
                        'tgl_tutup_pendaftaran': tgl_tutup_pendaftaran,
                        'periode_penerimaan':periode_penerimaan,
                        'status':status})

    def getKodeSkemaBeasiswa(self):
        return self.data['kode_skema_beasiswa']

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

    def __str__(self):
        return 'Skema Beasiswa Aktif: Kode skema beasiswa={}, nomor urut={}, Tanggal mulai pendaftaran={}, Tanggal tutup pendaftaran={}, Status={}'.format(
                self.getKodeSkemaBeasiswa(), self.getNoUrut(), 
                self.getTglMulaiPendaftaran(), self.getTglTutupPendaftaran(),
                self.getPeriodePenerimaan(), self.getStatus()
            )
    def __repr__(self):
        return self.__str__()