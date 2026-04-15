#Apartado para el fondo de la pagina

import reflex as rx
from Portafolio_Web_Mick.video_state import VideoState # Importa el estado en el que se fuerza la reproducción del video para evitar problemas de autoplay

def background():
    return rx.el.video(
        rx.el.source(src="/Stars.webm", type="video/webm"),
        rx.el.source(src="/Stars.mp4", type="video/mp4"),
        id="bg-video",
        poster="/Stars_Fallback.png",
        autoPlay=True,
        muted=True,
        loop=True,
        playsInline=True,
        preload="auto",
        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100vw",
            "height": "100vh",
            "objectFit": "cover",
            "zIndex": "-1",
            "pointerEvents": "none",
            "backgroundColor": "black",
        },
        on_mount=VideoState.force_video,
    )

# import reflex as rx

# def background():
#     return rx.html(
#         """
#         <video 
#             autoplay 
#             loop 
#             muted 
#             playsinline 
#             preload="auto"
#             style="
#                 position: fixed;
#                 top: 0;
#                 left: 0;
#                 width: 100vw;
#                 height: 100vh;
#                 z-index: -1;
#                 object-fit: cover;
#                 filter: brightness(0.6);
#                 background-color: black;
#                 transform: translateZ(0); /* Fuerza aceleración 3D en Opera */
#             ">
#             <source src="/Stars.mp4" type="video/mp4">
#         </video>
#         """
#     )