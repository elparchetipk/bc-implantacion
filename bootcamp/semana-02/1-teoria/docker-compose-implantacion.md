# Docker Compose para Implantación de Software

## 🎯 Objetivo

Aprender a usar Docker Compose para implantar aplicaciones multi-contenedor de forma simple y reproducible, enfocándose en lo esencial para la implantación de software.

**Tiempo estimado**: 45 minutos (lectura + comprensión de ejemplos)

---

## 🤔 ¿Por qué necesitamos Docker Compose?

### Problema: Comandos Repetitivos y Propensos a Error

En la Semana 1 aprendiste a ejecutar contenedores con `docker run`. Pero, ¿qué pasa cuando necesitas múltiples contenedores?

**Ejemplo real de implantación**:

```bash
# ¿Qué? Ejecutar base de datos
docker run -d \
  --name mi-db \
  -e POSTGRES_PASSWORD=secreto123 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mi_sistema \
  -v datos_postgres:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15

# ¿Qué? Ejecutar API
docker run -d \
  --name mi-api \
  -e DATABASE_URL=postgresql://admin:secreto123@mi-db:5432/mi_sistema \
  -p 3000:3000 \
  --link mi-db \
  mi-api:1.0

# ¿Qué? Ejecutar frontend
docker run -d \
  --name mi-frontend \
  -p 80:80 \
  mi-frontend:1.0
```

**Problemas**:

- ❌ 3 comandos largos que hay que recordar
- ❌ Difícil de compartir con el equipo
- ❌ Propenso a errores de tipeo
- ❌ ¿Qué se ejecuta primero? ¿En qué orden?
- ❌ Difícil de replicar en otro servidor

---

### Solución: Docker Compose - Todo en UN Archivo

Con Docker Compose defines TODA tu aplicación en un archivo `docker-compose.yml`:

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secreto123
      POSTGRES_USER: admin
      POSTGRES_DB: mi_sistema
    volumes:
      - datos_postgres:/var/lib/postgresql/data
    ports:
      - '5432:5432'

  api:
    image: mi-api:1.0
    environment:
      DATABASE_URL: postgresql://admin:secreto123@db:5432/mi_sistema
    ports:
      - '3000:3000'
    depends_on:
      - db

  frontend:
    image: mi-frontend:1.0
    ports:
      - '80:80'

volumes:
  datos_postgres:
```

**Y lo ejecutas con UN SOLO comando**:

```bash
docker compose up -d
```

✅ **Ventajas**:

- Toda la configuración en un archivo
- Fácil de compartir (Git, USB, email)
- Reproducible (funciona igual en cualquier servidor)
- Orden automático (depends_on)
- Menos errores

---

## 📄 Sintaxis Básica de docker-compose.yml

### Estructura General

```yaml
# ¿Qué? Archivo YAML - usa indentación (2 espacios)
services: # ¿Para qué? Define los contenedores
  nombre-servicio:
    image: nombre-imagen
    # ... más configuración

volumes: # ¿Para qué? Define volúmenes para persistencia
  nombre-volumen:

networks: # ¿Para qué? Define redes (opcional, se crea una por defecto)
  nombre-red:
```

---

### 1. Services (Servicios/Contenedores)

Cada servicio es un contenedor:

```yaml
services:
  db: # ¿Qué? Nombre del servicio (lo usas para conectarte: "db:5432")
    image: postgres:15 # ¿Qué? Imagen de Docker Hub
    container_name: mi-postgres # ¿Para qué? Nombre del contenedor (opcional)

    environment: # ¿Para qué? Variables de entorno
      POSTGRES_PASSWORD: micontraseña
      POSTGRES_USER: admin
      POSTGRES_DB: base_datos

    ports: # ¿Para qué? Exponer puertos (host:contenedor)
      - '5432:5432'

    volumes: # ¿Para qué? Persistir datos
      - postgres_data:/var/lib/postgresql/data

    restart: unless-stopped # ¿Para qué? Reiniciar si falla
