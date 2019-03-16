from pathlib import Path
from math import sin, cos, floor, log1p, log, e, pi, log10
from numpy import ones, uint8, random, multiply
from PIL import Image
from random import randint
import imageio as imio
import sys

from helper import random_name, random_array, n_array

SIZE = 256 * 4


def main():
    base_color = (118, 122, 252)
    base = n_array(base_color, SIZE)
    roll = rolling_array()
    combo = multiply(base, roll)
    
    base = Image.fromarray(base)
    roll = Image.fromarray(roll)
    combo = Image.fromarray(combo)

    base.save("base.png")
    roll.save("roll.png")
    combo.save("combo.png")

    return

def par_main():
    power = 0
    if len(sys.argv) != 2:
        print("Usage: "+sys.argv[0]+" STEP_POWER\n")
        return 1
    else:
        power = float(sys.argv[1])

    base_color = (114, 101, 169)
    base = n_array(base_color, SIZE)
    para = parameteric(power)
    mult = multiply(para, base)
    mult = Image.fromarray(mult)
    mult.save("pcombo.png")
    para = Image.fromarray(para)
    para.save("para.png")
    base_path = Path("pbase.png")
    if not base_path.is_file():
        base = Image.fromarray(base)
        base.save("pbase.png")

def x_value(t):
    value = t
    return int(value)

def y_value(t):
    value = t*sin(t)
    return int(value)

def valid_t(t):
    return 0 < x_value(t) < SIZE and 0 < y_value(t) < SIZE

def parameteric(pow):
    start = (ones((SIZE, SIZE, 3))).astype(uint8)
    STEP = 10 ** pow
    for t in range(0, SIZE**2 * floor(STEP)):
        t = t / STEP
        if valid_t(t):
            x = x_value(t)
            y = y_value(t)
            factor = 255
            start[x][y] = (start[x][y] * factor).astype(uint8)
    return start


def rolling_array():
    start = (ones((SIZE, SIZE, 3))).astype(uint8)
    for row in range(start.shape[0]):
        for col in range(start.shape[1]):
            m = .5
            x = row
            y = col
            factor = ((x + y)**2) * ((x - y)**2)
            factor = int(factor)
            start[row][col] = (start[row][col] * factor).astype(uint8)
    return start

#main()
par_main()

