class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


import math

INFINITY = math.inf  # float("inf")

def vertices(G):
    return sorted(G)

def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]

def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)

def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)

def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()

def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()

def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a

v_G1 = [Vertex(i) for i in range(8)]

G1 = {v_G1[0]: [v_G1[5], v_G1[4]],
      v_G1[1]: [v_G1[4], v_G1[5], v_G1[6]],
      v_G1[2]: [v_G1[4], v_G1[5], v_G1[6]],
      v_G1[3]: [v_G1[7]],
      v_G1[4]: [v_G1[0], v_G1[1], v_G1[2], v_G1[5]],
      v_G1[5]: [v_G1[0], v_G1[1], v_G1[2], v_G1[4]],
      v_G1[6]: [v_G1[1], v_G1[2]],
      v_G1[7]: [v_G1[3]]}

v_G2 = [Vertex(i) for i in range(8)]

G2 = {v_G2[0]: [v_G2[3], v_G2[4]],
      v_G2[1]: [v_G2[3], v_G2[4], v_G2[5]],
      v_G2[2]: [v_G2[3], v_G2[4], v_G2[5]],
      v_G2[3]: [v_G2[0], v_G2[1], v_G2[2], v_G2[4]],
      v_G2[4]: [v_G2[3], v_G2[0], v_G2[1], v_G2[2]],
      v_G2[5]: [v_G2[1], v_G2[2]]
      }


def is_connected(G):
    BFS(G,vertices(G)[0])
    for v in vertices(G):
        print(v.distance)
        if v.distance == INFINITY:
            return False
    return True

print(is_connected(G1))

print(is_connected(G2))