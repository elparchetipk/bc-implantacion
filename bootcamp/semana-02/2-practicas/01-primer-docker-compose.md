# Práctica 1: Primera Aplicación con Docker Compose

## 🎯 Objetivo

Crear tu primera aplicación multi-contenedor usando Docker Compose: PostgreSQL + Adminer (gestor de bases de datos web).

**Tiempo estimado**: 40 minutos

---

## 📋 Pre-requisitos

Antes de comenzar, verifica:

```bash
# ¿Qué? Verificar que Docker Compose está instalado
docker compose version

# Salida esperada: Docker Compose version v2.xx.x
```

---

## 📁 Estructura del Proyecto

Vamos a crear la siguiente estructura:

```
mi-primera-app/
├── docker-compose.yml
├── .env
└── init-db/
    └── 01-crear-tablas.sql
```

---

## 🚀 Parte 1: Crear el Proyecto

### Paso 1: Crear la Carpeta del Proyecto

```bash
# ¿Qué? Crear carpeta y entrar
mkdir -p ~/bootcamp/mi-primera-app
cd ~/bootcamp/mi-primera-app

# ¿Qué? Crear subcarpeta para scripts SQL
mkdir init-db
```

---

### Paso 2: Crear docker-compose.yml

```bash
# ¿Qué? Crear archivo docker-compose.yml
touch docker-compose.yml
```

**Contenido del archivo** (copiar y pegar):

```yaml
# ¿Qué? Versión del formato de Docker Compose (opcional en v2)
version: '3.8'

# ¿Qué? Definir los servicios (contenedores)
services:
  # ===== SERVICIO 1: Base de Datos PostgreSQL =====
  db:
    # ¿Qué? Imagen oficial de PostgreSQL versión 15 Alpine (ligera)
    image: postgres:15-alpine

    # ¿Qué? Nombre personalizado del contenedor
    container_name: mi-postgres

    # ¿Qué? Variables de entorno para configurar PostgreSQL
    environment:
      # ¿Para qué? Usuario de la base de datos
      POSTGRES_USER: ${DB_USER}

      # ¿Para qué? Contraseña (leer desde .env por seguridad)
      POSTGRES_PASSWORD: ${DB_PASSWORD}

      # ¿Para qué? Nombre de la base de datos a crear automáticamente
      POSTGRES_DB: ${DB_NAME}

    # ¿Qué? Mapear puertos (host:contenedor)
    ports:
      - '5432:5432'
      # ¿Para qué? Permitir conexión desde el host (pgAdmin, DBeaver, etc.)

    # ¿Qué? Volúmenes para persistencia y scripts de inicialización
    volumes:
      # ¿Para qué? Persistir datos de PostgreSQL (named volume)
      - postgres_data:/var/lib/postgresql/data

      # ¿Para qué? Ejecutar scripts SQL al crear el contenedor (bind mount)
      - ./init-db:/docker-entrypoint-initdb.d
      # ¿Cómo? PostgreSQL ejecuta automáticamente todos los .sql en esa carpeta

    # ¿Qué? Política de reinicio
    restart: unless-stopped
    # ¿Para qué? Reiniciar automáticamente si falla, excepto si se detiene manualmente

    # ¿Qué? Health check para verificar que PostgreSQL está listo
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${DB_USER}']
      # ¿Para qué? Verificar que PostgreSQL acepta conexiones
      interval: 10s
      timeout: 5s
      retries: 5
      # ¿Cómo? Intentar cada 10s, máximo 5 veces, timeout 5s

  # ===== SERVICIO 2: Adminer (Gestor de BD Web) =====
  adminer:
    # ¿Qué? Imagen oficial de Adminer
    image: adminer:latest

    # ¿Qué? Nombre personalizado del contenedor
    container_name: mi-adminer

    # ¿Qué? Mapear puerto 8080 del host al 8080 del contenedor
    ports:
      - '8080:8080'
      # ¿Para qué? Acceder a Adminer desde el navegador (http://localhost:8080)

    # ¿Qué? Política de reinicio
    restart: unless-stopped

    # ¿Qué? Dependencias entre servicios
    depends_on:
      db:
        condition: service_healthy
        # ¿Para qué? Esperar a que PostgreSQL esté saludable antes de iniciar Adminer
        # ¿Cómo? Usa el health check de 'db'

# ¿Qué? Declarar volúmenes nombrados
volumes:
  postgres_data:
    # ¿Para qué? Docker gestiona este volumen automáticamente
    # ¿Dónde? /var/lib/docker/volumes/mi-primera-app_postgres_data
```

---

### Paso 3: Crear Archivo .env

```bash
# ¿Qué? Crear archivo de variables de entorno
touch .env
```

**Contenido del archivo**:

