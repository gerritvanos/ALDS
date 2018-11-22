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

test_check_string()