def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random

def qsort(a,low=0,high=-1):
    counter =0
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
        for j in range(low+1,high+1):
            counter +=1
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
                           # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
        swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
        if m > 0:
            return qsort(a,low,m-1) +counter
        return qsort(a,m+1,high) +counter
    return 1


def isSorted(a):
    i = 0;
    while i < len(a)-1 and a[i] <= a[i+1]:
        i += 1

    return i == len(a)-1

def qsort_count():
    a = [0]*10000
    for i in range(10000):
        a[i] = random.randint(0,10000)
    print("a generatad")


    counter = qsort(a)
    print("is list a sorted:", isSorted(a))
    print("with 10.000 element elements get compared ",counter, " times")

qsort_count()