```bash
# ¿Qué? Variables de entorno para PostgreSQL
# ¿Para qué? Evitar hardcodear credenciales en docker-compose.yml

DB_USER=admin_bootcamp
DB_PASSWORD=MiContraseñaSegura123!
DB_NAME=bootcamp_db
```

**⚠️ IMPORTANTE**: Agregar `.env` al `.gitignore` para no subirlo a Git:

```bash
# ¿Qué? Crear .gitignore
echo ".env" > .gitignore
```

---

### Paso 4: Crear Script de Inicialización SQL

```bash
# ¿Qué? Crear script SQL
touch init-db/01-crear-tablas.sql
```

**Contenido del archivo**:

```sql
-- ¿Qué? Script de inicialización de base de datos
-- ¿Para qué? Crear tablas automáticamente al levantar el contenedor

-- ¿Qué? Crear tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ¿Qué? Insertar datos de ejemplo
INSERT INTO estudiantes (nombre, apellido, email) VALUES
    ('Juan', 'Pérez', 'juan.perez@example.com'),
    ('María', 'García', 'maria.garcia@example.com'),
    ('Carlos', 'López', 'carlos.lopez@example.com');

-- ¿Qué? Crear tabla de cursos
CREATE TABLE IF NOT EXISTS cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    duracion_semanas INT NOT NULL,
    instructor VARCHAR(100)
);

-- ¿Qué? Insertar cursos de ejemplo
INSERT INTO cursos (nombre, duracion_semanas, instructor) VALUES
    ('Docker Avanzado', 8, 'Instructor SENA'),
    ('Bases de Datos', 10, 'Instructor SENA'),
    ('Desarrollo Web', 12, 'Instructor SENA');
```

---

## 🏃 Parte 2: Ejecutar la Aplicación

### Paso 5: Levantar los Servicios

```bash
# ¿Qué? Levantar todos los servicios definidos en docker-compose.yml
docker compose up -d

# ¿Para qué? -d = modo detached (background)
```

**Salida esperada**:

```
[+] Running 3/3
 ✔ Network mi-primera-app_default    Created
 ✔ Container mi-postgres             Started
 ✔ Container mi-adminer              Started
```

---

### Paso 6: Verificar que los Contenedores Están Corriendo

```bash
# ¿Qué? Ver contenedores activos
docker compose ps

# O también:
docker ps
```

**Salida esperada**:

```
NAME          IMAGE               STATUS          PORTS
mi-postgres   postgres:15-alpine  Up 30s (healthy)  0.0.0.0:5432->5432/tcp
mi-adminer    adminer:latest      Up 30s            0.0.0.0:8080->8080/tcp
```

**✅ Importante**: Verifica que el estado de `mi-postgres` sea `(healthy)`.

---

### Paso 7: Ver Logs de los Servicios

```bash
# ¿Qué? Ver logs de TODOS los servicios
docker compose logs

# ¿Qué? Ver logs de UN servicio específico
docker compose logs db

# ¿Qué? Ver logs en tiempo real (como tail -f)
docker compose logs -f

# ¿Qué? Ver últimas 20 líneas de logs
docker compose logs --tail 20
```

---

## 🌐 Parte 3: Acceder a Adminer

### Paso 8: Abrir Adminer en el Navegador

1. **Abrir navegador**: http://localhost:8080

2. **Datos de conexión**:

   - **Sistema**: PostgreSQL
   - **Servidor**: `db` (¿Por qué? Es el nombre del servicio en docker-compose.yml)
   - **Usuario**: `admin_bootcamp` (del archivo .env)
   - **Contraseña**: `MiContraseñaSegura123!` (del archivo .env)
   - **Base de datos**: `bootcamp_db` (del archivo .env)

3. **Click en "Autenticarse"**

---

### Paso 9: Verificar las Tablas

Una vez dentro de Adminer:

1. **Click en "bootcamp_db"** (barra lateral izquierda)
2. Deberías ver las tablas:
   - `estudiantes`
   - `cursos`
3. **Click en "estudiantes"** → **"Seleccionar datos"**
4. Deberías ver los 3 estudiantes insertados

---

## 🔍 Parte 4: Explorar Docker Compose

### Paso 10: Comandos Útiles

```bash
# ¿Qué? Ejecutar comando en contenedor específico
docker compose exec db psql -U admin_bootcamp -d bootcamp_db

# Dentro de psql:
\dt  -- ¿Qué? Listar tablas
SELECT * FROM estudiantes;  -- ¿Qué? Ver datos
\q  -- ¿Qué? Salir

# ¿Qué? Ver configuración final (con variables expandidas)
docker compose config

# ¿Qué? Ver uso de recursos
docker compose stats

# ¿Qué? Pausar servicios (sin eliminar)
docker compose pause

# ¿Qué? Reanudar servicios pausados
docker compose unpause
```

