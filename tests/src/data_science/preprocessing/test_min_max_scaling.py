from src.data_science.preprocessing.min_max_scaling import get_min_max_scaled_values


def test_valid_input_success():
  """
  Tests that the function returns the correct for a valid input.

  The input vector also contains a negative value.
  """

  # Get result
  input_value = [1, 2, 3, 4, 5]
  obtained_result = get_min_max_scaled_values(input_value)

  # Reference
  expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]

  assert obtained_result == expected_result


def test_valid_input_with_negative_success():
  """
  Tests that the function returns the correct for a valid input.
  """

  # Get result
  input_value = [-1, 2, 3, 4]
  obtained_result = get_min_max_scaled_values(input_value)

  # Reference
  expected_result = [0.0, 0.6, 0.8, 1.0]

  assert obtained_result == expected_result