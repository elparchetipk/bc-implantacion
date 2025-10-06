# Docker Compose: Fundamentos y Sintaxis

## 🎯 Objetivo

Dominar Docker Compose v2 para definir y gestionar aplicaciones multi-contenedor usando archivos YAML, simplificando el despliegue y la configuración de sistemas complejos.

**Tiempo estimado**: 35 minutos (lectura + ejemplos)

---

## 🐋 ¿Qué es Docker Compose?

**Docker Compose** es una herramienta para definir y ejecutar aplicaciones con múltiples contenedores Docker mediante un archivo YAML.

**Definición simple**:  
En lugar de ejecutar múltiples comandos `docker run`, defines toda tu aplicación en un archivo `docker-compose.yml` y la levantas con un solo comando.

**Analogía**:  
Si Docker es como cocinar un plato individual, Docker Compose es como preparar un banquete completo con múltiples platos coordinados.

---

## 🆚 Antes vs Después de Docker Compose

### ❌ Sin Docker Compose (Manual y Propenso a Errores)

```bash
# ¿Qué? Crear red
docker network create mi-app-red

# ¿Qué? Crear volumen
docker volume create datos-postgres

# ¿Qué? Ejecutar PostgreSQL
docker run -d \
  --name db \
  --network mi-app-red \
  -v datos-postgres:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secreto123 \
  -e POSTGRES_USER=usuario \
  -e POSTGRES_DB=miapp \
  postgres:15

# ¿Qué? Ejecutar API
docker run -d \
  --name api \
  --network mi-app-red \
  -e DATABASE_URL=postgresql://usuario:secreto123@db:5432/miapp \
  -p 3000:3000 \
  mi-api:1.0

# ¿Qué? Ejecutar Nginx
docker run -d \
  --name web \
  --network mi-app-red \
  -p 80:80 \
  -v ./nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx:alpine
```

**Problemas**:

- 😫 Múltiples comandos largos
- 😫 Fácil olvidar parámetros
- 😫 Difícil de versionar
- 😫 Complejo de compartir con el equipo
- 😫 Propenso a errores de tipeo

---

### ✅ Con Docker Compose (Simple y Declarativo)

**Archivo `docker-compose.yml`**:

```yaml
# ¿Qué? Definición completa de la aplicación
# ¿Para qué? Describir todos los servicios, redes y volúmenes en un solo lugar

services:
  # ¿Qué? Servicio de base de datos
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secreto123
      POSTGRES_USER: usuario
      POSTGRES_DB: miapp
    volumes:
      - datos-postgres:/var/lib/postgresql/data

  # ¿Qué? Servicio de API
  api:
    image: mi-api:1.0
    environment:
      DATABASE_URL: postgresql://usuario:secreto123@db:5432/miapp
    ports:
      - '3000:3000'
    depends_on:
      - db

  # ¿Qué? Servicio de Nginx
  web:
    image: nginx:alpine
    ports:
      - '80:80'
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api

volumes:
  datos-postgres:
```

**Ejecutar todo**:

```bash
# ¿Qué? Inicia todos los servicios
# ¿Para qué? Levantar la aplicación completa
docker compose up -d
```

**Ventajas**:

- ✅ Un solo archivo YAML
- ✅ Fácil de leer y entender
- ✅ Versionable en Git
- ✅ Compartible con el equipo
- ✅ Un comando para todo

---

## 📄 Sintaxis de docker-compose.yml

### Estructura Básica

```yaml
# ¿Qué? Versión del formato (opcional en Compose v2)
# Nota: En Compose v2 no es necesario especificarla

services:
  # Aquí se definen los contenedores

volumes:
  # Aquí se definen los volúmenes nombrados

networks:
  # Aquí se definen las redes personalizadas
```

---

### Sección `services` (Lo más importante)

Cada servicio es un contenedor que se ejecutará.

