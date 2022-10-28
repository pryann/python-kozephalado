# NumPy/SciPy, PyDoc, Sphinx, EpyDoc, Google

def sum_two_number(a: int = 0, b: int = 0) -> int:
    '''
    This function summarize two number

    Parameters
    ----------
    a : int, default=0
        The first number
    b : int, default=0
        The second number

    Returns
    -------
    int
        The sum of two numbers
    '''

    return a + b


sum_two_number(10, 10)
