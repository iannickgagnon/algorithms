import pytest

from src.data_science.preprocessing.one_hot_encoding import one_hot_encode


def test_valid_input():
  """
  Tests that the function returns the correct output for a valid input.
  """

  obtained_value = one_hot_encode(['a', 'b', 'c']) 
  
  expected_value = [['a', 'b', 'c'], 
                    [ 1,   0,   0], 
                    [ 0,   1,   0], 
                    [ 0,   0,   1]]
  
  assert obtained_value == expected_value


def test_raises_wrong_input_type():
  """
  Tests that the proper error is raised when the input is of the incorrect type.
  """
  with pytest.raises(TypeError):
    one_hot_encode(None)


def test_raises_empty_list():
  """
  Tests that the proper error is raised when the input list is empty.
  """
  with pytest.raises(ValueError):
    one_hot_encode([])


def test_raises_list_with_non_string():
  """
  Tests that the proper error is raised when the input list contains non-strings.
  """
  with pytest.raises(TypeError):
    one_hot_encode(['feature_1', 'feature_2', None])
