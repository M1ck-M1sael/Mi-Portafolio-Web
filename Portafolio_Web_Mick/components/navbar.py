import reflex as rx
from ..state import State
from Portafolio_Web_Mick.styles import typewriter_style
from Portafolio_Web_Mick.views.links import SOCIAL_LINKS, social_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.avatar(src="/MickRM_Logo2.png", fallback="MM", size="5", border_radius="90px"),
                rx.divider(orientation="vertical", height="1.5em", border_color="rgba(255, 255, 255, 0.5)"),
                rx.text("Mick Misael", class_name="typewriter", font_weight="bold", font_family="monospace", size="6"),
                align="center",
                spacing="3",
                width="250px",
            ),
            href="#inicio",
            text_decoration="none",
            color="white",
            _hover={"opacity": "0.8", "text_decoration": "none"},
        ),

        rx.spacer(),

        rx.hstack(
            rx.foreach(
                State.menu_items,
                lambda item: rx.hstack(
                    rx.link(
                        item[1], 
                        href="#" + item[0],
                        color="white",
                        font_weight="medium",
                        padding_x="1em",
                        _hover={"color": "#0070f3", "text_decoration": "none", "transform": "scale(1.1)"},
                        transition="all 0.2s ease-in-out",
                    ),
                    rx.divider(orientation="vertical", height="1em", border_color="rgba(255, 255, 255, 0.2)"),
                    align="center",
                )
            ),
            spacing="0",
            align="center", 
        ),

        rx.spacer(),

        rx.hstack(
            rx.hstack(
                *[social_button(tag, url) for tag, url in SOCIAL_LINKS.items()],
                spacing="4",
                align="center",
            ),
            rx.divider(orientation="vertical", height="1.5em", border_color="rgba(255, 255, 255, 0.5)"),
            rx.button(
                State.contenido["btn_idioma"],
                on_click=State.cambiar_idioma,
                size="2",
                variant="ghost",
                cursor="pointer",
            ),
            align="center", 
            spacing="4",
            width="250px",
            justify="end",
        ),

        width="100%",
        padding_x="2em",
        padding_y="1em",
        align="center",
        justify="between",
        background_color="rgba(0, 0, 0, 0.8)",
        backdrop_filter="blur(10px)", 
        position="sticky",
        top="0",
        z_index="999",
    )