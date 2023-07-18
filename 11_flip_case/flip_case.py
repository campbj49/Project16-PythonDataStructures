def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    res = ""
    for letter in phrase:
        if(letter.capitalize() == to_swap.capitalize()):
            if(letter.isupper()): res += letter.lower()
            else: res += letter.upper()
        else: res += letter
        
    return res
