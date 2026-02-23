import reflex as rx
from Portafolio_Web_Mick.state import State
from Portafolio_Web_Mick.styles import typewriter_style
from Portafolio_Web_Mick.views.links import SOCIAL_LINKS, social_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.avatar(
                src="/MickRM_Logo2.png",
                fallback="MM",
                size="5",
                border_radius="full"
            ),
            rx.divider(orientation="vertical", height="1.5em", border_color="white"),
            rx.text(
                "Mick Misael",
                style=typewriter_style,
                font_weight="bold",
                font_family="monospace",
                size="5",
            ),
            align="center",
            spacing="3",
        ),

        rx.spacer(),

        rx.hstack(
            rx.hstack(
                rx.foreach(
                    State.menu_items,
                    lambda item: rx.link(
                        item[1], 
                        href="#" + item[0],
                        color="white",
                        font_weight="medium",
                        _hover={"color": "#0070f3", "text_decoration": "none"},
                    ),
                ),
                spacing="5",
                margin_right="1em",
            ),
            rx.divider(orientation="vertical", height="1.5em", border_color="white"),

            *[social_button(tag, url) for tag, url in SOCIAL_LINKS.items()],
            
            rx.divider(orientation="vertical", height="1.5em", border_color="white"),
            
            rx.button(
                State.contenido["btn_idioma"],
                on_click=State.cambiar_idioma,
                size="2",
                variant="ghost",
                cursor="pointer",
            ),
            align="center",
            spacing="4",
        ),

        width="100%",
        padding_x="2em",
        padding_y="1em",
        background_color="rgba(0, 0, 0, 0.8)",
        backdrop_filter="blur(10px)", 
        position="sticky",
        top="0",
        z_index="999",
        justify="between",
    )