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
    EPS_0 = 100  # MeV/km^3
    # Gravitational constant. Refer to `Calculations.md` for derivation.
    G_NU = 4.426810498  # km/M_sun.
    # Radius scaling constant
    A = 1 / np.sqrt(G_NU * EPS_0)  # km
    # Mass scaling constant
    B = 1 / np.sqrt(G_NU**3 * EPS_0)  # M_sun
    # Conversion factor to convert from MeV/fm^3 to M_sun/km^3
    MEV_FM3_TO_MSUN_KM3 = 8.96523625e-7


class StreamlitKeys:
    """
    Keys to use with Streamlit's session state API.
    """

    # Pressure (in natural units) input
    PRESSURE_NU_INPUT = "pressure-input-natural-units"
    # Pressure (in natural units) output value
    PRESSURE_NU_OUTPUT = "pressure-output-natural-units"
    # Pressure (dimensionless) input
    PRESSURE_PRIME_INPUT = "pressure-input-dimensionless"
    # Pressure (dimensionless) output value
    PRESSURE_PRIME_OUTPUT = "pressure-output-dimensionless"
