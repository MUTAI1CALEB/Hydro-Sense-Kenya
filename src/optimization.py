def find_required_irrigation(current_s, target_s, et_est, rain_est):
    """
    Calculates the exact irrigation needed to reach target moisture.
    Constraint: Irrigation cannot be negative.
    """
    # Based on S_next = S_t + R + I - ET
    # I = S_target - S_t - R + ET
    needed = target_s - current_s - rain_est + et_est
    return max(0, needed)

def minimize_water_usage(soil_levels, min_threshold, capacity):
    """Heuristic to propose irrigation schedule."""
    schedule = []
    for s in soil_levels:
        if s < min_threshold:
            schedule.append(capacity - s)
        else:
            schedule.append(0)
    return schedule

def irrigation_cost(I, S_t, R, ET, S_target, coeff, fc, lmbda=0.1):
    """Calculates the penalty for a specific irrigation amount."""
    # Predict next state
    S_next = S_t + R + I - ET - max(0, (S_t + R + I - ET - fc) * coeff)
    # Penalty = (Error from target)^2 + (Water use penalty)
    return (S_target - S_next)**2 + lmbda * (I**2)

def optimize_irrigation_gd(S_t, R, ET, S_target, coeff, fc, alpha=0.05, iters=100):
    """Finds optimal I using Gradient Descent."""
    I_opt = 5.0  # Initial guess
    h = 0.01     # Step for numerical derivative
    
    for _ in range(iters):
        # Calculate numerical gradient: [J(I+h) - J(I-h)] / 2h
        grad = (irrigation_cost(I_opt + h, S_t, R, ET, S_target, coeff, fc) - 
                irrigation_cost(I_opt - h, S_t, R, ET, S_target, coeff, fc)) / (2 * h)
        I_opt = I_opt - alpha * grad
        
    return max(0, I_opt) # Irrigation cannot be negative