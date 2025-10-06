# Práctica 1: Stack Básico con Docker Compose

## 🎯 Objetivo

Crear tu primer stack completo usando Docker Compose: PostgreSQL + Adminer, comprendiendo los conceptos fundamentales de forma práctica.

**Tiempo estimado**: 45 minutos

---

## 📋 Pre-requisitos

```bash
# Verificar que Docker Compose está instalado
docker compose version
# Salida esperada: Docker Compose version v2.xx.x
```

---

## 📁 Parte 1: Preparar el Proyecto (5 min)

### Paso 1: Crear Estructura

```bash
# ¿Qué? Crear carpeta del proyecto
mkdir -p ~/bootcamp/stack-basico
cd ~/bootcamp/stack-basico

# ¿Qué? Crear subcarpeta para scripts SQL
mkdir init-db
```

---

## 📝 Parte 2: Crear Archivos (15 min)

### Paso 2: Crear docker-compose.yml

```bash
# ¿Qué? Crear archivo principal
touch docker-compose.yml
```

**Contenido** (copiar y pegar):

```yaml
# ¿Qué? Definir servicios (contenedores) de la aplicación
services:

  # ===== SERVICIO 1: PostgreSQL =====
  db:
    # ¿Qué? Imagen oficial de PostgreSQL 15 (versión Alpine = ligera)
    image: postgres:15-alpine
    
    # ¿Qué? Nombre del contenedor (opcional pero recomendado)
    container_name: stack-postgres
    
    # ¿Qué? Variables de entorno para configurar PostgreSQL
    environment:
      POSTGRES_USER: ${DB_USER}
      # ¿Para qué? Leer la variable desde el archivo .env
      
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      # ¿Para qué? No hardcodear la contraseña en este archivo
      
      POSTGRES_DB: ${DB_NAME}
      # ¿Para qué? Nombre de la base de datos a crear
    
    # ¿Qué? Mapeo de puertos (host:contenedor)
    ports:
      - "5432:5432"
      # ¿Para qué? Acceder desde pgAdmin, DBeaver, o terminal del host
    
    # ¿Qué? Volúmenes para persistencia
    volumes:
      # Named volume para datos de PostgreSQL
      - postgres_data:/var/lib/postgresql/data
      # ¿Para qué? Los datos NO se pierden al eliminar el contenedor
      
      # Bind mount para scripts de inicialización
      - ./init-db:/docker-entrypoint-initdb.d
      # ¿Para qué? Ejecutar scripts .sql automáticamente al crear la BD
    
    # ¿Qué? Política de reinicio
    restart: unless-stopped
    # ¿Para qué? Reiniciar automáticamente si falla (excepto si lo detienes manualmente)

  # ===== SERVICIO 2: Adminer =====
  adminer:
    # ¿Qué? Gestor de bases de datos web (alternativa ligera a phpMyAdmin)
    image: adminer:latest
    
    container_name: stack-adminer
    
    # ¿Qué? Exponer puerto para acceder desde navegador
    ports:
      - "8080:8080"
      # ¿Para qué? Abrir http://localhost:8080 en el navegador
    
    restart: unless-stopped
    
    # ¿Qué? Dependencias de servicios
    depends_on:
      - db
      # ¿Para qué? Adminer espera a que PostgreSQL inicie primero

# ¿Qué? Declarar volúmenes nombrados
volumes:
  postgres_data:
    # ¿Para qué? Docker gestiona este volumen automáticamente
    # ¿Dónde? /var/lib/docker/volumes/stack-basico_postgres_data
```

---

### Paso 3: Crear .env

```bash
# ¿Qué? Archivo de variables de entorno (secretos)
touch .env
```

**Contenido**:

```bash
# ¿Qué? Variables para PostgreSQL
# ¿Para qué? NO hardcodear contraseñas en docker-compose.yml

DB_USER=admin_bootcamp
DB_PASSWORD=Bootcamp2024Seguro!
DB_NAME=sistema_bootcamp
```

**⚠️ IMPORTANTE**: Este archivo contiene contraseñas, NO debe subirse a Git.

---

### Paso 4: Crear .gitignore

```bash
# ¿Qué? Archivo para ignorar en Git
echo ".env" > .gitignore
```

