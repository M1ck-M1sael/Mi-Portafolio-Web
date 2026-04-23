import reflex as rx
from Portafolio_Web_Mick.views.about import download_cv_button

contact_glass_style = {
    "background_color": "rgba(15, 15, 15, 0.45)", 
    "backdrop_filter": "blur(5px)",
    "border": "1px solid rgba(255, 255, 255, 0.2)",
    "border_radius": "40px",
    "padding": ["2em", "3em", "5em"],
    "width": "100%", 
    "max_width": "1800px", 
}

def contact_item(icon_tag: str, title: str, subtitle: str, url: str, color: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon_tag, size=30, color=color),
            rx.vstack(
                rx.text(title, size="4", font_weight="bold", color="white"),
                rx.text(subtitle, size="2", color="rgba(255,255,255,0.6)"),
                spacing="0",
                align_items="start",
            ),
            padding="1.5em",
            border_radius="20px",
            border=f"1px solid rgba(255, 255, 255, 0.1)",
            background="rgba(255, 255, 255, 0.03)",
            _hover={
                "background": "rgba(255, 255, 255, 0.08)",
                "border_color": color,
                "transform": "scale(1.02)",
            },
            transition="all 0.2s ease",
            width="100%",
        ),
        href=url,
        is_external=True,
        text_decoration="none",
        width="100%",
    )

def contact() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading("Contacto", size="9", color="white", margin_bottom="1em", text_align="center", width="100%"),
                
                rx.flex(
                    # Lado Izquierdo: Texto Invitación
                    rx.vstack(
                        rx.heading("¿Tienes un proyecto en mente?", size="8", color="white"),
                        rx.text(
                            "Actualmente estoy abierto a nuevas oportunidades, colaboraciones en proyectos de infraestructura Cloud o consultorías técnicas a través de StackTON.",
                            size="5", color="rgba(255,255,255,0.8)", text_align="justify"
                        ),
                        rx.text(
                            "Si buscas un perfil con disciplina técnica, amor por la automatización y que sepa trabajar bajo presión (y con mucho café), ¡hablemos!",
                            size="5", color="rgba(255,255,255,0.8)", text_align="justify"
                        ),
                        rx.box(height="2em"),
                        # Aquí reciclamos tu botón de CV que ya funciona
                        rx.text("¿Necesitas mi perfil detallado?", size="3", color="white", margin_bottom="0.5em"),
                        download_cv_button(),
                        align_items="start",
                        spacing="4",
                        flex="1",
                    ),

                    # Lado Derecho: Botones de Acción
                    rx.vstack(
                        contact_item(
                            "mail", "Gmail", "mickmisa3l@gmail.com", 
                            "mailto:mickmisa3l@gmail.com", "#EA4335"
                        ),
                        contact_item(
                            "linkedin", "LinkedIn", "Conectemos profesionalmente", 
                            "https://www.linkedin.com/in/misael-lópez-franco-409566209", "#0077B5"
                        ),
                        contact_item(
                            "github", "GitHub", "Revisa mi código y despliegues", 
                            "https://github.com/M1ck-M1sael", "#FFFFFF"
                        ),
                        spacing="4",
                        width=["100%", "100%", "400px"],
                    ),
                    
                    spacing="9",
                    flex_direction=["column", "column", "row"],
                    align="center",
                    width="100%",
                ),
            ),
            style=contact_glass_style,
        ),
        id="contacto",
        padding_y="10em",
        width="100%",
    )