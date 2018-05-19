from . import Entity, User

class Mahasiswa(Entity):

    def __init__(self, user, npm, email, nama, alamat_tinggal, alamat_domisili, 
                 nama_bank, no_rekening, nama_pemilik_rekening, no_telp='-'):
        super().__init__({
            'npm': npm,
            'email': email,
            'nama': nama,
            'no_telp': no_telp,
            'alamat_tinggal': alamat_tinggal,
            'alamat_domisili': alamat_domisili,
            'nama_bank': nama_bank,
            'no_rekening': no_rekening,
            'nama_pemilik_rekening': nama_pemilik_rekening,
            'user': user.data # STORE ACTUAL OBJECT, NOT JUST FOREIGN KEY
        })
        self.__user = user

    def getNama(self):
        return self.data['nama']

    def getNpm(self):
        return self.data['npm']

    def getEmail(self):
        return self.data['email']

    def getNoTelp(self):
        return self.data['no_telp']

    def getAlamatTinggal(self):
        return self.data['alamat_tinggal']

    def getAlamatDomisili(self):
        return self.data['alamat_domisili']

    def getNamaBank(self):
        return self.data['nama_bank']

    def getNoRekening(self):
        return self.data['no_rekening']

    def getNamaPemilikRekening(self):
        return self.data['nama_pemilik_rekening']

    def getUser(self):
        return self.__user

    def __repr__(self):
        return 'Mahasiswa: nama={}, npm={}, email={}, no_telp={}, alamat_tinggal={} \
                alamat_domisili={}, nama_bank={}, no_rekening={}, nama_pemilik_rekening={}, \
                [{}]'.format(self.getNama(), self.getNpm(), self.getEmail(), self.getNoTelp(), 
                                self.getAlamatTinggal(), self.getAlamatDomisili(), self.getNamaBank(), 
                                self.getNoRekening(), self.getNamaPemilikRekening(), str(self.getUser()))
    
    def __str__(self):
        return self.__repr__()
