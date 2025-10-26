def one_hot_encode(features: list[str]) -> list:
  """
  Creates the one-hot-encoded table of a list of features.

  Args:
    features (list[str]): List of features to encode.

  Returns:
    (list): The one-hot encoded matrix with the following properties:
      - The first row is the list of unique features.
      - The following rows correspond to an identity matrix where M[i, j] == 1 if i == j, and 0 otherwise. 
  """

  # Ensure input is a nonempty list of strings
  if not isinstance(features, list):
    raise TypeError('Input must be a list')
  
  if not features:
    raise ValueError('Input list must not be empty')
  
  if not all(isinstance(feature, str) for feature in features):
    raise TypeError('Input must be a list of strings')

  # Extract unique features and count
  unique_features = set(features)
  n_features = len(unique_features)

  # Initialize one-hot table with column names header
  one_hot_table = [list(unique_features)]

  # Build one-hot table row by row
  for i in range(n_features):
    one_hot_table.append([1 if j == i else 0 for j in range(n_features)])

  return one_hot_table