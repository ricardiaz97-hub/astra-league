# Astra League — Modo Historia

## Premisa

El jugador es el miembro del escuadrón que queda separado cuando comienza la invasión. Debe sobrevivir, ayudar a los civiles y reunirse con su equipo. La historia tiene tres niveles compactos, pensados para el juego HTML y para reutilizar escenarios, enemigos y mecánicas existentes.

## Nivel 1 — La plaza: evacuar y reunirse

La invasión irrumpe en la plaza de la ciudad. El jugador está separado del escuadrón y encuentra civiles atrapados en medio del ataque.

**Objetivos:**

1. Abrir una ruta segura y evacuar a los civiles.
2. Defenderlos de las primeras oleadas de invasores regulares.
3. Cruzar calles bloqueadas usando salto, dash y carrera por muros.
4. Neutralizar a un invasor a distancia que amenaza la salida.
5. Seguir la señal de radio hasta reunirse con el escuadrón.

**Cierre:** El equipo se reúne y se entera de que un exmiembro dejó información importante en el Hotel Aurora. Esa información podría ayudarles a frenar la invasión.

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
- Las escenas se cuentan con diálogos de radio, textos cortos y objetivos en pantalla, sin cinemáticas largas. Las conversaciones usan retratos PNG cambiantes y un recuadro RPG persistente; ver `docs/dialogue-presentation.md`.
- Los enemigos y la pelea final deben reutilizar las mecánicas existentes siempre que sea posible.
