import reflex as rx

def contact() -> rx.Component:
    return rx.vstack(
        rx.heading("Contacto", size="8"),

        id="contacto",
        width="100%",
        min_height="100vh",
        padding_top="100px",
        align="center",
    )