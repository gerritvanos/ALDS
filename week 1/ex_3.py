import math

def my_max(a):
    max = 0
    assert len(a), "lengt of the list is 0"
    for i in range(len(a)):
        assert isinstance(a[i], (int, float)), str(a[i]) + " at possiton " +str(i)+ " is not an integer or float"
        if (max <a[i]):
            max = a[i]
    return max

def get_prime_slow(input_list):
    non_prime_set = set()

    for counter in range(2,my_max(input_list)+1):
        if (counter in non_prime_set):
            continue
        for i in range(counter*2,my_max(input_list)+1,counter):
            non_prime_set.add(i)

    return list(sorted(set(input_list)-non_prime_set))

def create_list(max_value):
    output_list = []
    for i in range(2,max_value+1):
        output_list.append(i)
    return output_list

my_list = create_list(1000)
print(get_prime_slow(my_list))
