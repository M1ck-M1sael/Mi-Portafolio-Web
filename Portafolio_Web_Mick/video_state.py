import reflex as rx

class VideoState(rx.State):
    def force_video(self):
        return rx.call_script("""
            const v = document.getElementById("bg-video");
            if (v && v.paused) {
                v.play().catch(error => {
                    console.log("Autoplay bloqueado, esperando interacción o error de carga:", error);
                });
            }
        """)