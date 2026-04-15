import reflex as rx

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos", size="8"),
        # ... tu contenido ...
        id="proyectos", # <--- ESTE ID DEBE COINCIDIR CON TU DICCIONARIO EN languages.py
        width="100%",
        min_height="100vh", # Para que cada sección ocupe toda la pantalla
        padding_top="100px", # Espacio para que el navbar no tape el título
        align="center",
    )