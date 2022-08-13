data=[]
globalvariable=0
def header_input():
    global globalvariable
    globalvariable=20
    nama=input("Nama karyawan :")
    gaji=float(input("Gaji karyawan :"))
    for i in data:
        if i["nama"]==nama.lower(): return "Data sudah ada"
    data.append({"nama":nama,"gaji":gaji})
    return "Data ditambah!"

while True:
    print(header_input()) 
    if input("Selesai?(y/n)")=="y":
        break
print(globalvariable)
for i,v in enumerate(data):
    print(f"{i+1}. \t{v['nama']}\t{v['gaji']}")
    
