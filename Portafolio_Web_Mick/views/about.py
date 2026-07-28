import reflex as rx
from ..state import State

glass_style = {
    "background_color": "rgba(15, 15, 15, 0.45)", 
    "backdrop_filter": "blur(5px)",
    "border": "1px solid rgba(255, 255, 255, 0.2)",
    "border_radius": "40px",
    "padding": ["2em", "3em", "5em"],
    "width": "100%", 
    "max_width": "1800px", 
}

def download_cv_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag="download", size=20),
                rx.text(State.contenido["btn_cv"], size="3", font_weight="bold"),
                align="center",
                spacing="2",
            ),
            padding="1.5em",
            height="auto",
            width="fit-content",
            background_color="rgba(0, 112, 243, 0.1)", 
            border="1px solid rgba(0, 112, 243, 0.4)",
            backdrop_filter="blur(5px)",
            color="white",
            border_radius="15px",
            _hover={
                "background_color": "rgba(0, 112, 243, 0.2)",
                "transform": "scale(1.05)",
                "border_color": "#0070f3",
                "box_shadow": "0 0 20px rgba(0, 112, 243, 0.3)",
            },
            transition="all 0.3s ease",
            cursor="pointer",
        ),
        href="/about/CV_Misael_Lopez_Franco.pdf", 
        is_external=True,
        custom_attrs={"download": "CV_Misael_Lopez_Franco.pdf"},
        style={"text_decoration": "none"} 
    )

def skill_column(title: rx.Var, skills_data: rx.Var) -> rx.Component:
    return rx.vstack(
        rx.text(title, size="7", font_weight="bold", color="white", margin_bottom="1.2em"),
        rx.vstack(
            rx.foreach(
                skills_data,
                lambda skill: rx.badge(
                    skill["name"], 
                    variant="surface", 
                    color_scheme=skill["color"],
                    border_radius="full",
                    padding_x="1.8em",
                    padding_y="0.6em",
                    size="3",
                )
            ),
            align="center",
            spacing="3",
        ),
        align="center",
        flex="1",
    )

def about() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.heading(
                        State.contenido["about_title"],
                        size="9", color="white", margin_bottom="1em", width="100%", text_align="center"
                    ),
                    rx.flex(
                        rx.image(
                            src="/about/Sun.jpg",
                            width=["100%", "100%", "700px"], 
                            border_radius="25px", 
                            border="3px solid rgba(255, 255, 255, 0.2)",
                            object_fit="cover",
                        ),
                        rx.vstack(
                            rx.heading(State.contenido["about_name"], size="8", color="white"),
                            rx.text(State.contenido["description_1"], size="5", color="white", text_align="justify"),
                            rx.text(State.contenido["description_2"], size="5", color="white", text_align="justify"),
                            rx.text(State.contenido["description_3"], size="5", color="white", text_align="justify"),
                            rx.text(
                                State.contenido["funfact"],
                                font_style="italic", color="#0070f3", size="5"
                            ),
                            rx.box(height="1.5em"),
                            download_cv_button(),
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
                        State.contenido["skills_title"],
                        size="9", color="white", margin_bottom="1.5em", width="100%", text_align="center"
                    ),
                    rx.flex(
                        skill_column(State.contenido["label_hard"], State.lista_duras),
                        rx.divider(orientation="vertical", height="22em", border_color="rgba(255,255,255,0.15)"),
                        
                        skill_column(State.contenido["label_soft"], State.lista_blandas),
                        rx.divider(orientation="vertical", height="22em", border_color="rgba(255,255,255,0.15)"),
                        
                        skill_column(State.contenido["label_useless"], State.lista_inutiles),
                        
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