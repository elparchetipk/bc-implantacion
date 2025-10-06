# 📋 Ejemplo Dominio: Restaurante

> **Propósito**: Proyecto de ejemplo completo para inspirar adaptaciones  
> **Dominio**: Sistema de gestión de restaurante  
> **Nivel**: Práctica 2 - Semana 2

---

## 📂 Estructura del Proyecto

```
restaurante-docker/
├── docker-compose.yml
├── .env
├── database/
│   └── init.sql
├── frontend/
│   ├── index.html
│   └── styles.css
└── README.md
```

---

## 🗄️ Base de Datos - init.sql

```sql
-- ============================================================================
-- SISTEMA DE GESTIÓN DE RESTAURANTE
-- ============================================================================
-- ¿Qué? - Esquema de base de datos para restaurante
-- ¿Para qué? - Gestionar menú, pedidos, mesas y empleados

-- ---------------------------------------------------------------------------
-- TABLA: categorias (Tipos de comida)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    activo BOOLEAN DEFAULT true,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: platos (Menú del restaurante)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS platos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL CHECK (precio > 0),
    categoria_id INTEGER REFERENCES categorias(id) ON DELETE SET NULL,
    disponible BOOLEAN DEFAULT true,
    imagen_url VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: mesas (Mesas del restaurante)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mesas (
    id SERIAL PRIMARY KEY,
    numero INTEGER NOT NULL UNIQUE,
    capacidad INTEGER NOT NULL CHECK (capacidad > 0),
    ubicacion VARCHAR(50),  -- 'Terraza', 'Interior', 'VIP'
    estado VARCHAR(20) DEFAULT 'disponible' CHECK (estado IN ('disponible', 'ocupada', 'reservada', 'mantenimiento')),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: clientes (Clientes frecuentes - opcional)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    puntos_fidelidad INTEGER DEFAULT 0,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: pedidos (Órdenes de los clientes)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    mesa_id INTEGER REFERENCES mesas(id) ON DELETE SET NULL,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE SET NULL,
    total DECIMAL(10, 2) DEFAULT 0,
    estado VARCHAR(20) DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'en_preparacion', 'servido', 'pagado', 'cancelado')),
    observaciones TEXT,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_entrega TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: detalle_pedidos (Items de cada pedido)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS detalle_pedidos (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
    plato_id INTEGER REFERENCES platos(id) ON DELETE RESTRICT,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    observaciones TEXT  -- "Sin cebolla", "Extra picante", etc.
);

-- ---------------------------------------------------------------------------
-- TABLA: empleados (Personal del restaurante)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    puesto VARCHAR(50) NOT NULL,  -- 'Mesero', 'Cocinero', 'Gerente'
    telefono VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    fecha_contratacion DATE DEFAULT CURRENT_DATE,
    salario DECIMAL(10, 2),
    activo BOOLEAN DEFAULT true
);

-- ============================================================================
-- DATOS DE PRUEBA
-- ============================================================================

-- Categorías
INSERT INTO categorias (nombre, descripcion) VALUES
    ('Entradas', 'Aperitivos y entrantes'),
    ('Platos Fuertes', 'Platos principales'),
    ('Postres', 'Dulces y postres'),
    ('Bebidas', 'Refrescos, jugos y bebidas calientes');

-- Platos
INSERT INTO platos (nombre, descripcion, precio, categoria_id, disponible) VALUES
    ('Ensalada César', 'Lechuga romana, crutones, parmesano', 8.50, 1, true),
    ('Ceviche Mixto', 'Pescado y mariscos frescos en limón', 12.00, 1, true),
    ('Lomo Saltado', 'Res salteada con papas fritas y arroz', 15.50, 2, true),
    ('Arroz con Pollo', 'Arroz amarillo con pollo y vegetales', 13.00, 2, true),
    ('Tiramisu', 'Postre italiano con café y mascarpone', 6.50, 3, true),
    ('Cheesecake', 'Tarta de queso con frutos rojos', 7.00, 3, true),
    ('Limonada Natural', 'Jugo de limón con hielo', 3.50, 4, true),
    ('Café Expreso', 'Café expreso de grano selecto', 2.50, 4, true);

-- Mesas
INSERT INTO mesas (numero, capacidad, ubicacion, estado) VALUES
    (1, 4, 'Interior', 'disponible'),
    (2, 2, 'Terraza', 'disponible'),
    (3, 6, 'VIP', 'disponible'),
    (4, 4, 'Interior', 'ocupada'),
    (5, 8, 'Terraza', 'reservada');

-- Clientes
INSERT INTO clientes (nombre, telefono, email, puntos_fidelidad) VALUES
    ('Juan Pérez', '555-0101', 'juan@ejemplo.com', 120),
    ('María García', '555-0102', 'maria@ejemplo.com', 85),
    ('Carlos López', '555-0103', 'carlos@ejemplo.com', 50);

-- Empleados
INSERT INTO empleados (nombre, apellido, puesto, telefono, email, salario) VALUES
    ('Pedro', 'Ramírez', 'Gerente', '555-0201', 'pedro@restaurante.com', 2500.00),
    ('Ana', 'Martínez', 'Mesera', '555-0202', 'ana@restaurante.com', 1200.00),
    ('Luis', 'Fernández', 'Cocinero', '555-0203', 'luis@restaurante.com', 1800.00);

-- Pedido de ejemplo
INSERT INTO pedidos (mesa_id, cliente_id, total, estado, observaciones) VALUES
    (4, 1, 37.50, 'en_preparacion', 'Sin sal');

INSERT INTO detalle_pedidos (pedido_id, plato_id, cantidad, precio_unitario, observaciones) VALUES
    (1, 3, 2, 15.50, NULL),  -- 2 Lomo Saltado
    (1, 7, 2, 3.50, 'Con hielo extra');  -- 2 Limonadas

-- ============================================================================
-- CONSULTAS ÚTILES (Para probar en Adminer)
-- ============================================================================

-- Ver menú completo con categorías
SELECT p.nombre, p.descripcion, p.precio, c.nombre as categoria
FROM platos p
LEFT JOIN categorias c ON p.categoria_id = c.id
WHERE p.disponible = true
ORDER BY c.nombre, p.nombre;

-- Ver mesas disponibles
SELECT numero, capacidad, ubicacion
FROM mesas
WHERE estado = 'disponible'
ORDER BY numero;

-- Ver pedidos activos con detalle
SELECT
    ped.id as pedido_id,
    m.numero as mesa,
    c.nombre as cliente,
    ped.estado,
    ped.total,
    ped.fecha_pedido
FROM pedidos ped
LEFT JOIN mesas m ON ped.mesa_id = m.id
LEFT JOIN clientes c ON ped.cliente_id = c.id
WHERE ped.estado IN ('pendiente', 'en_preparacion')
ORDER BY ped.fecha_pedido DESC;

-- Ver empleados activos
SELECT nombre, apellido, puesto, telefono
FROM empleados
WHERE activo = true
ORDER BY puesto, apellido;
```

