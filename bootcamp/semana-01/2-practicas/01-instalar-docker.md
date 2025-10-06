# Práctica 1: Instalación de Docker y Docker Compose

## 🎯 Objetivos

- Instalar Docker Engine en diferentes sistemas operativos
- Verificar la instalación correcta de Docker Compose v2
- Ejecutar el primer contenedor de prueba
- Configurar permisos de usuario

**Tiempo estimado**: 30-45 minutos

---

## 📋 Requisitos Previos

### Hardware Mínimo

- **CPU**: Procesador de 64 bits
- **RAM**: 4 GB (8 GB recomendado)
- **Disco**: 20 GB libres
- **Virtualización**: Habilitada en BIOS/UEFI

### Software

- Sistema operativo de 64 bits
- Conexión a internet

---

## 🐧 Instalación en Linux (Ubuntu/Debian)

### Método 1: Script Oficial (Recomendado)

```bash
# ¿Qué? Descarga e instala Docker usando el script oficial
# ¿Para qué? Instalación rápida y automatizada
# ¿Cómo? El script detecta tu distribución y configura repositorios
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# ¿Qué? Agregar tu usuario al grupo docker
# ¿Para qué? Ejecutar docker sin sudo
sudo usermod -aG docker $USER

# ¿Qué? Aplicar cambios de grupo
# ¿Para qué? Evitar cerrar sesión
newgrp docker
```

---

### Método 2: Instalación Manual (Fedora/Rocky Linux)

```bash
# ¿Qué? Instalar Docker en Fedora/Rocky Linux
# ¿Para qué? Configuración paso a paso con control total

# Paso 1: Instalar dependencias
sudo dnf -y install dnf-plugins-core

# Paso 2: Agregar repositorio oficial de Docker
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# Paso 3: Instalar Docker Engine y Compose
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Paso 4: Iniciar y habilitar Docker
# ¿Para qué? Que Docker se inicie automáticamente al arrancar el sistema
sudo systemctl start docker
sudo systemctl enable docker

# Paso 5: Agregar usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker
```

---

## 🪟 Instalación en Windows

### Opción 1: Docker Desktop (Recomendado para Windows 10/11)

**Requisitos**:

- Windows 10 64-bit: Pro, Enterprise o Education (Build 19041+)
- O Windows 11 64-bit: Home, Pro, Enterprise o Education
- WSL 2 instalado

**Pasos**:

