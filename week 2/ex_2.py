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

test_my_stack()