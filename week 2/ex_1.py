def machtv3(a,n):
    assert n > 0
    m = 1
    while n > 0:
        if n%2 == 0:
            a = a*a
            n /= 2
        else:
            m = m * a
            n -= 1

    return m

def machtv3_counter(a,n):
    assert n > 0
    counter =0
    m = 1
    while n > 0:
        if n%2 == 0:
            a = a*a
            n /= 2
        else:
            m = m * a
            n -= 1
        counter +=1

    return counter

print(machtv3_counter(2,10000))
print(2**10000)
