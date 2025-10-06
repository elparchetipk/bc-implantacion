# Mejores Prácticas de Docker para Producción

## 🎯 Objetivo

Aplicar las mejores prácticas de la industria para crear imágenes Docker optimizadas, seguras y listas para producción.

**Tiempo estimado**: 25 minutos (lectura + ejemplos)

---

## 🏆 ¿Por Qué son Importantes las Mejores Prácticas?

**Diferencia entre desarrollo y producción**:

| Aspecto           | Desarrollo    | Producción                        |
| ----------------- | ------------- | --------------------------------- |
| **Tamaño imagen** | No importa    | Crítico (menos MB = más rápido)   |
| **Seguridad**     | Relajada      | Estricta (sin secretos, sin root) |
| **Performance**   | Aceptable     | Optimizada (CPU, RAM)             |
| **Logs**          | En contenedor | Externos (centralizados)          |
| **Health checks** | Opcional      | Obligatorio                       |
| **Secretos**      | Hardcodeados  | Variables de entorno              |

**Analogía**:  
Desarrollo es como cocinar en casa (rápido, desordenado).  
Producción es como un restaurante (limpio, profesional, eficiente).

---

## 📝 1. Usar .dockerignore

### ¿Qué es .dockerignore?

**Archivo que lista** qué NO copiar al construir una imagen Docker.

**¿Para qué?**

- ⚡ Construir más rápido (menos archivos)
- 💾 Imágenes más pequeñas
- 🔐 Evitar copiar secretos accidentalmente

---

### Ejemplo de .dockerignore

```bash
# ¿Qué? Archivo .dockerignore en la raíz del proyecto

# ¿Para qué? Ignorar node_modules (se instalan en el contenedor)
node_modules/
npm-debug.log

# ¿Para qué? Ignorar archivos de control de versiones
.git/
.gitignore

# ¿Para qué? Ignorar archivos de configuración local
.env
.env.local
*.env

# ¿Para qué? Ignorar documentación
README.md
docs/
*.md

# ¿Para qué? Ignorar tests (no necesarios en producción)
tests/
__tests__/
*.test.js
coverage/

# ¿Para qué? Ignorar archivos de desarrollo
.vscode/
.idea/
*.log
tmp/
```

---

### Impacto del .dockerignore

**Sin .dockerignore**:

```bash
# Tamaño del contexto de construcción: 2.5 GB
# Tiempo de construcción: 5 minutos
# Tamaño de imagen: 800 MB
```

**Con .dockerignore**:

```bash
# Tamaño del contexto: 50 MB  ✅
# Tiempo de construcción: 30 segundos  ✅
# Tamaño de imagen: 150 MB  ✅
```

---

## 🖼️ 2. Usar Imágenes Base Pequeñas (Alpine)

### ¿Qué es Alpine Linux?

**Distribución Linux ultra ligera** (solo 5 MB).

**Comparación de tamaños**:

| Imagen Base       | Tamaño  | Uso                        |
| ----------------- | ------- | -------------------------- |
| `ubuntu:22.04`    | ~77 MB  | Desarrollo, compatibilidad |
| `debian:bullseye` | ~124 MB | Estabilidad                |
| `node:20`         | ~1.1 GB | ❌ Desarrollo rápido       |
| `node:20-alpine`  | ~170 MB | ✅ Producción              |
| `alpine:3.19`     | ~7 MB   | ✅ Mínimo absoluto         |

---

### Ejemplo: Node.js con Alpine

**❌ Imagen pesada**:

```dockerfile
FROM node:20
# Tamaño: 1.1 GB

WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]
```

**✅ Imagen optimizada**:

```dockerfile
FROM node:20-alpine
# Tamaño: 170 MB (6x más pequeña)

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production  # ¿Para qué? Solo dependencias de producción
COPY . .
CMD ["node", "server.js"]
```

---

### Consideraciones con Alpine

**Ventajas**:

