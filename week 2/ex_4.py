def my_bin(n):
    assert n>=0

    if n==1:
        return "1"
    elif n%2 ==1:
        return my_bin((n-1) / 2) + "1"
    elif n%2 ==0:
        return my_bin(n/2)+"0"

print("0b"+my_bin(100))