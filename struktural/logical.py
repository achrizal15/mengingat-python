sisi=int(input("Masukkan bilangan genap : "))
count=1
spasi=int(sisi/2)
lipatan=True
print(5*"=","MENGGUNAKAN WHILE",5*"=")
while True:
    if count == 0:break
    if lipatan:
        if count%2!=0:
            print(spasi*" ",count*"*")
            spasi-=1
        count+=1
        if count >= sisi :
            count-=1
            spasi+=1
            lipatan=False
    else:
        if count%2!=0:
            print(spasi*" ",count*"*")
            spasi+=1
        count -=1
print(5*"=","MENGGUNAKAN FOR",5*"=")
space=int(sisi/2)
for i in range(sisi):
    if i%2!=0:
        print(space*" ",i*"*")
        space-=1

for i in reversed(range(sisi)):
    if i % 2 != 0:
        space+=1
        print(space*" ",i*"*")

    