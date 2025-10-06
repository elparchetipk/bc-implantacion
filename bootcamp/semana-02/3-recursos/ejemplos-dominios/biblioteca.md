# 📚 Ejemplo Dominio: Biblioteca

> **Propósito**: Proyecto de ejemplo para sistema de gestión de biblioteca  
> **Dominio**: Préstamos de libros, usuarios, multas  
> **Nivel**: Práctica 2 - Semana 2

---

## 🗄️ Base de Datos - init.sql

```sql
-- ============================================================================
-- SISTEMA DE GESTIÓN DE BIBLIOTECA
-- ============================================================================

-- ---------------------------------------------------------------------------
-- TABLA: categorias_libros
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias_libros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: autores
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS autores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    biografia TEXT,
    fecha_nacimiento DATE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: libros
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS libros (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR(13) UNIQUE NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    categoria_id INTEGER REFERENCES categorias_libros(id),
    editorial VARCHAR(100),
    año_publicacion INTEGER CHECK (año_publicacion > 1000),
    numero_paginas INTEGER CHECK (numero_paginas > 0),
    idioma VARCHAR(20) DEFAULT 'Español',
    disponible BOOLEAN DEFAULT true,
    fecha_adquisicion DATE DEFAULT CURRENT_DATE,
    ubicacion VARCHAR(20),  -- Ejemplo: 'A1-15' (Estante-Fila)
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: libros_autores (Relación muchos a muchos)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS libros_autores (
    libro_id INTEGER REFERENCES libros(id) ON DELETE CASCADE,
    autor_id INTEGER REFERENCES autores(id) ON DELETE CASCADE,
    PRIMARY KEY (libro_id, autor_id)
);

-- ---------------------------------------------------------------------------
-- TABLA: usuarios
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    numero_carnet VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT,
    tipo VARCHAR(20) DEFAULT 'regular' CHECK (tipo IN ('regular', 'estudiante', 'docente', 'vip')),
    activo BOOLEAN DEFAULT true,
    fecha_registro DATE DEFAULT CURRENT_DATE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: prestamos
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS prestamos (
    id SERIAL PRIMARY KEY,
    libro_id INTEGER REFERENCES libros(id) ON DELETE RESTRICT,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE RESTRICT,
    fecha_prestamo DATE DEFAULT CURRENT_DATE,
    fecha_devolucion_programada DATE NOT NULL,
    fecha_devolucion_real DATE,
    estado VARCHAR(20) DEFAULT 'activo' CHECK (estado IN ('activo', 'devuelto', 'vencido', 'perdido')),
    observaciones TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: multas
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS multas (
    id SERIAL PRIMARY KEY,
    prestamo_id INTEGER REFERENCES prestamos(id) ON DELETE CASCADE,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE RESTRICT,
    monto DECIMAL(10, 2) NOT NULL CHECK (monto >= 0),
    razon TEXT NOT NULL,
    pagada BOOLEAN DEFAULT false,
    fecha_multa DATE DEFAULT CURRENT_DATE,
    fecha_pago DATE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------------------------------
-- TABLA: empleados
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    puesto VARCHAR(50) NOT NULL,  -- 'Bibliotecario', 'Asistente', 'Director'
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20),
    fecha_contratacion DATE DEFAULT CURRENT_DATE,
    activo BOOLEAN DEFAULT true,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- DATOS DE PRUEBA
-- ============================================================================

-- Categorías
INSERT INTO categorias_libros (nombre, descripcion) VALUES
    ('Ficción', 'Novelas y cuentos de ficción'),
    ('Ciencia', 'Libros científicos y técnicos'),
    ('Historia', 'Libros de historia y biografías'),
    ('Programación', 'Libros sobre desarrollo de software'),
    ('Literatura Clásica', 'Obras literarias clásicas');

-- Autores
INSERT INTO autores (nombre, apellido, nacionalidad, fecha_nacimiento) VALUES
    ('Gabriel', 'García Márquez', 'Colombiana', '1927-03-06'),
    ('Isaac', 'Asimov', 'Estadounidense', '1920-01-02'),
    ('Yuval Noah', 'Harari', 'Israelí', '1976-02-24'),
    ('Robert C.', 'Martin', 'Estadounidense', '1952-12-05'),
    ('Miguel de', 'Cervantes', 'Española', '1547-09-29');

-- Libros
INSERT INTO libros (isbn, titulo, categoria_id, editorial, año_publicacion, numero_paginas, ubicacion) VALUES
    ('9780307474728', 'Cien Años de Soledad', 1, 'Editorial Sudamericana', 1967, 417, 'A1-05'),
    ('9780553293357', 'Fundación', 2, 'Gnome Press', 1951, 255, 'B2-12'),
    ('9780062316097', 'Sapiens: De animales a dioses', 3, 'Harper', 2011, 443, 'C3-08'),
    ('9780132350884', 'Clean Code', 4, 'Prentice Hall', 2008, 464, 'D4-20'),
    ('9788423974177', 'Don Quijote de la Mancha', 5, 'Real Academia Española', 1605, 863, 'E5-01'),
    ('9780553382563', 'Yo, Robot', 2, 'Gnome Press', 1950, 224, 'B2-13'),
    ('9780134685991', 'Effective Java', 4, 'Addison-Wesley', 2017, 416, 'D4-21');

-- Relación libros-autores
INSERT INTO libros_autores (libro_id, autor_id) VALUES
    (1, 1),  -- Cien Años - García Márquez
    (2, 2),  -- Fundación - Asimov
    (3, 3),  -- Sapiens - Harari
    (4, 4),  -- Clean Code - Martin
    (5, 5),  -- Don Quijote - Cervantes
    (6, 2),  -- Yo, Robot - Asimov
    (7, 4);  -- Effective Java - Martin

-- Usuarios
INSERT INTO usuarios (numero_carnet, nombre, apellido, email, telefono, tipo) VALUES
    ('USR001', 'Ana', 'Rodríguez', 'ana@ejemplo.com', '555-1001', 'estudiante'),
    ('USR002', 'Carlos', 'Mendoza', 'carlos@ejemplo.com', '555-1002', 'regular'),
    ('USR003', 'Laura', 'Jiménez', 'laura@ejemplo.com', '555-1003', 'docente'),
    ('USR004', 'Pedro', 'Sánchez', 'pedro@ejemplo.com', '555-1004', 'vip');

-- Empleados
INSERT INTO empleados (nombre, apellido, puesto, email, telefono) VALUES
    ('María', 'González', 'Director', 'maria.g@biblioteca.com', '555-2001'),
    ('Jorge', 'Ramírez', 'Bibliotecario', 'jorge.r@biblioteca.com', '555-2002'),
    ('Sofia', 'Torres', 'Asistente', 'sofia.t@biblioteca.com', '555-2003');

-- Préstamos activos
INSERT INTO prestamos (libro_id, usuario_id, fecha_prestamo, fecha_devolucion_programada, estado) VALUES
    (1, 1, '2024-01-15', '2024-02-01', 'activo'),
    (4, 2, '2024-01-20', '2024-02-05', 'activo'),
    (3, 3, '2024-01-10', '2024-01-25', 'vencido');

-- Préstamos devueltos
INSERT INTO prestamos (libro_id, usuario_id, fecha_prestamo, fecha_devolucion_programada, fecha_devolucion_real, estado) VALUES
    (2, 1, '2023-12-01', '2023-12-15', '2023-12-14', 'devuelto'),
    (5, 4, '2024-01-05', '2024-01-20', '2024-01-18', 'devuelto');

-- Multas
INSERT INTO multas (prestamo_id, usuario_id, monto, razon, pagada) VALUES
    (3, 3, 5.00, 'Devolución tardía (5 días x $1.00)', false);

-- Actualizar disponibilidad de libros prestados
UPDATE libros SET disponible = false WHERE id IN (1, 3, 4);

-- ============================================================================
-- CONSULTAS ÚTILES
-- ============================================================================

-- Ver catálogo completo con autores
SELECT
    l.titulo,
    STRING_AGG(a.nombre || ' ' || a.apellido, ', ') as autores,
    c.nombre as categoria,
    l.año_publicacion,
    CASE WHEN l.disponible THEN 'Disponible' ELSE 'Prestado' END as estado
FROM libros l
LEFT JOIN libros_autores la ON l.id = la.libro_id
LEFT JOIN autores a ON la.autor_id = a.id
LEFT JOIN categorias_libros c ON l.categoria_id = c.id
GROUP BY l.id, l.titulo, c.nombre, l.año_publicacion, l.disponible
ORDER BY l.titulo;

-- Ver préstamos activos con fechas
SELECT
    u.numero_carnet,
    u.nombre || ' ' || u.apellido as usuario,
    l.titulo as libro,
    p.fecha_prestamo,
    p.fecha_devolucion_programada,
    CASE
        WHEN p.fecha_devolucion_programada < CURRENT_DATE THEN 'VENCIDO'
        ELSE 'VIGENTE'
    END as estado_prestamo
FROM prestamos p
JOIN usuarios u ON p.usuario_id = u.id
JOIN libros l ON p.libro_id = l.id
WHERE p.estado = 'activo'
ORDER BY p.fecha_devolucion_programada;

-- Ver usuarios con multas pendientes
SELECT
    u.numero_carnet,
    u.nombre || ' ' || u.apellido as usuario,
    SUM(m.monto) as total_adeudado,
    COUNT(m.id) as cantidad_multas
FROM multas m
JOIN usuarios u ON m.usuario_id = u.id
WHERE m.pagada = false
GROUP BY u.id, u.numero_carnet, u.nombre, u.apellido
HAVING SUM(m.monto) > 0
ORDER BY total_adeudado DESC;

-- Libros más prestados
SELECT
    l.titulo,
    COUNT(p.id) as veces_prestado
FROM libros l
LEFT JOIN prestamos p ON l.id = p.libro_id
GROUP BY l.id, l.titulo
ORDER BY veces_prestado DESC
LIMIT 10;
```

