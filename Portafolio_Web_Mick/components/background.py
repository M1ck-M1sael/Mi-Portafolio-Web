#Apartado para el fondo de la pagina

import reflex as rx

def background():
    return rx.html(
        """
        <video 
            autoplay 
            loop 
            muted 
            playsinline 
            preload="auto"
            style="
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                z-index: -1;
                object-fit: cover;
                filter: brightness(0.6);
                background-color: black;
                transform: translateZ(0); /* Fuerza aceleración 3D en Opera */
            ">
            <source src="/Stars.mp4" type="video/mp4">
        </video>
        """
    )