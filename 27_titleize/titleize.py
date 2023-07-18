def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    res = phrase[0].upper()
    cap = False
    for letter in phrase[1:]:
        if cap: 
            res += letter.upper()
            cap = False
        else: res += letter
        if(letter == " "): cap = True
    return res
    