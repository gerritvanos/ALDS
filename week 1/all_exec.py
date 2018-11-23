"""
naam: Gerrit van Os
klas: TI-V2C
student_nr: 1719977
docent: Frits Dannenberg
"""
import random
#opgave 1
"""
function to calculate max of a list

Parameters
-------------
a: list
    list needs to be longer than 0 and consist of ints or floats
    if len(a) == 0 or a[i] != int/float an error will occur

Return
------------
max: int
    the maximum of the list a
"""

def my_max(a):
    max = 0
    assert len(a), "list is 0"
    for i in range(len(a)):
        assert isinstance(a[i], (int, float)), str(a[i]) + " at possiton " + str(i) + " is not an integer or float"
        if (max <a[i]):
            max = a[i]
    return max

"""
function to test the assertions in the my_max function
tests with the folowing posibilitys:
1. list of only ints
2. list of ints and floats
3. list of ints with a char (error)
4. list with len(0) (error)
"""
def test_my_max():
    test_only_ints = [1,2,3,4,5,6,7,8,9,8,7,4,5,6,1,2,3,1,12,2,5,25,4]
    print("the my_max of test_only_ints ", my_max(test_only_ints))

    test_int_float = [1.2,1.2,2.1,5.5,6,7.5,10,10.5]
    print("the my_max of test_int_floats ", my_max(test_int_float))

    try:
        test_not_int = [1, 2, 3, 4, 45, 6, 7, 8, 9, 4, 4, 5, 6, 6, 7, 8, 8, 8, 8, 8, 8, 8, 888, "b"]
        print("the max of test_not_int ", my_max(test_not_int))
    except AssertionError:
        print("AssertionError!")

    try:
        test_len_0 = []
        print("the max of test_len_0 = ", my_max(test_len_0))
    except AssertionError:
        print("AssertionError!")


#opdracht 2:
"""
function to filter integers from a string of ints and chars

Parameters
-------------
s: string
    string of which the integers need to be filterd

Return
------------
output_list: list
    a list with all the integers from s
"""
def getNumbers(s):
    output_list = []
    temp = ""
    for i in range(len(s)):
        if(s[i] >='0' and s[i] <='9'):
            temp += s[i]
        elif(temp != ""):
            output_list.append(int(temp))
            temp = ""
    if(temp !=""):
        output_list.append(int(temp))
    return output_list

"""
function to test the getNumbers funtion
"""
def test_getNumber():
    a = 'een123zin45 6met-632meerdere+7777getallen'
    b = 'een123zin45 6met-632meerdere+7777getallen12'
    print("this is the result form get_numbers: ",getNumbers(a))
    print("test case with int on the back of string on bases of feedback",getNumbers(b))


#opdracht 3:
"""
function to get all prime numbers from a given list

Parameters
-------------
input_list : list
    list with sorted interges from 2-xxx from which the primes need to be found

Return
------------
 list
    a list of all the primes in the range of the input_list
"""
def get_prime(input_list):
    non_prime_set = set()

    for counter in range(2,my_max(input_list)+1):
        if (counter in non_prime_set):
            continue
        for i in range(counter*2,my_max(input_list)+1,counter):
            non_prime_set.add(i)

    return list(sorted(set(input_list)-non_prime_set))


"""
function to test the get_prime  funtion
"""
def test_get_prime():
    my_list = list(range(2,1000))
    print("primes from 2-1000", get_prime(my_list))
    my_list1 = list(range(2,100))
    print("primes from 2-100: ", get_prime(my_list1))


#opdracht 4:
"""
function to create a list of lists whith random numbers between 1 and 365

Parameters
-------------
items : int
    the number of items in each list
no_of_lists : int
    the amount of lists that need to be made

Return
------------
 list : list
    a list of lists with the number of items specified and repeated no_of_lists times
"""
def create_random_lists(items,no_of_lists):
    base_list =[]
    for i in range(no_of_lists):
        inside_list =[]
        for item in range(items):
            inside_list.append(random.randint(1,365))
        inside_list.sort()
        base_list.append(inside_list)
    return base_list

"""
function to check how often a list contains the same number

Parameters
-------------
list_of_lists : list
    a list of lists with integers

Return
------------
 counter : int
    the number of lists that contains the same integer
"""
def check_lists(list_of_lists):
    counter =0
    for i in range(len(list_of_lists)-1):
        for j in range(len(list_of_lists[i])):
            check = len(list_of_lists[i])-1
            if (j <  check):
                if (list_of_lists[i][j] == list_of_lists[i][j+1]):
                    counter += 1
                    break
    return counter

"""
function to test the check_lists funtion
"""
def test_lists():
    random_list = create_random_lists(23, 100)
    print("the amount of the same numbers in the random list is: ",check_lists(random_list))

test_my_max()
test_getNumber()
test_get_prime()
test_lists()