```

---

### 2. Environment (Variables de Entorno)

**Opción 1: Directamente en el archivo**

```yaml
services:
  api:
    image: mi-api:1.0
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_NAME: mi_base
```

**Opción 2: Usando archivo .env (MÁS SEGURO)**

```yaml
# docker-compose.yml
services:
  api:
    image: mi-api:1.0
    environment:
      DB_HOST: ${DB_HOST}
      DB_PASSWORD: ${DB_PASSWORD}
```

```bash
# .env (NO subir a Git)
DB_HOST=db
DB_PASSWORD=MiContraseñaSegura123!
```

⚠️ **Importante**: Siempre usa `.env` para contraseñas y datos sensibles.

---

### 3. Volumes (Persistencia de Datos)

**¿Para qué?** Que los datos NO se pierdan al eliminar contenedores.

```yaml
services:
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # ¿Qué? Named volume (Docker lo gestiona)

volumes:
  postgres_data: # ¿Qué? Declarar el volumen
```

**Tipos de montaje**:

```yaml
volumes:
  # ✅ Named volume (recomendado para producción)
  - postgres_data:/var/lib/postgresql/data

  # ✅ Bind mount (útil en desarrollo)
  - ./mi-codigo:/app/codigo

  # ✅ Read-only
  - ./config.json:/app/config.json:ro
```

---

### 4. Ports (Mapeo de Puertos)

```yaml
ports:
  - '8080:80' # host:contenedor
  # ¿Qué? Puerto 8080 del servidor apunta al puerto 80 del contenedor
```

**Ejemplos comunes**:

```yaml
services:
  web:
    ports:
      - '80:80' # HTTP estándar
      - '443:443' # HTTPS

  api:
    ports:
      - '3000:3000' # API Node.js

  db:
    ports:
      - '5432:5432' # PostgreSQL
```

---

### 5. Depends_on (Orden de Inicio)

```yaml
services:
  db:
    image: postgres:15

  api:
    image: mi-api:1.0
    depends_on:
      - db # ¿Para qué? API espera a que DB inicie primero
```

⚠️ **Nota**: `depends_on` solo espera a que el contenedor **inicie**, no a que esté **listo**. Para producción, usa health checks (tema avanzado).

---

## 🚀 Comandos Esenciales de Docker Compose

### 1. Levantar Servicios

```bash
# ¿Qué? Levantar todos los servicios en background
docker compose up -d

# ¿Qué? Ver logs mientras se levantan
docker compose up

# ¿Qué? Forzar recreación (después de cambios)
docker compose up -d --force-recreate
```

---

### 2. Detener y Eliminar

```bash
# ¿Qué? Detener servicios pero mantener volúmenes
docker compose down

# ⚠️ ¿Qué? Detener Y eliminar volúmenes (BORRA DATOS)
docker compose down -v
```

---

### 3. Ver Estado

```bash
# ¿Qué? Ver servicios corriendo
docker compose ps

# ¿Qué? Ver logs de todos los servicios
docker compose logs

# ¿Qué? Ver logs de UN servicio
docker compose logs db

# ¿Qué? Seguir logs en tiempo real
docker compose logs -f
```

---

### 4. Ejecutar Comandos

```bash
# ¿Qué? Ejecutar comando en contenedor corriendo
docker compose exec db psql -U admin -d mi_base

# ¿Qué? Reiniciar un servicio
docker compose restart api

# ¿Qué? Pausar servicios (sin eliminar)
docker compose pause

# ¿Qué? Reanudar servicios pausados
docker compose unpause
```

---

## 💻 Ejemplo Completo: PostgreSQL + Adminer

Este es un ejemplo completo listo para copiar y usar:

### Paso 1: Crear Estructura

```bash
mkdir mi-proyecto
cd mi-proyecto
```

### Paso 2: Crear docker-compose.yml

```yaml
# ¿Qué? Aplicación con base de datos y gestor web
services:
  # ===== BASE DE DATOS =====
  db:
    # ¿Qué? PostgreSQL versión 15 (imagen ligera Alpine)
    image: postgres:15-alpine

    # ¿Qué? Nombre del contenedor
    container_name: postgres-db

    # ¿Qué? Variables de entorno (configuración de PostgreSQL)
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}

    # ¿Qué? Persistencia de datos
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # ¿Para qué? Los datos NO se pierden al eliminar el contenedor

      - ./init-db:/docker-entrypoint-initdb.d
      # ¿Para qué? Ejecutar scripts .sql al crear la BD

    # ¿Qué? Exponer puerto (opcional, solo si necesitas conectar desde el host)
    ports:
      - '5432:5432'

    # ¿Qué? Política de reinicio
    restart: unless-stopped
    # ¿Para qué? Reiniciar automáticamente si falla

  # ===== GESTOR DE BASE DE DATOS WEB =====
  adminer:
    # ¿Qué? Adminer - Gestor de BD en navegador
    image: adminer:latest

    container_name: adminer-web

    # ¿Qué? Puerto para acceder desde navegador
    ports:
      - '8080:8080'
      # ¿Para qué? Acceder en http://localhost:8080

    restart: unless-stopped

    # ¿Qué? Esperar a que la BD inicie primero
    depends_on:
      - db

