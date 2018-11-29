import random

#opdracht 1
"""
function to calculate the power of a given radix
this function is more efficient than the builtin function
Parameters
-------------
a: radix
    the base of wich the power needs to be calculated
b: power
    the power to use
Return
------------
m: int
    a to the power of n
"""
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

"""
function to calculate the power of a given radix
this function is more efficient than the builtin function
this function is used to get the amount of multiply's 
Parameters
-------------
a: int
    the base of wich the power needs to be calculated
b: int
    the power to use
Return
------------
counter: int
    amount of multiply's 
"""
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
"""
function to test both the machtv3 and machtv3_counter function
"""
def test_machtv3():
    print("2 to the power of 6 with machtv3 function: ",machtv3(2, 6))
    print("2 to the power of 6 with ** operator: ", 2**6)
    print("amount of multiply's with n =10000: ", machtv3_counter(2,10000))

#opdracht 2:
"""
class to implement a stack using a python list
"""
class my_stack:
    """
    constructor of the stack no parameters needed
    """
    def __init__(self):
        self.array = list()
        self.top = 0

    """
    function to push a new item on the stack this will become the new top element
    -------------
    new_value: can be any kind of variable
        the new value that needs to be added to the stack
    """
    def push(self,new_value):
        if (not self.is_empty()):
            self.top +=1

        self.array.append(new_value)

    """
    function to pop an item from the stack, the top element will be retruned
    -------------
    Return
    ------------
    temp: can be any kind of variable
       the top element of the stack
    """
    def pop(self):
        try:
            temp = self.array.pop()
        except:
            print("stack empty")
            return
        if (self.top >=1):
            self.top -=1
        return temp

    """
    function to check if the stack is empty
    """
    def is_empty(self):
        if (len(self.array) == 0):
            return 1
        return 0

    """
     function to look at the top item without removing it
     -------------
     Return
     ------------
        the top element of the stack
     """
    def peek(self):
        return self.array[self.top]

    """
     function to print the stack
     """
    def __repr__(self):
        return "the stack: " + str(self.array)

"""
function to test the stack, will print some information
"""
def test_my_stack():

    s1 = my_stack() #create_stack

    s1.push(1)
    s1.push(2)
    print("after 2 pushed: ", s1)
    print("test peek: " ,s1.peek())
    s1.push(3)
    print("stack before pop: ",s1)
    print("test pop: " ,s1.pop())
    print("test pop: " ,s1.pop())

    print(s1)
    s1.push(4)
    print("test pop: " ,s1.pop())
    print(s1.pop())
    print("this happens when try to pop but stack empty: ",s1.pop())

#opdracht 3:
"""
function to check if a 'haakjes uitdrukking' is correct on the bases of the given rules
using my_stack
Parameters
-------------
s: string
    the string wich contains a 'haakjes uitdrukking'
Return
------------
 string
    "correcte string" if string is correct
    "incorrecte string" if string is not correct
"""
def check_string(s):
    stack = my_stack()
    for i in range(len(s)):
        if (s[i] == '<' or s[i] == '[' or s[i] == '('):
            stack.push(s[i])
        elif (s[i] == '>'):
            if stack.peek() == '<':
                stack.pop()
        elif(s[i] == ']'):
            if stack.peek() == '[':
                stack.pop()
        elif(s[i] == ')'):
            try:
                if stack.peek() == '(':
                    stack.pop()
            except:
                return "incorrecte string"


    if stack.is_empty():
        return "correcte string"
    return "incorrecte string"

"""
function to test check_string()
"""
def test_check_string():
    goed_voorbeeld_1 = "(())))"
    goed_voorbeeld_2 = "[(<>)]( )(( )( ))"
    goed_voorbeeld_3 = "((<>))"

    fout_voorbeeld_1 = "([)]"
    fout_voorbeeld_2 = "((( < ) >))"
    fout_voorbeeld_3 = "({}{}{}[[[]"

    print("dit is een goed voorbeeld:'",goed_voorbeeld_1,"':  ",check_string(goed_voorbeeld_1))
    print("dit is een goed voorbeeld: '",goed_voorbeeld_2,"':  ",check_string(goed_voorbeeld_2))
    print("dit is een goed voorbeeld: '",goed_voorbeeld_3,"':  ",check_string(goed_voorbeeld_3))

    print("dit is een fout voorbeeld: '",fout_voorbeeld_1,"':  ",check_string(fout_voorbeeld_1))
    print("dit is een fout voorbeeld: '",fout_voorbeeld_2,"':  ",check_string(fout_voorbeeld_2))
    print("dit is een fout voorbeeld: '", fout_voorbeeld_3, "':  ", check_string(fout_voorbeeld_3))

#opdracht 4:
"""
recursive function to return the binary representation of a given number
Parameters
-------------
n: int
    the number of wich the binary is needed
Return
------------
 string
    the binary value of the number
"""
def my_bin(n):
    assert n>=0

    if n==1:
        return "1"
    elif n%2 ==1:
        return my_bin((n-1) / 2) + "1"
    elif n%2 ==0:
        return my_bin(n/2)+"0"
"""
function to test my_bin()
"""
def test_my_bin():
    print("100 in binary with my_bin: 0b",my_bin(100))
    print("100 in binary with python function ",bin(100))
    print("220 in binary with my_bin: 0b",my_bin(220))
    print("220 in binary with python function ",bin(220))


#opdracht 5
def swap(a,i,j): #function from joop
    a[i],a[j] = a[j],a[i]

counter = 0
def qsort(a,low=0,high=-1): #qsort from joop modified with counter
    global counter
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
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



def isSorted(a): #function from joop
    i = 0;
    while i < len(a)-1 and a[i] <= a[i+1]:
        i += 1

    return i == len(a)-1

def test_qsort_count():
    global counter
    random_list = [0]*10000
    random_list2 = [0] * 10000
    for i in range(10000):
        random_list[i] = random.randint(0,10000)
        random_list2[i]=random_list[i]
    print("random_list generatad")

    qsort(random_list)
    print("is random_list sorted:", isSorted(random_list))
    print("with 10.000 elements, elements get compared ",counter, " times")

    counter =0
    modyfied_qsort(random_list2)
    print("with 10.000 elements in worst case scenario elements get compared ", counter, " times")

#alle opdrachten onder elkaar uitgeprint
print("\n opdracht 1:")
test_machtv3()
print("\n opdracht 2")
test_my_stack()
print("\n opdracht 3")
test_check_string()
print("\n opdracht 4")
test_my_bin()
print("\n opdracht 5")
test_qsort_count()