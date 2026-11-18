# Presentación de diálogos de Astra League

## Dirección

Contar conversaciones y momentos breves de historia con una interfaz 2D de RPG clásico. No depender de cinemáticas. La presentación debe sentirse directa y legible durante el juego.

## Composición de pantalla

- Mantener un único recuadro de diálogo fijo en la parte inferior de la pantalla.
- Usar `art/ui/dialogue-box-astra.png` como textura del panel. El centro crema queda libre para el texto; no rasterizar texto dentro de la textura.
- Mostrar el retrato PNG del personaje que habla justo encima o junto al panel, sin tapar el área de lectura.
- Al cambiar de hablante, reemplazar el retrato y actualizar el nombre y la línea dentro del mismo panel. El panel permanece en la misma posición entre turnos.
- Usar retratos PNG aprobados de `art/character-select-transparent/` cuando estén disponibles, conservando su transparencia y proporciones.

## Ritmo e interacción

- Presentar una línea corta por turno y revelar el texto progresivamente.
- Cuando la línea termine, mostrar el indicador de continuación. La acción de interacción avanza la conversación y cambia al siguiente hablante o línea.
- Mantener el nombre del hablante visible y separar claramente las líneas de cada personaje.
- Las conversaciones de radio pueden usar el mismo panel y el mismo ritmo; el retrato identifica a quien habla.
- Mantener objetivos, peligros y elementos interactivos importantes visibles mientras el panel aparece.

## Estilo visual

Seguir el diseño de Astra League: base crema y charcoal, contorno oscuro limpio, sombreado cel-shaded, acentos naranja y emblema de estrella de cuatro puntas. El panel debe priorizar contraste y lectura; evitar patrones bajo el texto.
