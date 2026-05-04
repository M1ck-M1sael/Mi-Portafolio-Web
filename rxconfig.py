import reflex as rx
import os

api_url = os.getenv("API_URL", "http://localhost:8000")

config = rx.Config(
    app_name="Portafolio_Web_Mick",
    api_url=api_url, 
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)