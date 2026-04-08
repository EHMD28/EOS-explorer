# EoS Explorer

> [!IMPORTANT]
> This project is still very much a WIP. My deadline to finish it is May 14, 2026.

This is a web application for exploring the equation of state (EoS) of neutron-star matter. The application includes a Tolman-Oppenheimer-Volkoff (TOV) solver, which, when coupled with an EoS, is used to generate a mass-radius curve for neutron stars at different central pressures. See the full write-up for more details.

This project using [SciPy](https://scipy.org/) and [Numpy](https://numpy.org/) for solving the TOV equation, [Matplotlib](https://matplotlib.org/) for plotting the results, and [Streamlit](https://streamlit.io/) for creating the user interface.

## Running

If you would like to view the application locally, run the following command(s) in your terminal from the root directory of this repository. You must have Python version 3+ to run this. It's recommended to avoid installing depencies globally by using [virtual environments](https://docs.python.org/3/library/venv.html).

Using `python3`.

```bash
python3 -m venv .venv # create a virtual environment for installing dependencies
source .venv/bin/activate
python3 -m pip install -r pyproject.toml # install dependencies
python3 -m streamlit run src/app.py # (or just `streamlit run src/app.py`)
```

Using `uv`.

```bash
uv venv
uv pip install -r pyproject.toml
source .venv/bin/activate
streamlit run src/app.py
```
