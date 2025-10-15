def to_base_62(value: int) -> str:
  """
  Converts an integer to it's base 62 string representation.

  Args:
    value (int): The integer to convert.

  Returns:
    (str): The base 62 string representation of the integer.
  """

  # Symbols for base 62
  SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  # Build base 62 string by repeated division using the 
  # remainder as the index of the next symbol
  result = ""
  while value > 0:
    value, remainder = divmod(value, 62)
    result = SYMBOLS[remainder] + result
  
  return result