---

### Paso 11: Probar Persistencia de Datos

```bash
# ¿Qué? Detener y ELIMINAR contenedores
docker compose down

# ¿Qué? Ver que los contenedores ya no existen
docker ps -a | grep mi-

# ¿Qué? Verificar que el VOLUMEN sigue existiendo
docker volume ls | grep postgres_data

# ¿Qué? Levantar de nuevo los servicios
docker compose up -d

# ¿Qué? Acceder a Adminer (http://localhost:8080)
# ✅ Los datos siguen ahí! (porque usamos volumen nombrado)
```

---

## 🧹 Parte 5: Limpiar

### Paso 12: Detener y Eliminar Todo

```bash
# ¿Qué? Detener servicios (pero mantener volúmenes)
docker compose down

# ¿Qué? Detener servicios Y eliminar volúmenes (BORRA DATOS)
docker compose down -v

# ⚠️ CUIDADO: -v elimina los datos permanentemente
```

---

## 🎓 Ejercicios

### Ejercicio 1: Modificar Datos

1. Con los servicios corriendo, accede a Adminer
2. Inserta un nuevo estudiante
3. Verifica con `docker compose exec db psql -U admin_bootcamp -d bootcamp_db`
4. Ejecuta: `SELECT * FROM estudiantes;`
5. Haz `docker compose down` y `docker compose up -d`
6. Verifica que el estudiante sigue ahí

---

### Ejercicio 2: Agregar Variable de Entorno

1. Agrega al .env: `DB_PORT=5433`
2. Modifica docker-compose.yml:
   ```yaml
   ports:
     - '${DB_PORT}:5432'
   ```
3. Ejecuta `docker compose down` y `docker compose up -d`
4. Verifica que ahora el puerto del host es 5433:
   ```bash
   docker compose ps
   ```

---

### Ejercicio 3: Ver Logs en Tiempo Real

1. Abre dos terminales
2. En la Terminal 1:
   ```bash
   docker compose logs -f db
   ```
3. En la Terminal 2:
   ```bash
   docker compose exec db psql -U admin_bootcamp -d bootcamp_db -c "SELECT NOW();"
   ```
4. Observa los logs en la Terminal 1

---

## ❓ Troubleshooting

### Problema 1: Puerto 5432 ya está en uso

**Error**: `Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5432 -> 0.0.0.0:0: listen tcp 0.0.0.0:5432: bind: address already in use`

**Causa**: Ya tienes PostgreSQL instalado en tu máquina

**Solución**:

```yaml
# Cambiar puerto del host en docker-compose.yml
ports:
  - '5433:5432' # Host:Contenedor
```

---

### Problema 2: Adminer no se conecta a PostgreSQL

**Error**: "SQLSTATE[08006] [7] could not translate host name"

**Causa**: El servicio `db` no está saludable

**Solución**:

```bash
# Verificar estado de salud
docker compose ps

# Ver logs del servicio db
docker compose logs db

# Reiniciar servicios
docker compose restart
```

---

### Problema 3: Cambios en .env no se aplican

**Causa**: Docker Compose cachea las variables

**Solución**:

```bash
# Recrear contenedores forzando lectura de .env
docker compose down
docker compose up -d --force-recreate
```

---

## ✅ Criterios de Éxito

Has completado la práctica exitosamente si:

- [ ] ✅ `docker compose ps` muestra 2 contenedores corriendo
- [ ] ✅ `mi-postgres` tiene estado `(healthy)`
- [ ] ✅ Puedes acceder a Adminer en http://localhost:8080
- [ ] ✅ Puedes conectarte a PostgreSQL usando las credenciales del .env
- [ ] ✅ Ves las tablas `estudiantes` y `cursos` con datos
- [ ] ✅ Después de `docker compose down` y `up -d`, los datos persisten
- [ ] ✅ Entiendes cada línea del docker-compose.yml

---

## 🎯 Conceptos Clave Aprendidos

1. **Estructura de docker-compose.yml**: services, volumes, environment
2. **Variables de entorno**: Uso de `.env` para secretos
3. **Dependencias**: `depends_on` con health checks
4. **Volúmenes nombrados**: Persistencia automática de datos
5. **Bind mounts**: Inicialización de BD con scripts SQL
6. **Health checks**: Verificar que servicios están listos
7. **Comandos Docker Compose**: up, down, ps, logs, exec

---

## 📌 Próximos Pasos

Ahora que dominas Docker Compose básico, en la siguiente práctica crearás una **aplicación de 3 capas** con frontend, backend y base de datos.

**Continuar a**: [02-aplicacion-multicapa.md](./02-aplicacion-multicapa.md)
