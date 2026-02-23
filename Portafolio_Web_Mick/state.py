# Apartado para el cambio de idioma de la pagina

import reflex as rx

class State(rx.State):
    idioma_ingles: bool = False

    def cambiar_idioma(self):
        self.idioma_ingles = not self.idioma_ingles