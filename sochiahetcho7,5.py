sch = []#tao mang sch
for i in range(10,200):
    #dung for range chay tu 10 den 200
    if(i % 7 == 0) and (i % 5 !=0):
        #dieu kier chia het cho 7 nhung ko phai boi so cua 5
        sch.append(str(i))
        # them gia tri vao mang sch
print("," . join(sch))
#in thanh chuoi va cach nhau boi dau phay(,)