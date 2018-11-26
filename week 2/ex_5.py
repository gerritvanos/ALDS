def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random

counter = 0
def qsort(a,low=0,high=-1):
    global counter
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, min(a))
        m = low
        for j in range(low+1,high+1):

            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
            counter += 1
                            # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
        swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
        if m > 0:
            qsort(a,low,m-1)
        qsort(a,m+1,high)



def modyfied_qsort(a, low=0, high=-1):
    global counter
    if high == -1:
        high = len(a) - 1
    if low < high:
        swap(a, low, min(a))
        m = low
        for j in range(low + 1, high + 1):

            if a[j] < a[low]:
                m += 1
                swap(a, m, j)
            counter += 1
            # low < i <= m : a[i] < a[low]
            # i > m        : a[i] >= a[low]
        swap(a, low, m)
        # low <= i < m : a[i] < a[m]
        # i > m              : a[i] >= a[m]
        if m > 0:
            modyfied_qsort(a, low, m - 1)
        modyfied_qsort(a, m + 1, high)

def isSorted(a):
    i = 0;
    while i < len(a)-1 and a[i] <= a[i+1]:
        i += 1

    return i == len(a)-1

def test_qsort_count():
    a = [0]*10000
    for i in range(10000):
        a[i] = random.randint(0,10000)
    print("a generatad")


    qsort(a)
    print("is list a sorted:", isSorted(a))
    print("with 10.000 elements, elements get compared ",counter, " times")

test_qsort_count()
