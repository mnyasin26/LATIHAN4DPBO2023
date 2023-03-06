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
    def setKodeMK(self, kodeMK):
        self._kodeMK = kodeMK

    def setNamaMataKuliah(self, namaMataKuliah):
        self._namaMatakuliah = namaMataKuliah

    def setJmlhSKS(self, setKeahlian):
        self._jmlhSKS = setKeahlian

    # --- Getters ---
    def getKodeMK(self):
        return self._kodeMK

    def getNamaMataKuliah(self):
        return self._namaMatakuliah

    def getJmlhSKS(self):
        return self._jmlhSKS
