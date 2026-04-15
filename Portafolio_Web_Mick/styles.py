# styles.py
import reflex as rx

# NO USES rx.keyframes AQUÍ, están rompiendo tu venv
typewriter_style = {
    "overflow": "hidden",
    "white_space": "nowrap",
    "border_right": "3px solid",
    "margin": "0",
    "width": "100%",
    "animation": (
        "typing 3s steps(11, end) forwards, " # El nombre 'typing' lo sacará del CSS
        "blink-caret 0.75s step-end infinite"  # El nombre 'blink-caret' también
    ),
}