from base import Explorer
from kernels import mandelbrot

if __name__ == "__main__":
    Explorer(mandelbrot, -2, 1, -1, 1, 1000, 1000, interpolation='bilinear').show()