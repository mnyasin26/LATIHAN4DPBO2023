from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Course import Course


class ProgramStudi:
    # protected attributes
    _namaProdi = ""
    _kode = ""
    _fakultas = ""
    __listCourse = []
    __listDosen = []
    __listMhs = []

    # Constructor with default value
    def __init__(self, namaProdi="", kode="", fakultas=""):
        self._namaProdi = namaProdi
        self._kode = kode
        self._fakultas = fakultas
        self.__listCourse = []
        self.__listDosen = []
        self.__listMhs = []

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

    def addMhs(self, mahasiswa: Mahasiswa):
        self.__listMhs.append(mahasiswa)

    def addDosen(self, dosen: Dosen):
        self.__listDosen.append(dosen)

    def addCourse(self, course: Course):
        self.__listCourse.append(course)

    def getListMhs(self) -> list[Mahasiswa]:
        return self.__listMhs

    def getListDosen(self) -> list[Dosen]:
        return self.__listDosen

    def getListCourse(self) -> list[Course]:
        return self.__listCourse
