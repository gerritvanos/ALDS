class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        last = self.tail
        if last != None:
            current = last.next
            s = s + str(current)
            if current == last:
                return s
            current = current.next
            while current != last:
                s = s + " -> " + str(current)
                current = current.next
            s = s + " -> " + str(current)
        if not s: # s == '':
            s = 'empty list'
        return s

    def append(self,e):
        if not self.tail: # self.tail == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e,self.tail.next)
            self.tail.next = n
            self.tail = n

    def delete(self,e):
        if self.tail: # self.head != None:
            if self.tail.next == self.tail:
                if self.tail.data == e:
                    self.tail = None
            elif self.tail.data == e:
                current_node = self.tail
                while current_node.next != self.tail:
                    current_node = current_node.next
                current_node.next = self.tail.next
                self.tail = current_node
            else:
                current = self.tail.next
                while current != self.tail:
                    if current.data == e:
                        current_node = current.next
                        while current_node != current:
                            prev = current_node
                            current_node = current_node.next
                        prev.next = current.next
                        current.tail = None
                    current = current.next



mylist = MyCircularLinkedList()
print(mylist)
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
print(mylist)
mylist.delete(2)
print(mylist)
mylist.delete(3)
print(mylist)
mylist.delete(6)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(3)
print(mylist)
mylist.delete(4)
print(mylist)
mylist.delete(5)
print(mylist)


mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
mylist.delete(3)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(2)
print(mylist)
