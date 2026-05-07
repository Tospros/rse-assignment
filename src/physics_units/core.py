from pint import UnitRegistry

ureg = UnitRegistry()


def speed(distance_meters: float, time_seconds: float):
    distance = distance_meters * ureg.meter
    time = time_seconds * ureg.second
    return distance / time



def force(mass_kg: float, acceleration_mps2: float):
    mass = mass_kg * ureg.kilogram
    acceleration = acceleration_mps2 * ureg.meter / (ureg.second ** 2)
    return mass * acceleration



def kinetic_energy(mass_kg: float, velocity_mps: float):
    mass = mass_kg * ureg.kilogram
    velocity = velocity_mps * ureg.meter / ureg.second
    return 0.5 * mass * velocity ** 2