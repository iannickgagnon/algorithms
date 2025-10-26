def scale_within_range(x: list[int | float], range_min: int | float, range_max: int | float) -> list[float]:
  """
  Scales an input vector of numerical values to lie within a user-defined range.

  Args:
    x (list[int | float]): A vector of numerical values.
    range_min (int | float): The lower bound of the range.
    range_max (int | float): The upper bound of the range.

  Returns:
    (list[float]): The corresponding range-scaled values.
  """

  # Ensure input vector is a non-empty list of numerical values
  if not isinstance(x, list):
    raise TypeError("Input must be a list")

  if not all(isinstance(value, (int, float)) for value in x):
    raise TypeError("Elements must be int or float")

  if not len(x):
    raise ValueError("Input list must not be empty")

  # Ensure bounds are numbers where the minimum is less than the maximum
  if not isinstance(range_min, (int, float)) or \
     not isinstance(range_max, (int, float)):
     raise TypeError("Range limits must be int or float")

  if range_min >= range_max:
    raise ValueError("The lower bound must be less than the upper bound")

  # Calculate scaling parameters
  range_delta = range_max - range_min
  min_value = min(x)
  max_value = max(x)
  delta_value = max_value - min_value

  return [range_min + ((value - min_value) / delta_value) * range_delta for value in x]
