
import math
from numpy import ones, uint8, random, multiply, log2
from PIL import Image

SIZE = 512

def n_array():
    start = ones((int(SIZE/2), int(SIZE/2), 3))
    for x in range(SIZE, int(SIZE/2)):
        for y in range(int(SIZE/2), SIZE):
            t = x**2+y**2
            g = (y**.5)/(x+1)
            start[x-int(SIZE/2)][y-int(SIZE/2)] = ones(3)*( t*g,  t*g, t*g)
    return start.astype(uint8)

def main():
    m = n_array()
    m = Image.fromarray(m)
    m.save("test.png")

main()
    
