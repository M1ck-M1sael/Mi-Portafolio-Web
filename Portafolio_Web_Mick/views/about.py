import reflex as rx
from ..state import State

def about() -> rx.Component:
    return rx.vstack(
        rx.heading(
            #"Sobre mí", size="8"
            State.contenido["about_me"].to(dict)["heading"], size="8",
            ),
        # ... tu contenido ...
        id="sobre_mi", # <--- ESTE ID DEBE COINCIDIR CON TU DICCIONARIO EN languages.py
        width="100%",
        min_height="100vh", # Para que cada sección ocupe toda la pantalla
        padding_top="100px", # Espacio para que el navbar no tape el título
        align="center",
    )