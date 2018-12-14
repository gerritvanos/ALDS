import  copy

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

#bellow are the functions I added
#opdracht 1
def is_connected(G): #returns True if connected
    BFS(G,vertices(G)[0])
    for v in vertices(G):
        if v.distance == INFINITY:
            clear(G)
            return False
    return True


def test_is_connected():
    v_G1 = [Vertex(i) for i in range(8)]

    G1 = {v_G1[0]: [v_G1[5], v_G1[4]],
          v_G1[1]: [v_G1[4], v_G1[5], v_G1[6]],
          v_G1[2]: [v_G1[4], v_G1[5], v_G1[6]],
          v_G1[3]: [v_G1[7]],
          v_G1[4]: [v_G1[0], v_G1[1], v_G1[2], v_G1[5]],
          v_G1[5]: [v_G1[0], v_G1[1], v_G1[2], v_G1[4]],
          v_G1[6]: [v_G1[1], v_G1[2]],
          v_G1[7]: [v_G1[3]]}

    v_G2 = [Vertex(i) for i in range(6)]

    G2 = {v_G2[0]: [v_G2[3], v_G2[4]],
          v_G2[1]: [v_G2[3], v_G2[4], v_G2[5]],
          v_G2[2]: [v_G2[3], v_G2[4], v_G2[5]],
          v_G2[3]: [v_G2[0], v_G2[1], v_G2[2], v_G2[4]],
          v_G2[4]: [v_G2[3], v_G2[0], v_G2[1], v_G2[2]],
          v_G2[5]: [v_G2[1], v_G2[2]]
          }

    print("is G1 connected(should be False): ",is_connected(G1))
    print("is G2 connected(should be True): ",is_connected(G2))


#opdracht 2:
def no_cycles(G): # returns True if G has cycles
    if len(edges(G))/2 > len(vertices(G))-1:
        return True
    return False

def no_cycles_with_BFS(G):
    list_of_vertices = vertices(G)
    current_node = list_of_vertices[0]
    current_node.predecessor = None
    current_node.distance = 0
    for v in list_of_vertices:
        if v != current_node:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(current_node)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
            elif u.predecessor != v:
                return True
    return False

def test_no_cycles():
    v_G2 = [Vertex(i) for i in range(6)]

    G2 = {v_G2[0]: [v_G2[3], v_G2[4]],
          v_G2[1]: [v_G2[3], v_G2[4], v_G2[5]],
          v_G2[2]: [v_G2[3], v_G2[4], v_G2[5]],
          v_G2[3]: [v_G2[0], v_G2[1], v_G2[2], v_G2[4]],
          v_G2[4]: [v_G2[3], v_G2[0], v_G2[1], v_G2[2]],
          v_G2[5]: [v_G2[1], v_G2[2]]
          }
    v_G3 = [Vertex(i) for i in range(8)]

    G3 = {v_G3[0]: [v_G3[4], v_G3[5]],
          v_G3[1]: [v_G3[4], v_G3[6]],
          v_G3[2]: [v_G3[5]],
          v_G3[3]: [v_G3[7]],
          v_G3[4]: [v_G3[0], v_G3[1]],
          v_G3[5]: [v_G3[0], v_G3[2]],
          v_G3[6]: [v_G3[1]],
          v_G3[7]: [v_G3[3]]
           }

    print("does G2 have cycles(should be True): ",no_cycles(G2))
    print("does G3 have cycles(should be False): ",no_cycles(G3))
    print("does G2 have cycles(should be True)(with BFS): ", no_cycles_with_BFS(G2))
    print("does G3 have cycles(should be False)(with BFS): ", no_cycles_with_BFS(G3))

#opdracht 3:
def get_bridges(G):
    list_of_bridges =[]
    list_of_edges = edges(G)
    for edge in list_of_edges:
        G[edge[1]].remove(edge[0])
        G[edge[0]].remove(edge[1])
        BFS(G,edge[0])
        for v in vertices(G):
            if v == edge[1]:
                if v.distance == INFINITY:
                    list_of_bridges.append(edge)
        G[edge[1]].append(edge[0])
        G[edge[0]].append(edge[1])
    return list_of_bridges



def test_get_bridges():
    v_G4 = [Vertex(i) for i in range(8)]

    G4 = {v_G4[0]: [v_G4[1], v_G4[3]],
          v_G4[1]: [v_G4[0], v_G4[2]],
          v_G4[2]: [v_G4[1], v_G4[3], v_G4[4]],
          v_G4[3]: [v_G4[0], v_G4[2]],
          v_G4[4]: [v_G4[2], v_G4[5], v_G4[6]],
          v_G4[5]: [v_G4[4], v_G4[6]],
          v_G4[6]: [v_G4[4], v_G4[5], v_G4[7]],
          v_G4[7]: [v_G4[6]]
          }

    print("the bridges of G4 are: ",get_bridges(G4))
    print("should be: \t\t\t\t[(2, 4), (4, 2), (6, 7), (7, 6)]")


#opdracht 4:
def is_strongly_connected(G):
    current_node = vertices(G)[0]
    counter = 0
    while current_node:
        BFS(G, current_node)
        for v in vertices(G):
            if v.distance == INFINITY:
                return False
        counter +=1
        if counter >= len(vertices(G)):
            break;
        current_node = vertices(G)[counter]
    return True

def is_strongly_connected_with_reverse(G):
    current_node = vertices(G)[0]
    BFS(G,current_node)
    for v in vertices(G):
        if v.distance == INFINITY:
            return False

    for edge in edges(G): #reverse list
        G[edge[0]].remove(edge[1])
        G[edge[1]].append(edge[0])

    BFS(G,current_node)
    for v in vertices(G):
        if v.distance == INFINITY:
            return False

    return True

