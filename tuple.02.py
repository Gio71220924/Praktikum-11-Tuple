nota = {
    'Nama toko' : 'Toko 5 tangan',
    'Pelanggan' : 'Charles',
    'Tanggal'   : '16-05-2023',
    'barang'    : [
        {
            'nama_barang' : 'Penghapus',
            'harga_barang' : 5000,
            'Jumlah_barang' : 4,
            'Sub_total' : 20000
        },
        {
            'nama_barang' : 'Spidol hitam',
            'harga_barang' : 10000,
            'Jumlah_barang' : 200,
            'sub_total'     : 2_000_000,
        },
        {
            'nama_barang' : 'Pensil',
            'harga barang' : 3000,
            'Jumlah_barang' : 10,
            'sub_total'     : 30000,
        },
    ],
    'Total_transaksi' : 2_050_000,
}

print(nota.keys())

print(nota['barang'][0].keys())
print(nota.values())
print(nota.items())



print('\n')
print('===== Menampilkan daftar belanjaan per nama barang ====')
for key, value in nota.items():
    print(f'{key}\t: {value}')

for key, value in nota['barang'][0].items():
    print(f'{key}\t: {value}')


print('\n')
print('===== Menampilkan daftar belanjaan full =====')
for barang in nota['barang']:
    for key,value in barang.items():
        print(f'{key}\t: {value}')

