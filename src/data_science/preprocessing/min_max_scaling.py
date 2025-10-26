def get_min_max_scaled_values(x: list[int | float]) -> list[float]:
  """
  Calculates the min-max-scaled values of the input vector.

  Args:
    x (list[int | float]): A vector of numerical values.

  Returns:
    (list[float]): The corresponding min-max-scaled values.
  """

  # Ensure input is a non-empty list of numerical values
  if not isinstance(x, list):
    raise TypeError("Input must be a list")

  if not len(x):
    raise ValueError("Input list must not be empty")

  if not all(isinstance(value, (int, float)) for value in x):
    raise TypeError("Elements must int or float type")

  # Calculate limits and range
  x_min = min(x)
  x_max = max(x)
  range = x_max - x_min

  # Return scaled values
  return [(value - x_min) / range for value in x]
