from pathlib import Path

import numpy as np


class AppConstants:
    FAVICON_PATH = Path("assets/favicon.png")


class ScalingConstants:
    """
    Dimensionless TOV scaling constants. This implementation is taken directly
    from Section 4.3 of Compact Star Physics by  Jürgen Schaffner-Bielich.
    """

    # Arbitrary scaling constant.
    E_0 = 100
    # TODO: Find calculation for this constant. Possibly a bug.
    # This is the quantity for ensuring everything has a consistent unit for length and mass.
    G_NU = 1.4766  # km/solar-mass.
    # Radius scaling constant
    A = 1 / np.sqrt(G_NU * E_0)  # km
    # Mass scaling constant
    B = 1 / np.sqrt(G_NU**3 * E_0)  # M_sun
