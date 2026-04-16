import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.heading("footer", size="8"),
        
        id="footer",
        width="100%",
        min_height="100vh",
        padding_top="100px",
        align="center",
    )