def max_value(data):
    return max (data)

def min_value(data):
    return min (data)


def average(data):
    return sum(data)/len(data)


#Program utama
#Input user
n = int(input('Masukan n:'))
data = []
for i in range(n):
    angka  = int(input('Masukan angka:'))
    data.append(angka)

maks = max_value(data)
print(f'Nilai maksimum:{maks}')

min = min_value(data)
print(f'Nilai maksimum:{min}')

rata = average(data)
print(f'Nilai rata - rata: {rata:.2f}')


print('Urut ascending:', end="")
(data.sort())
print(data)
print('Urut ascending:', end="")
data.sort(reverse=True)
print(data)

