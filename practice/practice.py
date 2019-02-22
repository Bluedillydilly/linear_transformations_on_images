import math
from numpy import ones, uint8, random, multiply
from PIL import Image
from random import randint
import imageio as imio
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
    base_color = (118, 122, 252)
    #base_color = (122, 122, 122)
    arrays = []
    frames = 2
    for i in range(1, frames):
        roll = rolling_array(i)
        mult = multiply(roll, n_array(base_color))
        arrays.append(mult)
        combo = Image.fromarray(mult)
        combo.save(str(i)+".png")
        print("Saved "+str(i)+".png")
        roll = Image.fromarray(roll)
        roll.save("roll.png")
    #imio.mimsave("test", arrays, 'GIF', duration = frames/120)

    #add = random_array()-(5*rolling_array())
    #add = Image.fromarray(add)
    #add.save("R"+"1"+".png")
    return

def par_main():
    base_color = (118, 122, 252)
    para = parameteric(1)
    mult = multiply(para, n_array(base_color))
    mult = Image.fromarray(mult)
    mult.save("m.png")

a = 200

def x(t):
    return t

def y(t):
    return t**2

def valid_coord(x,y):
    return 0

def valid_t(t):
    return 0 < x(t) < SIZE and 0 < y(t) < SIZE

def parameteric(n):
    start = (ones((SIZE, SIZE, 3))*256).astype(uint8)
    #x = 3 * t
    #y = t ** 2
    for t in range(SIZE*SIZE):
        if valid_t(t):
            start[int(x(t))][int(y(t))] = (ones(3)*255).astype(uint8)
    return start


def rolling_array(n):
    start = (ones((SIZE, SIZE, 3))*256).astype(uint8)
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            m = .5
            x = i
            y = j
            factor = math.sin(x)*10 + y #- math.log((SIZE-x)**m + (SIZE/10-y))
            start[i][j] = (ones(3)*(factor)).astype(uint8)
    return start

par_main()

