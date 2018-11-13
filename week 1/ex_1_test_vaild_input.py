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




test_only_ints = [1,2,3,4,5,6,7,8,9,8,7,4,5,6,1,2,3,1,12,2,5,25,4]
print("the max of test_only_ints ", my_max(test_only_ints))

test_int_float = [1.2,1.2,2.1,5.5,6,7.5,10,10.5]
print("the max of test_int_floats ", my_max(test_int_float))

