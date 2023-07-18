def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    
    #if the number is prime, theres nothing left to do, so return
    if is_prime(num): return [1,num]
    #if it's not, find the first factor pair and call the find_factor function on both of them
    for i in range(2,num):
        if(num%i ==0):
            res = list(set(find_factors(i) + find_factors(int(num/i))+[num]))
            res.sort()
            return res
    #returning the results concatonated together
    #biggest problem is getting exactly one 1 in the final array
    #burn that bridge later
    return is_prime(num)
    
    
def is_prime(num):
    for i in range(2,num):
        if(num%i == 0): return False
    return True
