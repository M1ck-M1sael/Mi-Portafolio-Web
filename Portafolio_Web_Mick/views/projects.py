import reflex as rx

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos", size="8"),

        id="proyectos",
        width="100%",
        min_height="100vh",
        padding_top="100px",
        align="center",
    )