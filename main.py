NamaDepan = "Pakde"
NamaAkhir = "Jokowi"

NamaLengkap = NamaDepan + " " + NamaAkhir

print ("Nama depannya :", NamaDepan)
print ("Nama Belakagnya :", NamaAkhir)
print ("Nama Lengkapnya :", NamaLengkap)

#konveri string ke biner
res = ' '.join(format(ord(i), 'b') for i in NamaLengkap)
print("Bilangan biner dari", NamaLengkap, "adalah:", res)

#konversi string ke oktal
nama_int = int.from_bytes(NamaLengkap.encode(), 'big')
octal = oct(nama_int)
print("bilangan octal dari", NamaLengkap, "adalah :", octal)

#oktal ke hexadesimal
oct_int = int(octal, 8)
hexa = hex(oct_int)
print("bilangan hexadecimal dari", NamaLengkap, "adalah :", hexa)
