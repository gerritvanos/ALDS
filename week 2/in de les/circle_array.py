class cicle_array:

    def __init__(self, size):
        self.size = size
        self.add_pointer = 0
        self.pop_pointer = 0
        self.array = [None] *size

    def pop(self):
        temp = self.array[self.pop_pointer]
        self.array[self.pop_pointer] = None
        self.pop_pointer+=1
        if (self.pop_pointer == self.add_pointer):
            self.pop_pointer -=1
        elif(self.pop_pointer >=self.size):
            self.pop_pointer =0
        return str(temp)

    def append(self, new_value):
        self.array[self.add_pointer] = new_value

        self.add_pointer +=1
        if (self.add_pointer >=self.size):
            self.add_pointer =0


    def __repr__(self):
        return "the circle array" +  str(self.array)


c1 = cicle_array(4)

c1.append(1)
c1.append(2)
c1.append(3)
c1.append(4)

print(c1)
print(c1.pop())
print(c1)
print(c1.pop())
print(c1)
print(c1.pop())
print(c1)
print(c1.pop())

c1.append(5)
print(c1)
print(c1.pop())
print(c1)