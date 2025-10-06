# Práctica 2: Proyecto Adaptado a tu Dominio

## 🎯 Objetivo

Adaptar un stack Docker Compose completo (Frontend + Base de Datos) a tu dominio de negocio asignado, aplicando todo lo aprendido.

**Tiempo estimado**: 60 minutos

---

## 📋 Tu Dominio Asignado

**⚠️ IMPORTANTE**: El instructor te asignó un dominio de negocio específico (restaurante, biblioteca, clínica veterinaria, etc.). Usarás ese dominio para personalizar este proyecto.

**Ejemplo de dominios**:

- Restaurante (menú, pedidos, mesas)
- Biblioteca (libros, préstamos, usuarios)
- Gimnasio (miembros, rutinas, equipos)
- Tienda (productos, ventas, clientes)

---

## 📁 Parte 1: Preparar el Proyecto (5 min)

### Paso 1: Crear Estructura

```bash
# ¿Qué? Crear proyecto con tu dominio
# Ejemplo: si tu dominio es "restaurante"
mkdir -p ~/bootcamp/mi-dominio-stack
cd ~/bootcamp/mi-dominio-stack

# ¿Qué? Crear carpetas
mkdir frontend init-db
```

---

## 🗄️ Parte 2: Diseñar tu Base de Datos (15 min)

### Paso 2: Identificar Entidades de tu Dominio

**Piensa en tu negocio**:

- ¿Qué información necesitas guardar?
- ¿Cuáles son las entidades principales?
- ¿Qué relaciones hay entre ellas?

**Ejemplo - Restaurante**:

- Entidades: `mesas`, `platos`, `pedidos`, `empleados`
- Relaciones: Un pedido pertenece a una mesa, contiene varios platos

**Ejemplo - Biblioteca**:

- Entidades: `libros`, `usuarios`, `prestamos`, `categorias`
- Relaciones: Un préstamo conecta un usuario con un libro

---

### Paso 3: Crear Script SQL

Crea `init-db/01-crear-tablas.sql` adaptado a TU dominio:

**Template genérico** (adaptar):

```sql
-- ¿Qué? Base de datos para [TU_DOMINIO]
-- ¿Para qué? Gestionar [DESCRIPCIÓN_BREVE]

-- ===== ENTIDAD 1 (Principal) =====
CREATE TABLE IF NOT EXISTS entidad1 (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    campo1 VARCHAR(100),
    campo2 DECIMAL(10, 2),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ¿Qué? Índice para búsquedas rápidas
CREATE INDEX IF NOT EXISTS idx_entidad1_nombre ON entidad1(nombre);

-- ===== ENTIDAD 2 (Secundaria) =====
CREATE TABLE IF NOT EXISTS entidad2 (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ===== ENTIDAD 3 (Relación) =====
CREATE TABLE IF NOT EXISTS entidad3 (
    id SERIAL PRIMARY KEY,
    entidad1_id INT REFERENCES entidad1(id),
    entidad2_id INT REFERENCES entidad2(id),
    cantidad INT DEFAULT 1,
    total DECIMAL(10, 2),
    estado VARCHAR(50) DEFAULT 'pendiente',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ===== DATOS DE EJEMPLO =====
INSERT INTO entidad1 (nombre, descripcion, campo1, campo2) VALUES
    ('Registro 1', 'Descripción 1', 'Valor A', 100.00),
    ('Registro 2', 'Descripción 2', 'Valor B', 250.50),
    ('Registro 3', 'Descripción 3', 'Valor C', 75.00)
ON CONFLICT DO NOTHING;

INSERT INTO entidad2 (nombre, email, telefono) VALUES
    ('Usuario 1', 'usuario1@example.com', '3001234567'),
    ('Usuario 2', 'usuario2@example.com', '3009876543')
ON CONFLICT (email) DO NOTHING;
```

---

**Ejemplo Completo - Restaurante**:

