#1.1
class node:
    def __init__(self,e,next):
        self.element = e
        self.next = next

class my_queue:
    def __init__(self):
        self.begin = None
        self.end = None

    def enqueue(self,e):
        if not self.begin:
            self.begin = node(e,None)
            self.end =self.begin
        else:
            self.end.next = node(e,None)
            self.end = self.end.next

    def dequeue(self):
        if self.begin:
            value = self.begin.element
            self.begin = self.begin.next
            return value
        else:
            return None

print("1.1 queue(1,2,3,4,5,6)")
q = my_queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

#1.2

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

    def is_balanced(self):
        depth = self.get_depth()
        orderd_list =[]
        inorder_list(self.root, orderd_list)
        amount_of_elements = len(orderd_list)

        if amount_of_elements >= (2**(depth-1)):
            if amount_of_elements <= (2**depth-1):
                return True
        return False

def inorder_list(parent,orderd_list):
    if parent.left:
        inorder_list(parent.left,orderd_list)
    orderd_list.append(parent.element)

    if parent.right:
        inorder_list(parent.right,orderd_list)




print("\n1.2:")
b = BST([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
tree_2 = BST()
for i in range(1, 11):
    tree_2.insert(i)

orderd_list = []
inorder_list(b.root,orderd_list)
print(orderd_list)
print("depth of b: ", b.get_depth())
print("is b balanced: ",b.is_balanced())
print("is tree_2 balanced: ",tree_2.is_balanced())


