import random

def create_random_lists(items,no_of_lists):
    list =[]
    for i in range(no_of_lists):
        list1 =[]
        for item in range(items):
            list1.append(random.randint(1,365))
        list.append(list1)
    return list

def check_lists(list_of_lists):
    counter =0
    for i in range(len(list_of_lists)-1):
        list1=set(list_of_lists[i])
        list2= set(list_of_lists[i+1])
        counter += bool(list1.intersection(list2))
    return counter

random_list = create_random_lists(23,100)
print(random_list)
print(check_lists(random_list))