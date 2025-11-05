from statistics import mean, pstdev


def mean_std_encode(
    x: list[int | float], 
    target_mean: int | float, 
    target_std: int | float
) -> list[float]:
    """
    Rank-preserving encoding to match a target mean and standard deviation.

    This transformation preserves the relative ordering of values in `x`
    (like z-score normalization followed by rescaling).

    Args:
        x (list[int | float]): A vector of numerical values.
        target_mean (int | float): The desired mean of the output distribution.
        target_std (int | float): The desired standard deviation of the output distribution.

    Returns:
        (list[float]): A list of values with the same relative order as `x`,
                       rescaled to have `target_mean` and `target_std`.
    """

    # Ensure input is a non-empty list of numerical values
    if not isinstance(x, list):
      raise TypeError("Input must be a list")

    if not len(x):
      raise ValueError("Input list must not be empty")

    if not all(isinstance(value, (int, float)) for value in x):
      raise TypeError("Elements must be int or float")

    # Calculate standard deviation and validate
    x_std = pstdev(x)
    if x_std == 0:
        raise ValueError("Standard deviation of input is zero; cannot rescale.")

    # Calculate z-scores
    x_mean = mean(x)
    z_scores = [(xi - x_mean) / x_std for xi in x]
    
    return [target_mean + target_std * z for z in z_scores]
