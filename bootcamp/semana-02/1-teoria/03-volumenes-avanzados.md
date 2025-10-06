# Volúmenes Avanzados en Docker

## 🎯 Objetivo

Dominar los diferentes tipos de volúmenes en Docker, entender cuándo usar cada uno, y aplicar estrategias de persistencia de datos para aplicaciones en producción.

**Tiempo estimado**: 20 minutos (lectura + ejemplos)

---

## 💾 ¿Qué son los Volúmenes?

**Los volúmenes** son el mecanismo de Docker para persistir datos generados y usados por contenedores.

**Problema fundamental**:  
Los contenedores son **efímeros** (temporales). Cuando eliminas un contenedor, todos sus datos internos se pierden.

**Analogía**:  
Un contenedor es como RAM (volátil), un volumen es como un disco duro (persistente).

---

## 🔄 El Problema de la Efímera

```bash
# ¿Qué? Crear contenedor PostgreSQL SIN volumen
docker run -d --name db postgres:15

# Insertar 1000 registros en la base de datos...

# ¿Qué? Eliminar el contenedor
docker rm -f db

# ❌ PROBLEMA: Los 1000 registros se perdieron PARA SIEMPRE
```

**Solución: Volúmenes**

```bash
# ¿Qué? Crear contenedor PostgreSQL CON volumen
docker run -d --name db \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15

# Insertar 1000 registros...

# ¿Qué? Eliminar el contenedor
docker rm -f db

# ¿Qué? Crear NUEVO contenedor con el MISMO volumen
docker run -d --name db-nuevo \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15

# ✅ Los 1000 registros siguen ahí!
```

---

## 📦 Tipos de Volúmenes en Docker

Docker ofrece 3 formas de montar datos:

| Tipo              | Gestión | Ubicación                  | Portabilidad   | Uso Principal |
| ----------------- | ------- | -------------------------- | -------------- | ------------- |
| **Named Volumes** | Docker  | `/var/lib/docker/volumes/` | ✅ Alta        | Producción    |
| **Bind Mounts**   | Usuario | Ruta del host              | ⚠️ Media       | Desarrollo    |
| **tmpfs Mounts**  | Memoria | RAM                        | ❌ No persiste | Temporal      |

---

## 🏷️ 1. Named Volumes (Recomendado para Producción)

**¿Qué son?**  
Volúmenes gestionados completamente por Docker.

**Características**:

- ✅ Docker gestiona la ubicación
- ✅ Fácil de respaldar
- ✅ Funcionan en todos los SOs
- ✅ Mejor performance
- ✅ Pueden compartirse entre contenedores

### Crear y Usar Named Volumes

```bash
# ¿Qué? Crear volumen explícitamente
# ¿Para qué? Docker lo gestiona automáticamente
docker volume create mi_volumen

# ¿Qué? Ver volúmenes existentes
docker volume ls

# ¿Qué? Inspeccionar volumen (ver ubicación, tamaño)
docker volume inspect mi_volumen

# Salida típica:
# {
#     "Name": "mi_volumen",
#     "Driver": "local",
#     "Mountpoint": "/var/lib/docker/volumes/mi_volumen/_data",
#     "Scope": "local"
# }
```

### Usar en docker run

```bash
# ¿Qué? Montar volumen nombrado
# ¿Cómo? -v nombre_volumen:ruta_en_contenedor
docker run -d \
  --name postgres \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15

# Si el volumen no existe, Docker lo crea automáticamente
```

### Usar en Docker Compose

```yaml
services:
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # ¿Qué? Monta el volumen nombrado

volumes:
  postgres_data:
    # ¿Qué? Declarar el volumen (Docker lo gestiona)
```

---

### Opciones Avanzadas de Named Volumes

```yaml
volumes:
  postgres_data:
    driver: local # ¿Qué? Driver por defecto
    driver_opts:
      type: none
      o: bind
      device: /mnt/external-disk/postgres # ¿Para qué? Usar disco externo
```

---

## 📁 2. Bind Mounts (Ideal para Desarrollo)

**¿Qué son?**  
Montan una carpeta del host directamente en el contenedor.

**Características**:

