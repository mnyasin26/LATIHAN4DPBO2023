from ProgramStudi import ProgramStudi
from Course import Course
from Dosen import Dosen
from Mahasiswa import Mahasiswa

ojan = Mahasiswa("19832912732", "Fauzan", "Laki-laki", "Universitas_Pendidikan_Indonesia", "ojan@upi.edu", "FPMIPA", "2100137", "4", "3.97",)
maul = Mahasiswa("19832912245", "Maulana", "Laki-laki", "Institut_Teknologi_Bandung", "maul@itb.ac.id", "STEI-K", "435113434", "2", "3.85")
reyhan = Mahasiswa("19832916839", "Reyhan_Adonis", "Laki-laki", "Telkom_University", "reyhan@telkom.id", "Komunikasi", "20213623", "4", "3.9")

yudi = Dosen("19832916839", "Yudi_Wibisono", "Laki-laki", "Universitas_Pendidikan_Indonesia", "yudi@upi.edu", "FPMIPA", "198282147922", "S3", "Mobile_Programming")
asepWahyudin = Dosen("1979", "Asep_Wahyudin", "Laki-laki", "Universitas_Pendidikan_Indonesia", "away@upi.edu", "FPMIPA", "199638468216", "S3", "RPL")

promvis = Course("IK412", "Pemrograman Visual", "2")
eBusiness = Course("IK510", "E-Business", "2")

ilmuKomputer = ProgramStudi("Ilmu Komputer", "Kode", "FPMIPA")

ilmuKomputer.addCourse(promvis)
ilmuKomputer.addCourse(eBusiness)

ilmuKomputer.addDosen(asepWahyudin)
ilmuKomputer.addDosen(yudi)

ilmuKomputer.addMhs(ojan)
ilmuKomputer.addMhs(maul)
ilmuKomputer.addMhs(reyhan)

# print(ojan.getNim())

for i in ilmuKomputer.getListhMhs():
    print("NIK: "+i.getNik())
    print("Nama:" +i.getNama())
    print("Semester: " +i.getSemester())
    print("IPK: "+i.getIpk())
# print(ilmuKomputer.getListhMhs().getNim())
# print(ilmuKomputer.getListhDosen())
# print(ilmuKomputer.getListhCourse())