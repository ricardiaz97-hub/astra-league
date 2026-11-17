# SUNBURNT — Guía para reemplazar y agregar personajes

> **Para cualquier chat o agente que trabaje en este repo:** lee esto junto con `ART_DIRECTION.md` antes de tocar personajes. Todo lo de abajo sale del código real de `index.html` (busca los nombres en negrita con Ctrl+F). Si algo no coincide con el código, manda el código.

## Cómo funcionan los personajes

- Cada personaje 3D tiene un **slot numérico** en la tabla **`VRMS`** (línea ~1715 de `index.html`): `{slot:{url:'chars/archivo.glb', h:alturaEnMetros}}`.
- **`loadVRM(slot)`** descarga el archivo. Acepta **`.glb` directo** o **`.json`** (un GLB en base64 dentro de `{"data":"..."}`). Se elige por la extensión de la URL.
- **`prepVRM`** detecta los huesos: si el GLB trae metadatos VRM (`VRMC_vrm`, modelos de VRoid) los usa; si no, busca huesos de **Mixamo** con el nombre `mixamorig:Hips`, `mixamorig:Spine`, `mixamorig:LeftArm`, etc., comparándolos por nombre exacto tal como aparecen en los nodos GLB (incluido el prefijo `mixamorig:`). Los modelos de Tripo con rig de Mixamo funcionan así. Cualquier otro nombre de huesos **no se mapea** y el personaje no se anima.
- Las animaciones (`anims/*.json`) rotan esos huesos, así que el modelo tiene que venir con esqueleto humanoide estándar.
- El material se reemplaza por cel shading con contorno (`MeshToonMaterial` + `OUTL`); solo se conserva la textura (`map`).
- Mientras el modelo 3D carga, el juego usa un muñeco de bloques de respaldo (línea ~1678, `buildChar`).

### Slots actuales
| Slot | Archivo | Personaje |
|---|---|---|
| 10 | `chars/milena.glb` | Milena (Tripo + Mixamo) |
| 11 | `chars/avatar-c.json` | Avatar C (VRoid) |
| 12 | `chars/ricardo-tripo.json` | Ricardo |
| 13 | `chars/connie.json` | Connie |
| 14 | `chars/tefa.glb` | Tefa |
| 15 | `chars/yesy.json` | Yesy |
| 16 | `chars/andres.json` | Andrés |
| 17 | `chars/isma.json` | Isma |
| 18 | `chars/rebecca.json` | Rebecca |
| 19 | `chars/armando.json` | Armando |
| 20 | `chars/diego.json` | Diego |
| 21 | `chars/mau.json` | Mau |
| 22 | `chars/fiorella.glb` | Fiorella (Tripo + Mixamo) |
| 31–34 | `chars/story/c_civ1..4.json` | Civiles del modo historia |

Cris, Gaby, Jenny, Julio y Speaker todavía **no tienen modelo propio**: en la lista `CH` apuntan a los slots 10 u 11 (usan uno parecido).

---

## A) Reemplazar el modelo de un personaje que ya existe

1. Consigue el **GLB** (Tripo, con rig de Mixamo; ver "Requisitos del modelo").
2. Ponlo en `chars/` con el nombre del personaje. Si usas el mismo nombre que el archivo actual, solo reemplázalo.
3. En `VRMS`, deja la entrada del slot apuntando al archivo nuevo. Ejemplo (así se hizo con Milena):
   `10:{url:'chars/milena.glb',h:1.69}`
4. Ajusta `h` (altura real en metros) si el personaje se ve más alto o más bajo que los demás. Referencias: Ricardo 1.84, Andrés 1.84, Isma 1.83, Armando y Diego y Mau 1.75, Connie y Rebecca 1.60, Tefa y Yesy 1.45.
5. Si ya no se usa el `.json` viejo, bórralo para no dejar archivos muertos.
6. No cambies nada más: la lista `CH`, los retratos y las animaciones se quedan como están.

## B) Agregar un personaje nuevo

1. **Modelo:** GLB en `chars/<nombre>.glb` (o `.json` base64 si lo necesitas para publicar).
2. **Slot nuevo en `VRMS`:** usa un número libre (23, 24…; el 22 ya es Fiorella y los 31–34 son del modo historia). Ejemplo:
   `23:{url:'chars/nuevo.glb',h:1.70}`
