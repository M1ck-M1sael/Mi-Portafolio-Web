import reflex as rx
from Portafolio_Web_Mick.languagues import TEXTOS
from typing import Dict

class State(rx.State):
    idioma: str = "es"
    sidebar_open: bool = False 

    def set_sidebar_open(self, open: bool):
        self.sidebar_open = open

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def cambiar_idioma(self):
        self.idioma = "en" if self.idioma == "es" else "es"

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @rx.var
    def menu_items(self) -> list[list[str]]:
        return [[k, v] for k, v in TEXTOS[self.idioma]["nav_items"].items()]
    
    @rx.var
    def contenido(self) -> dict:
        return TEXTOS[self.idioma]
    
    @rx.var
    def lista_duras(self) -> list[dict[str, str]]:
        return self.contenido["habilidades_duras"]

    @rx.var
    def lista_blandas(self) -> list[dict[str, str]]:
        return self.contenido["habilidades_blandas"]

    @rx.var
    def lista_inutiles(self) -> list[dict[str, str]]:
        return self.contenido["habilidades_inutiles"]
    
