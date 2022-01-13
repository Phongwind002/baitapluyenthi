"""
# Chuyển đổi số nguyên n sang hệ cơ số b
#
# @param n: so nguyen
# @param b: he co so
# @return he co so b
"""
def covert_number(n , b):
    if(n < 0 or b < 2 or b > 16):
        return "";
    sb = "";
    m = 0;
    remainder = n;

    while (remainder > 0):
        if(b > 10):
            m = remainder % b;
            if ( m >= 10):
                sb = sb + str(chr(55 + m));
            else:
                sb = sb +str(m);
        else:
            sb = sb + str(remainder % b);
        remainder = int(remainder / b);
    return    "".join(reversed(sb));
n = int(input("Nhap 2 so nguyen n = "));
print("He co so 2 cua so nguyen" , n, "la:" , covert_number(n , 2))
print("He co so 16 cua so nguyen to" , n, "la:" , covert_number(n , 16))
