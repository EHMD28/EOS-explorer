from ui.eos_tab import (
    draw_and_get_eos_dropdown,
    draw_ui_for_polytropic_eos,
    draw_ui_for_soc_eos,
)


def draw_ui():
    """
    Write components to user interface.
    """
    eos_dropdown = draw_and_get_eos_dropdown()
    match eos_dropdown:
        case "Polytropic":
            draw_ui_for_polytropic_eos()
        case "Speed-of-Sound Interpolation":
            draw_ui_for_soc_eos()
