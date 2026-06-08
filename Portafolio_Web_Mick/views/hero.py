import reflex as rx
from ..styles import HERO_MARGIN_TOP

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/HeadImageMisaelLogo.png",
                width={"initial": "90%", "sm": "70%", "md": "100%"}, 
                max_width="100%", 
                height="auto",
                alt="Mick Misael Logo",
                style={"filter": "drop-shadow(0px 0px 30px rgba(0, 112, 243, 0.4))"}
            ),

            rx.text(
                "COMPUTER SYSTEMS ENGINEER | SYSADMIN | DEVOPS Inprogress",
                size={"initial": "1", "sm": "2", "md": "5"},
                font_family="monospace",
                text_align="center",
                letter_spacing={"initial": "0px", "md": "2px"}, 
                white_space="normal",
                word_break="break-word",
            ),
            spacing={"initial": "4", "md": "6"}, 
            align="center",
            max_width="1200px",
            width="100%",
        ),
        width="100%",
        max_width="100vw",
        min_height="100dvh", 
        margin_top=HERO_MARGIN_TOP,
        padding_bottom="5vh",
        padding_x={"initial": "1em", "md": "2em"},
        box_sizing="border-box",
        overflow_x="hidden",
    )