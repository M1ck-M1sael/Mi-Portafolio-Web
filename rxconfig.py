import reflex as rx

config = rx.Config(
    app_name="Portafolio_Web_Mick",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)