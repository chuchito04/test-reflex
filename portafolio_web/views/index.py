import reflex as rx
from portafolio_web.routes import Routes, Titles
import portafolio_web.utils as utils
from portafolio_web.components.header import header

@rx.page(
    title=Titles.INDEX.value,
    description=utils.index_description,
    )
def index() -> rx.Component:
   
  return rx.container(
      utils.lang(),
      rx.box(
        header(),
        rx.box(
            rx.text("Probando reflex"),
            rx.text("con tailwind"),
            class_name="text-xl md:text-5xl font-bold text-center"
        ),
      class_name="flex items-center justify-center h-[90vh]",
      )
  )