---

## 🐳 Docker Compose - docker-compose.yml

```yaml
services:
  db:
    image: postgres:15-alpine
    container_name: biblioteca_db
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

  frontend:
    image: nginx:alpine
    container_name: biblioteca_frontend
    restart: unless-stopped
    volumes:
      - ./frontend:/usr/share/nginx/html:ro
    ports:
      - '80:80'
    depends_on:
      db:
        condition: service_healthy

  adminer:
    image: adminer:latest
    container_name: biblioteca_adminer
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
DB_NAME=biblioteca_db
DB_USER=admin_biblioteca
DB_PASSWORD=BibliotecaSegura2024!
```

---

## 🎨 Frontend - index.html (Ejemplo simplificado)

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>Sistema de Gestión - Biblioteca</title>
    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 2rem;
      }
      .container {
        max-width: 1200px;
        margin: 0 auto;
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
      }
      h1 {
        color: #667eea;
        margin-bottom: 1rem;
      }
      .stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
      }
      .stat {
        background: #f0f0f0;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
      }
      .stat h3 {
        color: #667eea;
        font-size: 2rem;
        margin-bottom: 0.5rem;
      }
      .btn {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 1rem 2rem;
        text-decoration: none;
        border-radius: 5px;
        margin: 1rem 0;
      }
      .btn:hover {
        background: #764ba2;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>📚 Sistema de Gestión de Biblioteca</h1>
      <p>Bienvenido al sistema de administración de libros y préstamos</p>

      <div class="stats">
        <div class="stat">
          <h3>7</h3>
          <p>Libros Registrados</p>
        </div>
        <div class="stat">
          <h3>4</h3>
          <p>Usuarios Activos</p>
        </div>
        <div class="stat">
          <h3>3</h3>
          <p>Préstamos Activos</p>
        </div>
        <div class="stat">
          <h3>$5.00</h3>
          <p>Multas Pendientes</p>
        </div>
      </div>

      <h2>🔗 Acceso al Sistema</h2>
      <a
        href="http://localhost:8080"
        target="_blank"
        class="btn">
        Abrir Adminer (Base de Datos)
      </a>

      <h3>Credenciales:</h3>
      <ul>
        <li>Servidor: <code>db</code></li>
        <li>Usuario: <code>admin_biblioteca</code></li>
        <li>Contraseña: <code>BibliotecaSegura2024!</code></li>
        <li>Base de datos: <code>biblioteca_db</code></li>
      </ul>
    </div>
  </body>
</html>
```

---

## ✅ Características Principales

- **8 Tablas**: Completo esquema relacional
- **Relaciones M:M**: Libros-Autores
- **Datos realistas**: 7 libros, 5 autores, 4 usuarios
- **Préstamos activos**: Con fechas y estados
- **Multas**: Sistema de penalización por retraso
- **Consultas útiles**: Queries SQL de ejemplo incluidas

Este dominio puede adaptarse a: videoteca, ludoteca, centro de documentación, etc.
