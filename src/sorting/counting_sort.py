def counting_sort(array: list, reverse: bool = False) -> list:
    """
    Implements counting sort on a list.

    Args:
        array (list): The array to sort.
        reverse (bool): If True, returns the array in descending order.

    Returns:
        list: A new sorted array.
    """

    # Empty list
    if not array:
        return []
    
    # Find the maximum value
    max_value_plus_one = max(array) + 1

    # Compute the frequency array
    frequencies = [array.count(i) for i in range(max_value_plus_one)]
    
    # Build the sorted array
    sorted_array = []
    for i in range(max_value_plus_one):
        sorted_array.extend([i] * frequencies[i])

    # Return in the correct order
    if reverse:
        return sorted_array[::-1]
    else:
        return sorted_array


if __name__ == "__main__":

    # Array to sort
    array = [1, 9, 2, 5, 3, 0]

    # Display before sorting
    print(f"Before sorting: {array}")

    # Sort the array
    sorted_array = counting_sort(array)

    # Display after sorting
    print(f"After sorting: {sorted_array}")
