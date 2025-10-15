def int_to_base_62(value: int) -> str:
    """
    Converts an integer to it's base 62 string representation.

    Args:
        value (int): The integer to convert.

    Returns:
        (str): The base 62 string representation of the integer.
    """

    # Symbols for base 62
    SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Build base 62 string by repeated division using the 
    # remainder as the index of the next symbol
    result = ""
    while value > 0:
        value, remainder = divmod(value, 62)
        result = SYMBOLS[remainder] + result

    return result


def base_62_to_int(value: str) -> int:
    """
    Converts a base 62 string to it's integer value.

    Args:
        value (str): The string to convert.

    Returns:
        int: The integer value of the string.
    """

    # Symbols for base 62
    SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Build integer representation by repeated multiplication
    result = 0
    for character in value:
        result = (result * 62) + SYMBOLS.find(character)
        
    return result
