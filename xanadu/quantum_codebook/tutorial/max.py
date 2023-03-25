
"""
Codercise T.2 Find and return the maximum value of a provided array.
"""

def find_max(x):
    """A simple function to find the largest value in a numpy array.

    Args:
        x (array[float]): an array of numbers of size n
          
    Returns:
        float: The maximum value in x.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    maximum = 0.0
    for i in range(len(x)):
        if x[i] > maximum:
            maximum = x[i]
    
    return maximum
