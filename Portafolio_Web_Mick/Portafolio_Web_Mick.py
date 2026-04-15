import reflex as rx
from .components.navbar import navbar
from .components.footer import footer
from .components.background import background
from .views.hero import hero     # <--- Nueva importación
from .views.about import about
from .views.projects import projects
from .views.contact import contact

def index() -> rx.Component:
    return rx.box(
        background(), # El video de las estrellas fijo al fondo
        navbar(),     # El menú pegado arriba
        rx.vstack(
            hero(),     # <--- Primera sección que se ve
            about(),    
            projects(), 
            contact(),
            footer(),
            width="100%",
            spacing="0",
        ),
    )

app = rx.App(
    stylesheets=["/styles.css"],
)
app.add_page(index)

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
