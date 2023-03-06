class Course:
    # protected attributes
    _kodeMK = ""
    _namaMatakuliah = ""
    _jmlhSKS = ""

    # Constructor with default value
    def __init__(self, kodeMK="", namaMataKuliah="", jmlhSKS=""):
        self._kodeMK = kodeMK
        self._namaMatakuliah = namaMataKuliah
        self._jmlhSKS = jmlhSKS

    # --- Setters ---
    # set value of nim
    def setKodeMK(self, kodeMK):
        self._kodeMK = kodeMK

    # set value of programStudi
    def setNamaMataKuliah(self, namaMataKuliah):
        self._namaMatakuliah = namaMataKuliah

    def setJmlhSKS(self, setKeahlian):
        self._jmlhSKS = setKeahlian

    # --- Getters ---
    # set value of nim
    def getKodeMK(self):
        return self._kodeMK

    # set value of programStudi
    def getNamaMataKuliah(self):
        return self._namaMatakuliah

    def getJmlhSKS(self):
        return self._jmlhSKS
