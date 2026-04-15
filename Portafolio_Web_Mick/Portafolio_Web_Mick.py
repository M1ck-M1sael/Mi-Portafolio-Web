import reflex as rx
from .components.navbar import navbar
from .components.footer import footer
from .components.background import background
from .views.about import about
from .views.projects import projects
from .views.contact import contact

def index() -> rx.Component:
    return rx.box(
        background(), # El video de las estrellas de fondo
        navbar(),     # El menú que ya tenemos con State.menu_items
        rx.vstack(
            # Aquí "inyectas" tus vistas una tras otra
            about(),    
            projects(), 
            contact(),
            footer(),
            width="100%",
            spacing="0", # Evita espacios en blanco entre secciones
        ),
    )

# Solo una ruta principal
app = rx.App(
    stylesheets=[
        "/styles.css", 
    ],
)
app.add_page(index)

# import reflex as rx
# from Portafolio_Web_Mick.state import State
# from Portafolio_Web_Mick.components.background import background
# from Portafolio_Web_Mick.components.navbar import navbar

# def index():
#     return rx.box(
#         background(),
#         navbar(),
#         rx.hstack(
#             rx.text("Esto es el inicioo de mi portafolio")
#         )
#     )
    

# app = rx.App()
# app.add_page(index)