# ¿Qué? Declarar volúmenes
volumes:
  postgres_data:
    # ¿Para qué? Docker gestiona este volumen automáticamente
```

---

### Paso 3: Crear .env

```bash
# ¿Qué? Variables de entorno (NO subir a Git)
DB_USER=admin_bootcamp
DB_PASSWORD=MiContraseña2024!
DB_NAME=sistema_db
```

---

### Paso 4: Crear .gitignore

```bash
# ¿Qué? Archivo para NO subir secretos a Git
.env
.env.local
*.env
```

---

### Paso 5: (Opcional) Script de Inicialización

```bash
mkdir init-db
```

**Crear `init-db/01-crear-tablas.sql`**:

```sql
-- ¿Qué? Script que se ejecuta al crear la base de datos

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ¿Qué? Insertar datos de ejemplo
INSERT INTO usuarios (nombre, email) VALUES
    ('Juan Pérez', 'juan@example.com'),
    ('María García', 'maria@example.com')
ON CONFLICT (email) DO NOTHING;
```

---

### Paso 6: Levantar la Aplicación

```bash
# ¿Qué? Levantar todos los servicios
docker compose up -d

# Salida esperada:
# [+] Running 3/3
#  ✔ Network mi-proyecto_default    Created
#  ✔ Container postgres-db           Started
#  ✔ Container adminer-web           Started
```

---

### Paso 7: Verificar

```bash
# ¿Qué? Ver contenedores corriendo
docker compose ps

# ¿Qué? Ver logs
docker compose logs
```

**Abrir navegador**: http://localhost:8080

**Datos de conexión**:

- Sistema: `PostgreSQL`
- Servidor: `db` (nombre del servicio)
- Usuario: `admin_bootcamp` (del .env)
- Contraseña: `MiContraseña2024!` (del .env)
- Base de datos: `sistema_db` (del .env)

---

### Paso 8: Probar Persistencia

```bash
# ¿Qué? Detener y eliminar contenedores
docker compose down

# ¿Qué? Verificar que el volumen sigue existiendo
docker volume ls | grep postgres_data

# ¿Qué? Levantar de nuevo
docker compose up -d

# ✅ Los datos siguen ahí (porque usamos volumen)
```

---

## 🔧 Comunicación entre Contenedores

**¿Cómo se conectan los servicios entre sí?**

Docker Compose crea automáticamente una **red interna** donde los servicios se encuentran por **nombre**.

### Ejemplo: API conectándose a Base de Datos

```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secreto

  api:
    image: mi-api:1.0
    environment:
      # ¿Qué? Usar nombre del servicio "db" como host
      DATABASE_URL: postgresql://user:secreto@db:5432/mibd
      #                                        ↑
      #                         Nombre del servicio, NO "localhost"
```

**Regla importante**: Dentro de Docker Compose, los servicios se conectan por **nombre de servicio**, NO por `localhost`.

---

## 📋 Cheatsheet - Comandos Rápidos

```bash
# ===== BÁSICOS =====
docker compose up -d              # Levantar servicios
docker compose down               # Detener servicios
docker compose ps                 # Ver estado
docker compose logs               # Ver logs
docker compose logs -f            # Seguir logs en vivo

# ===== GESTIÓN =====
docker compose restart            # Reiniciar todos los servicios
docker compose restart api        # Reiniciar un servicio
docker compose stop               # Detener (sin eliminar)
docker compose start              # Iniciar servicios detenidos

