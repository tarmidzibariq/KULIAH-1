class Pengguna():
    def __init__(self, nama, umur, jenis_kelamin):
        self.nama = nama
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin

    def tampilkan_detail(self):
        print("data pribadi")
        print("")
        print("nama: ", self.nama)
        print("umur: ", self.umur)
        print("jenis_kelamin: ", self.jenis_kelamin)

class Bank(Pengguna):
    def __init__(self, nama, umur, jenis_kelamin):
        super().__init__(nama, umur, jenis_kelamin)
        self.saldo = 0

    def lihat_saldo(self):
        self.tampilkan_detail()
        print("Saldo: Rp", self.saldo)

    def setoran(self,jumlah):
        self.jumlah = jumlah
        self.saldo = self.saldo + self.jumlah
        print("Saldo anda telah diperbarui: Rp", self.saldo)

    def penarikan(self,jumlah):
        self.jumlah = jumlah
        if self.jumlah > self.saldo:
            print("Saldo anda tidak cukup untuk melakukan penarikan: Rp", self.saldo)
        else:
            self.saldo = self.saldo - self.jumlah
            print("Sisa saldo anda: Rp", self.saldo)

    def transfer(self, nama_tujuan, jumlah):
        self.jumlah = jumlah
        self.nama_tujuan = nama_tujuan
        if self.jumlah > self.saldo:
            print("Transfer ke rekening tujuan", self.nama_tujuan, "gagal, saldo tidak cukup: Rp", self.saldo)
        else:
            self.saldo = self.saldo - self.jumlah
            print("Transfer ke rekening tujuan", self.nama_tujuan, "berhasil, sisa saldo sebesar: Rp", self.saldo)

rafli = Bank("Rafli", 18, "pria")
rafli.setoran(4000)
rafli.penarikan(1000)
rafli.transfer