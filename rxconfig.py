import reflex as rx

config = rx.Config(
    app_name="Portafolio_Web_Mick",
    api_url="http://54.145.241.44:8000", 
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)