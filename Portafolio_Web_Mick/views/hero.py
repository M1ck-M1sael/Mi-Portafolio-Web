import reflex as rx
from ..styles import HERO_MARGIN_TOP

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/HeadImageMisaelLogo.png",
                width={"initial": "75%", "sm": "60%", "md": "100%"}, 
                max_width="1200px",
                alt="Mick Misael Logo",
                style={"filter": "drop-shadow(0px 0px 30px rgba(0, 112, 243, 0.4))"}
            ),

            rx.text(
                "COMPUTER SYSTEMS ENGINEER | SYSADMIN | CEO of StackTON",
                size={"initial": "2", "sm": "3", "md": "5"}, 
                color="rgba(255, 255, 255, 0.9)",
                font_family="monospace",
                text_align="center",
                letter_spacing={"initial": "0px", "md": "2px"}, 
                padding_x={"initial": "1em", "md": "0"}, 
            ),
            spacing={"initial": "4", "md": "6"}, 
            align="center",
        ),
        width="100%",
        min_height="100dvh", 
        margin_top=HERO_MARGIN_TOP,
        padding_bottom="5vh",
        padding_x="1em", 
    )