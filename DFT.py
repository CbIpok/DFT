import math

def iexp(n):
    return complex(math.cos(n), math.sin(n))


def dft(xs):
    "naive dft"
    n = len(xs)
    return [sum((xs[k] * iexp(-2 * math.pi * i * k / n) for k in range(n)))
            for i in range(n)]




if __name__ == "__main__":
    wave = [0, 1, 2, 3, 3, 2, 1, 0]
    print(dft(wave))
