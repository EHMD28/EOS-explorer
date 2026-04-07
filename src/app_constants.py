from pathlib import Path

import numpy as np


class AppConstants:
    FAVICON_PATH = Path("assets/favicon.png")


# EOS_FILE_PATH = Path("src/data/eos_68.txt")
# MRL_FILE_PATH = Path("src/data/mrl_eos_68.txt")


class ScalingConstants:
    """
    Dimensionless TOV scaling constants. This implementation is taken directly
    from Section 4.3 of Compact Star Physics by  Jürgen Schaffner-Bielich.
    """

    E_0 = 100  # Arbitrary scaling constant.
    G_NU = 1.4766  # km/solar-mass. This is the quantity for ensuring everything has a consistent unit for length and mass.
    A = 1 / np.sqrt(G_NU * E_0)
    B = 1 / np.sqrt(G_NU**3 * E_0)
