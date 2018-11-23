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

def test_machtv3():
    print("2 to the power of 6 with machtv3 function: ",machtv3(2, 6))
    print("2 to the power of 6 with ** operator: ", 2**6)
    print("amount of multiply's with n =10000: ", machtv3_counter(2,10000))

test_machtv3()