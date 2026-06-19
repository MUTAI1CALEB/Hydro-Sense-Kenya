import numpy as np

# def calculate_et(temp, wind, solar, humidity):
#     """Simplified Evapotranspiration Formula: 0.12*T + 0.35*W + 2.4*Solar - 0.025*H"""
#     et = 0.12 * temp + 0.35 * wind + 2.4 * solar - 0.025 * humidity
#     if isinstance(et, np.ndarray):
#         return np.maximum(0, et)
#     return max(0, et)

# def calculate_et_scalar(temp, wind, solar, humidity):
#     et = 0.12 * temp + 0.35 * wind + 2.4 * solar - 0.025 * humidity
#     return max(0, et)

def calculate_et(temp, wind, solar, humidity):
    et = 0.12 * temp + 0.35 * wind + 2.4 * solar - 0.025 * humidity
    return np.maximum(0, et)


def water_balance_model(s_t, r_t, i_t, et_t, drainage_coeff, field_capacity):
    """
    Computes S_{t+1}.
    Drainage is calculated as a fraction of water exceeding field capacity.
    """
    d_t = 0
    potential_s = s_t + r_t + i_t - et_t
    if potential_s > field_capacity:
        d_t = (potential_s - field_capacity) * drainage_coeff
    
    return potential_s - d_t

def euler_method(s_start, days, params):
    """Simulates soil moisture over time using Euler approximation."""
    results = [s_start]
    for t in range(days):
        # Simplified change rate
        ds_dt = params['rainfall'][t] - params['et'][t]
        results.append(results[-1] + ds_dt)
    return results

def monte_carlo_rainfall(base_rainfall, iterations=1000):
    """Generates stochastic rainfall scenarios."""
    return [base_rainfall * np.random.uniform(0.5, 1.5) for _ in range(iterations)]

def moisture_rate_of_change(S, R, I, ET, drainage_coeff, field_capacity):
    """The ODE function: dS/dt"""
    # Drainage only happens if S > field_capacity
    drainage = max(0, (S - field_capacity) * drainage_coeff)
    return R + I - ET - drainage

def rk4_step(S, R, I, ET, coeff, fc, dt=1):
    """4th Order Runge-Kutta Step for higher precision."""
    k1 = dt * moisture_rate_of_change(S, R, I, ET, coeff, fc)
    k2 = dt * moisture_rate_of_change(S + 0.5*k1, R, I, ET, coeff, fc)
    k3 = dt * moisture_rate_of_change(S + 0.5*k2, R, I, ET, coeff, fc)
    k4 = dt * moisture_rate_of_change(S + k3, R, I, ET, coeff, fc)
    return S + (k1 + 2*k2 + 2*k3 + k4) / 6

