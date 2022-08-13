def faktorial(n=0):
    if n < 1:
        return f"Proses faktorial: 1 \nHasil faktorial: 1"
    hasil=n;
    proses=n;
    for i in reversed(range(1,n)):
        proses=f"{proses}x{i}"
        print(proses)
        hasil*=i
    return f"Proses faktorial: {proses} \nHasil faktorial: {hasil}"

def faktorialRecursifTail(n,hasil=0,result="",iterate=0):
    if iterate==0:
        hasil=n
        result=n
    if n <= 1 :
        return f"Proses faktorial: {result} \nHasil faktorial: {hasil}"
    result=f"{result}*{n-1}"
    print(result)
    hasil=hasil*(n-1)
    return faktorialRecursifTail(n-1,hasil,result,iterate-1)
def faktorialRecursif(n):
    if n<=1:
        return n
    return n*faktorialRecursif(n-1)
nilaiN=input("Masukkan nilai n: ")
print(faktorialRecursif(int(nilaiN)))