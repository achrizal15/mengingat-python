def pecahin(kata):
    return [character for character in reversed(kata)]

while True:
    kata=input("Masukkan kata yang ingin dibalik : ")
    kata_terbalik="".join(pecahin(kata))
    print(kata_terbalik)
    isLanjut=input("Mau lagi?(Y/N)")
    if isLanjut.lower()=="n":
        break