---

## 🐳 Docker Compose - docker-compose.yml

```yaml
services:
  # Base de datos
  db:
    image: postgres:15-alpine
    container_name: restaurante_db
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_HOST_AUTH_METHOD: scram-sha-256
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    ports:
      - '5432:5432'
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${DB_USER} -d ${DB_NAME}']
      interval: 10s
      timeout: 5s
      retries: 5

  # Interfaz web
  frontend:
    image: nginx:alpine
    container_name: restaurante_frontend
    restart: unless-stopped
    volumes:
      - ./frontend:/usr/share/nginx/html:ro
    ports:
      - '80:80'
    depends_on:
      db:
        condition: service_healthy

  # Administrador de BD
  adminer:
    image: adminer:latest
    container_name: restaurante_adminer
    restart: unless-stopped
    ports:
      - '8080:8080'
    environment:
      ADMINER_DEFAULT_SERVER: db
    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres_data:
```

---

## 🔐 Variables de Entorno - .env

```bash
DB_NAME=restaurante_db
DB_USER=admin_restaurante
DB_PASSWORD=RestauranteSeguro2024!
```

---

## 🎨 Frontend - frontend/index.html

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>Sistema de Gestión - Restaurante</title>
    <link
      rel="stylesheet"
      href="styles.css" />
  </head>
  <body>
    <header>
      <h1>🍽️ Restaurante "El Buen Sabor"</h1>
      <p>Sistema de Gestión - Docker Compose</p>
    </header>

    <main>
      <section class="card">
        <h2>📋 Menú del Día</h2>
        <div class="menu-items">
          <div class="item">
            <h3>Lomo Saltado</h3>
            <p>Res salteada con papas fritas y arroz</p>
            <span class="price">$15.50</span>
          </div>
          <div class="item">
            <h3>Arroz con Pollo</h3>
            <p>Arroz amarillo con pollo y vegetales</p>
            <span class="price">$13.00</span>
          </div>
          <div class="item">
            <h3>Ceviche Mixto</h3>
            <p>Pescado y mariscos frescos en limón</p>
            <span class="price">$12.00</span>
          </div>
        </div>
      </section>

      <section class="card">
        <h2>🪑 Mesas Disponibles</h2>
        <div class="tables">
          <div class="table available">Mesa 1 - 4 personas</div>
          <div class="table available">Mesa 2 - 2 personas</div>
          <div class="table reserved">Mesa 5 - 8 personas (Reservada)</div>
        </div>
      </section>

      <section class="card">
        <h2>📊 Estadísticas del Día</h2>
        <div class="stats">
          <div class="stat">
            <h3>15</h3>
            <p>Pedidos Totales</p>
          </div>
          <div class="stat">
            <h3>$432.50</h3>
            <p>Ingresos</p>
          </div>
          <div class="stat">
            <h3>3/5</h3>
            <p>Mesas Ocupadas</p>
          </div>
        </div>
      </section>

      <section class="card">
        <h2>🔗 Accesos del Sistema</h2>
        <div class="links">
          <a
            href="http://localhost:8080"
            target="_blank"
            class="btn">
            📊 Adminer (Base de Datos)
          </a>
          <p class="help">
            <strong>Credenciales:</strong><br />
            Servidor: <code>db</code><br />
            Usuario: <code>admin_restaurante</code><br />
            Contraseña: <code>RestauranteSeguro2024!</code><br />
            Base de datos: <code>restaurante_db</code>
          </p>
        </div>
      </section>
    </main>

    <footer>
      <p>Proyecto de Implantación de Software - SENA CGMLTI 2024</p>
      <p>Dominio: Restaurante | Stack: Docker Compose + PostgreSQL + Nginx</p>
    </footer>
  </body>
