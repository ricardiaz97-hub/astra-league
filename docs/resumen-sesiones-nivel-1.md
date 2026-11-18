# Astra League: resumen de trabajo, Nivel 1 (Mercado de Olocuilta)

Fecha: 2026-11-18 · Rama: `codex/market-map-level`

> **Estado:** nada está commiteado. Nadie ha jugado el nivel completo de principio a fin.
> Los cambios están en la sección `MODO HISTORIA` de `index.html` y en `story/nivel1.json`.
> Detalle del diseño en `docs/campaign-level-1-layout.md`.

---

## Sesión anterior

### Repo
- La rama `codex/market-map-level` avanzó (fast-forward) hasta `origin/main`.
- Los cambios viejos quedaron guardados en `stash@{0}`.
- Se agregó `.claude/launch.json` para servir el juego en `localhost:8000`.

### Diálogos
- El marco es `art/ui/dialogue-box-astra.png` y el texto aparece letra por letra.
- El retrato de cuerpo entero va detrás del marco: el marco tapa la parte baja y se ve del pecho para arriba, como en un RPG clásico.

### Flujo del Nivel 1
El modo historia ahora usa el mapa 4.

1. Intro frente a la catedral.
2. Rescatar a los civiles.
3. Saltar los puestos volcados.
4. Derribar a los rastreros de las vigas.
5. Subir la rampa en U construida a mano y recorrer la galería por tres lados del mercado.
6. Correr por el muro y saltar el tramo derrumbado de la galería.
7. Jalar la palanca para abrir la cortina.
8. Cruzar la plaza, de unos 200 m.
9. Reunirse con el escuadrón en la barricada y aguantar 3:00.
10. Aterriza la nave y todos suben.
11. Despegue: el mercado arde y termina el nivel.

Todos los diálogos los escribió la IA, así que conviene revisarlos.

### Escenario
- El piso interior del mercado se subió 0.9 m para quedar al nivel del porche. Hay escalones en la entrada, en la puerta trasera y en el portón este.
- Se usan tus modelos: puestos, rueda de la fortuna, autos, pod, nave, civiles (13, con rig Mixamo), árboles, molinos y bardas.
- Se usan tus texturas en pisos, muros y galería.
- Los puestos no se estiran. En la plaza hay muchos, de tamaños distintos.
- Ciudad en capas, colinas, skybox y niebla de atardecer, para que no se vea el borde del mapa.

### Luz y ambiente
- La sombra sigue al jugador. El sol está bajo y es cálido, con más contraste.
- El techo oscurece el interior. Hay polvo, rayos de luz, columnas de humo, brasas y explosiones lejanas.
- Los objetos llevan contorno de tinta, estilo cel shading.

### Cámara
- La intro sobrevuela la zona y corta al ver al escuadrón y la nave. Los diálogos llevan franjas negras. Todo se puede saltar.
- Al manejar, la cámara se aleja y el personaje queda oculto dentro del vehículo.
- La ulti ya no aleja la cámara, tampoco en multijugador.
- En el final, la cámara queda del lado lejano de la nave para que el casco tape a los que suben.

### Combate
- Los enemigos son más lentos, pegan menos y se empujan entre sí para no amontonarse.
- El escuadrón tiene 7 miembros con la IA de los bots de multijugador: se mueven, disparan, se cubren, pelean cuerpo a cuerpo y usan habilidades. Su daño se bajó al 30%.
- Hay 6 vehículos manejables. Se sube y se baja con `G`, y atropellan enemigos. El pod flota.

### Carga y rendimiento
- La pantalla de carga tapa el juego hasta que cargan los recursos, con un máximo de 40 s.
- Triángulos: de 12.5 M a 4.4 M. Lo lejano usa modelos low-poly y el contorno de tinta solo se aplica de cerca.

### Otra sesión en paralelo
- Se hicieron efectos de Ki dibujados a mano y se mejoró la sensación de movimiento.
- **Pendiente:** Ricardo peleando a mano limpia.

---

## Esta sesión: arreglos de geometría y colisión

Todos los arreglos están en `index.html`, dentro del bloque del Nivel 1.

| # | Problema | Arreglo |
|---|----------|---------|
| 1 | El último tramo de la rampa en U pasaba debajo de un descanso con colisión pero sin piso visible. Por unos 5.6 m el jugador flotaba hasta 0.55 m sobre la rampa y luego subía de golpe a un piso invisible. | La rampa ahora termina en x=33, donde empieza el descanso, que ya tiene piso visible. Los puntos de la rampa se comparten en `RAMP_P`. |
| 2 | Había un hueco sin barandal de 3.3 × 1.4 m entre la galería este y la rampa: se podía caer unos 5.5 m. | Se agregaron barandal y muro invisible. |
| 3 | Desde el piso se podía trepar el tramo bajo de la cortina, junto al muro este, y bajar del otro lado durante la fase de la rampa. Ahí la palanca no responde, así que la historia se trababa. | Ese tramo queda bloqueado hasta que empieza la fase de la carrera por el muro (`STORY.shutCap`). Además, llegar detrás de la cortina en la fase de la rampa ahora también avanza la historia. |
| 4 | La parte de arriba de la cortina central no tenía bloqueo, a diferencia de las laterales. | Se bloqueó igual que las laterales. |
| 5 | La losa caída de la galería y el trozo bajo no tenían colisión: el jugador los atravesaba. | Se les puso colisión escalonada que sigue la pendiente de la losa. |
| 6 | Había un hueco de 0.5 m entre el escalón del portón este y el piso interior. | Se cerró. |
| 7 | La colisión del porche estaba duplicada. | Se quitó la duplicada. |

### Verificación
- El script se analiza sin errores de sintaxis.
- La pendiente de los tramos de la rampa es de 11.6°, 9.3° y 11.5°. El escalón máximo es de 0.35 m (el límite para subir sin saltar es 0.75 m) y la unión con el descanso es de 0.08 m.
- El juego carga en `http://localhost:8000` sin errores en la consola.
- **Falta jugarlo:** probar la rampa, el descanso, las cortinas y la galería derrumbada.

### Pendiente o a decidir
- Los escombros pequeños, a la altura del tobillo, siguen sin colisión. Ponérsela haría que caminar sobre ellos se sienta brusco.
- Durante la fase de la carrera por el muro, la losa caída permite subir a la repisa por otro camino. Si la carrera por el muro debe ser obligatoria, hay que ajustarlo.
- Revisar las texturas y la guía visual del jugador mientras se juega.
- Commitear los cambios.
