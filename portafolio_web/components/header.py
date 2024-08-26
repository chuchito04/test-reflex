import reflex as rx

def header() -> rx.Component:
    return rx.flex(
        # Contenedor para el botón de modo de color, alineado a la izquierda
        rx.box(
            rx.color_mode.button(),
            rx.icon("align_justify", class_name="md:hidden"),
            class_name="flex-shrink-0 invert",  # No permite que el botón se reduzca
            #border="1px solid white"
        ),
        
        # Contenedor para el icono y enlaces, centrado
        rx.box(
            rx.flex(
                
                rx.link("Inicio", href="#", class_name="px-4 py-2 text-current invert"),
                rx.link("Servicios", href="#", class_name="px-4 py-2 text-current invert"),
                rx.link("Contacto", href="#", class_name="px-4 py-2 text-current invert"),
                class_name="space-x-4 items-center",  # Alinea verticalmente en el centro
            ),
            class_name="flex-1 hidden md:flex justify-end",  # Ocupa el espacio disponible y centra los elementos
            #border="1px solid blue"
        ),
        
        class_name="absolute p-6 top-0 w-screen flex items-center bg-current",
        #border="1px solid red",
    )
