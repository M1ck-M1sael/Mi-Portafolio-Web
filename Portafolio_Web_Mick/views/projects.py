import reflex as rx
from ..state import State

project_card_style = {
    "background_color": "rgba(15, 15, 15, 0.45)",
    "backdrop_filter": "blur(5px)",
    "border": "1px solid rgba(255, 255, 255, 0.1)",
    "border_radius": "20px",
    "overflow": "hidden",
    "transition": "transform 0.3s ease, border-color 0.3s ease",
    "_hover": {
        "transform": "translateY(-10px)",
        "border_color": "#0070f3",
    }
}

def project_item(title: str, description: str, image: str, tags: list, repo_url: str = "", docs_url: str = "") -> rx.Component:
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

                    rx.hstack(

                        rx.cond(
                            docs_url != "",
                            rx.link(
                                rx.icon(tag="file-text", size=20),
                                href=docs_url,
                                is_external=True,
                                color="white",
                                _hover={"color": "#0070f3", "transform": "scale(1.2)"},
                                transition="all 0.2s",
                            )
                        ),

                        rx.cond(
                            repo_url != "",
                            rx.link(
                                rx.icon(tag="github", size=20),
                                href=repo_url,
                                is_external=True,
                                color="white",
                                _hover={"color": "#0070f3", "transform": "scale(1.2)"},
                                transition="all 0.2s",
                            )
                        ),
                        spacing="4",
                        position="absolute",
                        bottom="1.2em",
                        right="1.2em",
                    ),

                    position="absolute",
                    top="0",
                    left="0",
                    width="100%",
                    height="100%",
                    background="rgba(0, 0, 0, 0.85)",
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
                rx.heading(title, size="5", color="white", padding="1em", text_align="center"),
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
            rx.heading(
                State.contenido["projects_title"], 
                size="9", color="white", margin_bottom="1.5em", text_align="center"
            ),
            rx.grid(
                project_item(
                    State.contenido["project_1"],
                    State.contenido["project_1_description"],
                    "/projects/portafolio_web/portafolio_web_mick.webp",
                    ["AWS", "Python", "AWS"],
                    repo_url="https://github.com/M1ck-M1sael/Mi-Portafolio-Web",
                    docs_url="/documentacion"
                ),
                project_item(
                    State.contenido["project_2"],
                    State.contenido["project_2_description"],
                    "/projects/metodos_numericos/Metod_Py.webp", 
                    ["Python", "GitHub", "Mathematics"],
                    repo_url="https://github.com/M1ck-M1sael/Metodos-Numericos-Scripts-Python"
                ),

                project_item(
                    State.contenido["project_3"],
                    State.contenido["project_3_description"],
                    "/projects/stackton/StackTON_Projects.jpg ",
                    ["Reflex", "AWS", "Python"],
                    repo_url="",
                    docs_url=""
                ),
                project_item(
                    State.contenido["project_4"],
                    State.contenido["project_4_description"],
                    "/projects/OnProcess_Projects.jpg", 
                    ["Matarile", "Rile", "Ro"],
                    repo_url="https://www.youtube.com/watch?v=-jHYYzS0U-c"
                ),
                project_item(
                    State.contenido["project_5"],
                    State.contenido["project_5_description"],
                    "/projects/OnProcess_Projects.jpg", 
                    ["Matarile", "Rile", "Ro"],
                    repo_url="https://www.youtube.com/watch?v=qwfhifRyhok"
                ),
                project_item(
                    State.contenido["project_6"],
                    State.contenido["project_6_description"],
                    "/projects/OnProcess_Projects.jpg", 
                    ["Matarile", "Rile", "Ro"],
                    repo_url="https://www.youtube.com/watch?v=-jHYYzS0U-c"
                ),
                columns={"initial": "1", "sm": "2", "lg": "3"},
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