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
print ("Điểm đầu tiên là: ", diem[0])
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
sv = {"ten": "Nguyễn Hoàng Thiên", "lop": "26DKHA1", "diem" :7.5}
sv ["xep_loai"]="Khá"
for key, value in sv.items():
    print (key, ":", value)

#5
sinh_vien = ("SV001", "Nguyễn Văn An", 8.5)
ma_sv,ho_ten,diem = sinh_vien
print (f"Mã sinh viên: {ma_sv}, Họ tên: {ho_ten}, Điểm :{diem} ")

#6 
diem = [8.0, 4.5, 7.0, 3.5, 9.0, 5.5, 6.0]
dat =[]
chua_dat = []
for i in diem:
    if i >= 5.0:
        dat.append(i)
    else:
        chua_dat.append(i)
print ("Danh sách điểm đạt: ", dat)
print ("Danh sách điểm chưa đạt: ", chua_dat)
print ("Điểm trung bình của nhóm đạt là: ", sum(dat)/len(dat))

 #7
lop_a = ["SV01", "SV02", "SV03", "SV02"]
lop_b = ["SV03", "SV04", "SV01"]
ca_hai = set (lop_a) & set(lop_b)
chi_lop_a = set(lop_a).difference(set(lop_b))
print ("Các sinh viên có trong cả hai lớp là: ", ca_hai)
print ("Các sinh viên chỉ có trong lớp A là: ", chi_lop_a)
print ("Tổng số sinh viên có trong 2 lớp là: ",len(set(lop_a).union(set(lop_b))))

#8
tu = ["python", "ai", "python", "data", "ai", "python"]
dem = {}
for t in tu:
    if t in dem:

        dem[t] += 1
    else:
        dem[t] = 1
print ("Số lần xuất hiện của từng từ: ", dem)

#9
lop = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Bình", "diem": 7.0},
    {"ten": "Chi", "diem": 9.0},
    {"ten": "Dũng", "diem": 4.5},
]

for v in lop:
    if v["diem"] >= 8.5:
        v["xep_loai"] = "Giỏi"
    elif v["diem"] >= 7.0:
        v["xep_loai"] = "Khá"
    elif v["diem"] >= 5.0:
        v["xep_loai"] = "Trung bình"
    else:
        v["xep_loai"] = "Yếu"
for v in lop:
    print (v)