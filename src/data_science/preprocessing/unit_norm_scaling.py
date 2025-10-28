def unit_norm_scale(x: list[int | float]) -> list[float]:
  """
  Scales an input vector so that its magnitude becomes equal to 1. This 
  is also called L2 normalization.

  For example, this simplifies measuring cosine similarity defined as : 

    cos(theta) = dot(x_vector, y_vector)  / (||x_vector|| * ||y_vector||)

  Which simplifies to the following when the norms are unitary :

    cos(theta) = dot(x_vector_unit, y_vector_unit)

  As such, it is independent of the magnitudes and depends purely on the
  orientation in the feature space. It is faster and more numerically 
  stable.

  Cosine similarity is used extensively with embeddings (TD-IDF, word2vec), 
  recommender systems, and clustering. It avoids large-magnitude vectors
  from dominating.
  
  Args:
    x (list[int | float]): A vector of numerical values.

  Returns:
    (list[float]): The corresponding robust-scaled values.
  """

  # To avoid division by zero
  MIN_NORM = 1e-6

  # Ensure input vector is a non-empty list of numerical values
  if not isinstance(x, list):
    raise TypeError("Input must be a list")

  if not all(isinstance(value, (int, float)) for value in x):
    raise TypeError("Elements must be int or float")

  if not len(x):
    raise ValueError("Input list must not be empty")

  # Calculate the norm
  norm = sum([value ** 2 for value in x]) ** 0.5

  # Default result for zero-norm input vector
  if norm < MIN_NORM:
    return [float('inf') for _ in x]

  return [value / norm for value in x]