```yaml
services:
  # ¿Qué? Nombre del servicio (puede ser cualquiera)
  nombre-servicio:
    # ¿Qué? Imagen Docker a usar
    image: postgres:15

    # O construir desde Dockerfile:
    # build: ./ruta-a-dockerfile

    # ¿Qué? Nombre del contenedor (opcional)
    container_name: mi-postgres

    # ¿Qué? Variables de ambiente
    environment:
      VAR1: valor1
      VAR2: valor2

    # ¿Qué? Mapeo de puertos (host:contenedor)
    ports:
      - '8080:80'

    # ¿Qué? Volúmenes montados
    volumes:
      - nombre-volumen:/ruta/en/contenedor
      - ./carpeta-local:/ruta/en/contenedor

    # ¿Qué? Dependencias (qué servicios deben iniciar antes)
    depends_on:
      - otro-servicio

    # ¿Qué? Comando a ejecutar (sobrescribe CMD del Dockerfile)
    command: ['npm', 'start']

    # ¿Qué? Política de reinicio
    restart: unless-stopped
```

---

## 🔧 Propiedades Clave Explicadas

### 1. `image` vs `build`

**Usar imagen existente**:

```yaml
services:
  db:
    image: postgres:15 # ¿Para qué? Usar imagen oficial de Docker Hub
```

**Construir desde Dockerfile**:

```yaml
services:
  api:
    build:
      context: ./mi-api # ¿Qué? Carpeta con el Dockerfile
      dockerfile: Dockerfile # ¿Qué? Nombre del Dockerfile (opcional si se llama "Dockerfile")
```

---

### 2. `environment` (Variables de Ambiente)

**Forma 1: Inline**

```yaml
services:
  db:
    environment:
      POSTGRES_PASSWORD: secreto
      POSTGRES_USER: usuario
```

**Forma 2: Array**

```yaml
services:
  db:
    environment:
      - POSTGRES_PASSWORD=secreto
      - POSTGRES_USER=usuario
```

**Forma 3: Archivo .env (RECOMENDADO para secrets)**

```yaml
services:
  db:
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD} # ¿Cómo? Lee de archivo .env
```

**Archivo `.env`**:

```bash
DB_PASSWORD=supersecretpassword
```

**⚠️ IMPORTANTE**: Nunca subir `.env` a Git. Agregar a `.gitignore`.

---

### 3. `ports` (Mapeo de Puertos)

```yaml
services:
  web:
    ports:
      - '8080:80' # ¿Qué? Host:Contenedor
      - '443:443'
      - '127.0.0.1:5432:5432' # ¿Para qué? Solo localhost puede acceder
```

**Formato**: `"PUERTO_HOST:PUERTO_CONTENEDOR"`

**Ejemplo**:

- `"8080:80"` → Acceder a `http://localhost:8080` en el host, va al puerto 80 del contenedor

---

### 4. `volumes` (Persistencia de Datos)

**Named Volumes (Recomendado)**:

```yaml
services:
  db:
    volumes:
      - postgres_data:/var/lib/postgresql/data # ¿Para qué? Docker gestiona el volumen

volumes:
  postgres_data: # ¿Qué? Declarar el volumen
```

**Bind Mounts** (Mapear carpeta del host):

```yaml
services:
  web:
    volumes:
      - ./mi-sitio:/usr/share/nginx/html # ¿Para qué? Editar archivos en el host
      - ./nginx.conf:/etc/nginx/nginx.conf:ro # ro = read-only
```

**Volúmenes Anónimos**:

```yaml
services:
  app:
    volumes:
      - /app/node_modules # ¿Para qué? Evitar sobreescribir carpeta del contenedor
```

---

### 5. `depends_on` (Orden de Inicio)

```yaml
services:
  db:
    image: postgres:15

  api:
    image: mi-api:1.0
    depends_on:
      - db # ¿Para qué? Asegurar que db inicie antes que api
```

**⚠️ Nota**: `depends_on` solo espera que el contenedor **inicie**, NO que el servicio esté **listo**.

**Solución con health check**:

```yaml
services:
  db:
    image: postgres:15
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 5s
      timeout: 3s
      retries: 5

  api:
    image: mi-api:1.0
    depends_on:
      db:
        condition: service_healthy # ¿Para qué? Esperar a que db esté LISTO
```

---

### 6. `restart` (Política de Reinicio)

```yaml
services:
  db:
    restart: unless-stopped # ¿Para qué? Reiniciar automáticamente si falla
```

**Opciones**:

