import reflex as rx

typewriter_style = {
    "overflow": "hidden",
    "white_space": "nowrap",
    "border_right": "3px solid",
    "margin": "0",
    "width": "100%",
    "animation": (
        "typing 3s steps(11, end) forwards, "
        "blink-caret 0.75s step-end infinite"
    ),
}

MAIN_WIDTH = {"initial": "100%", "md": "80%"}

HERO_TITLE_SIZE = {"initial": "3", "sm": "5", "md": "7"}
HERO_MARGIN_TOP = {"initial": "-2em", "md": "-5em"}

SECTION_TITLE_SIZE = {"initial": "5", "md": "8"}
SECTION_SPACING = {"initial": "4", "md": "8"}

CARD_WIDTH = {"initial": "100%", "sm": "45%", "lg": "30%"}