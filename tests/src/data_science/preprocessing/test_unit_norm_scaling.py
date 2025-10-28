import pytest

from src.data_science.preprocessing.unit_norm_scaling import unit_norm_scale


def test_valid_input_success():
  """
  Tests that the function returns the correct for a valid input.

  The input vector also contains a negative value.
  """

  # Get result
  input_value = [-1, 1]
  obtained_result = unit_norm_scale(input_value)

  # Reference
  expected_result = [-1 / (2 ** 0.5), 1 / (2 ** 0.5)]

  assert pytest.approx(obtained_result) == expected_result


def test_zero_norm_success():
  """
  Tests that the function returns the correct result when the interquartile range is null.
  """

  # Get result
  input_value = [0.0, 0.0]
  obtained_result = unit_norm_scale(input_value)

  # Reference
  expected_result = [float('inf'), float('inf')]

  assert obtained_result == expected_result


def test_raises_wrong_input_type():
  """
  Tests that the proper error is raised when the input is of the incorrect type.
  """
  with pytest.raises(TypeError):
    unit_norm_scale(None)


def test_raises_empty_list():
  """
  Tests that the proper error is raised when the input list is empty.
  """
  with pytest.raises(ValueError):
    unit_norm_scale([])


def test_raises_list_with_non_numbers():
  """
  Tests that the proper error is raised when the input list contains non-numbers.
  """
  with pytest.raises(TypeError):
    unit_norm_scale([1, 1.0, None])