```sql
-- ¿Qué? Base de datos para RESTAURANTE
-- ¿Para qué? Gestionar platos, mesas y pedidos

-- ===== PLATOS =====
CREATE TABLE IF NOT EXISTS platos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2) NOT NULL,
    disponible BOOLEAN DEFAULT true,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_platos_categoria ON platos(categoria);

-- ===== MESAS =====
CREATE TABLE IF NOT EXISTS mesas (
    id SERIAL PRIMARY KEY,
    numero INT UNIQUE NOT NULL,
    capacidad INT NOT NULL,
    ubicacion VARCHAR(50),
    estado VARCHAR(20) DEFAULT 'disponible'
);

-- ===== PEDIDOS =====
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    mesa_id INT REFERENCES mesas(id),
    plato_id INT REFERENCES platos(id),
    cantidad INT DEFAULT 1,
    total DECIMAL(10, 2),
    estado VARCHAR(50) DEFAULT 'pendiente',
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ===== DATOS DE EJEMPLO =====
INSERT INTO platos (nombre, descripcion, categoria, precio) VALUES
    ('Bandeja Paisa', 'Plato típico colombiano completo', 'Platos Fuertes', 25000.00),
    ('Ajiaco', 'Sopa tradicional bogotana', 'Sopas', 18000.00),
    ('Arepa con Queso', 'Arepa de maíz con queso costeño', 'Entradas', 8000.00),
    ('Jugo Natural', 'Jugo de frutas frescas', 'Bebidas', 5000.00)
ON CONFLICT DO NOTHING;

INSERT INTO mesas (numero, capacidad, ubicacion) VALUES
    (1, 4, 'Ventana'),
    (2, 2, 'Interior'),
    (3, 6, 'Terraza'),
    (4, 4, 'Interior')
ON CONFLICT (numero) DO NOTHING;
```

---

## 🐳 Parte 3: Crear Docker Compose (10 min)

### Paso 4: Crear docker-compose.yml

```yaml
services:
  # ===== BASE DE DATOS =====
  db:
    image: postgres:15-alpine
    container_name: ${PROYECTO_NOMBRE}-db
    # ¿Para qué? Usar variable para nombre personalizado

    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}

    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-db:/docker-entrypoint-initdb.d

    ports:
      - '5432:5432'

    restart: unless-stopped

  # ===== ADMINER (Gestor Web) =====
  adminer:
    image: adminer:latest
    container_name: ${PROYECTO_NOMBRE}-adminer

    ports:
      - '8080:8080'

    restart: unless-stopped

    depends_on:
      - db

  # ===== FRONTEND (Interfaz Web) =====
  web:
    image: nginx:alpine
    container_name: ${PROYECTO_NOMBRE}-web

    ports:
      - '80:80'

    volumes:
      - ./frontend:/usr/share/nginx/html:ro
      # ¿Para qué? Servir archivos HTML desde carpeta frontend

    restart: unless-stopped

    depends_on:
      - db

volumes:
  postgres_data:
```

---

### Paso 5: Crear .env

```bash
# ¿Qué? Variables personalizadas para tu dominio
PROYECTO_NOMBRE=mi-dominio
# Ejemplo: restaurante, biblioteca, gimnasio

DB_USER=admin_dominio
DB_PASSWORD=MiDominio2024!
DB_NAME=dominio_db
```

---

## 🎨 Parte 4: Crear Frontend Básico (20 min)

### Paso 6: Crear index.html

