def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    freq = {}
    for num in nums:
        if num in freq: freq[num] +=1
        else: freq[num] = 1
    
    mx = 0
    max_val = None;
    
    for item in freq.items():
        if item[1] > mx:
            mx = item[1]
            max_val = item[0]
            
    return max_val