
from numpy import ones, uint8
from PIL import Image
from random import randint

SIZE = 100

def random_name():
    """
    .
    """
    return "".join(str(randint(0, 9)) for n in range(5))

def main():
    im = Image.fromarray(rolling_array())
    im.save(random_name()+".png")
    return

def rolling_array():
    start = ones((SIZE, SIZE, 3)).astype(uint8)
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            start[i][j] = (ones(3)*(i+j)%255).astype(uint8)
    print(start)
    return start

main()

