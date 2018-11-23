def my_bin(n):
    assert n>=0

    if n==1:
        return "1"
    elif n%2 ==1:
        return my_bin((n-1) / 2) + "1"
    elif n%2 ==0:
        return my_bin(n/2)+"0"


def test_my_bin():
    print("100 in binary with my_bin: 0b",my_bin(100))
    print("100 in binary with python function ",bin(100))
    print("220 in binary with my_bin: 0b",my_bin(220))
    print("220 in binary with python function ",bin(220))

test_my_bin()