1. **Descargar Docker Desktop**:

   - Ir a [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
   - Descargar instalador para Windows

2. **Instalar WSL 2** (si no está instalado):

   ```powershell
   # Ejecutar en PowerShell como Administrador
   wsl --install
   # Reiniciar la computadora
   ```

3. **Ejecutar instalador de Docker Desktop**:

   - Doble clic en `Docker Desktop Installer.exe`
   - Seguir el asistente
   - Marcar "Use WSL 2 instead of Hyper-V"
   - Completar instalación

4. **Verificar instalación**:
   ```powershell
   docker --version
   docker compose version
   ```

**Nota**: Docker Desktop incluye Docker Compose v2 integrado.

---

### Opción 2: Docker en WSL 2 (Sin Docker Desktop)

**Ventajas**:

- Sin interfaz gráfica (más ligero)
- Gratis para uso personal y comercial
- Experiencia similar a Linux

**Pasos**:

1. **Instalar WSL 2 con Ubuntu**:

   ```powershell
   wsl --install -d Ubuntu-22.04
   ```

2. **Dentro de Ubuntu WSL, instalar Docker**:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   ```

3. **Iniciar Docker daemon**:

   ```bash
   sudo service docker start
   ```

4. **Auto-iniciar Docker** (opcional):
   Agregar al archivo `~/.bashrc`:
   ```bash
   if ! service docker status > /dev/null; then
       sudo service docker start > /dev/null
   fi
   ```

---

## 🍎 Instalación en macOS

### Opción 1: Docker Desktop (Recomendado)

**Requisitos**:

- macOS 11 o superior
- Mac con chip Intel o Apple Silicon (M1/M2/M3)

**Pasos**:

1. **Descargar Docker Desktop**:

   - Para Intel: [Docker Desktop para Mac (Intel)](https://desktop.docker.com/mac/main/amd64/Docker.dmg)
   - Para Apple Silicon: [Docker Desktop para Mac (Apple Silicon)](https://desktop.docker.com/mac/main/arm64/Docker.dmg)

2. **Instalar**:

   - Abrir el archivo `.dmg`
   - Arrastrar Docker a la carpeta Aplicaciones
   - Abrir Docker desde Aplicaciones
   - Seguir configuración inicial

3. **Verificar**:
   ```bash
   docker --version
   docker compose version
   ```

---

### Opción 2: Homebrew + Colima (Alternativa libre)

**Ventajas**:

- Open source
- Más ligero que Docker Desktop
- Sin limitaciones de licencia

```bash
# ¿Qué? Instalar Homebrew (si no está instalado)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# ¿Qué? Instalar Docker CLI y Colima
# ¿Para qué? Colima provee el backend de contenedores
brew install docker docker-compose colima

# ¿Qué? Iniciar Colima
# ¿Para qué? Levantar la VM que ejecuta contenedores
colima start

# ¿Qué? Verificar instalación
docker --version
docker compose version
```

---

## ✅ Verificación de Instalación

### 1. Verificar versiones

```bash
# ¿Qué? Muestra versión de Docker Engine
docker --version
# Salida esperada: Docker version 25.0.0+

# ¿Qué? Muestra versión de Docker Compose
# ¿Para qué? Confirmar que es v2 (sin guion)
docker compose version
# Salida esperada: Docker Compose version v2.39.4+
```

**⚠️ Importante**: Si ves `docker-compose` (con guion) estás usando v1 (deprecated). Instala v2.

---

### 2. Probar con contenedor "Hello World"

```bash
# ¿Qué? Ejecuta el contenedor de prueba oficial
# ¿Para qué? Verificar que Docker puede descargar y ejecutar imágenes
# ¿Cómo? Descarga imagen, crea contenedor, ejecuta y muestra mensaje
docker run hello-world
```

**Salida esperada**:

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
...
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

---

### 3. Verificar información del sistema

```bash
# ¿Qué? Muestra información detallada de Docker
# ¿Para qué? Ver configuración, recursos, y estado
docker info
```

**Buscar**:

- `Server Version`: >= 25.0
- `Storage Driver`: overlay2
- `Cgroup Driver`: systemd o cgroupfs
- `CPUs`: Cantidad de cores disponibles
- `Total Memory`: RAM asignada

---

### 4. Verificar permisos (Linux)

```bash
# ¿Qué? Ejecuta comando sin sudo
# ¿Para qué? Confirmar que el usuario está en el grupo docker
docker ps
```

**Si ves error** "permission denied":

```bash
# Solución:
sudo usermod -aG docker $USER
newgrp docker
# O cerrar sesión y volver a entrar
```

---

## 🐳 Primer Contenedor Real: Nginx

Ahora vamos a ejecutar un servidor web Nginx en un contenedor.

```bash
# ¿Qué? Ejecuta Nginx en modo detached (segundo plano)
# ¿Para qué? Levantar un servidor web de prueba
# ¿Cómo? -d = detached, -p = mapeo de puertos, --name = nombre personalizado
docker run -d -p 8080:80 --name mi-nginx nginx:latest

# Verificar que está corriendo:
docker ps
```

**Abrir navegador**: [http://localhost:8080](http://localhost:8080)

Deberías ver: **"Welcome to nginx!"**

---

### Explorar el contenedor

```bash
# ¿Qué? Muestra logs del contenedor
# ¿Para qué? Ver mensajes de inicio y peticiones HTTP
docker logs mi-nginx

# ¿Qué? Muestra logs en tiempo real
docker logs -f mi-nginx

# ¿Qué? Ejecuta un comando dentro del contenedor
# ¿Para qué? Entrar al shell del contenedor para explorar
docker exec -it mi-nginx /bin/bash

# Dentro del contenedor:
ls /usr/share/nginx/html/  # Archivos del sitio web
cat /etc/nginx/nginx.conf  # Configuración de Nginx
exit  # Salir del contenedor
```

---

### Detener y eliminar el contenedor

```bash
# ¿Qué? Detiene el contenedor
# ¿Para qué? Liberar el puerto 8080
docker stop mi-nginx

# ¿Qué? Elimina el contenedor detenido
docker rm mi-nginx

# O ambos en un comando:
docker rm -f mi-nginx  # -f = force (detiene y elimina)
```

---

## 🔧 Configuración Adicional (Opcional pero Recomendado)

### 1. Limitar recursos (Para laptops con poca RAM)

**Docker Desktop**:

- Ir a Settings → Resources
- Ajustar:
  - CPUs: 2-4 cores
  - Memory: 4-8 GB
  - Swap: 1 GB
  - Disk: 60 GB

**Linux (systemd)**:

Crear archivo `/etc/docker/daemon.json`:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "default-address-pools": [
    {
      "base": "172.80.0.0/16",
      "size": 24
    }
  ]
}
```

```bash
# ¿Qué? Reinicia Docker para aplicar cambios
sudo systemctl restart docker
```

---

### 2. Configurar inicio automático (Linux)

```bash
# ¿Qué? Habilita Docker para que inicie con el sistema
# ¿Para qué? No tener que iniciar Docker manualmente
sudo systemctl enable docker
```

---

### 3. Instalar Docker Compose (si no está incluido)

**En algunas distribuciones antiguas**:

```bash
# ¿Qué? Descarga Docker Compose v2 como plugin
# ¿Para qué? Tener la última versión estable
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

# Verificar:
docker compose version
```

---

## 🧪 Prueba Completa: Stack Multi-Contenedor

Vamos a probar Docker Compose con un stack simple.

**Crear archivo `docker-compose.yml`**:

```yaml
# ¿Qué? Stack de prueba con 3 servicios
# ¿Para qué? Verificar que Docker Compose funciona correctamente

services:
  # ¿Qué? Servidor web Nginx
  web:
    image: nginx:latest
    ports:
      - '8080:80'
    volumes:
      - ./html:/usr/share/nginx/html:ro

  # ¿Qué? Base de datos PostgreSQL
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: testpassword
      POSTGRES_DB: testdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 10s

  # ¿Qué? Adminer (GUI para bases de datos)
  adminer:
    image: adminer:latest
    ports:
      - '8081:8080'
    depends_on:
      - db

volumes:
  postgres_data: # ¿Qué? Volumen para persistir datos de PostgreSQL
```

**Crear contenido web**:

```bash
mkdir html
echo "<h1>¡Docker funciona!</h1>" > html/index.html
```

**Levantar el stack**:

```bash
# ¿Qué? Inicia todos los servicios
# ¿Para qué? Probar Docker Compose con múltiples contenedores
docker compose up -d

# Ver estado:
docker compose ps

# Ver logs:
docker compose logs -f
```

**Probar los servicios**:

- Nginx: [http://localhost:8080](http://localhost:8080)
- Adminer: [http://localhost:8081](http://localhost:8081)
  - Sistema: PostgreSQL
  - Servidor: db
  - Usuario: postgres
  - Contraseña: testpassword
  - Base de datos: testdb

**Detener el stack**:

```bash
# ¿Qué? Detiene y elimina todos los contenedores
docker compose down

# Con volúmenes (cuidado, elimina datos):
docker compose down -v
```

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "Cannot connect to the Docker daemon"

**Causa**: Docker no está corriendo.

**Solución Linux**:

```bash
sudo systemctl start docker
sudo systemctl status docker
```

**Solución Windows/Mac**: Abrir Docker Desktop.

---

### Problema 2: "permission denied" en Linux

**Causa**: Usuario no está en el grupo `docker`.

**Solución**:

```bash
sudo usermod -aG docker $USER
newgrp docker
# O cerrar sesión y volver a entrar
```

---

### Problema 3: "port already in use"

**Causa**: Otro proceso está usando el puerto.

**Solución**:

```bash
# Encontrar qué proceso usa el puerto 8080:
sudo lsof -i :8080
# O:
sudo netstat -tulpn | grep 8080

# Detener el proceso o usar otro puerto:
docker run -p 8090:80 nginx
```

---

### Problema 4: Descarga lenta de imágenes

**Causa**: Conexión lenta o mirrors lentos.

**Solución**: Configurar mirror de Docker Hub.

**Archivo `/etc/docker/daemon.json`**:

```json
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}
```

```bash
sudo systemctl restart docker
```

---

### Problema 5: "no space left on device"

**Causa**: Disco lleno de imágenes y contenedores antiguos.

**Solución**:

```bash
# ¿Qué? Limpia recursos no usados
# ¿Para qué? Liberar espacio en disco
docker system prune -a --volumes

# Ver espacio usado:
docker system df
```

---

## 📝 Checklist de Verificación

Marca cada item cuando lo completes:

- [ ] Docker Engine instalado (versión 25.0+)
- [ ] Docker Compose v2 instalado (versión 2.39+)
- [ ] Comando `docker --version` funciona
- [ ] Comando `docker compose version` funciona (sin guion)
- [ ] Contenedor "hello-world" ejecutado exitosamente
- [ ] Nginx corriendo en puerto 8080
- [ ] Explorado contenedor con `docker exec`
- [ ] Usuario agregado al grupo docker (Linux)
- [ ] Stack multi-contenedor funciona con Docker Compose
- [ ] Logs visibles con `docker compose logs`

---

## 📊 Entregable

**Captura de pantalla** que muestre:

1. Salida de `docker --version`
2. Salida de `docker compose version`
3. Salida de `docker ps` con al menos 2 contenedores corriendo
4. Navegador mostrando Nginx en http://localhost:8080

**Formato**: PDF o imagen PNG  
**Nombre**: `S01-P01-InstalarDocker-[TuNombre].pdf`

---

## 🔗 Referencias

- [Docker Install Documentation](https://docs.docker.com/engine/install/)
- [Docker Compose v2](https://docs.docker.com/compose/install/)
- [Docker Hub](https://hub.docker.com/)
- [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)

---

## 📌 Próximos Pasos

Ahora que tienes Docker instalado, en la siguiente práctica crearás tu primer contenedor PostgreSQL y aprenderás a gestionar bases de datos en contenedores.

**Continuar a**: [02-primer-contenedor-postgresql.md](./02-primer-contenedor-postgresql.md)
