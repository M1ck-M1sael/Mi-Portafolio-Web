import reflex as rx

config = rx.Config(
    app_name="Portafolio_Web_Mick",
    api_url="http://13.221.97.68:8000", 
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)