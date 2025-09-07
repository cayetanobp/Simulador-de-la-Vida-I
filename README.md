# 🌱 Proyecto: Simulación de Vida / Mini-Farm

## Creación del entorno virtual
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
## Descripción
Simulación en tiempo real donde el jugador puede construir su casa, sembrar y cuidar cultivos, recolectar recursos y expandir su granja. Proyecto desarrollado con **Pygame**, pensado para trabajar en equipo.

---

## Etapas de desarrollo

### **Etapa 1: Movimiento y mapa básico**
**Objetivo:** Tener un jugador que se pueda mover por un mapa definido con tiles.
**Tareas:**
- Diseñar un mapa base con diferentes tipos de terreno (pasto, tierra, caminos).  
- Crear sistema de tiles (cuadrículas) para el mapa.  
- Implementar movimiento del jugador con teclas de dirección.  
- Dibujar sprites básicos para el personaje y el terreno.  
- Definir límites del mapa y colisiones simples.  

---

### **Etapa 2: Construcción**
**Objetivo:** Permitir al jugador colocar y remover bloques para construir estructuras.
**Tareas:**
- Crear un sistema de selección de bloques (casa, cercas, caminos).  
- Permitir colocar bloques en casillas específicas del mapa.  
- Permitir remover bloques ya colocados.  
- Guardar la posición de los bloques en memoria para mantener el estado del mapa.  
- Implementar una interfaz simple para seleccionar el tipo de bloque.  

---

### **Etapa 3: Cultivos**
**Objetivo:** Sembrar y ver crecer cultivos con simulación en tiempo real.
**Tareas:**
- Permitir plantar semillas en casillas de tierra.  
- Implementar fases de crecimiento de cada cultivo (semilla → brote → maduro).  
- Crear un timer que gestione el crecimiento con base en tiempo real o frames.  
- Implementar riego opcional para acelerar o ralentizar el crecimiento.  
- Crear sprites para cada fase de crecimiento.  

---

### **Etapa 4: Inventario y acciones**
**Objetivo:** Gestionar recursos y permitir acciones del jugador.
**Tareas:**
- Crear un inventario para semillas, herramientas y objetos recolectables.  
- Permitir seleccionar items del inventario para plantar, regar o recolectar.  
- Implementar acciones de recolección, siembra y riego.  
- Mostrar información básica del inventario en pantalla.  
- Controlar límites de inventario y cantidad de recursos.  

---

### **Etapa 5: Ciclo de día/noche**
**Objetivo:** Añadir dinámica temporal al juego.
**Tareas:**
- Implementar un ciclo de día/noche que cambie el fondo y colores del mapa.  
- Ajustar crecimiento de cultivos según el ciclo de día.  
- Opcional: efectos de iluminación y sombras simples.  
- Mostrar reloj o indicador de tiempo en pantalla.  

---

### **Etapa 6: Guardar/Cargar partida**
**Objetivo:** Permitir continuar el juego más tarde.
**Tareas:**
- Implementar sistema de guardado de mapa, posición del jugador y estado de cultivos.  
- Guardar inventario y recursos en un archivo (ej. JSON).  
- Implementar carga de partida al iniciar el juego.  
- Añadir verificación de integridad de archivos guardados.  

---

### **Etapa 7 (Opcional): Multiplayer local**
**Objetivo:** Permitir juego cooperativo en la misma pantalla.
**Tareas:**
- Implementar un segundo jugador con controles separados.  
- Sincronizar movimientos y acciones de ambos jugadores.  
- Ajustar interfaz e inventarios para dos jugadores.  
- Gestionar interacciones colaborativas (construir juntos, regar juntos, cosechar juntos).  

---

### **Extras / Mejoras futuras**
- Añadir enemigos o eventos aleatorios.  
- Mejorar sprites y animaciones de personajes y cultivos.  
- Implementar ciclos climáticos (lluvia, sol, nieve).  
- Crear sistema de puntuación o logros.

