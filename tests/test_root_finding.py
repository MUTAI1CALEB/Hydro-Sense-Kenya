import sys
import os
import pytest

# Ensure src is reachable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.numerical_methods import bisection_method, newton_raphson

def test_bisection_standard():
    """Test root finding for a simple linear function."""
    func = lambda x: x - 5
    result = bisection_method(func, 0, 10)
    assert pytest.approx(result, 1e-5) == 5.0

def test_bisection_no_root():
    """Edge case: Function does not cross zero in the given interval."""
    func = lambda x: x**2 + 1  # Always positive
    result = bisection_method(func, -1, 1)
    assert result is None

def test_newton_convergence():
    """Test Newton-Raphson on a quadratic function."""
    func = lambda x: x**2 - 9
    dfunc = lambda x: 2*x
    result = newton_raphson(func, dfunc, x0=2)
    assert pytest.approx(result, 1e-5) == 3.0

def test_newton_zero_derivative():
    """Edge case: Newton-Raphson encountering a flat slope (division by zero)."""
    func = lambda x: x**2 - 9
    dfunc = lambda x: 0 # Artificial flat slope
    result = newton_raphson(func, dfunc, x0=2)
    # The function should handle this by breaking out or returning the last estimate
    assert result is not None