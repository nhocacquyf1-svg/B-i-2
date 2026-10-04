#D1
diem = [7, 8.5, 6, 9, 5.5]
tong = 0
for i in diem:
        tong += i
print("Tổng điểm là: ", tong)
print ("Điểm trung bình là: ", tong/len(diem))

#D2
so = [12, 45, 7, 89, 23, 56]
lon_nhat = so[0]
for i in so:
    if i > lon_nhat:
                lon_nhat = i
print("Số lớn nhất là: ", lon_nhat)

#D3
so_chan = 0
for i in so:
    if i%2==0:
        so_chan +=1
print ("Số lượng số chẵn là: ", so_chan)

#D4
so1 =[]
for x in so:
    if x >=20:
        so1.append(x)
print("Các số lớn hơn hoặc bằng 20 là: ", so1)