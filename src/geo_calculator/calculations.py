
def find_average(list):
    return sum(list)/len(list)

def gardners_equation(velocity):
    """Calculate the bulk density of a waves litheology
    Args:
        Velocity: Seismic P-wave velcity
    Returns:
        Bulk density of the waves litheology based on velocity
    """
    return 0.31*velocity**(0.25)