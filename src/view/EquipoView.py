        boton_equipo = self._mostrar_boton(
            None,
            (ANCHO * 0.54, ALTO * 0.55),
            "               ",
            get_fuente(60),
            NEGRO,
            NEGRO,
        )
                self._botones["boton_equipo"] = boton_equipo
                
        texto_equipo = get_fuente(60).render("  EQUIPO:", True, NEGRO)