import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src.numerical_methods as nm

def test_trapezoidal_rule():
    """Requirement: Trapezoidal rule implementation."""
    # Integral of x from 0 to 4 is 8
    f = lambda x: x
    result = nm.trapezoidal_rule(f, 0, 4, n=1000)
    assert pytest.approx(result, 1e-4) == 8.0

def test_simpson_rule():
    """Requirement: Simpson rule implementation."""
    # Integral of x^2 from 0 to 3 is 9
    f = lambda x: x**2
    result = nm.simpson_rule(f, 0, 3, n=1000)
    assert pytest.approx(result, 1e-4) == 9.0

def test_simpson_error_handling():
    """Requirement: Simpson's rule requires even n."""
    f = lambda x: x
    with pytest.raises(ValueError):
        nm.simpson_rule(f, 0, 2, n=11)