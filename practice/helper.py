
from numpy import ones, uint8, random
from random import randint

def random_name():
    """
    Generates a random name.
    Names are 5 numbers long, each character being [0-9]
    """
    return "".join(str(randint(0, 9)) for n in range(5))

def random_array(SIZE):
    """
    returns an SIZE x SIZE x 3 array int8 type.
    """
    return (random.rand(SIZE, SIZE, 3)*256).astype(uint8)

def n_array(n, SIZE):
    """
    returns an SIZE x SIZE x 3 array with n as the color
    """
    return (ones((SIZE, SIZE, 3))*n).astype(uint8)
