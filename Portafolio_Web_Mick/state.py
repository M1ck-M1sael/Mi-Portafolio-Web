import reflex as rx
from Portafolio_Web_Mick.languagues import TEXTOS
from typing import Dict

class State(rx.State):
    idioma: str = "es"

    def cambiar_idioma(self):
        self.idioma = "en" if self.idioma == "es" else "es"

    @rx.var
    def menu_items(self) -> list[list[str]]:
        return [[k, v] for k, v in TEXTOS[self.idioma]["nav_items"].items()]
    
    @rx.var
    def contenido(self) -> dict:
        return TEXTOS[self.idioma]