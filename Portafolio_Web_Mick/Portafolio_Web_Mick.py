import reflex as rx
from .styles import MAIN_WIDTH
from .components.navbar import navbar
from .components.footer import footer
from .components.background import background
from .views.hero import hero
from .views.about import about
from .views.cert import certifications
from .views.projects import projects
from .views.contact import contact
from .views.document import documentacion_page

def index() -> rx.Component:
    return rx.box(
        background(),
        navbar(),
        rx.vstack(
            hero(),
            about(),   
            certifications(),
            projects(), 
            contact(),
            footer(),
            margin_x="auto",
            width=MAIN_WIDTH,
            spacing="0",
        ),
        width="100%",
        min_height="100vh",
    )

app = rx.App(
    style={
        "body": {
            "margin": "0",
            "padding": "0",
            "overflow_x": "hidden",
        }
    },
    stylesheets=["/styles.css"],
)

app.add_page(
    index,
    route="/",
    title="Mick Misael | Portafolio",
)

app.add_page(
    documentacion_page,
    route="/documentacion",
    title="Documentación | Mick Misael",
)