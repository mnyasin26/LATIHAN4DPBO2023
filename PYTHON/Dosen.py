from SivitasAkademik import SivitasAkademik


class Dosen(SivitasAkademik):
    # protected attributes
    _nip = ""
    _pendidikanTerakhir = ""
    _keahlian = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", jenisKelamin="", asalUniversitas="", emailEdu="", fakultas="", nip="", pendidikanTerakhir="", keahlian=""):
        super().__init__(nik, nama, jenisKelamin, asalUniversitas, emailEdu, fakultas)
        self._nip = nip
        self._pendidikanTerakhir = pendidikanTerakhir
        self._keahlian = keahlian

    # --- Setters ---
    # set value of nim
    def setNip(self, nip):
        self._nip = nip

    # set value of programStudi
    def setPendidikanTerkahir(self, pendidikanTerakhir):
        self._pendidikanTerakhir = pendidikanTerakhir

    def setKeahlian(self, setKeahlian):
        self._keahlian = setKeahlian

    # --- Getters ---
    # set value of nim
    def getNip(self):
        return self._nip

    # set value of programStudi
    def getPendidikanTerkahir(self):
        return self._pendidikanTerakhir

    def getKeahlian(self):
        return self._keahlian
