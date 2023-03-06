class Human:
    # private attributes
    _nik = ""
    _nama = ""
    _jenisKelamin = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", jenisKelamin=""):
        self._nik = nik
        self._nama = nama
        self._jenisKelamin = jenisKelamin

    # --- Setters ---
    def setNik(self, nik):
        self._nik = nik

    def setNama(self, nama):
        self._nama = nama

    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin

    # --- Getters ---

    def getNik(self):
        return self._nik

    def getNama(self):
        return self._nama

    def getJenisKelamin(self):
        return self._jenisKelamin