# Práctica 1: Setup Inicial de Servidor en Cloud

> **Objetivo**: Crear y configurar un servidor Ubuntu Server en Google Cloud Platform, instalar Docker y preparar el entorno para despliegue de aplicaciones.

## 📋 Tabla de Contenidos

1. [Pre-requisitos](#pre-requisitos)
2. [Paso 1: Crear Cuenta GCP](#paso-1-crear-cuenta-gcp)
3. [Paso 2: Crear VM Ubuntu Server](#paso-2-crear-vm-ubuntu-server)
4. [Paso 3: Conectar vía SSH](#paso-3-conectar-vía-ssh)
5. [Paso 4: Actualizar Sistema](#paso-4-actualizar-sistema)
6. [Paso 5: Instalar Docker](#paso-5-instalar-docker)
7. [Paso 6: Configurar Firewall](#paso-6-configurar-firewall)
8. [Paso 7: Crear Usuario No-Root](#paso-7-crear-usuario-no-root)
9. [Verificación Final](#verificación-final)
10. [Troubleshooting](#troubleshooting)

**⏱️ Tiempo estimado**: 60 minutos

---

## Pre-requisitos

Antes de comenzar, asegúrate de tener:

- [ ] Cuenta de Google (Gmail)
- [ ] Tarjeta de crédito/débito (para verificación, no se cobra si usas Free Tier)
- [ ] Conexión a internet estable
- [ ] Cliente SSH instalado:
  - **Linux/Mac**: Ya incluido (`ssh`)
  - **Windows**: PowerShell, CMD, o Git Bash

---

## Paso 1: Crear Cuenta GCP

### 1.1 Registrarse en Google Cloud

```bash
# ¿Qué? - Crear cuenta gratuita en Google Cloud Platform
# ¿Para qué? - Acceder a $300 de créditos + servicios Always Free
# ¿Cómo? - Visita: https://cloud.google.com/free
```

1. Visita: [https://cloud.google.com/free](https://cloud.google.com/free)
2. Click en **"Comenzar gratis"** o **"Start Free"**
3. Inicia sesión con tu cuenta de Google
4. Completa el formulario:
   - País: Colombia
   - Tipo de cuenta: Individual
   - Acepta términos y condiciones
5. Ingresa datos de tarjeta (solo verificación, no se cobra)

### 1.2 Verificar Créditos

Después de registrarte deberías ver:

- ✅ $300 USD en créditos (válidos por 90 días)
- ✅ Always Free tier (no expira)

**Always Free incluye:**

- 1 VM f1-micro en regiones de EE.UU.
- 30 GB de almacenamiento HDD
- 1 GB de snapshot storage
- 1 GB de tráfico de red saliente (excepto China/Australia)

---

## Paso 2: Crear VM Ubuntu Server

### 2.1 Acceder a Compute Engine

1. En la consola de GCP, ve a: **Menú ☰** → **Compute Engine** → **VM instances**
2. Si es la primera vez, espera que se active la API (1-2 minutos)
3. Click en **"Create Instance"** o **"Crear Instancia"**

### 2.2 Configurar la VM

**Configuración recomendada (FREE TIER):**

```yaml
# ¿Qué? - Especificaciones de la VM gratuita
# ¿Para qué? - Cumplir con Free Tier y evitar costos

Nombre: ubuntu-bootcamp-implantacion
Región: us-central1 (Iowa) o us-west1 (Oregon)
Zona: us-central1-a (o cualquier "a" de la región seleccionada)

# Tipo de máquina:
Serie: E2
Tipo de máquina: e2-micro (2 vCPU, 1 GB RAM)
# IMPORTANTE: f1-micro es parte del Always Free, pero e2-micro da mejor rendimiento
# Si quieres 100% gratis, elige: f1-micro (1 vCPU compartida, 614 MB RAM)

# Disco de arranque:
Sistema operativo: Ubuntu
Versión: Ubuntu 22.04 LTS
Tipo de disco de arranque: Balanced persistent disk
Tamaño: 10 GB (mínimo), 20 GB (recomendado)

# Firewall:
☑ Permitir tráfico HTTP
☑ Permitir tráfico HTTPS
```

### 2.3 Configuración Detallada en Consola

**Nombre y región:**

- **Name**: `ubuntu-bootcamp-implantacion`
- **Region**: Selecciona `us-central1 (Iowa)` ← **IMPORTANTE: Free Tier**
- **Zone**: `us-central1-a`

**Machine configuration:**

- **Series**: E2
- **Machine type**: e2-micro (2 vCPU, 1 GB memory)
  - Para Always Free: Cambia a f1-micro

**Boot disk:**

- Click en **"CHANGE"**
- **Operating system**: Ubuntu
- **Version**: Ubuntu 22.04 LTS
- **Boot disk type**: Balanced persistent disk
- **Size**: 20 GB
- Click **"SELECT"**

**Firewall:**

- ☑ Allow HTTP traffic
- ☑ Allow HTTPS traffic

**Costo estimado:**

- Con f1-micro: **$0.00/mes** (Free Tier)
- Con e2-micro: ~$6-7/mes (no es Free, pero más rendimiento)

### 2.4 Crear la VM

1. Revisa que todo esté correcto
2. Click en **"CREATE"** (abajo de la página)
3. Espera 30-60 segundos mientras se crea

**Resultado esperado:**

- VM con estado: ✅ **Running** (círculo verde)
- IP externa asignada (ej: `34.123.45.67`)

---

## Paso 3: Conectar vía SSH

### 3.1 Opción A: SSH desde Navegador (Más Fácil)

```bash
# ¿Qué? - Conectar desde navegador web
# ¿Para qué? - No requiere configuración local
```

1. En la lista de VMs, ubica tu instancia
2. Click en **"SSH"** (botón en la columna de la derecha)
3. Se abrirá una ventana nueva con terminal
4. ¡Listo! Ya estás conectado

**Ventajas:**

- ✅ No requiere configuración
- ✅ Funciona desde cualquier computador
- ✅ No hay problemas de firewall institucional

**Desventajas:**

- ❌ No puedes transferir archivos fácilmente
- ❌ Dependes de navegador

### 3.2 Opción B: SSH desde Terminal Local (Recomendado)

```bash
# ¿Qué? - Conectar desde tu terminal local
# ¿Para qué? - Mejor experiencia, transferencia de archivos
# ¿Cómo? - Usa comando ssh con IP externa
```

**Paso 1: Obtener IP externa**

- En la consola GCP, copia la **External IP** de tu VM
- Ejemplo: `34.123.45.67`

**Paso 2: Conectar**

```bash
# Reemplaza EXTERNAL_IP con tu IP
ssh YOUR_USERNAME@EXTERNAL_IP

# Ejemplo:
ssh usuario_12345678@34.123.45.67

# Primera vez te preguntará:
# "Are you sure you want to continue connecting (yes/no)?"
# Escribe: yes
```

**¿Cómo saber tu username?**

- En GCP, el username es tu nombre de usuario de Google (antes del @)
- Ejemplo: Si tu email es `juan.perez@gmail.com`, tu username es `juan_perez`
- GCP reemplaza `.` por `_` automáticamente

**Si no funciona:**

- Ve a la VM en GCP → Click en **"SHOW INFO PANEL"** (arriba derecha)
- Busca **SSH** → Copia el comando completo

### 3.3 Verificar Conexión

Una vez conectado, deberías ver algo como:

```
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-1047-gcp x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

usuario@ubuntu-bootcamp-implantacion:~$
```

✅ **¡Estás dentro del servidor!**

---

## Paso 4: Actualizar Sistema

### 4.1 Actualizar Lista de Paquetes

```bash
# ¿Qué? - Actualizar índice de paquetes disponibles
# ¿Para qué? - Obtener información de últimas versiones
# ¿Cómo? - Consulta repositorios oficiales de Ubuntu

sudo apt update
```

**Explicación:**

- `sudo`: Ejecuta con permisos de administrador
- `apt`: Gestor de paquetes de Ubuntu
- `update`: Actualiza la lista (no instala nada)

**Salida esperada:**

```
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
...
Reading package lists... Done
Building dependency tree... Done
```

### 4.2 Actualizar Paquetes Instalados

```bash
# ¿Qué? - Actualizar todos los paquetes instalados
# ¿Para qué? - Aplicar parches de seguridad y mejoras
# ¿Cómo? - Descarga e instala nuevas versiones

sudo apt upgrade -y
```

**Explicación:**

- `upgrade`: Actualiza paquetes instalados
- `-y`: Responde "yes" automáticamente (no pide confirmación)

**Tiempo estimado:** 2-5 minutos

**Salida esperada:**

```
Reading package lists... Done
Building dependency tree... Done
...
Unpacking xxx ...
Setting up xxx ...
```

### 4.3 Reiniciar (Opcional, si actualizó kernel)

```bash
# ¿Qué? - Verificar si se requiere reinicio
# ¿Para qué? - Aplicar actualizaciones del kernel

ls /var/run/reboot-required

# Si existe el archivo:
sudo reboot

# Espera 30 segundos y reconecta con SSH
```

---

## Paso 5: Instalar Docker

### 5.1 Método Rápido: Script Oficial

```bash
# ¿Qué? - Descargar script de instalación de Docker
# ¿Para qué? - Instalar Docker de forma automatizada
# ¿Cómo? - Script configura repositorio y instala Docker Engine

curl -fsSL https://get.docker.com -o get-docker.sh
```

**Explicación:**

- `curl`: Descarga archivos de internet
- `-fsSL`: Opciones (fail silently, show errors, follow redirects, Location)
- `-o`: Guarda en archivo `get-docker.sh`

```bash
# ¿Qué? - Ejecutar script de instalación
# ¿Para qué? - Instalar Docker Engine + Docker Compose
# ¿Cómo? - Script detecta SO y configura todo automáticamente

sudo sh get-docker.sh
```

**Tiempo estimado:** 1-2 minutos

**Salida esperada:**

```
# Executing docker install script, commit: xxx
+ sh -c apt-get update -qq >/dev/null
+ sh -c apt-get install -y docker-ce docker-ce-cli ...
...
================================================================================
To run Docker as a non-privileged user, consider setting up the
Docker daemon in rootless mode for your user:

    dockerd-rootless-setuptool.sh install

Visit https://docs.docker.com/go/rootless/ to learn about rootless mode.

================================================================================
```

### 5.2 Agregar Usuario al Grupo Docker

```bash
# ¿Qué? - Agregar usuario actual al grupo "docker"
# ¿Para qué? - Ejecutar docker sin sudo (más cómodo)
# ¿Cómo? - Modifica grupos del usuario

sudo usermod -aG docker $USER
```

**Explicación:**

- `usermod`: Modificar usuario
- `-aG docker`: Agregar (a) a grupo (G) "docker"
- `$USER`: Variable con tu nombre de usuario actual

**Para aplicar cambios:**

```bash
# Opción 1: Cerrar sesión y volver a conectar (recomendado)
exit
# Luego: ssh usuario@ip

# Opción 2: Nuevo shell con grupos actualizados
newgrp docker
```

### 5.3 Verificar Instalación

```bash
# ¿Qué? - Verificar versión de Docker
docker --version

# Salida esperada:
# Docker version 24.0.7, build xxx

# ¿Qué? - Verificar versión de Docker Compose
docker compose version

# Salida esperada:
# Docker Compose version v2.23.0

# ¿Qué? - Probar que funciona
docker run hello-world
```

**Si `docker run hello-world` funciona, verás:**

```
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

✅ **Docker instalado correctamente!**

### 5.4 Habilitar Docker al Inicio

```bash
# ¿Qué? - Configurar Docker para iniciar automáticamente con el sistema
# ¿Para qué? - Que los contenedores arranquen tras reinicio del servidor

sudo systemctl enable docker

# Verificar estado
systemctl status docker
```

**Salida esperada:**

```
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; ...)
     Active: active (running) since ...
```

---

## Paso 6: Configurar Firewall

### 6.1 Verificar Estado Inicial

```bash
# ¿Qué? - Ver estado del firewall UFW
# ¿Para qué? - Saber si está activo y qué reglas tiene

sudo ufw status
```

**Salida esperada:**

```
Status: inactive
```

### 6.2 Permitir SSH (Puerto 22)

```bash
# ¿Qué? - Permitir conexiones SSH (puerto 22)
# ¿Para qué? - Mantener acceso remoto al servidor
# ⚠️ CRÍTICO: Hacer ANTES de activar el firewall

sudo ufw allow 22/tcp
```

**Salida:**

```
Rules updated
Rules updated (v6)
```

### 6.3 Permitir HTTP y HTTPS

```bash
# ¿Qué? - Permitir tráfico web (puertos 80 y 443)
# ¿Para qué? - Acceder a aplicaciones web desde navegador

sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

### 6.4 Permitir Puertos Personalizados (Ejemplo)

```bash
# ¿Qué? - Permitir puerto 8080 (ejemplo para aplicación)
# ¿Para qué? - Acceder a app que corre en puerto específico

sudo ufw allow 8080/tcp

# Puedes agregar los puertos que necesites:
sudo ufw allow 3000/tcp  # Frontend React/Vue
sudo ufw allow 5000/tcp  # Backend Flask
sudo ufw allow 5432/tcp  # PostgreSQL (si quieres acceso externo)
```

### 6.5 Activar Firewall

```bash
# ¿Qué? - Activar el firewall UFW
# ¿Para qué? - Aplicar las reglas de seguridad

sudo ufw enable
```

**Preguntará:**

```
Command may disrupt existing ssh connections. Proceed with operation (y|n)?
```

**Responde:** `y` (ya permitiste SSH, no hay problema)

### 6.6 Verificar Reglas

```bash
# ¿Qué? - Ver reglas activas del firewall
sudo ufw status

# Salida esperada:
# Status: active
#
# To                         Action      From
# --                         ------      ----
# 22/tcp                     ALLOW       Anywhere
# 80/tcp                     ALLOW       Anywhere
# 443/tcp                    ALLOW       Anywhere
# 8080/tcp                   ALLOW       Anywhere
```

✅ **Firewall configurado correctamente!**

---

## Paso 7: Crear Usuario No-Root

### 7.1 ¿Por qué crear otro usuario?

**Seguridad:**

- ❌ Usar usuario root es peligroso (poder total)
- ✅ Usuario normal con `sudo` es más seguro
- ✅ Separación de responsabilidades

### 7.2 Crear Usuario "deploy"

```bash
# ¿Qué? - Crear nuevo usuario llamado "deploy"
# ¿Para qué? - Usuario dedicado para despliegues

sudo adduser deploy
```

**Te preguntará:**

```
New password: (escribe contraseña segura)
Retype new password: (repite)
Full Name []: Deploy User
Room Number []: (Enter)
Work Phone []: (Enter)
Home Phone []: (Enter)
Other []: (Enter)
Is the information correct? [Y/n] y
```

### 7.3 Agregar a Grupos

```bash
# ¿Qué? - Agregar usuario "deploy" a grupos sudo y docker
# ¿Para qué? - Permitirle usar sudo y ejecutar docker sin sudo

sudo usermod -aG sudo,docker deploy

# Verificar grupos
groups deploy

# Salida esperada:
# deploy : deploy sudo docker
```

### 7.4 Probar Usuario (Opcional)

```bash
# ¿Qué? - Cambiar a usuario deploy
su - deploy

# Verificar que puede usar docker
docker ps

# Verificar que puede usar sudo
sudo echo "Funciona!"

# Volver al usuario original
exit
```

---

## Verificación Final

### Checklist de Completación

Ejecuta estos comandos para verificar que todo está correcto:

```bash
# 1. Verificar sistema operativo y versión
cat /etc/os-release | grep PRETTY_NAME
# Esperado: Ubuntu 22.04.x LTS

# 2. Verificar RAM disponible
free -h
# Esperado: ~1 GB (e2-micro) o ~600 MB (f1-micro)

# 3. Verificar espacio en disco
df -h | grep "/$"
# Esperado: ~20 GB total, 5-10 GB usado

# 4. Verificar Docker
docker --version
docker compose version
docker ps

# 5. Verificar firewall
sudo ufw status
# Esperado: Status active, reglas para 22, 80, 443

# 6. Verificar usuario deploy existe
id deploy
# Esperado: uid=1001(deploy) gid=1001(deploy) groups=...
```

### Test de Conectividad

```bash
# ¿Qué? - Verificar que el servidor puede descargar de internet
# ¿Para qué? - Asegurar que Docker puede descargar imágenes

curl -I https://hub.docker.com

# Esperado: HTTP/2 200
```

### Resumen de Estado

Si todo está correcto, deberías tener:

- ✅ Ubuntu Server 22.04 LTS corriendo
- ✅ Sistema actualizado (apt update/upgrade)
- ✅ Docker 24.0+ y Docker Compose v2
- ✅ Usuario agregado al grupo docker
- ✅ Firewall (UFW) activo con reglas básicas
- ✅ Usuario "deploy" creado con permisos sudo
- ✅ Acceso SSH funcionando

---

## Troubleshooting

### Problema 1: No puedo conectar por SSH

**Síntoma:**

```
ssh: connect to host 34.123.45.67 port 22: Connection refused
```

**Soluciones:**

1. Verifica que la VM está **Running** en GCP
2. Verifica la IP externa (puede cambiar si apagas/prendes)
3. Usa SSH desde navegador (botón SSH en GCP)
4. Verifica firewall de GCP (debe permitir puerto 22)

### Problema 2: Docker requiere sudo

**Síntoma:**

```
$ docker ps
permission denied while trying to connect to the Docker daemon socket
```

**Solución:**

```bash
# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Cerrar sesión y volver a conectar
exit
ssh usuario@ip

# Verificar
docker ps
```

### Problema 3: UFW bloquea Docker

**Síntoma:**
Los contenedores no son accesibles desde internet

**Solución:**

```bash
# Permitir puertos específicos
sudo ufw allow 8080/tcp

# O deshabilitar UFW temporalmente (solo troubleshooting)
sudo ufw disable

# No olvides reactivarlo después
sudo ufw enable
```

### Problema 4: Espacio en disco lleno

**Síntoma:**

```
no space left on device
```

**Solución:**

```bash
# Ver uso de disco
df -h

# Limpiar imágenes Docker no usadas
docker system prune -a

# Limpiar paquetes APT
sudo apt autoremove
sudo apt clean
```

### Más Problemas

Consulta: `3-recursos/troubleshooting-linux.md`

---

## Próximos Pasos

✅ Has completado el setup básico del servidor!

**Ahora puedes:**

1. Continuar con **Práctica 2**: Desplegar proyecto remoto
2. Familiarizarte más con comandos Linux (ver cheatsheet)
3. Explorar el servidor (navegar carpetas, crear archivos)

**No olvides:**

- 🛑 **Shutdown VM** cuando termines la sesión (evita costos)
  - En GCP: VM instances → ⋮ → Stop
  - Volver a encender: ⋮ → Start
- 💾 Anotar tu IP externa (cambia si apagas/prendes)
- 📝 Documentar comandos que usaste

---

## Resumen de Comandos Usados

```bash
# Actualizar sistema
sudo apt update
sudo apt upgrade -y

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Configurar firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# Crear usuario deploy
sudo adduser deploy
sudo usermod -aG sudo,docker deploy

# Verificar
docker --version
sudo ufw status
free -h
df -h
```

---

¡Felicidades! Has completado la Práctica 1. 🎉

**Siguiente**: [Práctica 2 - Desplegar Proyecto Remoto](./02-deploy-proyecto-remoto.md)
