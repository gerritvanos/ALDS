def calculate_ways_to_pay(amount):
    if amount > 10000:
        return None
    coins= [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    ways_to_pay = []
    for coin in range(len(coins)): #check for the max coin we can use
        if amount > coins[coin]:
            max_coin = coin

    for coin in range(max_coin+2): #fill ways with list of 1's
        ways_to_pay.append([])
        for way in range(amount+1):
            ways_to_pay[coin].append(1)

    for coin in range(1,max_coin+2):
        for way in range (len(ways_to_pay[coin])):
            if way >= coins[coin]:
                ways_to_pay[coin][way] = ways_to_pay[coin-1][way]+ways_to_pay[coin][way-coins[coin]]
            elif way<coins[coin]:
                ways_to_pay[coin][way] = ways_to_pay[coin-1][way]

    max_ways =0
    for way in range(len(ways_to_pay)):
        if max(ways_to_pay[way]) >max_ways:
            max_ways = max(ways_to_pay[way])

    return max_ways


def test_calculate_ways_to_pay():
    print("7 cents can be payed: ",calculate_ways_to_pay(5)," different ways")
    print("10 cents can be payed: ",calculate_ways_to_pay(10)," different ways")
    print("100(1€) cents can be payed: ",calculate_ways_to_pay(100)," different ways")

test_calculate_ways_to_pay()