# Astra League Touchdown

Shooter de arena anime 3 contra 3 que corre en el navegador. Duelo por equipos: gana quien llegue primero a 25 bajas o tenga más al acabar los cinco minutos.

- **Clases:** Impacto, Bastión, Sanador y Destello, cada una con su poder de ki.
- **Movimiento:** doble salto, carrera por los muros, salto desde el muro, deslizamiento, dash y plataformas de salto.
- **Efectos de luz:** resplandor, aberración cromática y prismas, con interruptor en el menú para equipos lentos.
- **Todo en un archivo:** `index.html` usa three.js (r128) desde cdnjs y las texturas de `textures/`.

## Cómo probarlo en tu computadora

Las texturas no cargan abriendo el archivo con doble clic. Abre una terminal en esta carpeta y ejecuta:

```
python -m http.server 8000
```

Luego entra a `http://localhost:8000`.

## Controles

WASD moverte · ratón apuntar · clic atacar · Espacio salto y doble salto · corre junto a un muro para correr por él · Shift dash · C deslizarte · E o clic derecho poder de clase · 1 2 3 o Q cambiar arma · R recargar · Esc o P pausa.

## Créditos de arte

Las texturas de `textures/` se generaron con Gemini a partir de la dirección de arte de Ricardo.
