"""
Polytropic EOS
"""


def eos_eps(p: float, k: float, gamma: float) -> float:
    """
    Calculates the energy density [MeV/fm^3] as a function of pressure
    [MeV/fm^3] using a polytropic equation of state.
    """
    return (p / k) ** (1 / gamma)
