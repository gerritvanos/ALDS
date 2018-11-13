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
    the maximum of the list
"""

def my_max(a):
    max = 0
    assert len(a), "length of the list is 0"
    for i in range(len(a)):
        assert isinstance(a[i], (int, float)), str(a[i]) + " at possiton " + str(i) + " is not an integer or float"
        if (max <a[i]):
            max = a[i]
    return max




test_len_0 = []
print("the max of test_len_0 = ",my_max(test_len_0))