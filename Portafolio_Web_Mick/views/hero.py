import reflex as rx
from ..styles import HERO_MARGIN_TOP

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="/HeadImageMisaelLogo.png",
                # Ajustamos los anchos para que respire en móviles
                width={"initial": "90%", "sm": "70%", "md": "100%"}, 
                max_width="100%", 
                height="auto", # Mantiene la proporción
                alt="Mick Misael Logo",
                style={"filter": "drop-shadow(0px 0px 30px rgba(0, 112, 243, 0.4))"}
            ),

            rx.text(
                "COMPUTER SYSTEMS ENGINEER | SYSADMIN | CEO of StackTON",
                size={"initial": "1", "sm": "2", "md": "5"}, # Reduje un poco en móvil para que no se vea tan tosco
                color="rgba(255, 255, 255, 0.9)",
                font_family="monospace",
                text_align="center",
                letter_spacing={"initial": "0px", "md": "2px"}, 
                # Esta es la magia para que el texto no rompa el layout
                white_space="normal",
                word_break="break-word",
            ),
            spacing={"initial": "4", "md": "6"}, 
            align="center",
            max_width="1200px", # Movimos el límite rígido al contenedor
            width="100%",
        ),
        width="100%",
        max_width="100vw", # Evita el desbordamiento a toda costa
        min_height="100dvh", 
        margin_top=HERO_MARGIN_TOP,
        padding_bottom="5vh",
        padding_x={"initial": "1em", "md": "2em"},
        box_sizing="border-box", # Obliga a que el padding no engorde el contenedor
        overflow_x="hidden",
    )