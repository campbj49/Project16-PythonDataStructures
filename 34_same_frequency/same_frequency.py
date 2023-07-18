def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return get_frequecy(num1) == get_frequecy(num2)

def get_frequecy(num):
    """take integer and return the frequencies of numbers inside it"""
    
    num = str(num)
    res = {}
    for digit in num:
        if(digit in res): res[digit] +=1
        else:res[digit] = 1
    
    return res