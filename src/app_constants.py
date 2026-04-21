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

    # ----- EoS Tab -----
    ENERGY_DENSITY_SLIDER = "energy-density-slider"
    PRESSURE_SLIDER = "pressure-slider"
    EOS_FILE_UPLOAD_WIDGET = "eos-file-upload-widget"
    MR_FILE_UPLOAD_WIDGET = "mass-radius-file-upload-widget"
    POLYTROPIC_EOS_KAPPA_INPUT = "polytropic-eos-kappa-input"
    POLYTROPIC_EOS_GAMMA_INPUT = "polytropic-eos-gamma-input"

    # ----- Debugging Tab -----
    PRESSURE_NU_INPUT = "pressure-input-natural-units"
    PRESSURE_NU_OUTPUT = "pressure-output-natural-units"
    PRESSURE_PRIME_INPUT = "pressure-input-dimensionless"
    PRESSURE_PRIME_OUTPUT = "pressure-output-dimensionless"


class UiConstants:
    # The middle column is three times the width of the margin columns.
    CENTERED_WITH_MARGINS_SPEC = [1, 3, 1]
