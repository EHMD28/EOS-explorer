"""
This file in the entry point of the application.
"""

from app_constants import EOS_DATA
from tov import generate_mr_curve


def main():
    pressures, _ = EOS_DATA
    p_c_range = pressures
    radii, masses = generate_mr_curve(p_c_range)
    print(radii)
    print("-" * 80)
    print(masses)

    # fig = generate_log_fig(
    #     title="Mass Radius Curve",
    #     x_label="Radius [km]",
    #     y_label="Mass [M_sun]",
    #     xs=radii,
    #     ys=masses,
    #     is_scatter=True,
    # )
    # st.pyplot(fig)


if __name__ == "__main__":
    main()
