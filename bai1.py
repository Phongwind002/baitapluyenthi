"""
 * Tính số fibonacci thứ n
 * in day so fibonacci trong python ko su dung de quy
 * @param n: chỉ số của số fibonacci tính từ 0
 *           vd: F0 = 0, F1 = 1, F2 = 1, F3 = 2
 * @return số fibonacci thứ n
 *Quy luật của dãy số Fibonacci: số tiếp theo bằng tổng của 2 số trước, 2 số đầu tiên của dãy số là 0, 1. Ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
 """


def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;

    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;


print("10 số đầu tiên của dãy số Fibonacci: ");
sb = "";
for i in range(0, 10):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)