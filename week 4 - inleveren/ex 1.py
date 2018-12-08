import random

class seperate_chain_hash_table:
    def __init__(self):
        self.table = list()
        for i in range(8):
            self.table.append(set())
        self.elements_in_sets = 0
        self.table_size = len(self.table)

    def update_elements_in_sets(self):
        new_length =0
        for element in self.table:
            for sub_element in element:
                new_length +=1
        self.elements_in_sets = new_length

    def calculate_loadfactor(self):
        self.update_elements_in_sets()
        return self.elements_in_sets/(len(self.table))

    def insert_list(self,input_list):
        for item in input_list:
            self.insert(item)

    def insert(self,e):
        place = hash(e)%self.table_size
        self.table[place].add(e)
        if self.calculate_loadfactor() > 0.75: #if loadfactor to high rehash
            self.rehash(self.table_size*2)


    def rehash(self,new_len):
        old_elements = []
        for element in self.table:
            for sub_element in element:
                old_elements.append(sub_element)
        self.table.clear()
        for i in range(new_len):
            self.table.append(set())
        self.table_size = len(self.table)
        self.insert_list(old_elements)
        print("table rehashed")
        print("the new table: ",self.table,"\n")

    def __repr__(self):
        s1 = "the loadfactor: " + str(self.calculate_loadfactor()) + "\n"
        s2 = "the table_size: " + str(self.table_size) + "\n"
        s3 = "the table:\n" + str(self.table)

        return  s1+s2+s3

    def search(self,e):
        place = hash(e)%self.table_size
        if e in self.table[place]:
            return True
        return False


    def delete(self,e):
        if self.search(e):
            place = hash(e)%self.table_size
            self.table[place].remove(e)
            return True
        else:
            return False


def test_seperat_chain_hash_table():
    hash_table = seperate_chain_hash_table()
    input_list = [10,20,30,40,16,25,33,45,78,11,44,66]
    print("test with folowing list: ", input_list)
    hash_table.insert_list(input_list)
    print("the table looks like this",hash_table.table)

    print("\ntest of search function:")
    print("is 20 in hash_table (should be True): ",hash_table.search(20))
    print("is 66 in hash_table (should be True): ",hash_table.search(66))
    print("is 100 in hash_table (should be False): ",hash_table.search(100))

    print("\ntest of delete function:")
    print("delete function returns True if element is deleted and False if element was not in hash table")
    print("delete 30 from hash_table: ",hash_table.delete(30))
    print("the table:",hash_table.table)
    print("try to remove 30 again(should be false) ",hash_table.delete(30))
    print("delete 100 from hash_table (should be false): ",hash_table.delete(100))
    print("remove 10 from hash_table: ",hash_table.delete(10))
    print("the table:",hash_table.table)

    print("\nthe test case with 200 random numbers put in")
    hash_table2 = seperate_chain_hash_table()
    random_list = []
    for i in range(200):
        random_nr = random.randint(1,500)
        random_list.append(random_nr*0.42)
    hash_table2.insert_list(random_list)
    print("this is the completed table: ",hash_table2.table)
    print("\n test to delete 100 numbers")
    for i in range(100):
        hash_table2.delete(random_list.pop())
    print("this is how the table looks now: ",hash_table2.table)



test_seperat_chain_hash_table()

