from statistics import pstdev, stdev, mean


def z_score_normalize(x: list[int | float], is_population: bool = False) -> list[float]:
  """
  Calculates the Z-normalized values of the input vector. The sample standard deviation is used by default.

  Args:
    x (list[int | float]): A vector of numerical values.
    is_population (bool, optional): Whether to use the population statistics or not. Defaults to False.

  Returns:
    (list[float]): The corresponding Z-normalized values.
  """

  # Ensure input is a non-empty list of numerical values
  if not isinstance(x, list):
    raise TypeError("Input must be a list")

  if not len(x):
    raise ValueError("Input list must not be empty")

  if not all(isinstance(value, (int, float)) for value in x):
    raise TypeError("Elements must be int or float")

  # Calculate scaling statistics
  mean_value = mean(x)

  # Differentiate between population (N) and sample (N - 1) mean
  if is_population:
    standard_deviation = pstdev(x)
  else:
    standard_deviation = stdev(x)

  # Apply scaling
  return [(value - mean_value) / standard_deviation for value in x]
