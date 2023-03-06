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
    # set value of nama
    def setNik(self, nik):
        self._nik = nik

    # set value of nim
    def setNama(self, nama):
        self._nama = nama

    # set value of programStudi
    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin

    # --- Getters ---

    # get the value of nama
    def getNik(self):
        return self._nik

    # get the value of nim
    def getNama(self):
        return self._nama

    # get the value of programStudi
    def getJenisKelamin(self):
        return self._jenisKelamin