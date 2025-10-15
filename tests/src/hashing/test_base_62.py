import pytest

from src.hashing.base_62 import int_to_base_62


@pytest.mark.parametrize("value,expected", [
  (0, ""),
  (1, "1"),
  (61, "z"),
  (62, "10"),
  (123, "1z"),
  (3842, "zy"),
  (238326, "zzy"),
  (14776334, "zzzy"),
  (916132830, "zzzzy"),
  (56800235582, "zzzzzy"),
  (3521614606206, "zzzzzzy"),
  (218340105584894, "zzzzzzzy"),
  (13537086546263550, "zzzzzzzzy"),
  (839299365868340223, "zzzzzzzzzz"),
])
def test_to_base_62(value: int, expected: str):
  assert int_to_base_62(value) == expected