from byotest import *




usa_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
euro_coins = {200: 20, 100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}


def get_change(amount, coins=euro_coins):
    #if amount == 0:
    #    return []
        
    #if amount in coins:
    #    return [amount]
        
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
        
    return change

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(4), [2, 2])
test_are_equal(get_change(6), [5, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(8), [5, 2, 1])
test_are_equal(get_change(11), [10, 1])
test_are_equal(get_change(12), [10, 2])
test_are_equal(get_change(13), [10, 2, 1])
test_are_equal(get_change(14), [10, 2, 2])
test_are_equal(get_change(16), [10, 5, 1])
test_are_equal(get_change(35, usa_coins), [25,10])
test_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}),
    "Insufficient coins to give change.")




print ("All tests pass!")