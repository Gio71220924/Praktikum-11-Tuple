#List of tuplesssss
data_laundry = [
    (100, 'Charles', 20, 100000),
    (129, 'bambang', 5, 20000),      #index 0     #No, nama, transaksi terakhir(Kg), transaksi terakhir(Rp)
    (119, 'Agus', 2, 50000),         #index 1    
    (120, 'Wati', 1, 5000),         #Index 2
    
]

total = 0
for data in data_laundry:
    #print(data[3])                  #Ambil total pendapatan
    total = total + data[3]

print(f'Total pendapatan adalah Rp{total}')

#urutkan berdasarkan  nomor pelanggan (dengan syarat panjang tuple harus samaaaaa!!)
data_laundry.sort()                 #Kalau mau urut dibalik pake (reverse = True)
for data in data_laundry:           #Ambil nomor pelanggan dan nama pelanggan
    print(f'{data[0]}. {data[1]}')   
  
#urutkan pelanggan yang transaksi paling banyak dan paling sedikit.
data_laundry.sort(key = lambda x : x[3], reverse = True)
print('Top spending pelangggan laundry')
for data in data_laundry:
    print(f'{data[0]}. {data[1]}\t Rp.{data[3]}')
       