3. **Precarga:** en la línea que dice `for(const k of [10,11,12,...,21,22])loadVRM(k)...` (cerca de `window.__VRMS=VRMS`, línea ~3806) **agrega el número nuevo**. Si no, el modelo solo carga cuando se elige y tarda en aparecer.
4. **Lista de selección `CH`** (línea ~3688): agrega `['slug','NOMBRE',23]`. El primer valor es el nombre de archivo de sus retratos; el último es el slot. Si el personaje ya estaba en la lista usando otro slot, solo cambia ese número.
5. **Retratos** (el menú los pide por nombre, sin ellos sale un cuadro vacío):
   - `textures/chars/<slug>.webp` o `.png`: arte grande de la ficha. La zona `.cArt .frame` tiene aspecto 2:5; la figura debe llenar la altura sin cortar cabeza ni zapatos. Si un PNG tiene espacio transparente ancho a los lados, usa una clase CSS específica como `fitTall` con `object-fit: cover` solo después de comprobar que conserva manos y zapatos.
   - `textures/chars/<slug>-face.jpg` o `.png`: retrato de tarjeta cuadrado 1:1 y opaco, de busto, con cara y hombros ocupando el encuadre y un fondo que combine con los otros retratos. Si la referencia tiene pose en T, recorta los brazos extendidos fuera del encuadre. No uses la imagen transparente de cuerpo entero en la tarjeta: hace que la cara quede diminuta.
   - Usa la referencia frontal existente para conservar el diseño; recórtala a busto en lugar de inventar un nuevo retrato. En Fiorella, `fiorella-face.png` es un recorte cuadrado opaco de la vista frontal; `fiorella.png` sigue siendo el arte grande de cuerpo entero y puede llevar transparencia.
6. **Voz/género del cuerpo:** en `buildVRM`, la lista `fem:[10,13,14,15,18,22]` marca los slots femeninos actuales; agrega el slot nuevo si corresponde. Si el personaje nuevo es mujer, agrega su slot ahí.
7. **Respaldo de bloques** (línea ~1678, `if(look>=10){...}`): cuando el slot no ha cargado, el código elige un muñeco de bloques según el slot. Los slots que no estén en esa lista usan el muñeco por defecto; solo cámbialo si el personaje necesita uno distinto.
8. **Armas y poderes propios:** la dirección actual es que cada personaje tenga las suyas (Ricardo y sus compañeros, según cómo son en la vida real). Eso lo define Ricardo: **pídele el listado antes de inventar poderes.**

## Requisitos del modelo
- Esqueleto humanoide **Mixamo** (`mixamorig:Hips` … `mixamorig:RightToeBase`) o VRM con metadatos humanoides.
- Pose de reposo en T o A con el personaje **mirando a +Z**; el código lo gira 180° al construirlo.
- Peso razonable: los GLB de personajes pesan 1–3 MB. Los más pesados cargan lento en celular.
- Estilo: personajes anime con cel shading y contorno (ver `ART_DIRECTION.md`). No cambiar a otro estilo sin preguntar a Ricardo.

## Cómo comprobar que quedó bien
1. Servir la carpeta (`python -m http.server 8000`) o abrir la página de GitHub Pages.
2. Abrir la consola (F12): no debe haber líneas **rojas** que mencionen el archivo. Los avisos amarillos de "Tracking Prevention" del navegador son inofensivos.
3. Elegir el personaje en el menú y entrar a una partida: tiene que moverse (caminar, correr, atacar). Si queda en T-pose, los huesos no se mapearon: revisa los nombres del esqueleto.
4. Comprobar la altura frente a otro personaje.
5. En el menú, comprobar que la tarjeta enseña un retrato cercano y la ficha grande llena el marco; no dejar la figura entera reducida dentro de la tarjeta.

## Reglas al trabajar en el repo
- Cambia solo lo que se pidió y **abre un pull request**; Ricardo revisa y hace el merge.
- Si Ricardo ya editó un archivo a mano, pregúntale antes de reemplazarlo.
- Nada de assets que rompan el estilo de `ART_DIRECTION.md`.
