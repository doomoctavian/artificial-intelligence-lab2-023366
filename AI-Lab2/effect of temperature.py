
#Effect of Temperature(023-352)

import math

def acceptance_probability(delta_E, T):
    """
    Calculates probability of accepting an inferior node
    """
    if delta_E < 0:
        return 1.0   
    return math.exp(-delta_E / T)


def temperature_schedule(T):
    """
    Simple temperature reduction
    """
    return T * 0.5

if __name__ == "__main__":
    delta_E = 5      
    T = 100          

    print("Delta E (inferior cost):", delta_E)
    print("----------------------------------")
    print("Temperature | Acceptance Probability")
    print("----------------------------------")

    for step in range(6):
        prob = acceptance_probability(delta_E, T)
        print(f"{T:10.2f} | {prob:.6f}")
        T = temperature_schedule(T)