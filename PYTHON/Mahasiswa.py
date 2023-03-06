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
    def setNim(self, nim):
        self._nim = nim

    def setSemester(self, semester):
        self._semester = semester

    def setIpk(self, ipk):
        self._ipk = ipk

    # --- Getters ---
    def getNim(self):
        return self._nim
    
    def getSemester(self):
        return self._semester

    def getIpk(self):
        return self._ipk
