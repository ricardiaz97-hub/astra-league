# Astra League Touchdown

Shooter de arena anime 3 contra 3 que corre en el navegador. Duelo por equipos: gana quien llegue primero a 25 bajas o tenga más al acabar los cinco minutos.

- **Clases:** Impacto, Bastión, Sanador y Destello, cada una con su poder de ki.
- **Movimiento:** doble salto, carrera por los muros, salto desde el muro, deslizamiento, dash y plataformas de salto.
- **Combate de poder:** fijar rival, combo de tres golpes de hoja que lanza al rival contra los muros, parada, aparecer detrás del rival, caída en picada con onda de choque, carga de ki y rayo definitivo con choque de rayos.
- **Efectos de luz:** resplandor, aberración cromática y prismas, con interruptor en el menú para equipos lentos.
- **Todo en un archivo:** `index.html` usa three.js (r128) desde cdnjs y las texturas de `textures/`.

## Personajes y animaciones

- `chars/`: personajes hechos en VRoid Studio, aligerados para el navegador (sin gestos faciales y con texturas reducidas). Los anima el código moviendo los huesos humanoides del VRM.
- `anims/`: animaciones de Mixamo convertidas a JSON (rotación de cada hueso respecto a la pose de reposo). `sword-strafe.json` se usa al rodear a un rival fijado con la hoja.

## Cómo probarlo en tu computadora

Las texturas no cargan abriendo el archivo con doble clic. Abre una terminal en esta carpeta y ejecuta:

```
python -m http.server 8000
```

Luego entra a `http://localhost:8000`.

## Controles

WASD moverte · ratón apuntar · clic atacar · Espacio salto, doble salto y mantener para planear · corre junto a un muro para correr por él · Shift dash (sin moverte y con rival fijado, apareces detrás) · C deslizarte, o caída en picada en el aire · Tab o rueda del ratón fijar rival · F parar · V mantener para cargar ki · X rayo definitivo (en un choque, haz clic sin parar) · E o clic derecho poder de clase · 1 2 3 o Q cambiar arma · R recargar · Esc o P pausa.

## Créditos de arte

Las texturas de `textures/` se generaron con Gemini a partir de la dirección de arte de Ricardo.

`chars/avatar-c.glb` viene de AvatarSample_C de pixiv VRoid Project (permite modificar y redistribuir). `chars/milena.glb` es un personaje de Ricardo Vega. La animación de rodeo con espada viene de Mixamo.
