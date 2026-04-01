from pathlib import Path

from plotting import load_eos_from_file, load_mr_curve_from_df


EOS_FILE_PATH = Path("src/data/eos_68.txt")
MRL_FILE_PATH = Path("src/data/mrl_eos_68.txt")

EOS_DATA = load_eos_from_file(EOS_FILE_PATH)
# EOS_DATA_DIMENSIONLESS = [(eps_prime(eps), p_prime(p)) for (eps, p) in EOS_DATA]
MR_DATA = load_mr_curve_from_df(MRL_FILE_PATH)

E_0 = 1e-5
