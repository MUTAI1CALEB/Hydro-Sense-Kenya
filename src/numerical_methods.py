import math
import numpy as np
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid interval: f(a) and f(b) must have opposite signs.")

    c = a

    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for solving f(x) = 0.
    Requires derivative df(x).
    """
    x = x0

    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-12:
            raise ZeroDivisionError("Derivative too small; Newton method fails.")

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)

        if abs(f1 - f0) < 1e-12:
            raise ZeroDivisionError("Division instability in secant method.")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return x1

# Numerical Differentiation Methods
def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


# Numerical Differentiation Methods
def trapezoidal_rule(f, a, b, n=1000):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        total += f(a + i * h)

    return total * h


def simpson_rule(f, a, b, n=1000):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule.")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)

    return total * (h / 3)

def gaussian_elimination(A, b):
    """Manual implementation of Gaussian Elimination for Ax = b."""
    n = len(b)
    # Augment matrix
    Ab = np.hstack([A, b.reshape(-1, 1)])
    for i in range(n):
        # Pivot
        for j in range(i + 1, n):
            if abs(Ab[j, i]) > abs(Ab[i, i]):
                Ab[[i, j]] = Ab[[j, i]]
        # Eliminate
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    return x