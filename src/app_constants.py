from pathlib import Path

import numpy as np

from plotting import load_eos_from_file, load_mr_curve_from_df


class AppConstants:
    FAVICON_PATH = Path("assets/favicon.png")


EOS_FILE_PATH = Path("src/data/eos_68.txt")
MRL_FILE_PATH = Path("src/data/mrl_eos_68.txt")

EOS_DATA = load_eos_from_file(EOS_FILE_PATH)
MR_DATA = load_mr_curve_from_df(MRL_FILE_PATH)


class ScalingConstants:
    E_0 = 100
    G_NU = 1.4766  # km/solar-mass
    A = 1 / np.sqrt(G_NU * E_0)
    B = 1 / np.sqrt(G_NU**3 * E_0)
    MEV_PER_FM3_TO_SM_PER_KM_3 = (
        8.96498313e-7  # Conversion factor to convert from MeV/fm^3 to M☉/km^3
    )
