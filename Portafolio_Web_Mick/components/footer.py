import reflex as rx
from ..state import State
from Portafolio_Web_Mick.views.links import SOCIAL_LINKS

def footer() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="/MickRM_Logo2.png",
                            width="80px",
                            height="auto",
                            border_radius="90px",
                            border="2px solid rgba(255, 255, 255, 0.2)",
                        ),
                        rx.vstack(
                            rx.text(
                                "Misael López Franco",
                                font_weight="bold",
                                font_family="monospace",
                                size="5",
                                color="white",
                            ),
                            rx.text(
                                State.contenido["footer_copyright"],
                                size="2",
                                color="rgba(255, 255, 255, 0.6)",
                            ),
                            align_items="start",
                            spacing="0",
                        ),
                        align="center",
                        spacing="4",
                    ),
                    align_items="center",
                    spacing="2",
                ),

                rx.divider(
                    orientation="vertical", 
                    height="120px", 
                    border_color="rgba(255, 255, 255, 0.15)",
                    margin_x="3em"
                ),

                rx.vstack(
                    *[
                        rx.link(
                            rx.hstack(
                                rx.icon(
                                    tag=icon_tag,
                                    size=20,
                                    color="white"
                                ),
                                rx.text(
                                    "Spotify" if icon_tag == "music" else icon_tag.capitalize(),
                                    size="3",
                                    color="rgba(255, 255, 255, 0.8)",
                                ),
                                align="center",
                                spacing="3",
                            ),
                            href=url,
                            is_external=True,
                            _hover={"color": "#0070f3", "text_decoration": "none", "transform": "translateX(5px)"},
                            transition="all 0.2s",
                        )
                        for icon_tag, url in SOCIAL_LINKS.items()
                    ],
                    align_items="start",
                    spacing="3",
                ),
                align="center",
                justify="center",
                padding_y="4em",
                width="100%",
                max_width="1200px",
            ),
        ),
        background_color="rgba(15, 15, 15, 0.45)",
        backdrop_filter="blur(5px)",
        border_top="1px solid rgba(255, 255, 255, 0.1)",
        width="100%",
        margin_bottom="0",
    )