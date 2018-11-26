def cookies(k,A):
    counter = 0
    while min(A) <= k:
        if len(A) <= 1:
            return None
        a = min(A)
        A.remove(a)

        b = min(A)
        A.remove(b)

        A.append(a + 2*b)
        counter +=1


    return counter



k = 7

B=[1,2,3,9,10,12,13]
C=[1,2,5,6,7,12,13,14]

k = 1000
test_case1 = [1000,-1,-1,-1,-1,-1,-10]
result_test_case1 = cookies(k,test_case1)
print("er zijn",result_test_case1, "stappen nodig")

#test_case2= list(range(10**6))
#result_test_case2 = cookies(k,test_case2)

k = 8
test_case3 = [5,7,9,21,3,4,5,7,10,11,13,2,2,2,2,2,2]
result_test_case3 = cookies(k,test_case3)
print("er zijn",result_test_case3, "stappen nodig")

k = 9
test_case3 = [5,7,9,21,3,4,5,7,10,11,13,2,2,2,2,2,2]
result_test_case3 = cookies(k,test_case3)
print("er zijn",result_test_case3, "stappen nodig")

k = 10
test_case3 = [5,7,9,21,3,4,5,7,10,11,13,2,2,2,2,2,2]
result_test_case3 = cookies(k,test_case3)
print("er zijn",result_test_case3, "stappen nodig")

k = 11
test_case3 = [5,7,9,21,3,4,5,7,10,11,13,2,2,2,2,2,2]
result_test_case3 = cookies(k,test_case3)
print("er zijn",result_test_case3, "stappen nodig")

k = 12
test_case3 = [5,7,9,21,3,4,5,7,10,11,13,2,2,2,2,2,2]
result_test_case3 = cookies(k,test_case3)
print("er zijn",result_test_case3, "stappen nodig")

#resultB = cookies(k,B)
#resultC = cookies(k,C)

#print("er zijn",resultB, "stappen nodig")
#print("er zijn",resultC,"stappen nodig")