from physics_units.core import speed, force, kinetic_energy



def test_speed():
    result = speed(100, 10)
    assert round(result.magnitude, 2) == 10



def test_force():
    result = force(10, 2)
    assert round(result.magnitude, 2) == 20



def test_kinetic_energy():
    result = kinetic_energy(2, 10)
    assert round(result.magnitude, 2) == 100