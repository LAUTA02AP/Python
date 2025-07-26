# 🏆 Sistema de Gestión de Jugadores - Liga de Fútbol

Este sistema fue desarrollado para ayudar a una liga de fútbol regional a gestionar la información de los jugadores y facilitar la entrega de premios. Permite registrar y consultar datos relevantes como el rendimiento, categoría, amonestaciones y clubes de pertenencia.

---

## 📋 Datos de cada jugador:

Cada jugador tiene los siguientes atributos registrados:

- DNI
- Apellido y Nombre
- Club
- Categoría
- Goles
- Amonestaciones
- Expulsiones

---

## 🧩 Funcionalidades del sistema

### 1. 📄 Listado completo de jugadores
Muestra todos los jugadores con **toda su información detallada**.

---

### 2. 📝 Registro de un nuevo jugador
Permite **agregar un nuevo jugador** al sistema con sus datos correspondientes.


---

### 3. 📍 Listado por club
Muestra los jugadores **de un club específico**.

---

### 4. 📊 Evaluación de desempeño
Calcula el rendimiento de un jugador:
- **+10 puntos por gol**
- **−2 puntos por amonestación**
- **−5 puntos por expulsión**

Se muestra el **puntaje total** del jugador.

---

### 5. 🔍 Consulta por club y categoría
Permite consultar un **club y categoría específica**, mostrando el detalle de jugadores y el **total al finalizar**.

---

### 6. 🧮 Cantidad de jugadores por categoría
Muestra la **cantidad total de jugadores** por cada categoría.

---

### 7. 🧑‍🤝‍🧑 Detalle de jugadores por categoría
Muestra los jugadores de una **categoría seleccionada**, incluyendo el **club al que pertenece cada uno**.

---

## 💻 Tecnologías / Lenguaje sugerido
Este sistema puede ser desarrollado en cualquier lenguaje como Python, Java, C#, etc., usando estructuras de datos como listas, diccionarios u objetos.

---

## ✅ Objetivo
Brindar una solución completa para la gestión deportiva de una liga regional de fútbol, optimizando el manejo de datos de los jugadores para la premiación y organización general.

---
## 🛠️ Notas técnicas / Arquitectura

> 📌 **NOTA IMPORTANTE:**
> 
> - Se utilizó arquitectura **MVC (Modelo-Vista-Controlador)** para una mejor organización del sistema.
> - En la carpeta **`20`** se encuentra el **diagrama UML** y los **archivos de registro** utilizados por el sistema.
> - Cada vez que se **carga** o **modifica** un jugador, los datos se **actualizan automáticamente al finalizar el programa**.
> - Los datos cargados en los `.txt` son **de prueba**, y pueden no tener sentido real (se usan solo para trabajar el sistema).
