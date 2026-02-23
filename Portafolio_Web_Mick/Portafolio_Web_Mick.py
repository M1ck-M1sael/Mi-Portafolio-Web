import reflex as rx
from Portafolio_Web_Mick.components.background import background

def index():
    return rx.box(
        background(),
        rx.hstack(
            rx.text("Esto es el inicioo de mi portafolio")
        )
    )
    

app = rx.App()
app.add_page(index)
