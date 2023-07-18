def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    rev = ""
    for i in range(len(phrase)-1,-1,-1): rev += phrase[i]
    return rev