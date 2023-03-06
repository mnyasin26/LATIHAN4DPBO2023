from ProgramStudi import ProgramStudi
from Course import Course
from Dosen import Dosen
from Mahasiswa import Mahasiswa
from Table import Table

# data Dummy
ojan = Mahasiswa("19832912732", "Fauzan", "Laki-laki", "Universitas_Pendidikan_Indonesia",
                 "ojan@upi.edu", "FPMIPA", "2100137", "4", "3.97",)
maul = Mahasiswa("19832912245", "Maulana", "Laki-laki", "Universitas_Pendidikan_Indonesia",
                 "maul@upi_edu", "FPMIPA", "2100234", "2", "3.85")
reyhan = Mahasiswa("19832916839", "Reyhan_Adonis", "Laki-laki", "Universitas_Pendidikan_Indonesia",
                   "reyhan@upi_edu", "FPMIPA", "2100356", "4", "3.9")
darto = Mahasiswa("20203489298", "Naufal_Dhiya_Ulhaq", "Laki-laki", "Universitas_Pendidikan_Indonesia",
                  "darto@upi.edu", "FPMIPA", "20213623", "4", "3.9")

yudi = Dosen("19832916839", "Yudi_Wibisono", "Laki-laki", "Universitas_Pendidikan_Indonesia",
             "yudi@upi.edu", "FPMIPA", "198282147922", "S3", "Mobile_Programming")
asepWahyudin = Dosen("198329168234", "Asep_Wahyudin", "Laki-laki", "Universitas_Pendidikan_Indonesia",
                     "away@upi.edu", "FPMIPA", "199638468216", "S3", "RPL")
sunandar = Dosen("198329168234", "Sunandar", "Laki-laki", "Universitas_Pendidikan_Indonesia",
                 "thesunan@upi.edu", "FPSD", "1996384623423", "S2", "Ilustrasi")

promvis = Course("IK412", "Pemrograman Visual", "2")
eBusiness = Course("IK510", "E-Business", "2")
nirwana = Course("DKV320", "Nirwana", "3")

ilmuKomputer = ProgramStudi("Ilmu Komputer", "IK", "FPMIPA")
dkv = ProgramStudi("Desain Komunikasi Visual", "DKV", "FPSD")

ilmuKomputer.addCourse(promvis)
ilmuKomputer.addCourse(eBusiness)

ilmuKomputer.addDosen(asepWahyudin)
ilmuKomputer.addDosen(yudi)

ilmuKomputer.addMhs(ojan)
ilmuKomputer.addMhs(maul)
ilmuKomputer.addMhs(reyhan)

dkv.addCourse(nirwana)
dkv.addDosen(sunandar)
dkv.addMhs(darto)

listProdi = []
listProdi.append(ilmuKomputer)
listProdi.append(dkv)

for n in listProdi:
    print("=== "+n.getNamaProdi()+" ===")
    # Display Data Mhs
    print("-Mahasiswa")
    headerMhs = ["NIK", "Nama", "NIM", "Semester", "IPK"]
    tabelMhs = Table(headerMhs)
    for i in n.getListMhs():
        temp = [i.getNik(), i.getNama(), i.getNim(),
                i.getSemester(), i.getIpk()]
        tabelMhs.addRow(temp)
    tabelMhs.displayData()

    # Display Data Dosen
    print("-Dosen")
    headerDosen = ["NIK", "Nama", "NIP", "Pendidikan Terakhir", "Keahlian"]
    tabelDosen = Table(headerDosen)
    for i in n.getListDosen():
        temp = [i.getNik(), i.getNama(), i.getNip(),
                i.getPendidikanTerkahir(), i.getKeahlian()]
        tabelDosen.addRow(temp)
    tabelDosen.displayData()

    # Display Data Course
    print("-Mata Kuliah")
    headerCourse = ["Kode MK", "Nama Matkul", "SKS"]
    tabelCourse = Table(headerCourse)
    for i in n.getListCourse():
        temp = [i.getKodeMK(), i.getNamaMataKuliah(), i.getJmlhSKS()]
        tabelCourse.addRow(temp)
    tabelCourse.displayData()
