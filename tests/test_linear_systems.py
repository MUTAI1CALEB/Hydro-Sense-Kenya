import sys
import os
import numpy as np
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src.numerical_methods as nm

def test_gaussian_elimination_standard():
    """Requirement: Gaussian elimination implemented manually."""
    # Simple system: 2x + y = 5; x + 3y = 5 -> x=2, y=1
    A = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([5.0, 5.0])
    x = nm.gaussian_elimination(A, b)
    assert np.allclose(x, [2.0, 1.0])

def test_gaussian_elimination_3x3():
    """Test with a 3x3 matrix (representative of 3-zone allocation)."""
    A = np.array([[1.0, 1.0, 1.0], [0.0, 2.0, 1.0], [0.0, 0.0, 3.0]])
    b = np.array([6.0, 5.0, 9.0])
    # x=1, y=1, z=3
    x = nm.gaussian_elimination(A, b)
    assert np.allclose(x, [1.0, 1.0, 3.0])