- ✅ Mucho más pequeña
- ✅ Menos superficie de ataque (seguridad)
- ✅ Descargas más rápidas

**Desventajas**:

- ⚠️ Usa `musl` en lugar de `glibc` (algunos paquetes pueden tener problemas)
- ⚠️ Menos herramientas preinstaladas (necesitas instalar lo básico)

---

## 🏗️ 3. Multi-Stage Builds (Construcción en Múltiples Etapas)

### ¿Qué son Multi-Stage Builds?

**Usar múltiples imágenes** durante la construcción, pero solo la última se incluye en la imagen final.

**¿Para qué?**

- 🗑️ Eliminar herramientas de compilación de la imagen final
- 📦 Separar dependencias de desarrollo y producción
- 💾 Reducir tamaño drásticamente

---

### Ejemplo: Aplicación Go

**❌ Sin multi-stage**:

```dockerfile
FROM golang:1.21
# ¿Qué? Imagen con compilador Go (800 MB)

WORKDIR /app
COPY . .
RUN go build -o server .

CMD ["./server"]

# Problema: Imagen final incluye TODO el compilador Go
# Tamaño final: 850 MB
```

**✅ Con multi-stage**:

```dockerfile
# ¿Qué? ETAPA 1: Construcción
FROM golang:1.21 AS builder
# ¿Para qué? Compilar el código

WORKDIR /app
COPY . .
RUN go build -o server .

# ¿Qué? ETAPA 2: Producción (solo el binario)
FROM alpine:3.19
# ¿Para qué? Imagen mínima para ejecutar

WORKDIR /app
COPY --from=builder /app/server .
# ¿Qué? Copiar SOLO el binario compilado desde la etapa anterior

CMD ["./server"]

# Resultado: Imagen final 15 MB (57x más pequeña!)
```

---

### Ejemplo: Node.js con Multi-Stage

```dockerfile
# ¿Qué? ETAPA 1: Instalación de dependencias
FROM node:20-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# ¿Qué? ETAPA 2: Construcción (si tienes TypeScript, React, etc.)
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build  # ¿Para qué? Compilar TypeScript → JavaScript

# ¿Qué? ETAPA 3: Producción (solo archivos necesarios)
FROM node:20-alpine
WORKDIR /app

# ¿Qué? Copiar node_modules desde etapa 1
COPY --from=dependencies /app/node_modules ./node_modules

# ¿Qué? Copiar código compilado desde etapa 2
COPY --from=builder /app/dist ./dist

# ¿Qué? Copiar package.json (necesario para scripts)
COPY package.json ./

CMD ["node", "dist/server.js"]

# Resultado: Solo producción, sin devDependencies, sin código fuente
```

---

## 🔐 4. No Usar Usuario Root

### El Problema de Root

**Por defecto, Docker ejecuta contenedores como root** (superusuario).

**Riesgos**:

- 🚨 Si un atacante compromete el contenedor, tiene acceso root
- 🚨 Puede escapar del contenedor y atacar el host
- 🚨 Puede modificar archivos críticos del sistema

---

### Solución: Crear Usuario No-Root

```dockerfile
FROM node:20-alpine

# ¿Qué? Crear usuario sin privilegios
RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser
# ¿Para qué? Usuario con UID/GID 1000 (estándar)

WORKDIR /app

# ¿Qué? Copiar archivos como root
COPY package*.json ./
RUN npm ci --only=production

COPY . .

# ¿Qué? Cambiar propietario de archivos al usuario
RUN chown -R appuser:appuser /app

# ¿Qué? Cambiar al usuario no-root ANTES de ejecutar la app
USER appuser
# ¿Para qué? Toda ejecución subsecuente usa este usuario

CMD ["node", "server.js"]
```

---

### Verificar Usuario

```bash
# ¿Qué? Ver con qué usuario se ejecuta el contenedor
docker exec mi-contenedor whoami

# Salida esperada: appuser (no root)
```

---

## 🔑 5. Gestión Segura de Secretos

### ❌ Nunca Hardcodear Secretos

