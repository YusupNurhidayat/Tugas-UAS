
from decisionmaking import keluaran
def inputan(n):
    daftarnama = []
    nilaiuts = []
    nilaiuas = []
    tugas = []
    for x in range(n):
        daftarnama1 = str(input("Masukkan nama siswa ke-{} : ".format(x+1)))
        daftarnama.append(daftarnama1)
        nilaiuts1 = float(input("Masukkan nilai uts-{} :  ".format(daftarnama[x])))
        nilaiuts.append(nilaiuts1)
        nilaiuas1 = float(input("Masukkan nilai uas-{} :  ".format(daftarnama[x])))
        nilaiuas.append(nilaiuas1)
        tugas1 = float(input("Masukkan nilai tugas-{} :  ".format(daftarnama[x])))
        tugas.append(tugas1)
        print()
    a=1
    totalan(a,n,daftarnama,nilaiuts,nilaiuas,tugas)
        
def totalan(a,n,daftarnama,nilaiuts,nilaiuas,tugas):
    total = []
    while a <= n:
        hasil = (nilaiuts[a-1] + nilaiuas[a-1] + tugas[a-1]) / 3
        total.append(hasil)
        a = a + 1
    forloop(n,daftarnama,nilaiuts,nilaiuas,tugas,total)

def forloop(n,daftarnama,nilaiuts,nilaiuas,tugas,total):        
    for x in range(n):
        keluaran(total,daftarnama,nilaiuts,nilaiuas,tugas,x)


