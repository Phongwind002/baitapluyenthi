
"""
 * tinh giai thua ko su dung de quy
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return giai thua cua so n
"""
def tinhgiaithua(n):
    giai_thua = 1;
    if( n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range( 2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;
n = int( input("Nhap so nguyen duong n ="));
print("Giai thua cua" , n, "la" , tinhgiaithua(n));