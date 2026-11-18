# Astra League — Modo Historia

## Premisa

El jugador es el miembro del escuadrón que queda separado cuando comienza la invasión. Debe sobrevivir, ayudar a los civiles y reunirse con su equipo. La historia tiene tres niveles compactos, pensados para el juego HTML y para reutilizar escenarios, enemigos y mecánicas existentes.

## Nivel 1 — Mercado de Olocuilta: evacuación y reencuentro

La invasión comienza cuando el jugador está separado del escuadrón. Entra al mercado por el frente, del lado de la catedral, y encuentra supervivientes atrapados entre los puestos. La zona de evacuación está atrás, junto a la rueda de la fortuna; allí espera el resto del escuadrón.

**Objetivos y momentos de juego:**

1. Entrar por la fachada con columnas, desde el lado de la catedral.
2. Rescatar a los supervivientes que los invasores regulares tienen rodeados en la parte frontal-media del mercado.
3. Aprender a saltar/vault sobre puestos caídos que bloquean el pasillo central.
4. Evitar o combatir invasores a distancia que cuelgan de las vigas y se arrastran por el techo.
5. Subir por la rampa intacta al segundo nivel. Cruzar una sección derrumbada de la galería con wall-run y wall-jump; esta brecha queda lejos de la rampa, hacia la parte trasera.
6. Guiar a los supervivientes por la planta baja hasta la salida trasera del mercado.
7. Cruzar una explanada amplia de aproximadamente **200 metros** hasta la línea de barricadas distante, mientras las hordas avanzan desde el mercado y las calles laterales. Puestos, carretas y jardineras aislados dan cobertura sin ocultar a los enemigos.
8. Reunirse con el escuadrón detrás de las barricadas. Un compañero avisa que la nave de evacuación llegará en cinco minutos.
9. Defender la línea y mantener despejada la zona mientras los civiles cruzan por una abertura protegida y se refugian detrás del equipo.
10. Resistir oleadas crecientes hasta que llegue la nave, embarcar al escuadrón y a los civiles, y partir viendo cómo arde el mercado.

**Cierre:** La nave despega desde la zona de la rueda de la fortuna y deja atrás el mercado en llamas. Ya reunido, el escuadrón se entera de que un exmiembro dejó información importante en el Hotel Aurora; esa información podría ayudarles a frenar la invasión.

**Guía de mapa:** `docs/campaign-level-1-layout.md` y `docs/olocuilta-market-map-guide.md`. La vista aérea con techo abierto solo muestra el interior; el techo real del mercado permanece intacto.

## Nivel 2 — Hotel Aurora: la emboscada

El escuadrón llega al hotel para recuperar la información del exmiembro. Al entrar en el patio, descubren que llegaron tarde: los invasores prepararon una emboscada.

**Objetivos:**

1. Buscar la información entre el patio, la piscina vacía y los balcones dañados.
2. Resistir varias oleadas de enemigos mientras el equipo registra el hotel.
3. Cambiar de posición y defender distintos puntos del patio cuando los invasores rodean al escuadrón.
4. Recuperar la información y abrir una ruta para escapar.

**Cierre:** El equipo consigue la información, pero queda claro que ya no basta con huir. Con lo aprendido, planean atacar la fuerza invasora.

## Nivel 3 — Contraataque: romper el asedio

El escuadrón inicia el contraataque a bordo de mechs voladores, atacando la nave enemiga. Tras la secuencia aérea, la misión continúa en combate directo.

**Fases:**

1. **Asalto aéreo:** pilotar o controlar los mechs voladores y atacar la nave enemiga, esquivando sus defensas.
2. **Aterrizaje:** llegar a la nave o a su zona de asalto y abrir paso para el escuadrón.
3. **Oleadas:** sobrevivir a grupos de invasores regulares, enemigos a distancia y brawlers.
4. **Jefe final:** enfrentarse al comandante o criatura que dirige el asalto, usando las debilidades reveladas por la información del Hotel Aurora.

**Final:** El escuadrón destruye o detiene el núcleo de la invasión y sale de la nave. La ciudad queda a salvo por ahora.

## Alcance para el juego HTML

- Solo tres niveles, con objetivos claros y transiciones breves.
- Nivel 1 y nivel 2 reutilizan piezas de la ciudad y del Hotel Aurora.
- La parte de mechs del nivel 3 puede ser una sección corta con controles simplificados; después vuelve al combate actual.
- Las escenas se cuentan con diálogos de radio, textos cortos y objetivos en pantalla, sin cinemáticas largas.
- Los enemigos y la pelea final deben reutilizar las mecánicas existentes siempre que sea posible.

## Presentación de diálogos y secciones de historia

- Contar las conversaciones y los momentos de historia con una presentación 2D de RPG clásico, sin depender de cinemáticas.
- Mantener un solo recuadro de diálogo fijo en la parte inferior de la pantalla. Usar la textura `art/ui/dialogue-box-astra.png`.
- Mostrar el retrato PNG del personaje que habla justo encima o al lado del recuadro. Cuando responde otro personaje, cambiar el retrato y el nombre del hablante; conservar el mismo recuadro y actualizar el texto.
- Revelar el texto en líneas cortas y mostrar el indicador de continuación cuando la línea esté completa. El jugador avanza a la siguiente línea con la acción de interacción.
- Usar los PNG aprobados de `art/character-select-transparent/` cuando estén disponibles, conservando su transparencia y diseño.
- Mantener el texto de alto contraste y con espacio suficiente para leerse durante el juego. Evitar paneles que cubran objetivos u objetos interactivos.

Guía completa: `docs/dialogue-presentation.md`.