Crea `frontend/index.html` adaptado a tu dominio:

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>[TU DOMINIO] - Sistema de Gestión</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
      }

      .container {
        max-width: 1200px;
        margin: 0 auto;
        background: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
      }

      h1 {
        color: #333;
        text-align: center;
        margin-bottom: 10px;
        font-size: 2.5em;
      }

      .subtitulo {
        text-align: center;
        color: #666;
        margin-bottom: 40px;
        font-size: 1.2em;
      }

      .seccion {
        margin-bottom: 40px;
        padding: 30px;
        background: #f8f9fa;
        border-radius: 10px;
        border-left: 5px solid #667eea;
      }

      .seccion h2 {
        color: #667eea;
        margin-bottom: 20px;
        font-size: 1.8em;
      }

      .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 20px;
      }

      .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
      }

      .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
      }

      .card h3 {
        color: #667eea;
        margin-bottom: 10px;
      }

      .stats {
        display: flex;
        justify-content: space-around;
        margin: 30px 0;
      }

      .stat {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        min-width: 150px;
      }

      .stat .numero {
        font-size: 3em;
        font-weight: bold;
        color: #667eea;
      }

      .stat .label {
        color: #666;
        margin-top: 10px;
      }

      .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 2px solid #eee;
        color: #666;
      }

      .btn {
        display: inline-block;
        padding: 12px 24px;
        background: #667eea;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        margin: 10px 5px;
        transition: background 0.3s;
      }

      .btn:hover {
        background: #764ba2;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>🎯 [TU DOMINIO]</h1>
      <p class="subtitulo">Sistema de Gestión - Bootcamp SENA</p>

      <!-- Estadísticas -->
      <div class="stats">
        <div class="stat">
          <div class="numero">XX</div>
          <div class="label">[Entidad 1]</div>
        </div>
        <div class="stat">
          <div class="numero">XX</div>
          <div class="label">[Entidad 2]</div>
        </div>
        <div class="stat">
          <div class="numero">XX</div>
          <div class="label">[Entidad 3]</div>
        </div>
      </div>

      <!-- Sección 1 -->
      <div class="seccion">
        <h2>📋 [Nombre Sección 1]</h2>
        <div class="grid">
          <div class="card">
            <h3>Item 1</h3>
            <p>Descripción del item 1</p>
          </div>
          <div class="card">
            <h3>Item 2</h3>
            <p>Descripción del item 2</p>
          </div>
          <div class="card">
            <h3>Item 3</h3>
            <p>Descripción del item 3</p>
          </div>
        </div>
      </div>

      <!-- Sección 2 -->
      <div class="seccion">
        <h2>👥 [Nombre Sección 2]</h2>
        <p>Información relevante de tu dominio...</p>
      </div>

      <!-- Enlaces -->
      <div style="text-align: center; margin-top: 40px;">
        <a
          href="http://localhost:8080"
          class="btn"
          target="_blank">
          🗄️ Gestor de Base de Datos (Adminer)
        </a>
      </div>

      <div class="footer">
        <p><strong>Bootcamp Implantación de Software - SENA 2024</strong></p>
        <p>Ficha: 3147234 | Semana 2 - Docker Compose</p>
      </div>
    </div>
  </body>
</html>
```

---

**Ejemplo Completo - Restaurante**:

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>Restaurante El Buen Sabor - Sistema de Gestión</title>
    <style>
      /* Estilos del template anterior */
    </style>
  </head>
  <body>
    <div class="container">
      <h1>🍽️ Restaurante El Buen Sabor</h1>
      <p class="subtitulo">Sistema de Gestión de Pedidos - Bootcamp SENA</p>

      <div class="stats">
        <div class="stat">
          <div class="numero">24</div>
          <div class="label">Platos Disponibles</div>
        </div>
        <div class="stat">
          <div class="numero">12</div>
          <div class="label">Mesas Activas</div>
        </div>
        <div class="stat">
          <div class="numero">45</div>
          <div class="label">Pedidos Hoy</div>
        </div>
      </div>

      <div class="seccion">
        <h2>🍲 Menú del Día</h2>
        <div class="grid">
          <div class="card">
            <h3>Bandeja Paisa</h3>
            <p>
              Plato típico colombiano completo con frijoles, arroz, carne,
              huevo...
            </p>
            <p><strong>$25,000</strong></p>
          </div>
          <div class="card">
            <h3>Ajiaco Santafereño</h3>
            <p>Sopa tradicional bogotana con papa criolla, pollo, mazorca...</p>
            <p><strong>$18,000</strong></p>
          </div>
          <div class="card">
            <h3>Sancocho de Gallina</h3>
            <p>Sopa sustanciosa con gallina criolla, yuca, plátano...</p>
            <p><strong>$20,000</strong></p>
          </div>
        </div>
      </div>

      <div class="seccion">
        <h2>📍 Ubicación de Mesas</h2>
        <p>
          Tenemos 12 mesas distribuidas entre zona de ventana, interior y
          terraza.
        </p>
        <p>Capacidad total: 48 personas</p>
      </div>

      <div style="text-align: center; margin-top: 40px;">
        <a
          href="http://localhost:8080"
          class="btn"
          target="_blank">
          🗄️ Gestor de Base de Datos
        </a>
      </div>

      <div class="footer">
        <p><strong>Bootcamp Implantación de Software - SENA 2024</strong></p>
        <p>Ficha: 3147234 | Semana 2 - Docker Compose</p>
        <p>Aprendiz: [TU NOMBRE]</p>
      </div>
    </div>
  </body>
</html>
```

---

## 🚀 Parte 5: Ejecutar y Probar (10 min)

### Paso 7: Levantar el Stack

```bash
# ¿Qué? Levantar todos los servicios
docker compose up -d

# ¿Qué? Verificar que todo funciona
docker compose ps
```

**Deberías ver 3 contenedores**:

- `[tu-dominio]-db`
- `[tu-dominio]-adminer`
- `[tu-dominio]-web`

---

### Paso 8: Probar la Aplicación

1. **Frontend**: http://localhost

   - Deberías ver tu página personalizada

2. **Adminer**: http://localhost:8080

   - Conectar con: servidor=`db`, usuario y contraseña del .env
   - Verificar tus tablas con datos

3. **Verificar logs**: `docker compose logs`

---

## ✅ Entregables

Al finalizar debes tener:

1. **Carpeta del proyecto** con:

   - `docker-compose.yml`
   - `.env`
   - `.gitignore`
   - `init-db/01-crear-tablas.sql` (personalizado a tu dominio)
   - `frontend/index.html` (personalizado a tu dominio)

2. **Capturas de pantalla**:

   - Frontend funcionando (http://localhost)
   - Adminer mostrando tus tablas con datos
   - Terminal con `docker compose ps`

3. **Documento README.md** explicando:
   - Tu dominio asignado
   - Entidades de tu base de datos
   - Cómo ejecutar el proyecto
   - Decisiones técnicas tomadas

---

## 📝 Rúbrica de Evaluación

| Criterio                                                        | Puntos   |
| --------------------------------------------------------------- | -------- |
| Base de datos diseñada correctamente (3+ tablas con relaciones) | 25%      |
| docker-compose.yml funcional                                    | 20%      |
| Script SQL ejecuta sin errores                                  | 15%      |
| Frontend personalizado a dominio                                | 20%      |
| Persistencia de datos verificada                                | 10%      |
| Documentación (README.md)                                       | 10%      |
| **TOTAL**                                                       | **100%** |

---

## 🎯 Ejemplo de README.md

````markdown
# Sistema de Gestión - [TU DOMINIO]

## 📋 Descripción

Sistema de gestión para [describe tu dominio] desarrollado con Docker Compose.

## 🗄️ Base de Datos

### Entidades:

1. **[Entidad1]**: [descripción]
2. **[Entidad2]**: [descripción]
3. **[Entidad3]**: [descripción]

### Relaciones:

- [Entidad1] → [Entidad3]
- [Entidad2] → [Entidad3]

## 🚀 Cómo Ejecutar

```bash
# Clonar o descargar proyecto
cd mi-dominio-stack

# Levantar servicios
docker compose up -d

# Acceder a:
# Frontend: http://localhost
# Adminer: http://localhost:8080
```
````

## 🛠️ Tecnologías

- PostgreSQL 15 (Base de datos)
- Nginx (Servidor web)
- Adminer (Gestor de BD)
- Docker Compose (Orquestación)

## 👤 Autor

[Tu Nombre] - Ficha 3147234 - SENA 2024

```

---

## 💡 Consejos

1. **Adapta nombres**: Cambia todos los `[TU_DOMINIO]` por tu dominio real
2. **Sé creativo**: Personaliza colores, títulos, contenido
3. **Datos reales**: Inserta datos coherentes con tu negocio
4. **Prueba todo**: Verifica que la persistencia funciona
5. **Documenta**: Explica tus decisiones técnicas

---

## 📌 Próximos Pasos

Este proyecto es la base para las siguientes semanas donde agregarás:
- API REST (Backend)
- Nginx como reverse proxy
- Migración y respaldo de datos

¡Excelente trabajo completando la Semana 2! 🎉
```
