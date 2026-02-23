#Esta sección  es para las rutas de los links y su lógica

import reflex as rx

SOCIAL_LINKS = {
    "music": "https://open.spotify.com/user/udsaws99krcqg1hxz618s3cgj?si=5249cf50f38842f4",
    "linkedin": "https://www.linkedin.com/in/misael-lópez-franco-409566209",
    "github": "https://github.com/M1ck-M1sael",
    "twitter": "https://x.com/MickMLF",
}

def social_button(icon_tag: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon_tag,
            size=25,
            color="white",
            _hover={"color": "#0070f3", "transform": "scale(1.1)", "transition": "0.3s"},
        ),
        href=url,
        is_external=True,
    )