---

### Paso 5: Crear Script SQL de Inicialización

```bash
# ¿Qué? Crear script de base de datos
touch init-db/01-crear-tablas.sql
```

**Contenido**:

```sql
-- ¿Qué? Script que se ejecuta automáticamente al crear la base de datos
-- ¿Para qué? Inicializar tablas con datos de ejemplo

-- ¿Qué? Crear tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ¿Qué? Insertar datos de ejemplo
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
    ('Laptop', 'Laptop HP 15 pulgadas', 1200.00, 10),
    ('Mouse', 'Mouse inalámbrico', 25.50, 50),
    ('Teclado', 'Teclado mecánico RGB', 85.00, 30),
    ('Monitor', 'Monitor 24 pulgadas Full HD', 300.00, 15)
ON CONFLICT DO NOTHING;
-- ¿Para qué? Si ya existen (al reiniciar), no duplicar

-- ¿Qué? Crear tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ¿Qué? Insertar clientes de ejemplo
INSERT INTO clientes (nombre, email, telefono) VALUES
    ('Juan Pérez', 'juan@example.com', '3001234567'),
    ('María García', 'maria@example.com', '3009876543')
ON CONFLICT (email) DO NOTHING;
```

---

## 🚀 Parte 3: Ejecutar el Stack (10 min)

### Paso 6: Levantar los Servicios

```bash
# ¿Qué? Levantar todos los servicios en background
docker compose up -d
```

**Salida esperada**:

```
[+] Running 3/3
 ✔ Network stack-basico_default    Created
 ✔ Container stack-postgres         Started
 ✔ Container stack-adminer          Started
```

---

### Paso 7: Verificar que Todo Funciona

```bash
# ¿Qué? Ver contenedores corriendo
docker compose ps
```

**Deberías ver**:

```
NAME              IMAGE                  STATUS
stack-postgres    postgres:15-alpine     Up (healthy)
stack-adminer     adminer:latest         Up
```

---

### Paso 8: Ver Logs

```bash
# ¿Qué? Ver logs de todos los servicios
docker compose logs

# ¿Qué? Ver logs solo de PostgreSQL
docker compose logs db

# ¿Qué? Seguir logs en tiempo real
docker compose logs -f
# Presionar Ctrl+C para salir
```

---

## 🌐 Parte 4: Acceder a Adminer (10 min)

### Paso 9: Abrir Adminer en el Navegador

1. Abrir navegador: **http://localhost:8080**

2. **Datos de conexión**:
   - **Sistema**: PostgreSQL
   - **Servidor**: `db` (¿Por qué? Es el nombre del servicio en docker-compose.yml)
   - **Usuario**: `admin_bootcamp` (del archivo .env)
   - **Contraseña**: `Bootcamp2024Seguro!` (del archivo .env)
   - **Base de datos**: `sistema_bootcamp` (del archivo .env)

3. Click en **"Autenticarse"**

---

### Paso 10: Explorar las Tablas

Una vez dentro:

1. **Click en "sistema_bootcamp"** (lado izquierdo)
2. Verás las tablas: `productos` y `clientes`
3. **Click en "productos"** → **"Seleccionar datos"**
4. Deberías ver los 4 productos insertados

---

### Paso 11: Probar Consultas SQL

En la pestaña **"Comando SQL"**:

```sql
-- ¿Qué? Ver todos los productos con stock > 20
SELECT * FROM productos WHERE stock > 20;

-- ¿Qué? Insertar nuevo producto
INSERT INTO productos (nombre, descripcion, precio, stock)
VALUES ('WebCam', 'WebCam Full HD 1080p', 65.00, 25);

-- ¿Qué? Ver productos ordenados por precio
SELECT nombre, precio FROM productos ORDER BY precio DESC;
```

---

## 🔍 Parte 5: Comandos Útiles (5 min)

### Conectarse a PostgreSQL desde Terminal

```bash
# ¿Qué? Ejecutar psql dentro del contenedor
docker compose exec db psql -U admin_bootcamp -d sistema_bootcamp

# Dentro de psql:
\dt                          # ¿Qué? Listar tablas
\d productos                 # ¿Qué? Describir tabla productos
SELECT * FROM clientes;      # ¿Qué? Ver clientes
\q                          # ¿Qué? Salir
```

