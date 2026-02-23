import reflex as rx
from Portafolio_Web_Mick.state import State
from Portafolio_Web_Mick.components.background import background
from Portafolio_Web_Mick.components.navbar import navbar

def index():
    return rx.box(
        background(),
        navbar(),
        rx.hstack(
            rx.text("Esto es el inicioo de mi portafolio")
        )
    )
    

app = rx.App()
app.add_page(index)
