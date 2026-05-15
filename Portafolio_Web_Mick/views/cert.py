import reflex as rx
from ..state import State

cert_card_style = {
    "background_color": "rgba(15, 15, 15, 0.45)",
    "backdrop_filter": "blur(5px)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "border_radius": "20px",
    "overflow": "hidden",
    "transition": "transform 0.3s ease, border-color 0.3s ease",
    "_hover": {
        "transform": "translateY(-10px)",
        "border_color": "#0070f3",
    }
}

def cert_card(cert: dict) -> rx.Component:
    """Componente individual responsivo para cada certificación."""
    return rx.box(
        rx.flex(
            rx.image(
                src=cert["badge_url"],
                width="80px",
                height="80px",
                border_radius="md",
            ),

            rx.vstack(
                rx.text(
                    cert["title"], 
                    weight="bold", 
                    size="4",
                    color="white" 
                ),
                rx.text(
                    cert["issuer"], 
                    color="rgba(255, 255, 255, 0.7)",
                    size="2"
                ),
                rx.text(
                    cert["date"], 
                    color_scheme="blue", 
                    size="1",
                    weight="medium"
                ),
                rx.link(
                    rx.button(
                        rx.icon(tag="external_link", size=14),
                        cert["btn_verify"],
                        size="1", 
                        variant="soft", 
                        margin_top="0.5em"
                    ),
                    href=cert["verify_url"],
                    is_external=True,
                ),
                align_items={"initial": "center", "md": "start"}, 
                text_align={"initial": "center", "md": "left"},
            ),
            direction={"initial": "column", "md": "row"}, 
            align_items="center",
            spacing="5",
            padding="1.5em",
        ),
        style=cert_card_style,
        width="100%",
    )

def certifications() -> rx.Component:
    """Sección principal que agrupa las certificaciones."""
    return rx.box(
        rx.vstack(
            rx.heading(
                State.contenido["cert_title"], 
                size={"initial": "7", "md": "9"}, 
                margin_bottom="0.5em",
                color="white"
            ),
            rx.text(
                State.contenido["cert_description"],
                color_scheme="gray",
                margin_bottom="2em",
                text_align="center",
            ),
            
            rx.grid(
                rx.foreach(
                    State.certificaciones_lista, 
                    cert_card
                ),
                columns={"initial": "1", "sm": "2", "lg": "3"},
                spacing="5",
                width="100%",
            ),
            align_items="center",
            width="95%",
            max_width="1600px",
            margin="0 auto", 
        ),
        id="certifications",
        width="100%",
        padding_y={"initial": "4em", "md": "6em"}, 
        padding_x={"initial": "1em", "md": "0"},
    )