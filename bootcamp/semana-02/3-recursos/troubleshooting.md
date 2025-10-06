# 🔧 Troubleshooting - Solución de Problemas Comunes

> **Propósito**: Guía de resolución de problemas más frecuentes en Docker Compose  
> **Audiencia**: Tecnólogos ADSO - Implantación de software  
> **Metodología**: Problema → Causa → Solución paso a paso

---

## 📋 Índice Rápido

| # | Problema | Página |
|---|----------|--------|
| 1 | [Puerto ya está en uso](#1-puerto-ya-está-en-uso) | ↓ |
| 2 | [Conexión rechazada (Connection refused)](#2-conexión-rechazada-connection-refused) | ↓ |
| 3 | [Adminer no puede conectar a PostgreSQL](#3-adminer-no-puede-conectar-a-postgresql) | ↓ |
| 4 | [Cambios en .env no se aplican](#4-cambios-en-env-no-se-aplican) | ↓ |
| 5 | [Contenedor se reinicia constantemente](#5-contenedor-se-reinicia-constantemente) | ↓ |
| 6 | [Volumen con permisos denegados](#6-volumen-con-permisos-denegados) | ↓ |
| 7 | [Init.sql no se ejecuta](#7-initsql-no-se-ejecuta) | ↓ |
| 8 | [Frontend muestra 403 Forbidden](#8-frontend-muestra-403-forbidden) | ↓ |
| 9 | [Servicio marcado como "unhealthy"](#9-servicio-marcado-como-unhealthy) | ↓ |
| 10 | [Los datos se pierden al reiniciar](#10-los-datos-se-pierden-al-reiniciar) | ↓ |
| 11 | [Error de sintaxis en docker-compose.yml](#11-error-de-sintaxis-en-docker-composeyml) | ↓ |
| 12 | [No se puede descargar la imagen](#12-no-se-puede-descargar-la-imagen) | ↓ |

---

## 1. Puerto ya está en uso

### 🔴 Síntoma

```bash
Error: Bind for 0.0.0.0:5432 failed: port is already allocated
```

Al ejecutar `docker compose up -d`, aparece este error y el servicio no inicia.

### 🧠 Causa

El puerto especificado (ej: 5432 para PostgreSQL, 8080 para Adminer) ya está siendo usado por:
- Otro contenedor Docker
- Una aplicación en el sistema host (PostgreSQL instalado localmente)
- Otro proyecto de Docker Compose

### ✅ Solución

**Opción 1: Cambiar el puerto en `docker-compose.yml`** (⭐ Recomendado)

```yaml
services:
  db:
    image: postgres:15-alpine
    ports:
      - "5433:5432"  # ✅ Usar 5433 en el host en lugar de 5432
```

**Cambios**:
- `5433:5432` significa: host:5433 → contenedor:5432
- Desde el host, conectar a `localhost:5433`
- Desde otros contenedores, seguir usando el nombre del servicio `db` (no cambia)

**Opción 2: Detener el servicio que ocupa el puerto**

```bash
# Ver qué proceso está usando el puerto 5432
sudo lsof -i :5432

# O con netstat
sudo netstat -tuln | grep 5432

# Detener el servicio (ejemplo: PostgreSQL instalado localmente)
sudo systemctl stop postgresql
```

**Opción 3: No exponer el puerto (si no lo necesitas)**

```yaml
services:
  db:
    image: postgres:15-alpine
    # ports:
    #   - "5432:5432"  # ❌ Comentar o eliminar
```

**¿Cuándo usar cada opción?**
- **Opción 1**: Si necesitas acceder desde el host (pgAdmin, DBeaver)
- **Opción 2**: Si estás en desarrollo y no necesitas el servicio local
- **Opción 3**: Si solo necesitas acceso desde otros contenedores (más seguro)

---

## 2. Conexión rechazada (Connection refused)

### 🔴 Síntoma

```bash
Error: connect ECONNREFUSED localhost:5432
Error: Connection refused - connect(2) for "localhost" port 5432
```

Tu aplicación (backend) no puede conectar a la base de datos.

### 🧠 Causa

Estás usando `localhost` o `127.0.0.1` para conectar a otro contenedor. Dentro de Docker, cada contenedor tiene su propio `localhost`.

### ✅ Solución

**Usar el nombre del servicio en lugar de `localhost`**

```yaml
# ❌ INCORRECTO:
environment:
  DB_HOST: localhost        # ❌ Apunta al mismo contenedor
  DB_HOST: 127.0.0.1       # ❌ Apunta al mismo contenedor

# ✅ CORRECTO:
environment:
  DB_HOST: db              # ✅ Apunta al servicio 'db'
```

**Verificación**:

```bash
# Desde el backend, hacer ping al servicio db
docker compose exec backend ping db

# Debería responder:
# PING db (172.18.0.2): 56 data bytes
# 64 bytes from 172.18.0.2: icmp_seq=0 ttl=64 time=0.123 ms
```

**Ejemplo completo**:

```yaml
services:
  backend:
    image: node:18-alpine
    environment:
      DB_HOST: db          # ✅ Nombre del servicio
      DB_PORT: 5432        # ✅ Puerto interno del contenedor
      DB_NAME: mi_base
      DB_USER: admin
      DB_PASSWORD: password
  
  db:
    image: postgres:15-alpine
    # ...
```

**⚠️ Excepción**: Desde tu navegador o herramientas en tu PC, SÍ debes usar `localhost`:

```javascript
// ✅ En frontend (navegador), conectar al backend:
fetch('http://localhost:3000/api/users')

// ❌ Esto NO funciona desde el navegador:
fetch('http://backend:3000/api/users')
```

---

## 3. Adminer no puede conectar a PostgreSQL

### 🔴 Síntoma

En Adminer (`http://localhost:8080`), al intentar conectar aparece:
```
Connection to database has been refused
SQLSTATE[08006] Unable to connect to PostgreSQL server
```

### 🧠 Causa

- Credenciales incorrectas en `.env`
- Usar `localhost` como servidor en Adminer
- PostgreSQL no ha terminado de inicializar
- Falta el `depends_on` con healthcheck

### ✅ Solución

**Paso 1: Verificar credenciales en `.env`**

```bash
# Ver las variables de entorno del contenedor
docker compose exec db env | grep POSTGRES

# Debería mostrar:
# POSTGRES_DB=mi_base_datos
# POSTGRES_USER=admin
# POSTGRES_PASSWORD=mi_password
```

**Paso 2: En Adminer, usar el nombre del servicio**

Al conectar en `http://localhost:8080`, llenar el formulario así:

| Campo | Valor |
|-------|-------|
| **Sistema** | PostgreSQL |
| **Servidor** | `db` ✅ (nombre del servicio, NO `localhost`) |
| **Usuario** | (valor de `DB_USER` en `.env`) |
| **Contraseña** | (valor de `DB_PASSWORD` en `.env`) |
| **Base de datos** | (valor de `DB_NAME` en `.env`) |

**Paso 3: Verificar que PostgreSQL esté listo**

```bash
# Ver logs de PostgreSQL
docker compose logs -f db

# Buscar esta línea:
# database system is ready to accept connections
```

**Paso 4: Asegurar `depends_on` con healthcheck**

```yaml
services:
  adminer:
    image: adminer:latest
    depends_on:
      db:
        condition: service_healthy  # ✅ Esperar a que DB esté saludable
  
  db:
    image: postgres:15-alpine
    healthcheck:  # ✅ Definir cómo verificar salud
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5
```

**Paso 5: Reiniciar servicios en orden**

```bash
# Detener todo
docker compose down

# Iniciar solo DB primero (verificar que funcione)
docker compose up -d db

# Ver logs hasta que diga "ready to accept connections"
docker compose logs -f db

# Iniciar Adminer
docker compose up -d adminer
```

---

## 4. Cambios en .env no se aplican

### 🔴 Síntoma

Modificas el archivo `.env`, reinicias con `docker compose up -d`, pero las variables siguen teniendo los valores antiguos.

### 🧠 Causa

Docker Compose cachea las variables de entorno al crear los contenedores. Reiniciar (`up -d`) no recrea los contenedores.

### ✅ Solución

**Opción 1: Recrear contenedores** (⭐ Recomendado)

```bash
# Detener y eliminar contenedores
docker compose down

# Volver a crear con nuevas variables
docker compose up -d
```

**Opción 2: Forzar recreación**

```bash
# Recrear contenedores aunque no haya cambios en el YAML
docker compose up -d --force-recreate
```

**Opción 3: Recrear solo un servicio específico**

```bash
# Solo recrear el servicio 'backend'
docker compose up -d --force-recreate backend
```

**Verificación**:

```bash
# Ver las variables de entorno del contenedor
docker compose exec db env

# Deberían reflejar los nuevos valores de .env
```

**💡 Tip**: Para cambios en código (no en `.env`), NO necesitas recrear:

```yaml
volumes:
  - ./backend:/app  # Los cambios en código se reflejan automáticamente
```

---

## 5. Contenedor se reinicia constantemente

### 🔴 Síntoma

Al ejecutar `docker compose ps`, ves:

```
NAME        STATUS
backend     Restarting (1) 5 seconds ago
```

El contenedor inicia, falla, se reinicia, falla de nuevo (ciclo infinito).

### 🧠 Causa

- Error en el código de la aplicación (crash al iniciar)
- Comando incorrecto en `command:`
- Puerto ya ocupado dentro del contenedor
- Dependencia no disponible (DB no lista)

### ✅ Solución

**Paso 1: Ver los logs del contenedor**

```bash
# Ver los últimos logs antes del crash
docker compose logs backend

# Buscar errores, excepciones, stack traces
```

**Paso 2: Comprobar el estado detallado**

```bash
# Ver eventos y razón del restart
docker compose events backend
```

**Paso 3: Cambiar restart policy temporalmente**

```yaml
services:
  backend:
    image: node:18-alpine
    restart: "no"  # ✅ Deshabilitar restart para depurar
    # restart: unless-stopped  # ❌ Comentar temporalmente
```

Ahora el contenedor NO se reiniciará y podrás ver el error completo:

```bash
docker compose up backend
```

**Paso 4: Soluciones según el error**

**Error común 1: "Cannot find module"** (Node.js)

```bash
# Solución: Instalar dependencias
cd backend
npm install

# Reiniciar
docker compose restart backend
```

**Error común 2: "Port already in use"**

```yaml
# Cambiar el puerto del servicio
services:
  backend:
    ports:
      - "3001:3000"  # Usar 3001 en lugar de 3000
```

**Error común 3: "Cannot connect to database"**

```yaml
# Asegurar que backend espere a que DB esté lista
services:
  backend:
    depends_on:
      db:
        condition: service_healthy  # ✅ Esperar a healthcheck
```

**Paso 5: Volver a habilitar restart**

Una vez solucionado el problema:

```yaml
services:
  backend:
    restart: unless-stopped  # ✅ Restaurar restart policy
```

---

## 6. Volumen con permisos denegados

### 🔴 Síntoma

```bash
Error: EACCES: permission denied, open '/app/data/file.txt'
Error: mkdir: cannot create directory '/var/lib/postgresql/data': Permission denied
```

El contenedor no puede leer/escribir en un volumen montado.

### 🧠 Causa

- Permisos incorrectos en la carpeta del host
- Usuario del contenedor no coincide con el dueño de la carpeta
- SELinux bloqueando el acceso (en sistemas RHEL/CentOS)

### ✅ Solución

**Opción 1: Cambiar permisos de la carpeta** (⭐ Más común)

```bash
# Dar permisos de lectura/escritura/ejecución
chmod -R 755 ./backend

# O permisos totales (menos seguro, pero funciona siempre)
chmod -R 777 ./backend
```

**Opción 2: Cambiar el dueño de la carpeta**

```bash
# Cambiar dueño al usuario actual
sudo chown -R $USER:$USER ./backend

# O al usuario del contenedor (ej: UID 1000)
sudo chown -R 1000:1000 ./backend
```

**Opción 3: Usar `:Z` o `:z` en el volumen (SELinux)**

```yaml
volumes:
  - ./backend:/app:z  # :z para compartido entre contenedores
  - ./backend:/app:Z  # :Z para privado de este contenedor
```

**Opción 4: Ejecutar contenedor como root (NO recomendado en producción)**

```yaml
services:
  backend:
    user: "0:0"  # UID:GID (0 = root)
    volumes:
      - ./backend:/app
```

**Verificación**:

```bash
# Ver permisos de la carpeta
ls -la ./backend

# Debería mostrar:
# drwxr-xr-x  5 usuario grupo 4096 Feb 10 10:30 backend
```

---

## 7. Init.sql no se ejecuta

### 🔴 Síntoma

Colocas un archivo `init.sql` en el volumen, pero las tablas no se crean al iniciar PostgreSQL.

### 🧠 Causa

- El volumen de datos ya existe de una ejecución anterior
- PostgreSQL solo ejecuta scripts en `/docker-entrypoint-initdb.d/` la primera vez
- Ruta del volumen incorrecta
- Sintaxis SQL con errores

### ✅ Solución

**Paso 1: Eliminar el volumen existente**

```bash
# Detener y eliminar contenedores + volúmenes
docker compose down -v

# ⚠️ Esto BORRA todos los datos de la BD
```

**Paso 2: Verificar la ruta del script**

```yaml
services:
  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # ✅ Ruta correcta para scripts de inicialización:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
      #   ↑ Local    ↑ Dentro del contenedor            ↑ Solo lectura
```

**Paso 3: Verificar sintaxis del SQL**

```sql
-- init.sql

-- ✅ CORRECTO: Usar IF NOT EXISTS
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- ❌ INCORRECTO: Sin IF NOT EXISTS falla al reintentar
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
```

**Paso 4: Ver logs de inicialización**

```bash
# Iniciar y ver logs en tiempo real
docker compose up -d db
docker compose logs -f db

# Buscar en los logs:
# /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql
# ✅ Si aparece, el script se ejecutó
```

**Paso 5: Verificar que las tablas se crearon**

```bash
# Conectar a PostgreSQL
docker compose exec db psql -U admin -d mi_base_datos

# Listar tablas
\dt

# Debería mostrar las tablas creadas por init.sql
```

**💡 Tip**: Para ejecutar scripts después de la inicialización:

```bash
# Ejecutar SQL manualmente
docker compose exec db psql -U admin -d mi_base_datos -f /scripts/update.sql

# O desde el host
cat update.sql | docker compose exec -T db psql -U admin -d mi_base_datos
```

---

## 8. Frontend muestra 403 Forbidden

### 🔴 Síntoma

Al acceder a `http://localhost` (Nginx), aparece:

```
403 Forbidden
nginx/1.25.3
```

### 🧠 Causa

- No existe `index.html` en la carpeta montada
- Permisos incorrectos en la carpeta `frontend/`
- Nginx busca `index.html` y no lo encuentra

### ✅ Solución

**Paso 1: Verificar que exista `index.html`**

```bash
# Listar archivos en la carpeta frontend
ls -la ./frontend/

# Debe existir index.html
# -rw-r--r-- 1 usuario grupo  512 Feb 10 10:30 index.html
```

**Paso 2: Crear `index.html` si no existe**

```bash
# Crear archivo index.html básico
cat > ./frontend/index.html << 'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Aplicación</title>
</head>
<body>
    <h1>¡Funciona!</h1>
    <p>Frontend corriendo correctamente</p>
</body>
</html>
EOF
```

**Paso 3: Verificar permisos**

```bash
# Dar permisos de lectura
chmod -R 755 ./frontend/
```

**Paso 4: Verificar la ruta del volumen**

```yaml
services:
  frontend:
    image: nginx:alpine
    volumes:
      # ✅ CORRECTO:
      - ./frontend:/usr/share/nginx/html:ro
      
      # ❌ INCORRECTO:
      # - ./frontend:/app  # Nginx no busca ahí
```

**Paso 5: Ver logs de Nginx**

```bash
docker compose logs -f frontend

# Buscar errores como:
# [error] 7#7: *1 directory index of "/usr/share/nginx/html/" is forbidden
```

**Paso 6: Reiniciar Nginx**

```bash
docker compose restart frontend
```

---

## 9. Servicio marcado como "unhealthy"

### 🔴 Síntoma

Al ejecutar `docker compose ps`:

```
NAME    STATUS
db      Up 2 minutes (unhealthy)
```

El contenedor está corriendo, pero marcado como no saludable.

### 🧠 Causa

- El healthcheck falla (comando devuelve error)
- PostgreSQL aún está inicializando
- Credenciales incorrectas en el healthcheck
- Timeout muy corto

### ✅ Solución

**Paso 1: Ver el comando healthcheck**

```yaml
services:
  db:
    image: postgres:15-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      #                                 ↑ Asegurar que coincida con POSTGRES_USER
      interval: 10s   # Cada cuánto se ejecuta
      timeout: 5s     # Tiempo máximo de espera
      retries: 5      # Intentos antes de marcar unhealthy
      start_period: 30s  # Tiempo de gracia al iniciar
```

**Paso 2: Ejecutar el healthcheck manualmente**

```bash
# Ejecutar el comando dentro del contenedor
docker compose exec db pg_isready -U admin -d mi_base_datos

# ✅ Si funciona, debería mostrar:
# localhost:5432 - accepting connections

# ❌ Si falla:
# pg_isready: could not connect to database
```

**Paso 3: Ver logs del healthcheck**

```bash
# Ver logs del contenedor
docker compose logs -f db

# Buscar líneas con "healthcheck"
```

**Paso 4: Ajustar timeouts**

Si la DB tarda en inicializar:

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
  interval: 15s           # ✅ Aumentar intervalo
  timeout: 10s            # ✅ Aumentar timeout
  retries: 10             # ✅ Más intentos
  start_period: 60s       # ✅ Más tiempo de gracia
```

**Paso 5: Verificar credenciales**

```bash
# Las credenciales en healthcheck deben coincidir con POSTGRES_*
docker compose exec db env | grep POSTGRES

# POSTGRES_USER debe coincidir con -U en pg_isready
# POSTGRES_DB debe coincidir con -d en pg_isready
```

**Paso 6: Simplificar el healthcheck (temporal)**

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready"]  # ✅ Sin especificar usuario/DB
  interval: 10s
  timeout: 5s
  retries: 5
```

---

## 10. Los datos se pierden al reiniciar

### 🔴 Síntoma

Creas tablas, insertas datos, detienes Docker Compose (`docker compose down`), vuelves a iniciar... y los datos desaparecieron.

### 🧠 Causa

- No estás usando volúmenes named
- Usaste `docker compose down -v` (elimina volúmenes)
- El volumen apunta a la ruta incorrecta
- Bind mount en lugar de named volume

### ✅ Solución

**Opción 1: Usar named volumes** (⭐ Recomendado)

```yaml
services:
  db:
    image: postgres:15-alpine
    volumes:
      # ✅ Named volume (persiste datos)
      - postgres_data:/var/lib/postgresql/data

# ✅ Declarar el volumen al final
volumes:
  postgres_data:
    driver: local
```

**Opción 2: Usar bind mount con ruta absoluta**

```yaml
services:
  db:
    image: postgres:15-alpine
    volumes:
      # ✅ Bind mount (carpeta local)
      - ./postgres_data:/var/lib/postgresql/data
```

**⚠️ Evitar**:

```yaml
# ❌ Sin declarar volumen (se pierde al hacer 'down')
services:
  db:
    volumes:
      - /var/lib/postgresql/data  # SIN nombre, se borra

# ❌ Usar 'down -v' elimina los volúmenes
docker compose down -v  # BORRA DATOS
```

**Verificación**:

```bash
# Listar volúmenes
docker volume ls

# Debería aparecer:
# DRIVER    VOLUME NAME
# local     mi-proyecto_postgres_data

# Ver detalles del volumen
docker volume inspect mi-proyecto_postgres_data
```

**Probar persistencia**:

```bash
# 1. Crear datos
docker compose exec db psql -U admin -d mi_base_datos
CREATE TABLE test (id SERIAL, nombre VARCHAR(50));
INSERT INTO test (nombre) VALUES ('dato de prueba');
\q

# 2. Detener (SIN -v)
docker compose down

# 3. Volver a iniciar
docker compose up -d

# 4. Verificar que los datos persisten
docker compose exec db psql -U admin -d mi_base_datos
SELECT * FROM test;
# Debería mostrar: id | nombre
#                   1 | dato de prueba
```

---

## 11. Error de sintaxis en docker-compose.yml

### 🔴 Síntoma

```bash
Error: yaml: line 15: did not find expected key
Error: services.db.volumes must be a list
```

Al ejecutar cualquier comando de Docker Compose, aparece un error de sintaxis YAML.

### 🧠 Causa

- Indentación incorrecta (YAML es muy estricto con espacios)
- Falta `:` después de una clave
- Uso de tabuladores en lugar de espacios
- Falta `-` en listas

### ✅ Solución

**Paso 1: Validar sintaxis antes de ejecutar**

```bash
# Validar y mostrar configuración final
docker compose config

# ✅ Si no hay errores, muestra el YAML procesado
# ❌ Si hay errores, muestra la línea problemática
```

**Paso 2: Reglas de indentación**

```yaml
# ✅ CORRECTO: 2 espacios por nivel
services:
  db:
    image: postgres:15-alpine
    ports:
      - "5432:5432"

# ❌ INCORRECTO: Tabuladores o indentación inconsistente
services:
	db:  # ❌ Tabulador
    image: postgres:15-alpine
   ports:  # ❌ Solo 1 espacio
      - "5432:5432"
```

**Paso 3: Listas requieren `-`**

```yaml
# ✅ CORRECTO:
volumes:
  - postgres_data:/var/lib/postgresql/data
  - ./init.sql:/docker-entrypoint-initdb.d/init.sql

# ❌ INCORRECTO:
volumes:
  postgres_data:/var/lib/postgresql/data  # ❌ Falta -
  ./init.sql:/docker-entrypoint-initdb.d/init.sql
```

**Paso 4: Claves requieren `:`**

```yaml
# ✅ CORRECTO:
environment:
  POSTGRES_DB: mi_base_datos

# ❌ INCORRECTO:
environment
  POSTGRES_DB: mi_base_datos  # ❌ Falta :
```

**Paso 5: Valores con caracteres especiales entre comillas**

```yaml
# ✅ CORRECTO:
environment:
  DB_PASSWORD: "P@ssw0rd!#$"  # Comillas por caracteres especiales

# ❌ INCORRECTO:
environment:
  DB_PASSWORD: P@ssw0rd!#$  # ❌ Rompe el parser
```

**Herramientas de validación**:

- **Editor con soporte YAML**: VS Code, Sublime Text, Vim
- **Linters online**: http://www.yamllint.com/
- **Extensión VS Code**: "YAML" por Red Hat

---

## 12. No se puede descargar la imagen

### 🔴 Síntoma

```bash
Error response from daemon: pull access denied for postgres16
Error: image not found: myapp:latest
```

Docker no puede descargar la imagen especificada.

### 🧠 Causa

- Nombre de imagen incorrecto (typo)
- Tag no existe en Docker Hub
- Imagen privada sin autenticación
- Problemas de conectividad

### ✅ Solución

**Paso 1: Verificar nombre y tag**

```yaml
# ❌ INCORRECTO:
services:
  db:
    image: postgres16  # Falta : entre nombre y versión

# ✅ CORRECTO:
services:
  db:
    image: postgres:16-alpine  # Formato correcto: nombre:tag
```

**Paso 2: Buscar la imagen en Docker Hub**

```bash
# Ver tags disponibles (desde terminal)
docker search postgres

# O visitar: https://hub.docker.com/_/postgres
```

**Paso 3: Descargar manualmente para verificar**

```bash
# Intentar descargar la imagen directamente
docker pull postgres:15-alpine

# ✅ Si funciona, el nombre/tag es correcto
# ❌ Si falla, verificar conectividad o nombre
```

**Paso 4: Usar una imagen alternativa**

```yaml
# Si postgres:16 no existe, usar una versión disponible
services:
  db:
    image: postgres:15-alpine  # ✅ Versión conocida que funciona
```

**Paso 5: Verificar conectividad**

```bash
# Probar conexión a Docker Hub
ping hub.docker.com

# Verificar que Docker puede conectarse
docker info | grep Registry

# Debería mostrar:
# Registry: https://index.docker.io/v1/
```

**Paso 6: Limpiar caché (si persiste)**

```bash
# Limpiar imágenes y caché
docker system prune -a

# Reintentar
docker compose pull
docker compose up -d
```

---

## 🆘 Flujo General de Depuración

**Cuando algo falle, seguir este orden**:

1. **Ver el estado de servicios**
   ```bash
   docker compose ps
   ```

2. **Revisar los logs**
   ```bash
   docker compose logs -f <servicio>
   ```

3. **Validar la configuración**
   ```bash
   docker compose config
   ```

4. **Verificar redes y volúmenes**
   ```bash
   docker network ls
   docker volume ls
   ```

5. **Entrar al contenedor para investigar**
   ```bash
   docker compose exec <servicio> bash
   ```

6. **Reiniciar servicios**
   ```bash
   docker compose restart
   ```

7. **Recrear desde cero (último recurso)**
   ```bash
   docker compose down
   docker compose up -d
   ```

---

## 📚 Recursos Adicionales

- **Documentación oficial**: https://docs.docker.com/compose/troubleshooting/
- **Docker Hub**: https://hub.docker.com/
- **Comunidad Docker**: https://forums.docker.com/

---

**Última actualización**: Semana 2 - Bootcamp Implantación de Software SENA CGMLTI  
**Versión**: Docker Compose v2.39.4+
