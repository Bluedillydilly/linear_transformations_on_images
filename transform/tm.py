
import math
from numpy import ones, uint8, random, multiply, log2
from PIL import Image

SIZE = 512

def n_array():
    start = ones((SIZE, SIZE, 3))
    for x in range(SIZE):
        for y in range(SIZE):
            t = x**2+y**2
            g = (y**.5)/(x+1)
            start[x][y] = ones(3)*( t*g,  t*g, t*g)
    return start.astype(uint8)

def main():
    m = n_array()
    m = Image.fromarray(m)
    m.save("test.png")

main()
    
