from Human import Human

class SivitasAkademik(Human):
    # protected attributes
    _asalUniversitas = ""
    _emailEdu = ""
    _fakultas = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", jenisKelamin="", asalUniversitas="", emailEdu="", fakultas=""):
        super().__init__(nik, nama, jenisKelamin)
        self._asalUniversitas = asalUniversitas
        self._emailEdu = emailEdu
        self._fakultas = fakultas

    # --- Setters ---
    def setAsalUniversitas(self, asalaUniversitas):
        self._asalUniversitas = asalaUniversitas

    def setEmailEdu(self, emailEdu):
        self._emailEdu = emailEdu

    def setFakultas(self, fakultas):
        self._fakultas = fakultas