def test_is_strongly_connected():
    v_sc_G = [Vertex(i) for i in range(3)]

    sc_G = {v_sc_G[0]: [v_sc_G[1]],
            v_sc_G[1]: [v_sc_G[2]],
            v_sc_G[2]: [v_sc_G[0]]
            }

    v_nsc_G = [Vertex(i) for i in range(3)]

    nsc_G = {v_nsc_G[0]: [v_nsc_G[1]],
             v_nsc_G[1]: [],
             v_nsc_G[2]: [v_nsc_G[0], v_nsc_G[1]]
             }

    v_nsc_G2 = [Vertex(i) for i in range(6)]

    nsc_G2 = {v_nsc_G2[0]: [v_nsc_G2[1]],
              v_nsc_G2[1]: [v_nsc_G2[2]],
              v_nsc_G2[2]: [v_nsc_G2[0], v_nsc_G2[3]],
              v_nsc_G2[3]: [v_nsc_G2[4]],
              v_nsc_G2[4]: [v_nsc_G2[5]],
              v_nsc_G2[5]: [v_nsc_G2[4]]
              }

    print("is sc_G strongly connected(should be True): ",is_strongly_connected_with_reverse(sc_G))
    print("is nsc_G strongly connected(should be False): ",is_strongly_connected_with_reverse(nsc_G))
    print("is nsc_G2 strongly connected(should be False): ",is_strongly_connected_with_reverse(nsc_G2))


#opdracht 5a:
def calculate_degree(node):
    return len(node)

def is_euler_graph(G):
    for node in vertices(G):
        degree = calculate_degree(G[node])
        if degree%2 != 0:
            return False
    return True

def test_is_euler_graph():
    v_G4 = [Vertex(i) for i in range(8)]

    G4 = {v_G4[0]: [v_G4[1], v_G4[3]],
          v_G4[1]: [v_G4[0], v_G4[2]],
          v_G4[2]: [v_G4[1], v_G4[3], v_G4[4]],
          v_G4[3]: [v_G4[0], v_G4[2]],
          v_G4[4]: [v_G4[2], v_G4[5], v_G4[6]],
          v_G4[5]: [v_G4[4], v_G4[6]],
          v_G4[6]: [v_G4[4], v_G4[5], v_G4[7]],
          v_G4[7]: [v_G4[6]]
          }

    v_e_G = [Vertex(i) for i in range(6)]

    e_G = {v_e_G[0]: [v_e_G[3], v_e_G[4]],
           v_e_G[1]: [v_e_G[3], v_e_G[5]],
           v_e_G[2]: [v_e_G[4], v_e_G[5]],
           v_e_G[3]: [v_e_G[0], v_e_G[1]],
           v_e_G[4]: [v_e_G[0], v_e_G[2]],
           v_e_G[5]: [v_e_G[1], v_e_G[2]]
           }

    print("is e_G an euler graph(should be True): ",is_euler_graph(e_G))
    print("is G4 an euler graph(sould be False): ",is_euler_graph(G4))

#opdracht 5b:
def get_euler_circuit(G,start):
    euler_circuit =[start] #add start_node to list
    bridges = get_bridges(G)
    list_of_edges = edges(G)
    current = start
    next_node = None;
    only_bridges = True

    while list_of_edges != []:
        for neighbor in G[current]:
            if (current,neighbor) not in bridges:
                next_node = neighbor
                only_bridges = False
                break

        if only_bridges == True:
            next_node = G[current][0]

        only_bridges = True

        G[current].remove(next_node)
        G[next_node].remove(current)

        list_of_edges = edges(G)
        bridges = get_bridges(G)

        current = next_node
        euler_circuit.append(current)

    return euler_circuit

def test_get_euler_circuit():
    v_G5 = [Vertex(i) for i in range(8)]

    G5 ={ v_G5[0]: [v_G5[1], v_G5[2]],
          v_G5[1]: [v_G5[0], v_G5[3]],
          v_G5[2]: [v_G5[0], v_G5[3]],
          v_G5[3]: [v_G5[1], v_G5[2], v_G5[4], v_G5[6]],
          v_G5[4]: [v_G5[3], v_G5[5], v_G5[6], v_G5[7]],
          v_G5[5]: [v_G5[4], v_G5[6]],
          v_G5[6]: [v_G5[3], v_G5[4], v_G5[5], v_G5[7]],
          v_G5[7]: [v_G5[4], v_G5[6]]
          }

    G6 = {key: value[:] for key, value in G5.items()} #copy of G5
    G7 = {key: value[:] for key, value in G5.items()} #copy of G5
    G8 = {key: value[:] for key, value in G5.items()} #copy of G5

    print("an euler circut of G5 when started at v_G5[4]: ",get_euler_circuit(G5,v_G5[4]))
    print("an euler circut of G5 when started at v_G5[5]: ",get_euler_circuit(G6,v_G5[5]))
    print("an euler circut of G5 when started at v_G5[6]: ",get_euler_circuit(G7,v_G5[6]))
    print("an euler circut of G5 when started at v_G5[0]: ", get_euler_circuit(G8,v_G5[0]))

print("opdracht 1:")
test_is_connected()
print("\nopdracht 2:")
test_no_cycles()
print("\nopdracht 3:")
test_get_bridges()
print("\nopdracht 4:")
test_is_strongly_connected()
print("\nopdracht 5a:")
test_is_euler_graph()
print("\nopdracht 5b:")
test_get_euler_circuit()
