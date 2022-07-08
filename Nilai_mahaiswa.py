def keluaran(total,daftarnama,nilaiuts,nilaiuas,tugas,x):
    if total[x] >= 95:
        predikat ='A+'
        lulus = 'Lulus'
    elif total[x] >= 85 and total[x] < 95:
        predikat ='A'
        lulus = 'Lulus'
    elif total[x] >= 75  and total[x] < 85:
        predikat ='B+'
        lulus = 'Lulus'
    elif total[x] >= 65  and total[x] < 75:
        predikat ='B'
        lulus = 'Lulus'
    elif total[x] >= 55  and total[x] < 65:
        predikat ='C'
        lulus = 'Lulus'
    elif total[x]>= 45  and total[x] < 55:
        predikat ='D'
        lulus = 'Tidak Lulus'
    elif total[x] < 45:
        predikat ='E'
        lulus = 'Tidak Lulus'
    print ('nama : ', daftarnama[x])
    print ('Predikat : ', predikat)
    print ('Hasil : ', lulus)
    print()
        
