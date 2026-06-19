import sys
import os
import numpy as np
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.simulation import calculate_et, water_balance_model

def test_et_non_negative():
    """Edge case: High humidity and low temp should not produce negative ET."""
    # T=5, W=0.1, Solar=0, H=99
    et = calculate_et(5, 0.1, 0, 99)
    assert et >= 0

def test_et_vectorized_alignment():
    """Check that array inputs produce array outputs with the same logic."""
    temps = np.array([20, 30])
    winds = np.array([2, 5])
    solars = np.array([0.5, 0.8])
    hums = np.array([50, 40])
    et_array = calculate_et(temps, winds, solars, hums)
    assert len(et_array) == 2
    assert et_array[0] > 0

def test_drainage_logic():
    """Test that drainage occurs only when exceeding field capacity."""
    # S=40, R=10, I=0, ET=2, Capacity=45, Coeff=0.2
    # Potential = 48. Exceeds by 3. Drainage = 3 * 0.2 = 0.6.
    # Result = 48 - 0.6 = 47.4
    res = water_balance_model(s_t=40, r_t=10, i_t=0, et_t=2, drainage_coeff=0.2, field_capacity=45)
    assert pytest.approx(res, 0.1) == 47.4

def test_zero_water_scenario():
    """Edge case: Absolute zero inputs."""
    res = water_balance_model(0, 0, 0, 0, 0.5, 40)
    assert res == 0