# ===== EJECUCIÓN =====
docker compose exec db bash       # Entrar al contenedor
docker compose exec db psql -U admin -d mibd  # Ejecutar comando

# ===== LIMPIEZA =====
docker compose down -v            # Detener Y eliminar volúmenes (BORRA DATOS)
docker compose down --remove-orphans  # Eliminar contenedores huérfanos

# ===== DEBUG =====
docker compose config             # Ver configuración final (con .env expandido)
docker compose logs --tail 50     # Ver últimas 50 líneas de logs
docker compose top                # Ver procesos corriendo
```

---

## ⚠️ Errores Comunes y Soluciones

### Error 1: "Port is already allocated"

**Problema**: El puerto ya está en uso

```bash
Error: bind: address already in use
```

**Solución**: Cambiar el puerto del host

```yaml
ports:
  - '5433:5432' # Cambiar 5432 → 5433
```

---

### Error 2: "Cannot connect to database"

**Problema**: Intentas conectar con `localhost` en lugar del nombre del servicio

**❌ Mal**:

```yaml
environment:
  DB_HOST: localhost # NO funciona dentro de Docker
```

**✅ Bien**:

```yaml
environment:
  DB_HOST: db # Nombre del servicio
```

---

### Error 3: "Volume not found"

**Problema**: Eliminaste el volumen accidentalmente

**Solución**: El volumen se recrea vacío automáticamente

```bash
# Verificar volúmenes
docker volume ls

# Recrear servicios
docker compose up -d
```

---

### Error 4: Cambios en .env no se aplican

**Problema**: Docker Compose cachea variables

**Solución**: Forzar recreación

```bash
docker compose down
docker compose up -d --force-recreate
```

---

## ✅ Autoevaluación

### Pregunta 1: ¿Cuál es la ventaja principal de Docker Compose?

<details>
<summary>Ver respuesta</summary>

**Respuesta**: Definir toda la aplicación (múltiples contenedores) en UN solo archivo YAML, facilitando:

- Reproducibilidad (funciona igual en cualquier servidor)
- Facilidad de compartir (Git, documentación)
- Menos errores (no escribir comandos largos repetidamente)
- Orden automático de inicio (depends_on)

</details>

---

### Pregunta 2: ¿Cómo se conecta un servicio a otro en Docker Compose?

<details>
<summary>Ver respuesta</summary>

**Respuesta**: Usando el **nombre del servicio** como host.

Ejemplo:

```yaml
services:
  db:
    image: postgres:15

  api:
    environment:
      DB_HOST: db # ← Nombre del servicio
```

La API se conecta a `db:5432`, NO a `localhost:5432`.

</details>

---

### Pregunta 3: ¿Qué hace `docker compose down -v`?

<details>
<summary>Ver respuesta</summary>

**Respuesta**:

- Detiene todos los contenedores
- Elimina los contenedores
- **Elimina los volúmenes (BORRA DATOS)**

⚠️ **PELIGRO**: Usar con cuidado, borra datos permanentemente.

Para detener SIN borrar datos, usa solo: `docker compose down`

</details>

---

## 🎯 Resumen - Lo Esencial para Implantar

### 3 Cosas que DEBES Saber

1. **docker-compose.yml** define toda tu aplicación
2. **services** son los contenedores (db, api, frontend)
3. **volumes** persisten datos (no se pierden al eliminar contenedores)

### 5 Comandos que DEBES Memorizar

```bash
docker compose up -d        # 1. Levantar aplicación
docker compose down         # 2. Detener aplicación
docker compose ps           # 3. Ver estado
docker compose logs         # 4. Ver logs
docker compose restart      # 5. Reiniciar
```

### Template Básico para Copiar

```yaml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  db_data:
```

---

## 📌 Próximos Pasos

Ahora que entiendes Docker Compose, en la siguiente práctica:

1. Crearás tu primer `docker-compose.yml` desde cero
2. Levantarás un stack completo (PostgreSQL + Adminer)
3. Verificarás persistencia de datos
4. Adaptarás el stack a tu dominio asignado

**Continuar a**: [../2-practicas/01-stack-basico.md](../2-practicas/01-stack-basico.md)
