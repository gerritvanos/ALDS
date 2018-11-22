#opdracht 1
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

#opdracht 2:
class my_stack:
    def __init__(self):
        self.array = list()
        self.top = 0

    def push(self,new_value):
        if (not self.is_empty()):
            self.top +=1

        self.array.append(new_value)


    def pop(self):
        try:
            temp = self.array.pop()
        except:
            print("stack empty")
            return
        if (self.top >=1):
            self.top -=1
        return temp

    def is_empty(self):
        if (len(self.array) == 0):
            return 1
        return 0

    def peek(self):
        return self.array[self.top]

    def __repr__(self):
        return "the stack: " + str(self.array)


def test_my_stack():

    s1 = my_stack() #create_stack

    s1.push(1)
    s1.push(2)
    print("after 2 pushed: ", s1)
    print("test peek: " ,s1.peek())
    s1.push(3)

    print("test pop: " ,s1.pop())
    print("test pop: " ,s1.pop())

    print(s1)
    s1.push(4)
    print("test pop: " ,s1.pop())
    print(s1.pop())
    print(s1.pop())

#opdracht 3:
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
            if stack.peek() == '(':
                stack.pop()


    if stack.is_empty():
        return "correcte string"
    return "incorrecte string"


def test_check_string():
    goed_voorbeeld_1 = "((<>)())"
    goed_voorbeeld_2 = "[(<>)]( )(( )( ))"
    goed_voorbeeld_3 = "((<>))"

    fout_voorbeeld_1 = "([)]"
    fout_voorbeeld_2 = "((( < ) >))"

    print("dit is een goed voorbeeld: ",check_string(goed_voorbeeld_1))
    print("dit is een goed voorbeeld: ",check_string(goed_voorbeeld_2))
    print("dit is een goed voorbeeld: ",check_string(goed_voorbeeld_3))

    print("dit is een fout voorbeeld: ",check_string(fout_voorbeeld_1))
    print("dit is een fout voorbeeld: ",check_string(fout_voorbeeld_2))

#opdracht 4:
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



test_machtv3()
test_my_stack()
test_check_string()
test_my_bin()