- ✅ Acceso directo a archivos del host
- ✅ Cambios reflejados en tiempo real
- ✅ Ideal para desarrollo (editar código)
- ⚠️ Dependen del sistema de archivos del host
- ⚠️ Menor portabilidad

### Sintaxis de Bind Mounts

```bash
# ¿Qué? Montar carpeta del host
# ¿Cómo? -v /ruta/absoluta/host:/ruta/contenedor
docker run -d \
  --name web \
  -v /home/usuario/mi-sitio:/usr/share/nginx/html \
  nginx:alpine

# ¿Para qué? Editar archivos en /home/usuario/mi-sitio
# y verlos reflejados INMEDIATAMENTE en el contenedor
```

### Con Docker Compose

```yaml
services:
  web:
    image: nginx:alpine
    volumes:
      - ./sitio-web:/usr/share/nginx/html # ¿Qué? Ruta relativa al docker-compose.yml
      - ./nginx.conf:/etc/nginx/nginx.conf:ro # :ro = read-only
```

**⚠️ Importante**: Siempre usar rutas **absolutas** o **relativas a docker-compose.yml**.

---

### Opciones de Bind Mounts

```yaml
volumes:
  # ¿Qué? Modo read-only
  - ./codigo:/app:ro

  # ¿Qué? Modo read-write (default)
  - ./data:/data:rw

  # ¿Qué? Consistencia (Mac/Windows)
  - ./node_modules:/app/node_modules:delegated
```

**Modos de consistencia** (solo Mac/Windows):

- `consistent`: Total sincronización (más lento)
- `delegated`: Escrituras del contenedor se propagan con delay (más rápido)
- `cached`: Lecturas del contenedor pueden estar desactualizadas (más rápido)

---

## 💨 3. tmpfs Mounts (Temporal en Memoria)

**¿Qué son?**  
Almacenamiento temporal en la RAM del host.

**Características**:

- ⚡ Ultra rápido (memoria RAM)
- ❌ No persiste al detener contenedor
- 🔐 Datos sensibles que no deben guardarse en disco
- 💾 Limitado por RAM disponible

### Cuándo Usar tmpfs

```bash
# ¿Qué? Montar tmpfs para archivos temporales
docker run -d \
  --name app \
  --tmpfs /tmp:size=100m,mode=1777 \
  mi-app:1.0

# ¿Para qué? /tmp en RAM, no en disco
# Útil para: tokens temporales, caché, sesiones
```

### Con Docker Compose

```yaml
services:
  app:
    image: mi-app:1.0
    tmpfs:
      - /tmp # ¿Para qué? Archivos temporales en RAM
      - /run # ¿Para qué? PIDs y sockets en RAM
```

---

## 🎯 ¿Cuándo Usar Cada Tipo?

### Named Volumes → Producción

**Usar para**:

- ✅ Bases de datos (PostgreSQL, MySQL, MongoDB)
- ✅ Datos que deben persistir
- ✅ Compartir datos entre contenedores
- ✅ Backups y migraciones

**Ejemplo**:

```yaml
services:
  db:
    image: postgres:15
    volumes:
      - db_data:/var/lib/postgresql/data # ✅ Producción

volumes:
  db_data:
```

---

### Bind Mounts → Desarrollo

**Usar para**:

- ✅ Código fuente (hot reload)
- ✅ Archivos de configuración
- ✅ Logs accesibles desde el host
- ✅ Desarrollo local

**Ejemplo**:

```yaml
services:
  api:
    image: node:20
    volumes:
      - ./src:/app/src # ✅ Hot reload en desarrollo
      - ./package.json:/app/package.json
    command: npm run dev # ¿Para qué? Reinicio automático
```

---

### tmpfs → Datos Temporales Sensibles

**Usar para**:

- ✅ Tokens de sesión
- ✅ Caché temporal
- ✅ Secretos que no deben persistir
- ✅ Archivos temporales de procesamiento

**Ejemplo**:

```yaml
services:
  auth:
    image: mi-auth:1.0
    tmpfs:
      - /tmp/sessions # ✅ Sesiones en RAM, no en disco
```

---

## 🔧 Gestión de Volúmenes