**Mal**:

```dockerfile
# ❌ PELIGRO: Secreto en la imagen
ENV DB_PASSWORD=MiContraseña123
```

**Problema**: Cualquiera con acceso a la imagen puede ver el secreto.

```bash
docker inspect mi-imagen | grep DB_PASSWORD
# Salida: "DB_PASSWORD=MiContraseña123"  ← Expuesto
```

---

### ✅ Usar Variables de Entorno

**docker-compose.yml**:

```yaml
services:
  api:
    image: mi-api:1.0
    environment:
      DB_PASSWORD: ${DB_PASSWORD} # ¿Qué? Lee desde .env
    env_file:
      - .env # ¿Qué? Archivo con secretos
```

**.env** (NO subir a Git):

```bash
DB_PASSWORD=MiContraseña123
API_KEY=secret-key-12345
```

**.gitignore**:

```bash
.env
.env.local
*.env
```

---

### ✅ Usar Docker Secrets (Swarm/Kubernetes)

```yaml
# docker-compose.yml con secrets
services:
  api:
    image: mi-api:1.0
    secrets:
      - db_password # ¿Qué? Referencia al secreto

secrets:
  db_password:
    file: ./secrets/db_password.txt # ¿Qué? Archivo con el secreto
```

**En el contenedor**, el secreto está en: `/run/secrets/db_password`

```javascript
// Leer secreto en Node.js
const fs = require('fs');
const dbPassword = fs.readFileSync('/run/secrets/db_password', 'utf8').trim();
```

---

## 💉 6. Health Checks (Verificaciones de Salud)

### ¿Qué son Health Checks?

**Comandos que Docker ejecuta** para verificar si el contenedor está funcionando correctamente.

**¿Para qué?**

- 🩺 Detectar contenedores "zombies" (corriendo pero no funcionando)
- 🔄 Reiniciar automáticamente contenedores no saludables
- ⚖️ Load balancers solo envían tráfico a contenedores saludables

---

### Ejemplo en Dockerfile

```dockerfile
FROM node:20-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .

# ¿Qué? Configurar health check
HEALTHCHECK --interval=30s \
            --timeout=10s \
            --start-period=40s \
            --retries=3 \
            CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1
# ¿Para qué? Verificar cada 30s que el endpoint /health responde
# ¿Cómo? Si falla 3 veces consecutivas, marca el contenedor como "unhealthy"

CMD ["node", "server.js"]
```

**Parámetros**:

- `--interval=30s`: Verificar cada 30 segundos
- `--timeout=10s`: Si no responde en 10s, falla
- `--start-period=40s`: Esperar 40s antes de la primera verificación (para que la app inicie)
- `--retries=3`: Intentar 3 veces antes de marcar como "unhealthy"

---

### Ejemplo en Docker Compose

```yaml
services:
  api:
    image: mi-api:1.0
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:3000/health']
      # ¿Qué? Comando para verificar salud
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

---

### Endpoint /health en Node.js

```javascript
// server.js
const express = require('express');
const app = express();

// ¿Qué? Endpoint de salud
app.get('/health', async (req, res) => {
  // ¿Para qué? Verificar que la app Y las dependencias funcionan

  try {
    // Verificar conexión a base de datos
    await db.ping();

    res.status(200).json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
    });
  } catch (error) {
    res.status(503).json({
      status: 'unhealthy',
      error: error.message,
    });
  }
});

app.listen(3000);
```

---

### Ver Estado de Salud

```bash
# ¿Qué? Ver salud de contenedores
docker ps

# Columna STATUS:
# Up 2 minutes (healthy)  ← ✅ Saludable
# Up 5 minutes (unhealthy)  ← ❌ No saludable
# Up 1 minute (health: starting)  ← ⏳ Iniciando

