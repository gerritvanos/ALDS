
def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("*", end= " ")
            else:
                print("*", end= " ")
        print()
    print()


def check(list_of_columns, new_column):  # ga na of i aan a toegevoegd kan worden
    n = len(list_of_columns)
    return not (new_column in list_of_columns or  # niet in dezelfde kolom
                new_column + n in [list_of_columns[j] + j for j in range(n)] or  # niet op dezelfde diagonaal
                new_column - n in [list_of_columns[j] - j for j in range(n)]) # niet op dezelfde diagonaal


def rsearch(amount_of_queens,list_of_columns):
    global list_of_solutions
    for i in range(amount_of_queens):
        if check(list_of_columns, i):
            list_of_columns.append(i)
            if len(list_of_columns) == amount_of_queens:
                if list_of_columns not in list_of_solutions:
                    list_of_solutions.append(list_of_columns)
                    rsearch(amount_of_queens,[]) # geschikte a gevonden
                    return True
            else:
                if rsearch(amount_of_queens,list_of_columns):
                    return True
            del list_of_columns[-1] # verwijder laatste element
    return False

list_of_columns =[]
list_of_solutions = [] # a geeft voor iedere rij de kolompositie aan
t = 0

rsearch(8,list_of_columns)
print(list_of_solutions)
print(len(list_of_solutions))