---

### Ver Configuración Final

```bash
# ¿Qué? Ver docker-compose.yml con variables .env expandidas
docker compose config
```

---

### Reiniciar un Servicio

```bash
# ¿Qué? Reiniciar solo PostgreSQL
docker compose restart db

# ¿Qué? Reiniciar todos los servicios
docker compose restart
```

---

## 🧪 Parte 6: Probar Persistencia (10 min)

### Paso 12: Agregar Datos Personalizados

1. En Adminer, agregar 3 productos más (inventa los datos)
2. Verificar que se guardaron

---

### Paso 13: Detener y Eliminar Contenedores

```bash
# ¿Qué? Detener servicios PERO mantener volúmenes
docker compose down

# ¿Qué? Verificar que contenedores ya no existen
docker ps -a | grep stack
# No debería aparecer nada

# ¿Qué? Verificar que el VOLUMEN sigue existiendo
docker volume ls | grep postgres_data
# Debería aparecer: stack-basico_postgres_data
```

---

### Paso 14: Levantar de Nuevo y Verificar

```bash
# ¿Qué? Levantar servicios de nuevo
docker compose up -d

# ¿Qué? Abrir Adminer (http://localhost:8080)
# ✅ Tus datos personalizados siguen ahí!
# ¿Por qué? Porque usamos volumen (persistencia)
```

---

## 🧹 Limpiar (Opcional)

```bash
# ¿Qué? Detener Y eliminar volúmenes (BORRA DATOS)
docker compose down -v

# ⚠️ CUIDADO: Esto borra TODOS los datos permanentemente
```

---

## ✅ Criterios de Éxito

Has completado la práctica si:

- [ ] ✅ `docker compose ps` muestra 2 contenedores corriendo
- [ ] ✅ Puedes acceder a Adminer en http://localhost:8080
- [ ] ✅ Ves las tablas `productos` y `clientes` con datos
- [ ] ✅ Puedes ejecutar consultas SQL en Adminer
- [ ] ✅ Después de `docker compose down` y `up -d`, los datos persisten
- [ ] ✅ Entiendes cada línea del docker-compose.yml

---

## 🎓 Ejercicios Extra (Opcional)

### Ejercicio 1: Agregar Otra Tabla

Crea `init-db/02-pedidos.sql`:

```sql
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    producto_id INT REFERENCES productos(id),
    cantidad INT NOT NULL,
    total DECIMAL(10, 2),
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Reinicia: `docker compose down && docker compose up -d`

---

### Ejercicio 2: Cambiar Puerto

Modifica docker-compose.yml:

```yaml
ports:
  - "5433:5432"  # Cambiar puerto del host
```

Aplica: `docker compose down && docker compose up -d`

---

### Ejercicio 3: Ver Uso de Recursos

```bash
# ¿Qué? Ver CPU y RAM que usan los contenedores
docker compose stats
```

---

## ❓ Troubleshooting

### Error: "port is already allocated"

**Solución**: Cambiar puerto en docker-compose.yml:

```yaml
ports:
  - "5433:5432"  # Usar otro puerto
```

---

### Error: "cannot connect to database"

**Causa**: Las variables .env están mal

**Solución**: Verificar .env y recrear:

```bash
docker compose down
docker compose up -d --force-recreate
```

---

### No veo los datos en Adminer

**Solución**: Verificar que usaste el nombre correcto del servicio:
- Servidor debe ser: `db` (NO `localhost`)

---

## 📌 Conceptos Clave Aprendidos

1. ✅ **docker-compose.yml** define servicios, volúmenes y configuración
2. ✅ **services** son los contenedores (db, adminer)
3. ✅ **volumes** persisten datos (no se pierden)
4. ✅ **.env** almacena variables de entorno (secretos)
5. ✅ **depends_on** controla orden de inicio
6. ✅ Los servicios se conectan por **nombre** (db, adminer)

---

## 🚀 Próximos Pasos

¡Excelente! Ahora dominas Docker Compose básico. En la siguiente práctica adaptarás este stack a tu **dominio asignado** específico.

**Continuar a**: [02-proyecto-dominio.md](./02-proyecto-dominio.md)
