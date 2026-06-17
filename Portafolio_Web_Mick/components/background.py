import reflex as rx

def background():
    return rx.box(
        rx.el.video(
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
                "width": "100%",
                "height": "100%",
                "objectFit": "cover",
                "zIndex": "-1",
                "pointerEvents": "none",
                "backgroundColor": "black",
            },
        ),
        rx.script("""
            setTimeout(() => {
                const v = document.getElementById("bg-video");
                if (v && v.paused) {
                    v.play().catch(error => console.log("Autoplay bloqueado:", error));
                }
            }, 500); // Un pequeño retraso para asegurar que el DOM cargó
        """)
    )