"""
 * check so nguyen to trong Python
 *
 * @author viettuts.vn
 * @param n: so nguyen duong
 * @return 1 la so nguyen so,
 *         0 khong la so nguyen to
"""
import math
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
    #check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True;
ListPrimrNumber = []
print("cac so nguyen to nho hon 100 la:")
for i in range(0 , 100):
    if(isPrimeNumber(i)):
        ListPrimrNumber.append(i)
print(ListPrimrNumber)
"""
* Dinh nghia so nguyen to la so lon hon 1 va chi chia het
1 va chinh no.
* 2,3,5,7,11,13,17,... la nhung so nguyen to.
*chu y: so 0 va 1 khong phai la so nguyen to .Chi co so 2 la
so nguyen to chan, tat ca cac so chan khac khng phai
la so nguyen to vi chung chia het cho 2.
"""
