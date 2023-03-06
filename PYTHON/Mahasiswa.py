from SivitasAkademik import SivitasAkademik

class Mahasiswa(SivitasAkademik):
    # protected attributes
    _nim = ""
    _semester = ""
    _ipk = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", jenisKelamin="", asalUniversitas="", emailEdu="", fakultas="", nim="", semester="", ipk=""):
        super().__init__(nik, nama, jenisKelamin, asalUniversitas, emailEdu, fakultas)
        self._nim = nim
        self._semester = semester
        self._ipk = ipk

    # --- Setters ---
    # set value of nim
    def setNim(self, nim):
        self._nim = nim

    # set value of programStudi
    def setSemester(self, semester):
        self._semester = semester

    def setIpk(self, ipk):
        self._ipk = ipk

    # --- Getters ---
    # set value of nim
    def setNim(self):
        return self._nim

    # set value of programStudi
    def setSemester(self):
        return self._semester

    def setIpk(self):
        return self._ipk
