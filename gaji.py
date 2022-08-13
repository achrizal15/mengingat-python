data=[]
globalvariable=0
def header_input():
    global globalvariable
    globalvariable=20
    nama=input("Nama karyawan :")
    gaji=float(input("Gaji karyawan :"))
    print(nama in data)
    data.append({"nama":nama,"gaji":gaji})

while True:
    header_input()    
    if input("Selesai?(y/n)")=="y":
        break
print(globalvariable)
for i,v in enumerate(data):
    print(f"{i+1}. \t{v['nama']}\t{v['gaji']}")
    
