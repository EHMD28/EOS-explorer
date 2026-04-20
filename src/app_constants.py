from pathlib import Path


class AppConstants:
    FAVICON_PATH = Path("assets/favicon.png")


class ScalingConstants:
    """
    Dimensionless TOV scaling constants. This implementation is taken directly
    from Section 4.3 of Compact Star Physics by  Jürgen Schaffner-Bielich.
    """

    # # Arbitrary scaling constant.
    EPS_0 = 100  # MeV/fm^3
    MEV_FM3_TO_J_M3 = 1.602176634e32
    M_SUN_IN_KG = 1.988416e30


class DebugConstants:
    # Polytrope fitted to lower densities
    LOW_DENSITY_KAPPA = 1e-2
    LOW_DENSITY_GAMMA = 1.4952530968
    # Polytrope fitted around 10 MeV/fm3
    MID_DENSITY_KAPPA = 1.2e-3
    MID_DENSITY_GAMMA = 1.75


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
