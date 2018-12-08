def pascal_triangle(no_rows, no_column):  # note no dependencies on any of the prior code
    result =[]
    for row in range(no_rows+1):
        result.append([]) # create empty row
        result[row].append(1) # row[0] always 1
        for column in range(1, row):
            result[row].append(result[row - 1][column - 1] + result[row - 1][column])
        if (no_rows != 0):
            result[row].append(1)

    return result[no_rows][no_column]


def test_pascal_triangle():
    print("test with (6,3) should be 20 result: ",pascal_triangle(6,3))
    print("test with (100,50) ")
    print("(100,50) result: \t",pascal_triangle(100,50))
    print("(100,50) should be: ",100891344545564193334812497256," calculated at www.decode.fr/pascal-triangle")
    print("note on the website need to enter(101,51) because the rows/columns start at 1 instead of 0")

test_pascal_triangle()