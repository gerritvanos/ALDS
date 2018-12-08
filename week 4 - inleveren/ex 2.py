import random
def find_and_print_fraction_with_same_hash():
    hashes_dict = dict()
    while True:
        new_number = random.randint(1,2**32)/3**22;
        new_number_hash = hash(new_number)
        if new_number_hash in hashes_dict:
            print("found same hash for new_number: ",repr(new_number))
            print("the number in the dict is: ",hashes_dict[new_number_hash])
            print("the hash van deze numers is: ",repr(hash(new_number)))
            return
        else:
            hashes_dict[new_number_hash] = new_number

find_and_print_fraction_with_same_hash()