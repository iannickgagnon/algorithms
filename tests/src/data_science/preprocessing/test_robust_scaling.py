import pytest

from src.data_science.preprocessing.robust_scaling import robust_scale


def test_valid_input_success():
  """
  Tests that the function returns the correct for a valid input.

  The input vector also contains a negative value.
  """

  # Get result
  input_value = [1, 2, 3, 4, 5]
  obtained_result = robust_scale(input_value)

  # Reference
  expected_result = [-2/3, -1/3, 0.0, 1/3, 2/3]

  assert pytest.approx(obtained_result) == expected_result


def test_null_iqr_success():
  """
  Tests that the function returns the correct result when the interquartile range is null.
  """

  # Get result
  input_value = [2, 2, 2, 2, 2]
  obtained_result = robust_scale(input_value)

  # Reference
  expected_result = [0.0, 0.0, 0.0, 0.0, 0.0]

  assert obtained_result == expected_result


def test_raises_wrong_input_type():
  """
  Tests that the proper error is raised when the input is of the incorrect type.
  """
  with pytest.raises(TypeError):
    robust_scale(None)


def test_raises_empty_list():
  """
  Tests that the proper error is raised when the input list is empty.
  """
  with pytest.raises(ValueError):
    robust_scale([])


def test_raises_list_with_non_numbers():
  """
  Tests that the proper error is raised when the input list contains non-numbers.
  """
  with pytest.raises(TypeError):
    robust_scale([1, 1.0, None])
