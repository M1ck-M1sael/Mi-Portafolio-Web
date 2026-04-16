import reflex as rx

glass_style = {
    "background_color": "rgba(15, 15, 15, 0.45)", 
    "backdrop_filter": "blur(5px)",
    "border": "1px solid rgba(255, 255, 255, 0.2)",
    "border_radius": "40px",
    "padding": ["2em", "3em", "5em"],
    "width": "100%", 
    "max_width": "1800px", 
}
# diccionario de colores para cada habilidad
def skill_column(title: str, skills_data: list[dict]) -> rx.Component:
    return rx.vstack(
        rx.text(title, size="7", font_weight="bold", color="white", margin_bottom="1.2em"),
        rx.vstack(
            *[
                rx.badge(
                    skill["name"], 
                    variant="surface", 
                    color_scheme=skill["color"],
                    border_radius="full",
                    padding_x="1.8em",
                    padding_y="0.6em",
                    size="3",
                ) for skill in skills_data
            ],
            align="center",
            spacing="3",
        ),
        align="center",
        flex="1",
    )

def about() -> rx.Component:
    # define el color específico para cada habilidad
    habilidades_duras = [
        {"name": "AWS Cloud", "color": "orange"},
        {"name": "SysAdmin (Windows & Linux)", "color": "gray"},
        {"name": "Python & Reflex", "color": "blue"},
        {"name": "Cultura DevOps", "color": "purple"}
    ]
    habilidades_blandas = [
        {"name": "Comunicación Asertiva", "color": "teal"},
        {"name": "Liderazgo", "color": "indigo"},
        {"name": "Trabajo en Equipo", "color": "cyan"},
        {"name": "Resolución de Problemas", "color": "crimson"}
    ]
    habilidades_inutiles = [
        {"name": "Hablar como Gollum", "color": "grass"},
        {"name": "Silbar (Infravalorado)", "color": "yellow"},
        {"name": "Hacer Guturales", "color": "tomato"},
        {"name": "Concer todo el lore del W2M Crew", "color": "pink"},
        {"name": "Redundar", "color": "amber"},
        {"name": "Hablar como Gollum", "color": "grass"}
    ]

    return rx.center(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Sobre mí", 
                        size="9", 
                        color="white", 
                        margin_bottom="1em", 
                        width="100%", 
                        text_align="center"
                    ),
                    rx.flex(
                        rx.image(
                            src="/Sun.jpg",
                            width=["100%", "100%", "700px"], 
                            border_radius="25px", 
                            border="3px solid rgba(255, 255, 255, 0.2)",
                            object_fit="cover",
                        ),
                        rx.vstack(
                            rx.heading("¡Hola! Soy Misael", size="8", color="white"),
                            rx.text(
                                "Soy estudiante de Ingeniería en Sistemas Computacionales en el Tecnológico Nacional de México, y actualmente trabajo como Systems Administrator, en donde gestiono infraestructura, soporte y operación de sistemas en entornos productivos.",
                                size="5", color="white", text_align="justify"
                            ),
                            rx.text(
                                "También tengo mi propia Startup llamada StackTON, una empresa de soluciones IT. En ella soy CEO y Arquitecto Cloud con AWS.",
                                size="5", color="white", text_align="justify"
                            ),
                            rx.text(
                                "Me caracterizo por el aprendizaje constante y la diciplina técnica. Actualmente me encuentro en proceso de obtener la certificación AWS Cloud Practitioner, fortaleciendo mis conocimientos en servicios cloud, buenas prácticas y  arquitectura básica.",
                                size="5", color="white", text_align="justify"
                            ),
                            rx.text(
                                "Amante de los gatos, arañas y el exceso de café... soy el estereotipo de mi carrera, ¿verdad? ¡Caray!",
                                font_style="italic", color="#0070f3", size="5"
                            ),
                            align_items="start",
                            spacing="5",
                            flex="1",
                        ),
                        spacing="9",
                        flex_direction=["column", "column", "row"],
                        align="center",
                    ),
                ),
                style=glass_style,
            ),

            rx.box(height="2em"), 

            rx.box(
                rx.vstack(
                    rx.heading(
                        "Habilidades", 
                        size="9", 
                        color="white", 
                        margin_bottom="1.5em", 
                        width="100%", 
                        text_align="center"
                    ),
                    rx.flex(
                        # Llamada actualizada con las nuevas listas de datos
                        skill_column("Habilidades Duras", habilidades_duras),
                        rx.divider(orientation="vertical", height="22em", border_color="rgba(255,255,255,0.15)"),
                        skill_column("Habilidades Blandas", habilidades_blandas),
                        rx.divider(orientation="vertical", height="22em", border_color="rgba(255,255,255,0.15)"),
                        skill_column("Habilidades Inútiles", habilidades_inutiles),
                        
                        width="100%",
                        flex_direction=["column", "column", "row"],
                        spacing="8",
                        justify="between",
                        align="center",
                    ),
                ),
                style=glass_style,
            ),
            
            width="95%", 
            align="center",
        ),
        id="sobre_mi",
        padding_y="10em",
        width="100%",
    )