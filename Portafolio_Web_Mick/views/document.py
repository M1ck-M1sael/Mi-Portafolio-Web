import reflex as rx
from ..state import State
from ..components.navbar import navbar
from ..components.footer import footer
from ..components.background import background

def documentacion_page() -> rx.Component:
    return rx.box(
        background(),
        navbar(),
        
        rx.center(
            rx.box(
                rx.markdown(
                    State.contenido["doc_markdown"],
                    color="white",
                ),
                max_width="900px", 
                width="90%",
                padding="3em",
                background_color="rgba(15, 15, 15, 0.7)", 
                backdrop_filter="blur(10px)",
                border_radius="15px",
                border="1px solid rgba(0, 255, 0, 0.2)",
                margin_top="8em", 
                margin_bottom="4em",
            ),
            width="100%",
        ),
        
        footer(),
        
        width="100%",
        min_height="100vh",
    )