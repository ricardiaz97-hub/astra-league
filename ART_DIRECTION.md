# SUNBURNT — Dirección de arte y biblioteca de assets

> **Para cualquier chat o agente que trabaje en este repo:** lee esto antes de crear o cambiar mapas, props o armas.
> Los assets de `assets-lowpoly/` son la biblioteca oficial del juego. **Úsalos primero** y no los olvides ni los reemplaces por otros estilos sin preguntarle a Ricardo.

## Estilo: Low Poly Anime Cel Shaded + VFX

1. **Escenarios, props y armas en low poly:** formas simples, colores planos o una textura de paleta. Nada de texturas fotográficas ni modelos realistas.
2. **Personajes anime** (el roster de Tripo en `chars/`) con cel shading y contorno. Son la identidad del juego: no se cambian por soldados anime genéricos.
3. **El espectáculo lo dan los VFX:** ki, auras, rayos, explosiones e impactos brillantes y saturados (módulo KFX en `index.html`), que contrastan con un mundo sencillo.
4. **Paleta:** naranja cálido, crema y carbón como base; cada personaje con su color de acento (Connie morado, Diego verde, Gaby naranja, Julio gris, Jenny amarillo, Rebecca rosa…).

Regla: si un asset no cumple estos cuatro puntos, no entra al juego. **Un solo estilo por todo el juego**, sin mezclar low poly con realista.

### Estado de la migración
- Lo que todavía es realista y hay que pasar a low poly: CENTRO (edificios de Hong Kong `props/hk.json`, supermercado `props/mk.json`, kit Downtown `props/city.json`), HOTEL, ATARDECER, AZOTEA y las armas (Sci-Fi Essentials, M338, `gun_smg`, `gun_shotgun`).
- Orden acordado: (1) mapas de campaña en low poly desde cero, (2) armas low poly cuando Ricardo encuentre un pack, (3) mapas multijugador uno por ronda, conservando trazado y colisiones.
- No cambian: los personajes, los mobs de Tripo y los VFX.

## Biblioteca `assets-lowpoly/`

Solo se guardaron los archivos glTF/GLB (los FBX, OBJ y DAE de los zips originales se descartaron). Los GLB traen las texturas incrustadas; los `.gltf` de KayKit usan el `.bin` y el atlas `.png` que están en la misma carpeta.

| Carpeta | Pack | Para qué |
|---|---|---|
| `postapoc/` | [AR] Post-Apocalyptic Starter Pack | Paredes rotas, barricadas de madera y púas, autos, postes: ciudad invadida, barricadas de la feria |
| `modular-roads/` | FREE Modular Roads – Base | Calles, cruces, curvas, semáforos, conos, árboles: la ciudad y los alrededores del mercado |
| `kaykit-city/` | KayKit City Builder Bits | Edificios A–H, autos (taxi, policía), bancas, basureros, hidrantes: manzanas de la ciudad |
| `kaykit-restaurant/` | KayKit Restaurant Bits | Cajas de verduras y carne, mesas, sillas, cocina: puestos del Mercado de Olocuilta |
| `kaykit-furniture/` | KayKit Furniture Bits | Muebles, camas, libreros, lámparas: interiores (Hotel Aurora, casas) |
| `kaykit-resources/` | KayKit Resource Bits | Barriles de combustible, lingotes, madera, piedras: utilería y botín |
| `kaykit-space-base/` | KayKit Space Base Bits | Módulos, módulos de techo, carga, plataformas de aterrizaje, módulos de aterrizaje: **la nave alienígena** (Nivel 4) y la nave de evacuación |
| `pharmacy/` | FREE Pharmacy | Botiquines, frascos, estantes: farmacia y botín de vida |
| `gas-station/` | FREE Gas Station | Bidones, tarimas, barreras: gasolinera y calles |
| `into-the-wild/` | FREE Into The Wild | Arbustos, estacas, sacos de dormir: campamentos de refugiados |
| `interiors/` | FREE Interiors | Librero, monitor: interiores |