### Listar Volúmenes

```bash
# ¿Qué? Ver todos los volúmenes
docker volume ls

# ¿Qué? Filtrar volúmenes sin usar
docker volume ls --filter dangling=true
```

---

### Inspeccionar Volumen

```bash
# ¿Qué? Ver detalles de un volumen
docker volume inspect postgres_data

# Información incluida:
# - Mountpoint (ubicación en el host)
# - Driver
# - Labels
# - Scope
```

---

### Eliminar Volúmenes

```bash
# ¿Qué? Eliminar volumen específico
# ⚠️ CUIDADO: Borra datos permanentemente
docker volume rm mi_volumen

# ¿Qué? Eliminar TODOS los volúmenes sin usar
# ⚠️ MUY PELIGROSO: Revisar antes con "ls"
docker volume prune

# ¿Qué? Forzar eliminación (sin confirmación)
docker volume prune -f
```

---

### Copiar Datos de Volúmenes

```bash
# ¿Qué? Copiar datos DESDE un volumen al host
# ¿Para qué? Hacer backup
docker run --rm \
  -v postgres_data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/db-backup.tar.gz -C /data .

# ¿Qué? Copiar datos HACIA un volumen desde el host
# ¿Para qué? Restaurar backup
docker run --rm \
  -v postgres_data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/db-backup.tar.gz -C /data
```

---

## 📦 Ejemplo Completo: Stack con Múltiples Tipos de Volúmenes

```yaml
# ¿Qué? Aplicación con los 3 tipos de volúmenes
# ¿Para qué? Demostrar uso apropiado de cada tipo

services:
  # ¿Qué? Base de datos con Named Volume
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data # ✅ Named: datos persisten
    restart: unless-stopped

  # ¿Qué? API con Bind Mount (desarrollo)
  api:
    build: ./api
    volumes:
      - ./api/src:/app/src:delegated # ✅ Bind: hot reload
      - ./api/package.json:/app/package.json:ro # :ro = no modificar desde contenedor
      - api_node_modules:/app/node_modules # ✅ Named: evitar sobreescribir
    tmpfs:
      - /tmp # ✅ tmpfs: archivos temporales en RAM
    environment:
      NODE_ENV: development
    command: npm run dev
    depends_on:
      - db

  # ¿Qué? Nginx con Bind Mount para configuración
  nginx:
    image: nginx:alpine
    ports:
      - '80:80'
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro # ✅ Bind: configuración
      - ./nginx/logs:/var/log/nginx # ✅ Bind: logs accesibles
    depends_on:
      - api

volumes:
  # ¿Qué? Volúmenes nombrados
  postgres_data: # Datos de PostgreSQL
  api_node_modules: # node_modules (no sobreescribir con bind mount)
```

**Explicación**:

- **DB**: Named volume (datos persisten, gestionado por Docker)
- **API**: Bind mount para código (editar y ver cambios), tmpfs para temporales
- **Nginx**: Bind mount para config y logs (acceso directo desde host)

---

## 🛡️ Mejores Prácticas

### 1. **Separar Código de Datos**

**❌ Mal**:

```yaml
volumes:
  - ./todo:/app # Mezcla código con node_modules
```

**✅ Bien**:

```yaml
volumes:
  - ./src:/app/src # Solo código fuente
  - node_modules:/app/node_modules # Named volume para dependencias
```

---

### 2. **Usar :ro para Configuraciones**

```yaml
volumes:
  - ./config.json:/app/config.json:ro # ¿Para qué? Evitar modificaciones accidentales
```

---

### 3. **Nombrar Volúmenes Descriptivamente**

**❌ Mal**:

```yaml
volumes:
  - data:/var/lib/postgresql/data

volumes:
  data:  # ¿Qué datos?
```

**✅ Bien**:

```yaml
volumes:
  - postgres_blog_data:/var/lib/postgresql/data

volumes:
  postgres_blog_data:  # Claro y específico
```

---

### 4. **Respaldar Volúmenes Regularmente**

