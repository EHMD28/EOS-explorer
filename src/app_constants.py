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


# class DebugConstants:
#     # Polytrope fitted to lower densities
#     LOW_DENSITY_KAPPA = 1e-2
#     LOW_DENSITY_GAMMA = 1.4952530968
#     # Polytrope fitted around 10 MeV/fm3
#     MID_DENSITY_KAPPA = 1.2e-3
#     MID_DENSITY_GAMMA = 1.75


class EosConstants:
    DEFAULT_KAPPA = 7.658467851116847e-05
    DEFAULT_GAMMA = 2.1675764038620957


class StreamlitKeys:
    """
    Keys to use with Streamlit's session state API.
    """

    # ----- EoS Tab -----

    ## ----- Polytropic EoS -----
    ENERGY_DENSITY_SLIDER = "energy-density-slider"
    EOS_FILE_UPLOAD_WIDGET = "eos-file-upload-widget"
    POLYTROPIC_EOS_KAPPA_INPUT = "polytropic-eos-kappa-input"
    POLYTROPIC_EOS_GAMMA_INPUT = "polytropic-eos-gamma-input"

    ## ----- Mass-Radius Curve -----
    PRESSURE_SLIDER = "pressure-slider"
    LIMIT_RADIUS_CHECKBOX = "limit-radius-checkbox"
    RADIUS_RANGE_SLIDER = "radius-range-slider"
    MR_FILE_UPLOAD_WIDGET = "mass-radius-file-upload-widget"

    ## ----- Observational Constraints -----
    J0740_CHECKBOX = "J0740-checkbox"
    J0030_CHECKBOX = "J0030-checkbox"
    J0437_CHECKBOX = "J0437-checkbox"
    J0614_CHECKBOX = "J0614-checkbox"
    GW170817_CHECKBOX = "GW170817-checkbox"

    # ----- Debugging Tab -----
    PRESSURE_NU_INPUT = "pressure-input-natural-units"
    PRESSURE_NU_OUTPUT = "pressure-output-natural-units"
    PRESSURE_PRIME_INPUT = "pressure-input-dimensionless"
    PRESSURE_PRIME_OUTPUT = "pressure-output-dimensionless"


class UiConstants:
    # The middle column is three times the width of the margin columns.
    CENTERED_WITH_MARGINS_SPEC = [1, 3, 1]
    SHOW_CONSTRAINTS_BY_DEFAULT = True
    DEFAULT_RADIUS_RANGE = (8, 16)
