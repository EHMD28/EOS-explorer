# M-R contours 

Four NICER pulsars and the GW170817 binary components are provided as
2D mass–radius confidence contours at 1σ, 2σ, 3σ.

## Files

All CSV files live in `data/` and share the same format:

```
R_km,M_solar
10.66,1.357
...
```

### NICER pulsars

| File stem in `data/` | Pulsar | Original posterior file | Reference |
|---|---|---|---|
| `J0740_latest_{1,2,3}sigma.csv` | PSR J0740+6620 | `J0740_gamma_NxX_lp40k_se001_mrsamples_post_equal_weights.dat` | Salmi et al. 2024 (NICER+XMM) |
| `J0030_{1,2,3}sigma.csv`        | PSR J0030+0451 | `ST+PDT.txt` | Riley et al. 2019 |
| `J0437_{1,2,3}sigma.csv`        | PSR J0437−4715 | `J0437_3C50_BKG_AGN_hiMN_lowXPSI_mrsamples_post_equal_weights.dat` | Choudhury et al. 2024 |
| `J0614_{1,2,3}sigma.csv`        | PSR J0614−3329 | `J0614_ST_PDT_20kLP_0p05SE_0p1ET_mrsamples_post_equal_weights.dat` | Mauviard et al. 2025 |

Contours were extracted from the 2D (R, M) posterior samples via a Gaussian KDE
(Scott's rule bandwidth) and the level curves enclosing 68.27% (1σ), 95.45% (2σ)
and 99.73% (3σ) of the probability mass.

### GW170817

| File stem in `data/` | Component | Source |
|---|---|---|
| `GW_w_mmax_NS1_{1sigma,2sigma,3sigma,90}.csv` | primary NS  (m₁) | LVC GW170817 parametrised EoS posterior `Parametrized-EoS_maxmass_posterior_samples.dat`, with the Mₘₐₓ ≥ 1.97 M☉ constraint applied |
| `GW_w_mmax_NS2_{1sigma,2sigma,3sigma,90}.csv` | secondary NS (m₂) | same |

The `_90.csv` files are the 90% credible region (default in the notebook);
`_{1,2,3}sigma.csv` are the 68/95/99.7% Gaussian-equivalent levels.
These correspond to the single GW170817 band shown in Fig. 4.

## Notebook

`plot_NICER_GW.ipynb:

- the **1σ** contour of each of the four NICER pulsars, and
- the **90% CI** GW170817 band (NS1 + NS2).

Axis limits are set to match Fig. 4: R ∈ [9, 16] km, M ∈ [1, 3] M☉.

To switch NICER to 1/2/3σ stacked contours, set
`nicer_sigmas = ['3sigma','2sigma','1sigma']` inside the notebook (outer to
inner — the innermost 1σ ends up darkest). The GW170817 level is controlled
independently by `gw_levels`, with choices `'90'` (default), `'1sigma'`,
`'2sigma'`, `'3sigma'`.

## Contact

Tuhin Malik — tuhin.malik@gmail.com
