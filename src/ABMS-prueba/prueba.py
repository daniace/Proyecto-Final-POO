import pygame
from pgu import gui

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sistema con Pestañas")

# Creación de la aplicación de GUI
app = gui.App()

# Definición de la ventana principal
main_window = gui.Container(width=640, height=480)

# Definición de las pestañas
tab_container = gui.Table(width=640, height=30)
content_container = gui.Container(width=640, height=450)

# Creación de contenedores para cada pestaña
tab1_content = gui.Container(width=640, height=450)
tab2_content = gui.Container(width=640, height=450)
tab3_content = gui.Container(width=640, height=450)

# Añadir contenido a cada pestaña
tab1_content.add(gui.Label("Contenido de la Pestaña 1"), 10, 10)
tab2_content.add(gui.Label("Contenido de la Pestaña 2"), 10, 10)
tab3_content.add(gui.Label("Contenido de la Pestaña 3"), 10, 10)


# Funciones para cambiar de pestaña
def show_tab1(btn):
    content_container.remove(tab2_content)
    content_container.remove(tab3_content)
    content_container.add(tab1_content, 0, 0)


def show_tab2(btn):
    content_container.remove(tab1_content)
    content_container.remove(tab3_content)
    content_container.add(tab2_content, 0, 0)


def show_tab3(btn):
    content_container.remove(tab1_content)
    content_container.remove(tab2_content)
    content_container.add(tab3_content, 0, 0)


# Añadir botones de pestañas
btn_tab1 = gui.Button("Pestaña 1")
btn_tab2 = gui.Button("Pestaña 2")
btn_tab3 = gui.Button("Pestaña 3")

btn_tab1.connect(gui.CLICK, show_tab1, btn_tab1)
btn_tab2.connect(gui.CLICK, show_tab2, btn_tab2)
btn_tab3.connect(gui.CLICK, show_tab3, btn_tab3)

tab_container.tr()
tab_container.td(btn_tab1)
tab_container.td(btn_tab2)
tab_container.td(btn_tab3)

# Añadir contenedores de pestañas a la ventana principal
main_window.add(tab_container, 0, 0)
main_window.add(content_container, 0, 30)

# Mostrar la primera pestaña por defecto
show_tab1(btn_tab1)

# Configuración de la aplicación
app.init(main_window)

# Bucle principal de Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        app.event(event)

    screen.fill((255, 255, 255))
    app.paint(screen)
    pygame.display.flip()

pygame.quit()