# ¿Qué? Inspeccionar detalles de salud
docker inspect --format='{{json .State.Health}}' mi-contenedor | jq
```

---

## 📊 7. Optimizar Capas de Imagen

### ¿Qué son las Capas?

**Cada instrucción en Dockerfile** (RUN, COPY, ADD) crea una **capa**.

**Analogía**: Capas como capas de una cebolla, apiladas una sobre otra.

**¿Por qué importa?**

- 💾 Menos capas = imagen más pequeña
- 🚀 Capas se cachean (construcciones más rápidas)

---

### ❌ Mal: Muchas Capas

```dockerfile
FROM alpine:3.19
RUN apk add --no-cache curl
RUN apk add --no-cache wget
RUN apk add --no-cache git
RUN apk add --no-cache vim
# Problema: 4 capas (una por cada RUN)
```

### ✅ Bien: Combinar en Una Capa

```dockerfile
FROM alpine:3.19
RUN apk add --no-cache \
    curl \
    wget \
    git \
    vim
# ¿Para qué? Una sola capa
```

---

### Orden de Capas (Cacheo Eficiente)

**Principio**: Capas que cambian menos frecuentemente **primero**.

**❌ Mal**:

```dockerfile
FROM node:20-alpine
COPY . .  # ¿Problema? Cambia frecuentemente (cada edición de código)
RUN npm install  # Se reinstala CADA VEZ (lento)
CMD ["node", "server.js"]
```

**✅ Bien**:

```dockerfile
FROM node:20-alpine
COPY package*.json ./  # ¿Para qué? Solo cambia cuando agregas dependencias
RUN npm ci --only=production  # Se cachea (rápido)
COPY . .  # ¿Para qué? Copiar código al final
CMD ["node", "server.js"]
```

**Resultado**: Cambios en código no reinstalan dependencias (construcción 10x más rápida).

---

## 🧹 8. Limpiar en la Misma Capa

### ❌ Mal: Limpiar en Capas Separadas

```dockerfile
FROM alpine:3.19
RUN apk add --no-cache build-base  # Capa 1: +100 MB
RUN make install  # Capa 2
RUN apk del build-base  # Capa 3: ❌ NO elimina los 100 MB de la Capa 1
# Problema: Imagen final SIGUE incluyendo los 100 MB
```

### ✅ Bien: Todo en Una Capa

```dockerfile
FROM alpine:3.19
RUN apk add --no-cache build-base && \
    make install && \
    apk del build-base
# ¿Para qué? Instalar, usar y LIMPIAR en la misma capa
# Resultado: Solo el binario compilado queda (imagen pequeña)
```

---

## 🔒 9. Escanear Vulnerabilidades

### Usar Docker Scout o Trivy

```bash
# ¿Qué? Escanear imagen en busca de vulnerabilidades
docker scout cves mi-imagen:1.0

# O con Trivy:
trivy image mi-imagen:1.0
```

**Salida típica**:

```
✓ 0 CRITICAL
⚠ 3 HIGH
⚠ 12 MEDIUM
○ 45 LOW
```

**Acción**: Actualizar imágenes base o dependencias con vulnerabilidades.

---

## 📋 10. Checklist de Producción

Antes de desplegar en producción, verifica:

- [ ] ✅ Imagen usa Alpine o imágenes slim
- [ ] ✅ Multi-stage build implementado
- [ ] ✅ .dockerignore configurado
- [ ] ✅ Usuario no-root configurado (`USER appuser`)
- [ ] ✅ Health check implementado
- [ ] ✅ Secretos en variables de entorno (NO hardcodeados)
- [ ] ✅ Logs van a stdout/stderr (no a archivos)
- [ ] ✅ Imagen escaneada con Docker Scout/Trivy (sin CRITICAL)
- [ ] ✅ restart: unless-stopped configurado
- [ ] ✅ Límites de recursos definidos (memory, cpu)

---

## 🎯 Ejemplo Completo: Dockerfile Optimizado

```dockerfile
# ===== ETAPA 1: Dependencias =====
FROM node:20-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# ===== ETAPA 2: Construcción =====
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build  # Compilar TypeScript/Build frontend

