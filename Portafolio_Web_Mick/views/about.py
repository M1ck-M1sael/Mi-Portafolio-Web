import reflex as rx

def about() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Sobre mí", size="8", color="white", margin_bottom="1em"),
            rx.flex(
                # Columna de texto
                rx.vstack(
                    rx.text(
                        "Soy un apasionado de la infraestructura y la automatización. "
                        "Mi camino en la ingeniería me ha llevado a entender que el software "
                        "solo es tan bueno como la plataforma donde corre.",
                        font_size="1.1em",
                        color="rgba(255,255,255,0.8)"
                    ),
                    rx.text(
                        "Como CEO de StackTON, busco simplificar la arquitectura cloud "
                        "para que los desarrolladores se enfoquen en crear.",
                        font_size="1.1em",
                        color="rgba(255,255,255,0.8)"
                    ),
                    align_items="start",
                    spacing="4",
                    flex="1",
                ),
                # Espacio entre columnas
                rx.box(width="4em"),
                # Columna de Skills (puedes usar iconos aquí luego)
                rx.vstack(
                    rx.badge("AWS Cloud", variant="outline", color_scheme="blue", size="3"),
                    rx.badge("SysAdmin (Linux)", variant="outline", color_scheme="green", size="3"),
                    rx.badge("Python & Reflex", variant="outline", color_scheme="purple", size="3"),
                    rx.badge("DevOps Culture", variant="outline", color_scheme="orange", size="3"),
                    align_items="end",
                    flex="1",
                ),
                width="100%",
                flex_direction=["column", "column", "row"], # Responsivo
            ),
            # El contenedor estilo "cristal"
            padding="3em",
            background_color="rgba(255, 255, 255, 0.05)",
            backdrop_filter="blur(15px)",
            border="1px solid rgba(255, 255, 255, 0.1)",
            border_radius="20px",
            max_width="1000px",
        ),
        id="sobre_mi",
        width="100%",
        min_height="80vh",
        padding_y="5em",
    )