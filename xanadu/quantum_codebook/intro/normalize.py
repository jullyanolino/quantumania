"""
Codercise I.1.1. Suppose we are given an unnormalized quantum state, write a function that given and normalizes this state.
"""


# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary 
    amplitudes.
    
    Args:
        alpha (complex): The amplitude associated with 
        the |0> state.
        beta (complex): The amplitude associated with 
        the |1> state.
        
    Returns:
        array[complex]: A vector (numpy array) with 2 
        elements that represents a normalized quantum state.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE A VECTOR [a', b'] BASED ON alpha AND beta SUCH THAT |a'|^2 + |b'|^2 = 1
    v = np.array([alpha, beta])
    v_n = np.linalg.norm(v)
    
    # RETURN A VECTOR
    return (v / v_n)