# ===== ETAPA 3: Producción =====
FROM node:20-alpine

# ¿Qué? Instalar solo lo necesario
RUN apk add --no-cache curl

# ¿Qué? Crear usuario no-root
RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser

WORKDIR /app

# ¿Qué? Copiar node_modules de producción
COPY --from=dependencies /app/node_modules ./node_modules

# ¿Qué? Copiar código compilado
COPY --from=builder /app/dist ./dist
COPY package.json ./

# ¿Qué? Cambiar propietario
RUN chown -R appuser:appuser /app

# ¿Qué? Cambiar a usuario no-root
USER appuser

# ¿Qué? Exponer puerto
EXPOSE 3000

# ¿Qué? Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# ¿Qué? Comando de inicio
CMD ["node", "dist/server.js"]
```

**docker-compose.yml**:

```yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    image: mi-api:1.0
    environment:
      NODE_ENV: production
      DB_HOST: db
      DB_PASSWORD: ${DB_PASSWORD} # Desde .env
    ports:
      - '3000:3000'
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:3000/health']
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

---

## 🔍 Comparación: Antes vs Después

| Métrica                 | ❌ Antes (Mal) | ✅ Después (Bien)       |
| ----------------------- | -------------- | ----------------------- |
| **Tamaño imagen**       | 1.2 GB         | 180 MB (6x más pequeña) |
| **Tiempo construcción** | 5 minutos      | 45 segundos (cacheo)    |
| **Usuario**             | root           | appuser (no-root)       |
| **Secretos**            | Hardcodeados   | Variables de entorno    |
| **Health check**        | ❌ No          | ✅ Sí                   |
| **Vulnerabilidades**    | 15 CRITICAL    | 0 CRITICAL              |
| **Capas**               | 25 capas       | 8 capas                 |

---

## ✅ Autoevaluación

### Pregunta 1

¿Por qué usar multi-stage builds?

<details>
<summary>Ver respuesta</summary>

**Ventajas**:

1. **Imágenes más pequeñas**: Solo incluyes lo necesario para ejecutar, no para construir
2. **Separación de concerns**: Construcción vs producción
3. **Seguridad**: No incluyes herramientas de desarrollo en producción

**Ejemplo**: Aplicación Go con multi-stage: 15 MB vs 850 MB (57x más pequeña).

</details>

---

### Pregunta 2

¿Cuál es el riesgo de ejecutar contenedores como root?

<details>
<summary>Ver respuesta</summary>

**Riesgos**:

1. **Escalada de privilegios**: Si un atacante compromete el contenedor, tiene acceso root
2. **Escape del contenedor**: Puede atacar el sistema host
3. **Modificación de archivos críticos**: Puede alterar configuraciones del sistema

**Solución**: Crear usuario no-root con `USER appuser`.

</details>

---

### Pregunta 3

¿Qué hace un health check y por qué es importante?

<details>
<summary>Ver respuesta</summary>

**¿Qué hace?**  
Ejecuta un comando periódicamente para verificar que el contenedor funciona correctamente.

**¿Por qué es importante?**

1. Detecta contenedores "zombies" (corriendo pero no funcionando)
2. Reinicia automáticamente contenedores no saludables
3. Load balancers solo envían tráfico a contenedores saludables

**Ejemplo**: `curl -f http://localhost:3000/health` cada 30 segundos.

</details>

---

## 🔗 Referencias

- [Dockerfile Best Practices (Docker Docs)](https://docs.docker.com/develop/dev-best-practices/)
- [Multi-Stage Builds](https://docs.docker.com/build/building/multi-stage/)
- [Docker Security](https://docs.docker.com/engine/security/)
- [Health Check Reference](https://docs.docker.com/engine/reference/builder/#healthcheck)

---

## 📌 Próximos Pasos

Ahora que conoces las mejores prácticas, es momento de **aplicarlas en las prácticas**.

**Continuar a**: [../2-practicas/01-primer-docker-compose.md](../2-practicas/01-primer-docker-compose.md)
