
def find_average(list):
    return sum(list)/len(list)

def gardners_equation(velocity):
    """Calculate the bulk density of a waves litheology
    Args:
        Velocity: Seismic P-wave velcity
    Returns:
        Bulk density of the waves litheology based on velocity
    """
    if velocity <= 0:
        raise ValueError("Negative velocity")
    
    return 0.31*velocity**(0.25)

def inverse_gardners_equation(density):

    if density <= 0:
        raise ValueError("Negative density")

    return (density/0.31)**4