import reflex as rx
from .components.navbar import navbar
from .components.footer import footer
from .components.background import background
from .views.hero import hero
from .views.about import about
from .views.projects import projects
from .views.contact import contact

def index() -> rx.Component:
    return rx.box(
        background(),
        navbar(),
        rx.vstack(
            hero(),
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

app = rx.App(
    stylesheets=[
        "/styles.css", 
    ],
)
app.add_page(index)

