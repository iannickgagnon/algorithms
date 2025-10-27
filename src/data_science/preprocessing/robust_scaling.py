from statistics import median


def robust_scale(x: list[int | float]) -> list[float]:
  """
  Scales an input vector of numerical values using the median and the interquartile range.

  Args:
    x (list[int | float]): A vector of numerical values.

  Returns:
    (list[float]): The corresponding robust-scaled values.
  """

  # Smallest IQR considered different from zero
  MIN_IQR = 1e-6

  # Ensure input vector is a non-empty list of numerical values
  if not isinstance(x, list):
    raise TypeError("Input must be a list")

  if not all(isinstance(value, (int, float)) for value in x):
    raise TypeError("Elements must be int or float")

  if not len(x):
    raise ValueError("Input list must not be empty")

  # Calculate scaling parameters
  x_sorted = sorted(x)

  # Extract median and position
  n = len(x_sorted)
  i_median = n // 2
  x_median = x_sorted[i_median]

  # Include median for even-numbered lists (there is no median in the list itself), exclude otherwise
  if n % 2 == 0:
      lower_half = x_sorted[:i_median]
      upper_half = x_sorted[i_median:]
  else:
      lower_half = x_sorted[:i_median]
      upper_half = x_sorted[i_median + 1:]

  # Calculate interquartile range (IQR)
  Q1 = median(lower_half)
  Q3 = median(upper_half)

  IQR = Q3 - Q1

  # Default values for null IQR
  if IQR < MIN_IQR:
    return [0.0 for _ in x]

  # Return IQR-scaled values
  return [(value - x_median) / IQR for value in x]
  