import reflex as rx

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es-MX'")


index_description = "Test de reflex en 2024"