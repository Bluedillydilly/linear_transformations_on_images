
from numpy import ones, uint8, random, multiply
from PIL import Image
from random import randint

SIZE = 512

def random_name():
    """
    .
    """
    return "".join(str(randint(0, 9)) for n in range(5))

def random_array():
    return (random.rand(SIZE, SIZE, 3)*256).astype(uint8)

def n_array(n):
    start = ones((SIZE, SIZE, 3))
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            start[i][j] = n
    return start.astype(uint8)

def main():
    im = Image.fromarray(rolling_array())
    n_arr = Image.fromarray(n_array((118,122,252)))
    n_arr.save("n.png")
    im.save("1"+".png")
    combo = Image.fromarray(multiply(rolling_array(),n_array((118,122,252))))
    combo.save("c.png")
    
    #add = random_array()-(5*rolling_array())
    #add = Image.fromarray(add)
    #add.save("R"+"1"+".png")
    return

def rolling_array():
    start = (ones((SIZE, SIZE, 3))*256).astype(uint8)
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            factor = i**1.5 + j**1.5 + 0 
            start[i][j] = (ones(3)*factor%255).astype(uint8)
    return start

main()