- `no`: No reiniciar automáticamente (default)
- `always`: Siempre reiniciar si se detiene
- `on-failure`: Solo reiniciar si hubo error
- `unless-stopped`: Reiniciar a menos que se haya detenido manualmente

---

### 7. `networks` (Redes Personalizadas)

**Por defecto**: Docker Compose crea una red automáticamente para todos los servicios.

**Red personalizada**:

```yaml
services:
  db:
    networks:
      - backend # ¿Qué? Este servicio solo en red backend

  api:
    networks:
      - backend
      - frontend # ¿Qué? Este servicio en ambas redes

  web:
    networks:
      - frontend # ¿Qué? Este servicio solo en red frontend

networks:
  backend:
  frontend:
```

**¿Para qué?** Aislar servicios (por ejemplo, el frontend no debe acceder directamente a la base de datos).

---

## 📦 Ejemplo Completo: Blog con PostgreSQL + Adminer

```yaml
# ¿Qué? Stack completo para un blog
# ¿Para qué? Base de datos + GUI de administración

services:
  # ¿Qué? Servicio de base de datos PostgreSQL
  db:
    image: postgres:15-alpine # ¿Por qué alpine? Más ligera
    container_name: blog-db
    environment:
      POSTGRES_DB: blogdb
      POSTGRES_USER: bloguser
      POSTGRES_PASSWORD: ${DB_PASSWORD} # ¿Cómo? Lee de .env
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro # ¿Para qué? Script de inicialización
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U bloguser -d blogdb']
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks:
      - blog-network

  # ¿Qué? Adminer - GUI web para gestionar base de datos
  adminer:
    image: adminer:latest
    container_name: blog-adminer
    ports:
      - '8080:8080' # ¿Para qué? Acceder a http://localhost:8080
    environment:
      ADMINER_DEFAULT_SERVER: db # ¿Para qué? Pre-seleccionar servidor db
      ADMINER_DESIGN: nette # ¿Qué? Tema visual
    depends_on:
      db:
        condition: service_healthy # ¿Para qué? Esperar a que db esté lista
    restart: unless-stopped
    networks:
      - blog-network

volumes:
  postgres_data: # ¿Qué? Volumen nombrado para persistir datos

networks:
  blog-network: # ¿Qué? Red privada para los servicios
    driver: bridge
```

**Archivo `.env`**:

```bash
# ¿Qué? Variables sensibles
# ¿Para qué? No exponer contraseñas en código

DB_PASSWORD=supersecretpassword123
```

**Archivo `init.sql`** (opcional):

```sql
-- ¿Qué? Script de inicialización de base de datos
-- ¿Para qué? Crear tablas automáticamente al primer inicio

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    author VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO posts (title, content, author) VALUES
('Bienvenido', 'Este es el primer post', 'Admin'),
('Docker Compose', 'Aprendiendo Docker Compose', 'Instructor');
```

---

## ⚙️ Comandos Esenciales de Docker Compose

### Gestión de Servicios

```bash
# ¿Qué? Iniciar todos los servicios
# ¿Para qué? Levantar la aplicación completa
docker compose up -d
# -d = detached (segundo plano)

# ¿Qué? Iniciar y reconstruir imágenes
docker compose up -d --build

# ¿Qué? Detener servicios (contenedores siguen existiendo)
docker compose stop

# ¿Qué? Detener y eliminar contenedores, redes
# ¿Para qué? Limpiar el ambiente (volúmenes persisten)
docker compose down

# ¿Qué? Detener y eliminar TODO (incluidos volúmenes)
# ⚠️ CUIDADO: Borra datos
docker compose down --volumes
```

---

### Monitoreo y Logs

```bash
# ¿Qué? Ver estado de servicios
docker compose ps

# ¿Qué? Ver logs de todos los servicios
docker compose logs

# ¿Qué? Ver logs en tiempo real
docker compose logs -f

# ¿Qué? Ver logs de un servicio específico
docker compose logs -f db

# ¿Qué? Ver últimas 50 líneas de logs
docker compose logs --tail=50
```

---

### Gestión Individual de Servicios

```bash
# ¿Qué? Iniciar solo un servicio
docker compose up -d db

# ¿Qué? Detener solo un servicio
docker compose stop api

# ¿Qué? Reiniciar un servicio
docker compose restart web

# ¿Qué? Ver logs de un servicio
docker compose logs -f api
```

