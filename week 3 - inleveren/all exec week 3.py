import string
#opdracht 1
def check(list_of_columns, new_column):  # ga na of i aan a toegevoegd kan worden
    n = len(list_of_columns)
    return not (new_column in list_of_columns or  # niet in dezelfde kolom
                new_column + n in [list_of_columns[j] + j for j in range(n)] or  # niet op dezelfde diagonaal
                new_column - n in [list_of_columns[j] - j for j in range(n)]) # niet op dezelfde diagonaal


def queen_rsearch(amount_of_queens,list_of_solutions,list_of_columns):
    for i in range(amount_of_queens):
        if check(list_of_columns, i):
            list_of_columns.append(i)
            if len(list_of_columns) == amount_of_queens:
                if list_of_columns not in list_of_solutions:
                    list_of_solutions.append(list(list_of_columns))
                    queen_rsearch(amount_of_queens,list_of_solutions,list_of_columns) # geschikte a gevonden
            else:
                if queen_rsearch(amount_of_queens,list_of_solutions,list_of_columns):
                    return True
            del list_of_columns[-1] # verwijder laatste element
    return False

def test_queen_rsearch():
    list_of_solutions = []
    queen_rsearch(8,list_of_solutions, [])
    print("the possible solutions for amount_of_qeeuns = 8")
    print(list_of_solutions)
    print("the amount of solutions: ",len(list_of_solutions))
    list_of_solutions2 = []
    queen_rsearch(4,list_of_solutions2,[])
    print("the possible solutions for amount_of_qeeuns = 4")
    print(list_of_solutions2)
    print("the amount of solutions: ", len(list_of_solutions2))

#opdracht 2:
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

def test_MyCircularLinkedList():
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

