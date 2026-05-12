import reflex as rx
from Portafolio_Web_Mick.video_state import VideoState 

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
            "width": "100%",
            "height": "100%",
            "objectFit": "cover",
            "zIndex": "-1",
            "pointerEvents": "none",
            "backgroundColor": "black",
        },
        on_mount=VideoState.force_video,
    )
