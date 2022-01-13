"""
 * Phân tích số nguyên thành tích các thừa số nguyên tố
 *
 * @param positiveInt
 * @return
"""
from typing import List, Sized


def phanTichSoNguyen(n):
    i = 2;
    ListNumbers = [];
    # phân tích
    while (n > 1):
        if( n % i == 0):
            n = int(n / i);
            ListNumbers.append(i);
        else:
            i = i + 1;
    # nếu ListNumbers trống thì add n vào ListNumbers
    if(len(ListNumbers) == 0):
        ListNumbers.append(n);
    return ListNumbers;

n = int(input("Nhập số nguyên dương n ="));
# phân tích số nguyên dương n
ListNumbers = phanTichSoNguyen(n);
size = len(ListNumbers);
sb = "";
for i in range(0, size - 1):
    sb = sb + str(ListNumbers[i]) + " x ";
sb = sb + str (ListNumbers[size - 1]);
# in ra kết quả ra màn hình
print("Kết quả", n, "=",sb);