from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Course import Course

class ProgramStudi:
    # protected attributes
    _namaProdi = ""
    _kode = ""
    _fakultas = ""
    _listCourse : Mahasiswa = []
    _listDosen : Dosen = []
    _listMhs : Course = []

    # Constructor with default value
    def __init__(self, namaProdi="", kode="", fakultas=""):
        self._namaProdi = namaProdi
        self._kode = fakultas
        self._fakultas = fakultas

    # --- Setters ---
    # set value of nim
    def setNamaProdi(self, namaProdi):
        self._namaProdi = namaProdi

    # set value of programStudi
    def setKode(self, kode):
        self._kode = kode

    def setFakultas(self, fakultas):
        self._fakultas = fakultas

    # --- Getters ---
    # set value of nim
    def getNamaProdi(self):
        return self._namaProdi

    # set value of programStudi
    def getKode(self):
        return self._kode

    def getFakultas(self):
        return self._fakultas
    
    def addMhs(self, mahasiswa : Mahasiswa):
        self._listMhs += mahasiswa
        pass

    def addDosen(self, dosen : Dosen):
        self._listDosen += dosen
        pass

    def addCourse(self, course : Course):
        self._listCourse += course

    def getListhMhs(self):
        return self._listhMhs
    
    def getListhDosen(self):
        return self._listDosen
    
    def getListhCourse(self):
        return self._listCourse
