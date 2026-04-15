import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.heading("footer", size="8"),
        # ... tu contenido ...
        id="footer", # <--- ESTE ID DEBE COINCIDIR CON TU DICCIONARIO EN languages.py
        width="100%",
        min_height="100vh", # Para que cada sección ocupe toda la pantalla
        padding_top="100px", # Espacio para que el navbar no tape el título
        align="center",
    )