</html>
```

---

## 🎨 Estilos - frontend/styles.css

```css
/* Reset y variables */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --primary: #ff6b6b;
  --secondary: #4ecdc4;
  --dark: #2d3436;
  --light: #dfe6e9;
  --success: #00b894;
  --warning: #fdcb6e;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: var(--dark);
  line-height: 1.6;
  min-height: 100vh;
}

header {
  background: white;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

header h1 {
  color: var(--primary);
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

header p {
  color: var(--dark);
  opacity: 0.7;
}

main {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.card {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.card h2 {
  color: var(--primary);
  margin-bottom: 1.5rem;
  border-bottom: 2px solid var(--light);
  padding-bottom: 0.5rem;
}

/* Menú */
.menu-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.item {
  padding: 1rem;
  border: 2px solid var(--light);
  border-radius: 8px;
  transition: all 0.3s ease;
}

.item:hover {
  border-color: var(--secondary);
  background: #f8f9fa;
}

.item h3 {
  color: var(--dark);
  margin-bottom: 0.5rem;
}

.item p {
  color: #636e72;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.price {
  display: inline-block;
  background: var(--success);
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-weight: bold;
}

/* Mesas */
.tables {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.table {
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  font-weight: bold;
}

.table.available {
  background: var(--success);
  color: white;
}

.table.reserved {
  background: var(--warning);
  color: var(--dark);
}

/* Estadísticas */
.stats {
  display: flex;
  justify-content: space-around;
  gap: 1rem;
}

.stat {
  text-align: center;
  padding: 1rem;
  background: var(--light);
  border-radius: 8px;
  flex: 1;
}

.stat h3 {
  color: var(--primary);
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.stat p {
  color: var(--dark);
  font-size: 0.9rem;
}

/* Enlaces */
.links {
  text-align: center;
}

.btn {
  display: inline-block;
  background: var(--secondary);
  color: white;
  padding: 1rem 2rem;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  transition: all 0.3s ease;
  margin: 1rem 0;
}

.btn:hover {
  background: var(--primary);
  transform: scale(1.05);
}

.help {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.help code {
  background: var(--dark);
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
}

footer {
  background: rgba(255, 255, 255, 0.9);
  text-align: center;
  padding: 1.5rem;
  margin-top: 3rem;
}

footer p {
  margin: 0.5rem 0;
  color: var(--dark);
  opacity: 0.7;
}

/* Responsive */
@media (max-width: 768px) {
  header h1 {
    font-size: 1.8rem;
  }

  main {
    grid-template-columns: 1fr;
  }

  .stats {
    flex-direction: column;
  }
}
```

---

## 📖 README del Proyecto - README.md

````markdown
# 🍽️ Sistema de Gestión de Restaurante

Proyecto de ejemplo para el bootcamp de Implantación de Software - SENA CGMLTI

## 📋 Descripción

Sistema completo de gestión para un restaurante utilizando Docker Compose. Incluye:

- Base de datos PostgreSQL con esquema completo
- Frontend web con Nginx
- Interfaz de administración con Adminer

## 🚀 Inicio Rápido

1. **Clonar o descargar el proyecto**

2. **Iniciar los servicios**
   ```bash
   docker compose up -d
   ```
````

3. **Acceder a las interfaces**
   - Frontend: http://localhost
   - Adminer: http://localhost:8080

## 🗄️ Estructura de la Base de Datos

- **categorias**: Tipos de comida (Entradas, Platos Fuertes, Postres, Bebidas)
- **platos**: Menú del restaurante con precios
- **mesas**: Mesas disponibles con capacidad y ubicación
- **clientes**: Clientes frecuentes con programa de fidelidad
- **pedidos**: Órdenes de los clientes
- **detalle_pedidos**: Items de cada pedido
- **empleados**: Personal del restaurante

## 📊 Datos de Prueba

El sistema incluye datos de ejemplo:

- 4 categorías de comida
- 8 platos en el menú
- 5 mesas
- 3 clientes frecuentes
- 3 empleados
- 1 pedido de ejemplo

## 🔧 Comandos Útiles

```bash
# Ver estado de servicios
docker compose ps

# Ver logs
docker compose logs -f

# Detener servicios
docker compose down

# Reiniciar servicios
docker compose restart

# Eliminar todo (incluidos datos)
docker compose down -v
```

## 📝 Notas

- Las credenciales están en el archivo `.env`
- Los datos persisten en el volumen `postgres_data`
- El frontend es estático (HTML/CSS), ideal para aprender Docker Compose

## 👨‍💻 Autor

Proyecto de ejemplo - Bootcamp Implantación de Software  
SENA CGMLTI - 2024

```

---

## ✅ Resultado Final

Al ejecutar `docker compose up -d`, tendrás:

1. **Base de datos** funcionando con esquema completo
2. **Frontend** accesible en http://localhost
3. **Adminer** para administrar la BD en http://localhost:8080
4. **Datos de prueba** listos para consultar

Este proyecto puede ser adaptado a cualquier dominio similar (cafetería, hotel, eventos, etc.)
```
