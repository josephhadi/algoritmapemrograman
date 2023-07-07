tuple_1 =("faqih","nicko","ageng","ihsan","adin")
tuple_2 =(23,42,12,53,64)
tuple_3 =("putri","puri","syifa","lord anggun")

print (tuple_1)
print (tuple_2)
print (tuple_3)

#membuat tuple yang bernilai kosong
empty_tuple =()
print("tuple kosong: ", empty_tuple)

#tuple bernilai integer
int_tuple = (4,6,8,10,12,14)
print ("tuple bernilai integer: ", int_tuple)

# tuple dengan kombinasi tipe data
mixed_tuple = (4,"phyton",9.3)
print ("tuple dengan type data yang berbeda: ", mixed_tuple)

#tuple bersarang
nested_tuple = ("phyton", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))
print ("A tuple bersarang: ", nested_tuple)

print ()
print ()
print ()

# membuat list

identitas = ["puri",19, "indonesia"]
prodi_1 = ["informatika",10]
prodi_2 = ["system informasi",11]
dosen_1 = [10,"Mr.Mursalim"]
dosen_2 = [11, "Mr..Satriawan"]

print("Cetak Semua Data...")
print("--------------------------------------------------------------")
print("nama ; %s, usia: %d, negara: %s"%(identitas[0], identitas[1],identitas[2]))
print("--------------------------------------------------------------")
print("cetak program studi...")
print("-------------------------------------------------------")
print("program studi 1:\nNama prodi Pertama: %s, ID: %d\nProgram Studi Kedua:\nNama prodi kedua: %s, ID:%s"%(prodi_1[0],prodi_1[1],prodi_2[0],prodi_2[1]))
print("---------------------------------------")
print("dosen pengampu...")
print("-----------------------------------")
print("Dosen informatika: %s, ID: %d"%(dosen_1[1],dosen_2[0]))
print("Dosen Sistem informasi: %s, Id: %d"%(dosen_2[1],dosen_2[0]))
print(type(identitas),type(prodi_1),type(prodi_2),type(prodi_1),type(prodi_2))

print()
print()
print()

list = [1,2,3,4,5]

#foward
print("-----------------------------------------")
print("foward")
print("-----------------------------------------------------")
print(list[1])
print(list[3:])
print(list[:1])
print(list[1:3])

#backward
print("-----------------------------------------")
print("backward")
print("-----------------------------------------------------")
print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-1:-3])
