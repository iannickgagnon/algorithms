import pytest

from src.data_science.preprocessing.z_score_normalizing import z_score_normalize


def test_valid_input_success():
  """
  Tests that the function returns the correct for a valid input.

  The input vector also contains a negative value.
  """

  # Get result
  input_value = [1, 2, 3]
  obtained_result = z_score_normalize(input_value)

  # Reference :
  #     mean = (1 + 2 + 3) / 3 = 2
  #     standard deviation = sqrt(((1-2)^2 + (2-2)^2 + (3-2)^2) / (3 - 1)) = sqrt(2 / 2) = 1
  #     z-scores = [(1-2)/1, (2-2)/1, (3-2)/1] = [-1, 0, 1]
  expected_result = [-1.0, 0.0, 1.0]

  assert pytest.approx(obtained_result) == expected_result


def test_valid_input_with_negative_success():
  """
  Tests that the function returns the correct for a valid input.
  """

  # Get result
  input_value = [-1, 2, 5]
  obtained_result = z_score_normalize(input_value)

  # Reference :
  #     mean = (-1 + 2 + 5) / 3 = 2
  #     standard deviation = sqrt(((1-2)^2 + (2-2)^2 + (3-2)^2) / (3 - 1)) = sqrt(2 / 2) = 1
  #     z-scores = [(1-2)/1, (2-2)/1, (3-2)/1] = [-1, 0, 1]
  expected_result = [-1.0, 0.0, 1.0]

  assert pytest.approx(obtained_result) == expected_result

  
def test_raises_wrong_input_type():
  """
  Tests that the proper error is raised when the input is of the incorrect type.
  """
  with pytest.raises(TypeError):
    z_score_normalize(None)


def test_raises_empty_list():
  """
  Tests that the proper error is raised when the input list is empty.
  """
  with pytest.raises(ValueError):
    z_score_normalize([])


def test_raises_list_with_non_numbers():
  """
  Tests that the proper error is raised when the input list contains non-numbers.
  """
  with pytest.raises(TypeError):
    z_score_normalize([1, 1.0, None])