**Licencias:** los packs KayKit son CC0. Los demás traen su propia licencia en el zip original; revísala antes de publicar el juego fuera de Claude.

### Uso por nivel (campaña: ver el handoff de historia)
- **Nivel 1 — Mercado de Olocuilta:** restaurant (puestos y cajas), modular-roads + kaykit-city (calles y catedral alrededor), postapoc (destrucción y barricadas de la feria), resources (barriles), space-base (nave de evacuación, provisional).
- **Nivel 2 — Alcantarillas:** postapoc (paredes de metal y concreto), resources, gas-station. Puede faltar un kit de túneles y tuberías: pedírselo a Ricardo.
- **Nivel 3 — Hotel Aurora:** furniture, interiors, restaurant (cocina del hotel), pharmacy.
- **Nivel 4 — Contraataque / nave alienígena:** space-base como base de la nave enemiga, con VFX morados.

### Cómo cargarlos en el juego
- Fusiona las piezas de un mapa en una sola librería, como `/tmp/w/city.mjs` (gltf-transform: merge, simplify, textureCompress) → `props/<nombre>.json` (glb-base64), y luego `propLib('<nombre>')`.
- **Los grupos que cargan de forma asíncrona se agregan a `mapGroup`, nunca a `scene`**: si no, quedan pegados en otros mapas (ese error pasó con HOTEL).
- `propLib` respeta `side` (doble cara) y convierte a materiales toon; el contorno lo da `shadeAll`.

## Inventario de modelos

