import reflex as rx

def index():
    return rx.text("Esto es el inicioo de mi portafolio")

app = rx.App()
app.add_page(index)
