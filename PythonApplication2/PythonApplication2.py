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

#Bài 3: List, turple, set, dictionary
#1
diem = [7.5, 8.0, 6.5, 9.0, 5.5]
print ("Điểm đầu tiên là: ")
print ("Điểm cuối cùng là: ", diem[-1])
print ("Điểm trung bình là: ", sum(diem)/len(diem))
print ("Điểm cao nhất là: ", max(diem))

#2
diem1 = [7.5, 8.0, 6.5]
diem1.append(9.0)
print ("Danh sách điểm sau khi thêm là: ", diem1)
diem1.insert(1, 5.5)
print ("Danh sách điểm sau khi chèn là: ", diem1)
diem1[0] = 8.5
print ("Danh sách điểm sau khi sửa điểm đầu tiên là: ",diem1)
diem1.remove(6.5)
print ("Danh sách điểm sau khi xóa điểm 6.5 là: ", diem1)

#3
ma = ["SV001", "SV002", "SV001", "SV003", "SV002"]
ma_ko_trung =set(ma)
print ("Số lượng mã không trùng là ", len(ma_ko_trung))

#4
sv = {"ten": "Nguyễn Hoàng Thiên", "lop": "26DKHA1", "diem" :"7.5"}
sv ["xep_loai"]="Khá"
for key, value in sv.items():
    print (key, ":", value)