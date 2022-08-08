data=[]
def header_input():
    nama=input("Nama karyawan :")
    gaji=float(input("Gaji karyawan :"))
    data.append({"nama":nama,"gaji":gaji})
while True:
    header_input()    
    if input("Selesai?(y/n)")=="y":
        break

for i,v in enumerate(data):
    print(f"{i+1}. \t{v['nama']}\t{v['gaji']}")
    
