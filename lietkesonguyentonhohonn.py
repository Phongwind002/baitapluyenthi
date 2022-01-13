import math
###
#check số nguyên tố
#
# @author viettuts.vn
# @param n: số nguyên dương
# @return true là số nguyên tố
# @return false không là số nguyên tố
###
def isPrimeNumber(n):
    # số nguyên n < 2 không phải là số nguyên tố
    if(n < 2):
        return False;
    # check số nguyên tố khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if(n % i ==0):
            return False;
    return True;

n = int(input("Nhập số nguyên dương n ="));
print ("Tất cả các sô nguyên tố nhỏ hơn" , n, "là");
sb =""
if(n >= 2):
    sb = sb + "2" + " ";
for i in range (3, n+1):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " ";
    i =  i + 2;
print(sb);    