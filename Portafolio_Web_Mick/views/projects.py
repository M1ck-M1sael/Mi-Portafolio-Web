import reflex as rx

# Reutilizamos tu estilo de vidrio pero adaptado a tarjetas
project_card_style = {
    "background_color": "rgba(15, 15, 15, 0.45)",
    "backdrop_filter": "blur(5px)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "border_radius": "20px",
    "overflow": "hidden", # Importante para que la imagen no se salga
    "transition": "transform 0.3s ease, border-color 0.3s ease",
    "_hover": {
        "transform": "translateY(-10px)",
        "border_color": "#0070f3",
    }
}

def project_item(title: str, description: str, image: str, tags: list) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.image(src=image, width="100%", height="200px", object_fit="cover"),
                rx.vstack(
                    rx.text(description, size="3", color="white", text_align="center"),
                    rx.hstack(
                        *[rx.badge(tag, color_scheme="blue", variant="surface") for tag in tags],
                        spacing="2",
                        padding_top="1em"
                    ),
                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    background="rgba(0, 0, 0, 0.8)",
                    opacity="0",
                    transition="opacity 0.3s",
                    justify="center",
                    align="center",
                    padding="1.5em",
                    _hover={"opacity": "1"},
                ),
                position="relative",
                width="100%",
            ),
            rx.box(
                rx.heading(title, size="5", color="white", padding="1em"),
                width="100%",
                background="rgba(20, 20, 20, 0.6)",
            ),
            spacing="0",
        ),
        style=project_card_style,
    )

def projects() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Proyectos", size="9", color="white", margin_bottom="1.5em"),
            rx.grid(
                project_item(
                    "StackTON", 
                    "Arquitectura de microservicios escalable usando AWS Lambda y API Gateway.", 
                    "/project1.jpg", 
                    ["AWS", "Python", "Terraform"]
                ),
                project_item(
                    "DevOps Dashboard", 
                    "Monitorización en tiempo real de logs de servidor con integración de Discord.", 
                    "/project2.jpg", 
                    ["Linux", "Docker", "Reflex"]
                ),
                # agregar mas
                columns={"initial": "1", "sm": "2", "lg": "3"}, # 1 col en móvil, 2 en tablet, 3 en desktop
                spacing="6",
                width="100%",
            ),
            max_width="1600px",
            width="95%",
            padding_y="5em",
            align="center",
        ),
        id="proyectos",
        width="100%",
    )