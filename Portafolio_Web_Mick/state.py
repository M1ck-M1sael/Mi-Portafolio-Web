import reflex as rx
from Portafolio_Web_Mick.languagues import TEXTOS
from typing import Dict # Importa Dict

class State(rx.State):
    idioma: str = "es"

    def cambiar_idioma(self):
        self.idioma = "en" if self.idioma == "es" else "es"

@rx.var
def menu_items(self) -> list[list[str]]:
    # Convierte el diccionario {"sobre_mi": "Sobre mí"} en [["sobre_mi", "Sobre mí"]]
    return [[k, v] for k, v in TEXTOS[self.idioma]["nav_items"].items()]