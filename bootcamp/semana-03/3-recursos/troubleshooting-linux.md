# Troubleshooting: Problemas Comunes en Linux Server

> **Propósito**: Soluciones paso a paso para los 10 problemas más frecuentes al trabajar con servidores Linux y despliegue remoto.

## 📋 Índice de Problemas

1. [No puedo conectar por SSH](#problema-1-no-puedo-conectar-por-ssh)
2. [Permission denied (permisos)](#problema-2-permission-denied)
3. [Connection refused](#problema-3-connection-refused)
4. [Port already in use](#problema-4-port-already-in-use)
5. [Docker requires sudo](#problema-5-docker-requires-sudo)
6. [UFW bloquea Docker](#problema-6-ufw-bloquea-docker)
7. [No space left on device](#problema-7-no-space-left-on-device)
8. [Container keeps restarting](#problema-8-container-keeps-restarting)
9. [Cannot transfer files (scp fails)](#problema-9-cannot-transfer-files)
10. [Comando not found](#problema-10-comando-not-found)

---

## Problema 1: No puedo conectar por SSH

### Síntomas

```bash
$ ssh ubuntu@34.123.45.67
ssh: connect to host 34.123.45.67 port 22: Connection refused
# O
ssh: connect to host 34.123.45.67 port 22: Connection timed out
```

### Causas Comunes

1. Servidor apagado
2. IP incorrecta
3. Firewall bloqueando puerto 22
4. Servicio SSH no corriendo

### Solución Paso a Paso

#### Verificación 1: ¿El servidor está corriendo?

**En GCP Console:**

- Ve a: Compute Engine → VM instances
- Verifica estado: Debe estar **Running** (círculo verde)
- Si está detenido: Click en ⋮ → **Start**

#### Verificación 2: ¿La IP es correcta?

```bash
# La IP puede cambiar si apagas/prendes el servidor
# Verifica la IP actual en GCP Console
```

**Solución:**

- Copia la **External IP** actual de GCP Console
- Usa esa IP para conectar

#### Verificación 3: ¿El firewall permite SSH?

**Firewall UFW (dentro del servidor):**

- Usa SSH desde navegador (botón SSH en GCP)
- Ejecuta:

```bash
sudo ufw status

# Si SSH no está permitido:
sudo ufw allow 22/tcp
sudo ufw enable
```

**Firewall GCP (reglas de red):**

- Ve a: VPC Network → Firewall → Firewall rules
- Busca regla que permita puerto 22
- Si no existe: Create Firewall Rule
  - Name: `allow-ssh`
  - Targets: All instances
  - Source IP ranges: `0.0.0.0/0`
  - Protocols and ports: `tcp:22`

#### Verificación 4: ¿SSH está corriendo?

**Desde SSH web (botón SSH en GCP):**

```bash
systemctl status sshd

# Si no está corriendo:
sudo systemctl start sshd
sudo systemctl enable sshd
```

### Solución Alternativa

**Usa SSH desde navegador:**

- En GCP Console, click en **SSH** junto a tu VM
- Trabaja desde allí temporalmente

---

## Problema 2: Permission denied

### Síntomas

```bash
$ cat /var/log/syslog
cat: /var/log/syslog: Permission denied

$ docker ps
permission denied while trying to connect to the Docker daemon socket

$ mkdir /opt/proyecto
mkdir: cannot create directory '/opt/proyecto': Permission denied
```

### Causas

1. No tienes permisos para el archivo/carpeta
2. Necesitas usar `sudo`
3. Usuario no está en grupo correcto (ej: docker)

### Soluciones

#### Para archivos del sistema: Usa sudo

```bash
# ¿Qué? - Ejecutar con permisos de administrador
# ¿Para qué? - Acceder a archivos/carpetas del sistema

# Leer archivo del sistema
sudo cat /var/log/syslog

# Editar archivo del sistema
sudo nano /etc/hosts

# Crear carpeta en /opt
sudo mkdir /opt/proyecto
```

#### Para Docker: Agregar usuario al grupo

```bash
# ¿Qué? - Agregar usuario actual al grupo docker
# ¿Para qué? - Ejecutar docker sin sudo

sudo usermod -aG docker $USER

# Aplicar cambios (opción 1: mejor)
exit
# Vuelve a conectar por SSH

# Aplicar cambios (opción 2: rápida)
newgrp docker

# Verificar
docker ps
```

#### Para tus propios archivos: Cambiar propietario

```bash
# ¿Qué? - Cambiar propietario de archivo/carpeta
# ¿Para qué? - Poder modificarlo sin sudo

sudo chown -R $USER:$USER /ruta/carpeta/

# Ejemplo:
sudo chown -R ubuntu:ubuntu /home/ubuntu/proyecto/
```

---

## Problema 3: Connection refused

### Síntomas

```bash
# Desde navegador: http://IP:3000
# Error: Unable to connect / Connection refused

# Desde servidor:
$ curl http://localhost:3000
curl: (7) Failed to connect to localhost port 3000: Connection refused
```

### Causas

1. Aplicación no está corriendo
2. Aplicación escucha en puerto diferente
3. Firewall bloquea el puerto

### Solución Paso a Paso

#### Paso 1: ¿La aplicación está corriendo?

```bash
docker compose ps

# Debe mostrar STATUS: Up
# Si dice "Exit 1" o "Restarting":
docker compose logs nombre-servicio
```

#### Paso 2: ¿En qué puerto escucha?

```bash
# Ver puertos expuestos
docker compose ps

# Ver puertos abiertos en el servidor
ss -tulpn | grep LISTEN

# Buscar puerto específico
ss -tulpn | grep :3000
```

#### Paso 3: ¿El firewall permite el puerto?

```bash
# Firewall UFW
sudo ufw status | grep 3000

# Si no está:
sudo ufw allow 3000/tcp
```

#### Paso 4: ¿GCP permite el puerto?

**En GCP Console:**

- VPC Network → Firewall → Create Firewall Rule
- Name: `allow-app-port-3000`
- Source IP ranges: `0.0.0.0/0`
- Protocols: `tcp:3000`

#### Paso 5: ¿Docker expone correctamente?

**Verifica docker-compose.yml:**

```yaml
services:
  app:
    ports:
      - '3000:3000' # Debe ser: HOST:CONTAINER
      # NO: "localhost:3000:3000"
```

---

## Problema 4: Port already in use

### Síntomas

```bash
$ docker compose up
Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use
```

### Causas

Otro proceso ya está usando ese puerto

### Soluciones

#### Solución 1: Encontrar y detener el proceso

```bash
# ¿Qué? - Buscar qué proceso usa el puerto
sudo ss -tulpn | grep :5432

# Salida ejemplo:
# tcp LISTEN 0 128 0.0.0.0:5432 0.0.0.0:* users:(("postgres",pid=1234,...))

# Detener el proceso
sudo kill 1234

# O detener servicio
sudo systemctl stop postgresql
```

#### Solución 2: Cambiar puerto en docker-compose.yml

```yaml
# Cambiar puerto del HOST (izquierda)
services:
  postgres:
    ports:
      - '5433:5432' # HOST:CONTAINER
      # Ahora accesible en puerto 5433
```

#### Solución 3: No exponer el puerto (si no es necesario)

```yaml
# Si no necesitas acceso desde fuera del servidor
services:
  postgres:
    # Elimina la sección ports:
    # Solo será accesible desde otros contenedores
```

---

## Problema 5: Docker requires sudo

### Síntomas

```bash
$ docker ps
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
```

### Causa

Usuario no está en el grupo `docker`

### Solución

```bash
# ¿Qué? - Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Aplicar cambios (IMPORTANTE)
# Opción 1: Cerrar y volver a conectar (recomendado)
exit
# Luego: ssh usuario@servidor

# Opción 2: Nuevo shell
newgrp docker

# Verificar que funciona
docker ps
```

---

## Problema 6: UFW bloquea Docker

### Síntomas

- `docker compose ps` muestra: STATUS Up
- `curl http://localhost:3000` funciona EN el servidor
- `http://IP:3000` NO funciona desde tu navegador

### Causa

UFW bloquea puertos de Docker

### Solución

```bash
# Permitir puertos necesarios
sudo ufw allow 3000/tcp
sudo ufw allow 8080/tcp

# Verificar
sudo ufw status

# Reiniciar Docker (por si acaso)
sudo systemctl restart docker
docker compose restart
```

### Solución Alternativa (Solo troubleshooting)

```bash
# Deshabilitar UFW temporalmente
sudo ufw disable

# Probar acceso
# http://IP:3000

# Si funciona, el problema es UFW
# Volver a habilitar
sudo ufw enable

# Agregar reglas correctas
sudo ufw allow 3000/tcp
```

---

## Problema 7: No space left on device

### Síntomas

```bash
$ docker compose up
Error: no space left on device

$ docker pull imagen
Error response from daemon: write /var/lib/docker: no space left on device
```

### Causa

Disco lleno

### Solución Paso a Paso

#### Paso 1: Verificar espacio

```bash
df -h

# Busca línea con "/"
# Si uso > 90%, estás sin espacio
```

#### Paso 2: Limpiar Docker

```bash
# Limpiar contenedores detenidos, imágenes no usadas
docker system prune

# Limpiar TODO (incluye imágenes en uso)
docker system prune -a

# Limpiar volúmenes (⚠️ BORRA DATOS)
docker volume prune
```

#### Paso 3: Limpiar paquetes APT

```bash
sudo apt autoremove
sudo apt clean
```

#### Paso 4: Encontrar archivos grandes

```bash
# Buscar carpetas que ocupan más espacio
sudo du -h --max-depth=1 /home | sort -hr

# Buscar archivos > 100MB
sudo find /home -type f -size +100M -exec ls -lh {} \;
```

#### Paso 5: Si nada funciona, ampliar disco

**En GCP:**

1. Detén la VM
2. Discos → Click en tu disco → Editar
3. Aumenta tamaño (ej: 20GB → 30GB)
4. Guarda y reinicia VM
5. Dentro de VM, expande partición:

```bash
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1
```

---

## Problema 8: Container keeps restarting

### Síntomas

```bash
$ docker compose ps
NAME                   STATUS
proyecto-postgres-1    Restarting (1) 5 seconds ago
```

### Causas

1. Error en la aplicación/servicio
2. Puerto ocupado
3. Variable de entorno incorrecta
4. Sintaxis en config

### Solución

#### Paso 1: Ver logs

```bash
# ¿Qué? - Ver por qué está fallando
docker compose logs postgres

# Últimas 50 líneas
docker compose logs --tail=50 postgres
```

#### Paso 2: Errores comunes y soluciones

**Error: "database \"xxx\" does not exist"**

```bash
# Verificar nombre de BD en .env
cat .env | grep POSTGRES_DB

# Verificar docker-compose.yml
grep POSTGRES_DB docker-compose.yml
```

**Error: "port is already allocated"**

```bash
# Ver qué usa el puerto
sudo ss -tulpn | grep :5432

# Cambiar puerto en docker-compose.yml
```

**Error: "initdb: invalid locale settings"**

```yaml
# En docker-compose.yml, agregar:
services:
  postgres:
    environment:
      - LC_ALL=C.UTF-8
```

#### Paso 3: Recrear contenedor

```bash
# Detener y eliminar
docker compose down

# Eliminar volúmenes (⚠️ BORRA DATOS)
docker compose down -v

# Volver a crear
docker compose up -d
```

---

## Problema 9: Cannot transfer files

### Síntomas

```bash
$ scp proyecto.zip ubuntu@servidor:/home/ubuntu/
Permission denied

# O
scp: Connection refused
```

### Soluciones

#### Si es "Permission denied"

```bash
# Transferir a carpeta donde tienes permisos
scp proyecto.zip ubuntu@servidor:/home/ubuntu/

# NO a /opt o /var (requieren sudo)
```

#### Si es "Connection refused"

Ver [Problema 1: SSH](#problema-1-no-puedo-conectar-por-ssh)

#### Alternativa: Usar rsync

```bash
rsync -avz proyecto/ ubuntu@servidor:/home/ubuntu/proyecto/
```

#### Alternativa: Usar Git

```bash
# En tu máquina local (si usas Git)
git push

# En el servidor
git clone https://github.com/tu-usuario/repo.git
# O
cd proyecto && git pull
```

---

## Problema 10: Comando not found

### Síntomas

```bash
$ docker
-bash: docker: command not found

$ nano
-bash: nano: command not found
```

### Causas

1. Comando no instalado
2. PATH incorrecta
3. Typo en el nombre

### Soluciones

#### Instalar comando faltante

```bash
# Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Nano (editor)
sudo apt install nano

# Htop (monitor)
sudo apt install htop

# Curl
sudo apt install curl

# Git
sudo apt install git
```

#### Verificar si está instalado

```bash
# Buscar comando
which docker
which nano

# Si devuelve ruta: está instalado
# Si no devuelve nada: no está instalado
```

#### Ver comandos disponibles

```bash
# Autocompletar con Tab
doc[Tab][Tab]
# Mostrará: docker, ...

# Buscar paquete
apt search nombre
```

---

## 🔄 Flujo General de Troubleshooting

Cuando encuentres un error, sigue este proceso:

### 1. Lee el Mensaje de Error

```bash
# Primera línea suele indicar el problema
# Última línea suele indicar el síntoma
```

### 2. Busca en este Documento

Usa `Ctrl+F` para buscar palabras clave del error

### 3. Google el Error (En Inglés)

```
# Formato recomendado:
ubuntu "mensaje de error exacto" docker

# Ejemplo:
ubuntu "permission denied" docker socket
```

### 4. Verifica lo Básico

```bash
# ¿Está corriendo?
docker compose ps
systemctl status docker

# ¿Hay logs útiles?
docker compose logs

# ¿Hay espacio en disco?
df -h

# ¿Hay RAM disponible?
free -h
```

### 5. Prueba Solución Más Simple Primero

```bash
# Antes de reinstalar o cambiar config:
# 1. Reinicia el servicio
docker compose restart

# 2. Reinicia Docker
sudo systemctl restart docker

# 3. Reinicia el servidor (último recurso)
sudo reboot
```

---

## 📚 Recursos Adicionales

### Logs Útiles

```bash
# Logs de sistema
sudo tail -f /var/log/syslog

# Logs de Docker
journalctl -u docker -f

# Logs de servicios
docker compose logs -f
```

### Comandos de Diagnóstico

```bash
# Estado general del sistema
htop
df -h
free -h
ss -tulpn

# Estado de servicios
systemctl status docker
systemctl status sshd

# Red
ip addr
curl -I http://localhost:3000
```

---

## 🆘 ¿Aún No Funciona?

Si después de seguir esta guía aún tienes problemas:

1. **Documenta el error:**

   - Comando que ejecutaste
   - Mensaje de error completo
   - Output de: `docker compose ps` y `docker compose logs`

2. **Toma screenshots** de:

   - Terminal con el error
   - GCP Console (estado de VM)

3. **Busca ayuda:**
   - Foro del curso
   - Stack Overflow
   - Email al instructor con detalles

---

> **Recuerda**: El 90% de los problemas se resuelven con: 1) Leer el error completo, 2) Buscar en Google, 3) Reiniciar el servicio. No te frustres, troubleshooting es parte del aprendizaje. 🚀