---

### Escalar Servicios

```bash
# ¿Qué? Escalar servicio API a 3 instancias
# ¿Para qué? Balanceo de carga
docker compose up -d --scale api=3

# Nota: El servicio no debe tener `container_name` definido
```

---

### Ejecutar Comandos en Servicios

```bash
# ¿Qué? Ejecutar comando en servicio corriendo
docker compose exec db psql -U bloguser -d blogdb

# ¿Qué? Ejecutar bash en servicio
docker compose exec api bash

# ¿Qué? Ejecutar comando sin TTY
docker compose exec -T db pg_dump -U bloguser blogdb > backup.sql
```

---

### Validación y Debugging

```bash
# ¿Qué? Validar sintaxis del docker-compose.yml
docker compose config

# ¿Qué? Ver configuración procesada (con variables resueltas)
docker compose config --services

# ¿Qué? Ver solo imágenes a usar
docker compose config --images
```

---

## 🎨 Mejores Prácticas

### 1. **Usar .env para Secrets**

**❌ Mal**:

```yaml
environment:
  POSTGRES_PASSWORD: mysecretpassword # Expuesto en código
```

**✅ Bien**:

```yaml
environment:
  POSTGRES_PASSWORD: ${DB_PASSWORD} # Lee de .env
```

---

### 2. **Nombrar Volúmenes Descriptivamente**

**❌ Mal**:

```yaml
volumes:
  - data:/var/lib/postgresql/data
```

**✅ Bien**:

```yaml
volumes:
  - postgres_blog_data:/var/lib/postgresql/data
```

---

### 3. **Usar Health Checks**

```yaml
services:
  db:
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 10s
      timeout: 5s
      retries: 5
```

**¿Para qué?** Otros servicios pueden esperar a que esté realmente listo.

---

### 4. **Imágenes Ligeras (Alpine)**

**❌ Regular**:

```yaml
image: nginx:latest # ~140 MB
```

**✅ Mejor**:

```yaml
image: nginx:alpine # ~40 MB (3.5x más ligera)
```

---

### 5. **Documentar con Comentarios**

```yaml
services:
  db:
    image: postgres:15
    # ¿Qué? Base de datos principal
    # ¿Para qué? Almacenar posts del blog
    environment:
      POSTGRES_DB: blogdb # ¿Qué? Nombre de la base de datos
```

---

## ✅ Autoevaluación

### Pregunta 1

¿Cuál es la ventaja principal de Docker Compose sobre múltiples comandos `docker run`?

<details>
<summary>Ver respuesta</summary>

Docker Compose permite definir toda la aplicación (servicios, redes, volúmenes) en un solo archivo YAML, haciéndola:

- Más fácil de mantener
- Versionable en Git
- Compartible con el equipo
- Ejecutable con un solo comando

</details>

---

### Pregunta 2

¿Cuál es la diferencia entre `docker compose stop` y `docker compose down`?

<details>
<summary>Ver respuesta</summary>

- **`docker compose stop`**: Detiene los contenedores pero los mantiene (puedes reiniciarlos con `start`)
- **`docker compose down`**: Detiene Y elimina los contenedores y redes (volúmenes persisten a menos que uses `--volumes`)

</details>

---

### Pregunta 3

¿Por qué es importante usar `depends_on` con `condition: service_healthy`?

<details>
<summary>Ver respuesta</summary>

`depends_on` solo espera que el contenedor **inicie**, pero no garantiza que el servicio esté **listo** (por ejemplo, PostgreSQL puede tardar unos segundos en aceptar conexiones).

Usar `condition: service_healthy` con un health check asegura que el servicio dependiente espere hasta que la base de datos realmente esté aceptando conexiones.

</details>

---

## 🔗 Referencias

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Compose CLI Reference](https://docs.docker.com/compose/reference/)
- [Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

## 📌 Próximos Pasos

Ahora que entiendes Docker Compose, en la siguiente sección aprenderás sobre **redes Docker** para controlar cómo se comunican los contenedores entre sí.

**Continuar a**: [02-redes-docker.md](./02-redes-docker.md)