#opdracht 3:
class BSTNode:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self, nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' ' * nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def insert(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)
        return not found

    def insertArray(self, a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a) - 1
        mid = (low + high + 1) // 2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a, low, mid - 1)
        if high > mid:
            self.insertArray(a, mid + 1, high)

    def search(self, e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def search2(self, e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left;
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None

    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self, e):
        parent = self.getParent(e);

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True

    #hieronder staan de door mij toegevoegde functies:
    def rsearch(self,e):
        if self.element == e:
            return True
        elif self.element < e and self.right != None:
            return self.right.rsearch(e)
        elif self.element > e and self.left != None:
            return self.left.rsearch(e)
        else:
            return False

    def rinsert(self,e):
        if self.element < e:
            if not self.right:
                self.right = BSTNode(e,None,None)
                return True
            return self.right.rinsert(e)
        elif self.element > e:
            if not self.left:
                self.left = BSTNode(e,None,None)
                return True
            return self.left.rinsert(e)
        return False

class BST:
    def __init__(self, a=None):
        if a:
            mid = len(a) // 2
            self.root = BSTNode(a[mid], None, None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid + 1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def search(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def insert(self, e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False


    def delete(self, e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree();
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False

    def get_depth(self):
        node_list = []
        node_list.append(self.root)
        new_level = True
        level_counter = 0
        while new_level:
            level = []
            while len(node_list):
                level.append(node_list.pop(0))
            if len(level) == 0:
                new_level = False
                return level_counter

            for node in level:
                if node.left != None:
                    node_list.append(node.left)

                if node.right != None:
                    node_list.append(node.right)

            level_counter += 1

    #hieronder staan de door mij toegevoegde functies
    def max(self):
        root = self.root
        l_child = self.root.left
        r_child = self.root.right
        maximum =0
        while l_child != None or r_child != None:
            if l_child != None:
                if maximum <= l_child.element:
                    maximum = l_child.element
                l_child = l_child.left
            elif r_child != None:
                if maximum <= r_child.element:
                    maximum = r_child.element
                r_child = r_child.right

        return maximum

    def rsearch(self, e):
        if self.root and e:
            return self.root.rsearch(e)
        else:
            return None

    def rinsert(self, e):
        if e:
            if self.root:
                return self.root.rinsert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        return False

    def showLevelOrder(self):
        element_queue = myqueue([self.root])
        new_level = True
        level_counter =0
        while new_level:
            level = []

            while len(element_queue):
                level.append(element_queue.dequeue())
            if len(level) == 0:
                new_level = False
                return
            print("level", level_counter , ": ", end='')

            for node in level:
                print(node.element,end=' ')
            print()
            for node in level:
                if node.left != None:
                    element_queue.append(node.left)

                if node.right != None:
                    element_queue.append(node.right)

            level_counter +=1

    def pretty_print(self):
        offset = self.get_depth();
        element_queue = myqueue([self.root])
        level_counter = 0
        while offset:
            level = []

            while len(element_queue):
                level.append(element_queue.dequeue())

            print("level", level_counter, ": ", end=' ')

            for item in level:
                s = " " * offset**2
                if item:
                    print(s,item.element, end=' ')
                else:
                    print(s+" ", end ='  ')

            print()

            for i in range(len(level)):
                none_list = [None]*len(level)
                if level == none_list:
                    return
                elif level[i]:
                    if level[i].left != None:
                        element_queue.append(level[i].left)
                    else:
                        element_queue.append(None)

                    if level[i].right != None:
                        element_queue.append(level[i].right)
                    else:
                        element_queue.append(None)
                elif level[i] == None:
                    element_queue.append(None)
                    element_queue.append(None)

            level_counter += 1
            offset -=1


class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


def test_of_new_functions():
    tree_1= BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    tree_2 = BST()
    for i in range(1, 11):
        tree_2.insert(i)

    print("this is test tree_1\n",tree_1)
    print("this is test tree_2\n",tree_2)
    #test max function
    print("test of max function:\n the max of tree_1:",tree_1.max(),"\n the max of tree_2:",tree_2.max())
    #test of rsearch() function
    print("\ntest of rsearch function: ")
    print("is 14 in tree_1 (should be True): ",tree_1.rsearch(14))
    print("is 8 in tree_2 (should be True): ", tree_2.rsearch(8))
    print("is 2 in tree_2 (should be True): ", tree_2.rsearch(2))
    print("is 14 in tree_2 (should be False): ", tree_2.rsearch(14))
    print("is 20 in tree_1 (should be False): ", tree_1.rsearch(20))
    print("is 25 in tree_2 (should be False): ", tree_2.rsearch(25))
    #test of rinsert() function
    print("\ntest of rinsert function: ")
    print("rinsert(20)")
    tree_1.rinsert(20);
    print(tree_1)
    print("delete(2)")
    tree_1.delete(2)
    print(tree_1)
    print("rinsert(2)")
    tree_1.rinsert(2)
    print(tree_1)
    print ("delete(12))")
    tree_1.delete(12)
    print(tree_1)
    print("rinsert(12)")
    tree_1.rinsert(12)
    print(tree_1)
    #test of showLevelOrder() function:
    print("\ntest of showLevelOrder function: ")
    tree_1.showLevelOrder()
    print("\ntest of pretty_print function")
    tree_1.pretty_print()


#opdracht 4 (dictionary methode werkt, deze schrijft de input.txt file naar een frequentie tabel in output.csv
# trie implementatie is nog work in progress
def get_word_frequency_from_file_dict(file_name):
    input_file = open(file_name, "r")
    words_dict = {}
    for line in input_file:
        for word in line.split():
            #delete punctuation:
            table = str.maketrans({key: None for key in string.punctuation})
            word = word.translate(table)
            word = word.lower()
            if word is not '':
                if word not in words_dict:
                    words_dict[word] = 1
                else:
                    words_dict[word] += 1
    return words_dict

def write_freq_dict_to_file(file_name,freq_dict):
    output_file = open(file_name,"w")
    output_file.write("sep=;\n")
    output_file.write("word;frequency\n")
    for key in freq_dict:
        output_string = key + ";" + str(freq_dict.get(key)) + "\n"
        output_file.write(output_string)
    output_file.close()

class trie_node:
    def __init__(self,next_nodes,freq=0):
        self.freq = freq
        self.next_nodes = next_nodes

    def write_to_file(self,output_file,word = None):
        if self.freq > 0:
            output_string = word +";" +str(self.freq) + "\n"
            output_file.write(output_string)
        if self.next_nodes:
            for node in self.next_nodes:
                self.next_nodes[node].write_to_file(output_file,node)

class trie:
    def __init__(self):
        self.root = trie_node({})

    def add_word(self,word):
        current = self.root
        if word[0] not in current.next_nodes:  # add first letter of the word when not in next_nodes from the root
            current.next_nodes[word[0]] = trie_node({})
        current = current.next_nodes[word[0]]
        if len(word) <= 1:
            current.freq += 1
        for letters in range(1, len(word)):
            w = word[:letters + 1]
            if w not in current.next_nodes:
                current.next_nodes[w] = trie_node({})
            if letters == len(word) - 1:
                current.next_nodes[w].freq += 1
                return
            current = current.next_nodes[w]


    def fill_from_file(self,file_name):
        input_file = open(file_name,'r')
        for line in input_file:
            for word in line.split():
                # delete punctuation:
                table = str.maketrans({key: None for key in string.punctuation})
                word = word.translate(table)
                word = word.lower()
                if word is not '':
                    self.add_word(word)

    def write_to_file(self,file_name):
        output_file = open(file_name,"w")
        output_file.write("sep=;\n")
        output_file.write("word;frequency\n")
        self.root.write_to_file(output_file)



def test_freq_table():
    freq_dict = get_word_frequency_from_file_dict("input.txt")  # create dictionary with words and freqencies
    print("method 1: the dictionary:")
    print(freq_dict)  # show dict on screen
    print("frequency table writen to output_dict.csv")
    write_freq_dict_to_file("output_dict.csv", freq_dict)  # wirte dict as frequency table to output_dict.csv

    print("method 2: the trie")
    t = trie()  # make empty trie
    t.fill_from_file("input.txt")  # fill trie with contents of input.txt
    t.write_to_file("output_trie.csv")  # write freqency table to output_trie.csv
    print("frequency table wirten to output_trie.csv")


print("opdracht 1: ")
test_queen_rsearch()
print("\nopdracht 2: ")
test_MyCircularLinkedList()
print("\nopdracht 3: ")
test_of_new_functions()
print("\nopdracht 4: ")
test_freq_table()