```bash
# ¿Qué? Script de backup automático
#!/bin/bash
DATE=$(date +%Y%m%d-%H%M%S)
docker run --rm \
  -v postgres_data:/data:ro \
  -v ./backups:/backup \
  alpine tar czf /backup/db-$DATE.tar.gz -C /data .

echo "Backup creado: db-$DATE.tar.gz"
```

---

### 5. **No Usar Bind Mounts en Producción**

**❌ En producción**:

```yaml
volumes:
  - ./codigo:/app # Depende de archivos del host
```

**✅ En producción**:

```yaml
volumes:
  - app_data:/app/data # Named volume, independiente del host
```

---

## 🧪 Troubleshooting

### Problema 1: Permisos de Archivos

**Síntoma**: Error "permission denied" al escribir en volumen

**Causa**: Usuario del contenedor no tiene permisos

**Solución**:

```bash
# ¿Qué? Verificar permisos en el host
ls -la /var/lib/docker/volumes/mi_volumen/_data

# ¿Qué? Cambiar permisos
sudo chown -R 1000:1000 /var/lib/docker/volumes/mi_volumen/_data

# O en docker-compose:
services:
  app:
    user: "1000:1000"  # ¿Para qué? Ejecutar como usuario específico
```

---

### Problema 2: Volumen no se Monta

**Síntoma**: Archivos no aparecen en el contenedor

**Solución**:

```bash
# ¿Qué? Verificar montaje
docker inspect mi-contenedor | grep -A 20 Mounts

# ¿Qué? Verificar que el volumen existe
docker volume ls | grep mi_volumen

# ¿Qué? Recrear el contenedor
docker compose down && docker compose up -d
```

---

### Problema 3: Espacio en Disco Lleno

**Síntoma**: Error "no space left on device"

**Solución**:

```bash
# ¿Qué? Ver tamaño de volúmenes
docker system df -v

# ¿Qué? Limpiar volúmenes no usados
docker volume prune

# ¿Qué? Limpiar todo (contenedores, imágenes, volúmenes)
docker system prune -a --volumes
```

---

## ✅ Autoevaluación

### Pregunta 1

¿Cuándo deberías usar Named Volumes vs Bind Mounts?

<details>
<summary>Ver respuesta</summary>

**Named Volumes**:

- ✅ Producción
- ✅ Bases de datos
- ✅ Datos que deben persistir
- ✅ Portabilidad entre hosts

**Bind Mounts**:

- ✅ Desarrollo local
- ✅ Hot reload de código
- ✅ Acceso a logs desde host
- ✅ Configuraciones que editas frecuentemente

**Regla simple**: Named volumes para datos, Bind mounts para desarrollo.

</details>

---

### Pregunta 2

¿Qué sucede con los datos en un Named Volume cuando eliminas el contenedor?

<details>
<summary>Ver respuesta</summary>

**Los datos PERSISTEN** ✅

El volumen es independiente del ciclo de vida del contenedor. Puedes:

1. Eliminar el contenedor
2. Crear un nuevo contenedor
3. Montar el mismo volumen
4. Los datos siguen ahí

Para eliminar los datos, debes eliminar explícitamente el volumen con `docker volume rm`.

</details>

---

### Pregunta 3

¿Por qué usar tmpfs para datos sensibles?

<details>
<summary>Ver respuesta</summary>

**Seguridad** 🔐:

- Los datos solo existen en RAM
- Al detener el contenedor, se borran automáticamente
- No quedan rastros en disco
- Útil para: tokens, sesiones, secretos temporales

**Performance** ⚡:

- Acceso ultra rápido (RAM vs disco)
- Ideal para caché y archivos temporales

**Limitación**: No persiste, limitado por RAM disponible.

</details>

---

## 🔗 Referencias

- [Docker Volumes Documentation](https://docs.docker.com/storage/volumes/)
- [Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
- [tmpfs Mounts](https://docs.docker.com/storage/tmpfs/)
- [Volume Drivers](https://docs.docker.com/engine/extend/legacy_plugins/#volume-plugins)

---

## 📌 Próximos Pasos

Ahora que dominas volúmenes, en la siguiente sección aprenderás las **mejores prácticas de Docker** para producción.

**Continuar a**: [04-mejores-practicas-docker.md](./04-mejores-practicas-docker.md)
