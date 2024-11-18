        for boton in [FACIL, NORMAL, DIFICIL, SONIDO_ON, SONIDO_OFF, OPCIONES_ATRAS]:
            boton.changeColor(OPCIONES_POS_MOUSE)
            boton.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SONIDO_ON.checkForInput(OPCIONES_POS_MOUSE):
                    pygame.mixer.music.set_volume(0.5)
                if SONIDO_OFF.checkForInput(OPCIONES_POS_MOUSE):
                    pygame.mixer.music.set_volume(0)
                if OPCIONES_ATRAS.checkForInput(OPCIONES_POS_MOUSE):
                    menu_principal()
                if DIFICIL.checkForInput(OPCIONES_POS_MOUSE):
                    pass
                    # dificultadd.dificil()
                if FACIL.checkForInput(OPCIONES_POS_MOUSE):
                    pass
                    # dificultadd.facil()
        clock.tick(60)
        pygame.display.update()