```
gas-station: jerry_can_with_nozzle pallet_cluster_1 road_barrier 
interiors: Bookshelf_1 Monitor_1 
into-the-wild: bush_1 sharpened_stick sleeping_bag 
kaykit-city: base bench box_A box_B building_A building_A_withoutBase building_B building_B_withoutBase building_C building_C_withoutBase building_D building_D_withoutBase building_E building_E_withoutBase building_F building_F_withoutBase building_G building_G_withoutBase building_H building_H_withoutBase bush car_hatchback car_police car_sedan car_stationwagon car_taxi dumpster firehydrant road_corner road_corner_curved road_junction road_straight road_straight_crossing road_tsplit streetlight trafficlight_A trafficlight_B trafficlight_C trash_A trash_B watertower 
kaykit-furniture: armchair armchair_pillows bed_double_A bed_double_B bed_single_A bed_single_B book_set book_single cabinet_medium cabinet_medium_decorated cabinet_small cabinet_small_decorated cactus_medium_A cactus_medium_B cactus_small_A cactus_small_B chair_A chair_A_wood chair_B chair_B_wood chair_C chair_stool chair_stool_wood couch couch_pillows lamp_standing lamp_table pictureframe_large_A pictureframe_large_B pictureframe_medium pictureframe_small_A pictureframe_small_B pictureframe_small_C pictureframe_standing_A pictureframe_standing_B pillow_A pillow_B rug_oval_A rug_oval_B rug_rectangle_A rug_rectangle_B rug_rectangle_stripes_A rug_rectangle_stripes_B shelf_A_big shelf_A_small shelf_B_large shelf_B_large_decorated shelf_B_small shelf_B_small_decorated table_low table_medium table_medium_long table_small 
kaykit-resources: Copper_Bar Copper_Bars Copper_Bars_Stack_Large Copper_Bars_Stack_Medium Copper_Bars_Stack_Small Copper_Nugget_Large Copper_Nugget_Medium Copper_Nugget_Small Copper_Nuggets Fuel_A_Barrel Fuel_A_Barrel_Dirty Fuel_A_Barrels Fuel_A_Jerrycan Fuel_B_Barrel Fuel_B_Barrel_Dirty Fuel_B_Barrels Fuel_B_Jerrycan Fuel_C_Barrel Fuel_C_Barrel_Dirty Fuel_C_Barrels Fuel_C_Jerrycan Gold_Bar Gold_Bars Gold_Bars_Stack_Large Gold_Bars_Stack_Medium Gold_Bars_Stack_Small Gold_Nugget_Large Gold_Nugget_Medium Gold_Nugget_Small Gold_Nuggets Iron_Bar Iron_Bars Iron_Bars_Stack_Large Iron_Bars_Stack_Medium Iron_Bars_Stack_Small Iron_Nugget_Large Iron_Nugget_Medium Iron_Nugget_Small Iron_Nuggets Pallet_Wood Pallet_Wood_Covered_A Pallet_Wood_Covered_B Parts_Cog Parts_Pile_Large Parts_Pile_Medium Parts_Pile_Small Silver_Bar Silver_Bars Silver_Bars_Stack_Large Silver_Bars_Stack_Medium Silver_Bars_Stack_Small Silver_Nugg
kaykit-restaurant: bowl bowl_dirty bowl_small chair_A chair_B chair_stool crate crate_buns crate_carrots crate_cheese crate_ham crate_lettuce crate_lid crate_onions crate_potatoes crate_steak crate_tomatoes cuttingboard dishrack dishrack_plates door_A door_B extractorhood floor_kitchen floor_kitchen_small food_burger food_dinner food_ingredient_bun food_ingredient_bun_bottom food_ingredient_bun_top food_ingredient_burger_cooked food_ingredient_burger_trash food_ingredient_burger_uncooked food_ingredient_carrot food_ingredient_carrot_chopped food_ingredient_carrot_pieces food_ingredient_cheese food_ingredient_cheese_chopped food_ingredient_cheese_slice food_ingredient_ham food_ingredient_ham_cooked food_ingredient_ham_trash food_ingredient_lettuce food_ingredient_lettuce_chopped food_ingredient_lettuce_slice food_ingredient_onion food_ingredient_onion_chopped food_ingredient_onion_rings food_ingredient_pota
kaykit-space-base: basemodule_A basemodule_B basemodule_C basemodule_D basemodule_E basemodule_garage cargo_A cargo_A_packed cargo_A_stacked cargo_B cargo_B_packed cargo_B_stacked cargodepot_A cargodepot_B cargodepot_C containers_A containers_B containers_C containers_D drill_structure lander_A lander_B lander_base landingpad_large landingpad_small lights rock_A rock_B rocks_A rocks_B roofmodule_base roofmodule_cargo_A roofmodule_cargo_B roofmodule_cargo_C roofmodule_solarpanels solarpanel spacetruck spacetruck_large spacetruck_trailer structure_low structure_tall terrain_low terrain_low_curved terrain_mining terrain_slope terrain_slope_inner_corner terrain_slope_outer_corner terrain_tall terrain_tall_curved tunnel_diagonal_long_A tunnel_diagonal_long_B tunnel_diagonal_short_A tunnel_diagonal_short_B tunnel_straight_A tunnel_straight_B windturbine_low windturbine_tall 
modular-roads: Road1 Road10_90angle_Corner Road11_Y_Splitter Road11_Y_Splitter_45 Road12_Diagonal_Splitter_L Road12_Diagonal_Splitter_R Road1_Curve1 Road1_Curve2 Road1_Curve3 Road1_Curve4 Road2_T Road2_X Road6_End Tree3 Tree4 bush_1 hazzard_cone_1 lamp_1 lamp_2 road_barier_2a road_barier_2b road_barrier_1 traffic_barell_1 traffic_light_1 traffic_light_2 traffic_light_3 tree_1_a 
pharmacy: medpack_1 scissors shelf_3 small_bottle_1 small_bottle_2 small_bottle_tall_1 small_bottle_tall_2 test_tube_1 test_tube_2 test_tube_3 test_tube_4 
postapoc: barrel box_1 car electric_pole_1 ground_1 ground_2 ground_planks ground_road_1_L ground_road_1_R ground_road_2_L ground_road_2_R metal_board_1 metal_board_2 metal_board_3 tire wall_1 wall_1_brick wall_1_door_boarded wall_1_hole wall_1_window_1 wall_1_window_2 wall_column wall_concrete_metal wall_metal_1 wall_metal_2 wall_spiked wheel wooden_spike_barricade wooden_wall 
```
