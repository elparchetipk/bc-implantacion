# Cheatsheet: Linux Server para Implantación

> **Propósito**: Referencia rápida de los 15 comandos más usados en implantación de software. Imprime esta página o tenla siempre abierta.

## 📋 Índice Rápido

1. [SSH y Conexión](#ssh-y-conexión)
2. [Navegación y Archivos](#navegación-y-archivos)
3. [Transferencia de Archivos](#transferencia-de-archivos)
4. [Gestión de Paquetes](#gestión-de-paquetes)
5. [Docker](#docker)
6. [Firewall (UFW)](#firewall-ufw)
7. [Servicios (systemctl)](#servicios-systemctl)
8. [Monitoreo de Recursos](#monitoreo-de-recursos)
9. [Permisos](#permisos)
10. [Flujos de Trabajo Típicos](#flujos-de-trabajo-típicos)

---

## SSH y Conexión

### Conectar a Servidor

```bash
# Sintaxis básica
ssh usuario@ip-del-servidor

# Ejemplo
ssh ubuntu@34.123.45.67

# Con puerto personalizado
ssh -p 2222 usuario@servidor

# Con clave SSH específica
ssh -i ~/.ssh/mi-clave.pem usuario@servidor
```

### Generar Claves SSH

```bash
# Generar par de claves (privada + pública)
ssh-keygen -t rsa -b 4096 -C "tu-email@ejemplo.com"

# Copiar clave pública al servidor
ssh-copy-id usuario@servidor
```

### Salir de SSH

```bash
# Cerrar sesión
exit

# O presiona: Ctrl + D
```

---

## Navegación y Archivos

### Los 5 Comandos Esenciales

```bash
# 1. ¿Dónde estoy?
pwd

# 2. ¿Qué hay aquí?
ls -la

# 3. Ir a otra carpeta
cd /ruta/carpeta

# 4. Ver contenido de archivo
cat archivo.txt

# 5. Ver fin de archivo (logs)
tail -f archivo.log
```

### Comandos Completos

```bash
# Listar archivos
ls              # Simple
ls -l           # Detallado
ls -la          # Incluye ocultos
ls -lh          # Tamaños legibles (KB, MB)

# Cambiar directorio
cd /ruta        # Absoluta
cd ..           # Subir un nivel
cd ~            # Home del usuario
cd -            # Directorio anterior

# Crear/Eliminar
mkdir carpeta           # Crear carpeta
mkdir -p a/b/c          # Crear estructura completa
rm archivo.txt          # Eliminar archivo
rm -r carpeta/          # Eliminar carpeta
rm -rf carpeta/         # Forzar eliminación (¡cuidado!)

# Copiar/Mover
cp origen destino       # Copiar archivo
cp -r carpeta/ copia/   # Copiar carpeta
mv viejo nuevo          # Renombrar
mv archivo /ruta/       # Mover

# Ver contenido
cat archivo.txt         # Todo el archivo
less archivo.txt        # Con paginación (q para salir)
head -n 20 archivo.txt  # Primeras 20 líneas
tail -n 50 archivo.txt  # Últimas 50 líneas
tail -f archivo.log     # Seguir en tiempo real

# Buscar
find /ruta -name "*.txt"        # Buscar archivos
grep "texto" archivo.txt        # Buscar en archivo
grep -r "TODO" .                # Buscar recursivamente
```

---

## Transferencia de Archivos

### SCP (Secure Copy)

```bash
# DESDE máquina local HACIA servidor
scp archivo.txt usuario@servidor:/ruta/destino/
scp -r carpeta/ usuario@servidor:/home/ubuntu/

# DESDE servidor HACIA máquina local
scp usuario@servidor:/ruta/archivo.txt ./

# Con puerto personalizado
scp -P 2222 archivo.txt usuario@servidor:/ruta/
```

### RSYNC (Recomendado)

```bash
# Sincronizar carpeta (más eficiente que scp)
rsync -avz carpeta/ usuario@servidor:/ruta/destino/

# Explicación de flags:
# -a: modo archivo (preserva permisos)
# -v: verbose (muestra progreso)
# -z: compresión (más rápido)

# Con progreso visual
rsync -avz --progress carpeta/ usuario@servidor:/ruta/

# Excluir archivos
rsync -avz --exclude 'node_modules' carpeta/ usuario@servidor:/ruta/
```

---

## Gestión de Paquetes

### APT (Ubuntu/Debian)

```bash
# Actualizar lista de paquetes
sudo apt update

# Actualizar paquetes instalados
sudo apt upgrade -y

# Instalar paquete
sudo apt install nombre-paquete

# Buscar paquete
apt search nombre

# Ver info de paquete
apt show nombre

# Eliminar paquete
sudo apt remove nombre
sudo apt purge nombre   # Incluye configuración

# Limpiar
sudo apt autoremove     # Elimina dependencias no usadas
sudo apt clean          # Limpia cache
```

---

## Docker

### Comandos Esenciales

```bash
# Ver versión
docker --version
docker compose version

# Listar contenedores
docker ps               # Solo corriendo
docker ps -a            # Todos (incluye detenidos)

# Listar imágenes
docker images

# Docker Compose (Proyecto)
docker compose up -d            # Levantar (segundo plano)
docker compose down             # Detener y eliminar
docker compose ps               # Estado de servicios
docker compose logs             # Ver logs
docker compose logs -f          # Seguir logs en tiempo real
docker compose restart          # Reiniciar servicios
docker compose pull             # Descargar imágenes

# Contenedores Individuales
docker start nombre             # Iniciar
docker stop nombre              # Detener
docker restart nombre           # Reiniciar
docker logs nombre              # Ver logs
docker logs -f nombre           # Seguir logs
docker exec -it nombre bash     # Entrar al contenedor

# Limpieza
docker system prune             # Limpiar no usados
docker system prune -a          # Limpiar todo (incluye imágenes)
docker volume prune             # Limpiar volúmenes no usados

# Verificar recursos
docker stats                    # Uso de CPU/RAM en tiempo real
```

---

## Firewall (UFW)

### Comandos Básicos

```bash
# Ver estado
sudo ufw status
sudo ufw status numbered        # Con números (para eliminar)

# Activar/Desactivar
sudo ufw enable
sudo ufw disable

# Permitir puertos
sudo ufw allow 22/tcp           # SSH
sudo ufw allow 80/tcp           # HTTP
sudo ufw allow 443/tcp          # HTTPS
sudo ufw allow 8080/tcp         # Puerto personalizado

# Permitir rango
sudo ufw allow 3000:3010/tcp

# Permitir desde IP específica
sudo ufw allow from 192.168.1.100

# Denegar
sudo ufw deny 23/tcp

# Eliminar regla
sudo ufw status numbered
sudo ufw delete 3               # Número de la regla

# Resetear (elimina todas las reglas)
sudo ufw reset
```

### Configuración Típica Web

```bash
sudo ufw allow 22/tcp           # SSH
sudo ufw allow 80/tcp           # HTTP
sudo ufw allow 443/tcp          # HTTPS
sudo ufw allow 3000/tcp         # App (ejemplo)
sudo ufw enable
```

---

## Servicios (systemctl)

### Comandos Básicos

```bash
# Ver estado de servicio
systemctl status docker
systemctl status nginx

# Iniciar/Detener
sudo systemctl start docker
sudo systemctl stop docker
sudo systemctl restart docker
sudo systemctl reload docker    # Recargar config sin reiniciar

# Habilitar/Deshabilitar (inicio automático)
sudo systemctl enable docker    # Inicia con el sistema
sudo systemctl disable docker   # No inicia automáticamente

# Verificar si está habilitado
systemctl is-enabled docker

# Ver servicios corriendo
systemctl list-units --type=service --state=running

# Ver logs de servicio
journalctl -u docker
journalctl -u docker -f         # Seguir logs
journalctl -u docker -n 50      # Últimas 50 líneas
```

---

## Monitoreo de Recursos

### Ver Recursos del Sistema

```bash
# Uso de RAM
free -h

# Uso de disco
df -h
df -h /                         # Solo partición raíz

# Uso de CPU/RAM en tiempo real
top                             # Presiona q para salir
htop                            # Versión mejorada (instalar: sudo apt install htop)

# Ver procesos
ps aux                          # Todos los procesos
ps aux | grep docker            # Buscar proceso específico

# Ver puertos abiertos
ss -tulpn                       # Todos los puertos
ss -tulpn | grep LISTEN         # Solo escuchando
ss -tulpn | grep :80            # Puerto específico

# Ver tamaño de carpetas
du -sh carpeta/                 # Tamaño total
du -h --max-depth=1 /home       # Tamaño por subcarpeta
```

### Diagnóstico Rápido

```bash
# ¿Cuánta RAM disponible?
free -h | grep Mem

# ¿Cuánto espacio en disco?
df -h | grep "/$"

# ¿Qué procesos consumen más RAM?
ps aux --sort=-%mem | head

# ¿Qué procesos consumen más CPU?
ps aux --sort=-%cpu | head
```

---

## Permisos

### Comandos Básicos

```bash
# Ver permisos
ls -l archivo.txt

# Cambiar permisos (numérico)
chmod 755 archivo.txt           # rwxr-xr-x
chmod 644 archivo.txt           # rw-r--r--
chmod +x script.sh              # Hacer ejecutable

# Cambiar propietario
sudo chown usuario archivo.txt
sudo chown -R usuario carpeta/  # Recursivo

# Cambiar grupo
sudo chgrp grupo archivo.txt

# Cambiar propietario y grupo
sudo chown usuario:grupo archivo.txt
```

### Permisos Comunes

| Código | Permisos  | Uso típico           |
| ------ | --------- | -------------------- |
| 755    | rwxr-xr-x | Scripts, carpetas    |
| 644    | rw-r--r-- | Archivos config      |
| 600    | rw------- | Claves privadas SSH  |
| 777    | rwxrwxrwx | ⚠️ Evitar (inseguro) |

---

## Flujos de Trabajo Típicos

### Setup Inicial de Servidor

```bash
# 1. Conectar
ssh ubuntu@servidor-ip

# 2. Actualizar sistema
sudo apt update && sudo apt upgrade -y

# 3. Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# 4. Configurar firewall
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# 5. Verificar
docker --version
sudo ufw status
free -h
```

### Desplegar Aplicación

```bash
# 1. Transferir código (desde tu máquina)
rsync -avz ./proyecto/ ubuntu@servidor:/home/ubuntu/proyecto/

# 2. Conectar al servidor
ssh ubuntu@servidor

# 3. Ir al proyecto
cd ~/proyecto

# 4. Desplegar
docker compose up -d

# 5. Verificar
docker compose ps
docker compose logs -f
```

### Actualizar Aplicación

```bash
# 1. Transferir cambios (desde tu máquina)
rsync -avz ./proyecto/ ubuntu@servidor:/home/ubuntu/proyecto/

# 2. En el servidor
ssh ubuntu@servidor
cd ~/proyecto
docker compose pull
docker compose up -d --build
docker compose restart
```

### Troubleshooting Rápido

```bash
# 1. Ver logs
docker compose logs -f

# 2. Ver recursos
docker stats
htop

# 3. Ver puertos
ss -tulpn | grep LISTEN

# 4. Ver firewall
sudo ufw status

# 5. Reiniciar servicios
docker compose restart
sudo systemctl restart docker
```

---

## ⚡ Atajos de Teclado

### En Terminal

| Atajo      | Acción                       |
| ---------- | ---------------------------- |
| `Ctrl + C` | Cancelar comando actual      |
| `Ctrl + D` | Cerrar sesión / EOF          |
| `Ctrl + L` | Limpiar pantalla (= `clear`) |
| `Ctrl + R` | Buscar en historial          |
| `Ctrl + A` | Ir al inicio de línea        |
| `Ctrl + E` | Ir al final de línea         |
| `Ctrl + U` | Borrar hasta inicio          |
| `Ctrl + K` | Borrar hasta final           |
| `↑ ↓`      | Navegar historial            |
| `Tab`      | Autocompletar                |

---

## 🔥 Comandos Peligrosos (Usar con Precaución)

```bash
# ⚠️ Elimina TODO sin confirmación
sudo rm -rf /

# ⚠️ Elimina carpeta completa
rm -rf carpeta/

# ⚠️ Cambia permisos de TODO (inseguro)
chmod -R 777 /

# ⚠️ Elimina volúmenes de Docker (BORRA DATOS)
docker compose down -v
```

**Regla de oro:** Si ves `rm -rf` o `chmod 777`, verifica DOS VECES antes de ejecutar.

---

## 📊 Tabla de Comparación: APT vs YUM

| Acción             | Ubuntu (APT)               | Rocky Linux (YUM/DNF)      |
| ------------------ | -------------------------- | -------------------------- |
| Actualizar lista   | `sudo apt update`          | `sudo dnf check-update`    |
| Actualizar sistema | `sudo apt upgrade`         | `sudo dnf upgrade`         |
| Instalar           | `sudo apt install paquete` | `sudo dnf install paquete` |
| Buscar             | `apt search paquete`       | `dnf search paquete`       |
| Eliminar           | `sudo apt remove paquete`  | `sudo dnf remove paquete`  |
| Limpiar            | `sudo apt autoremove`      | `sudo dnf autoremove`      |

---

## 🎯 Tips Finales

1. **Usa `Tab`** para autocompletar (ahorra tiempo)
2. **Usa `↑`** para repetir comandos anteriores
3. **Usa `Ctrl+R`** para buscar en historial
4. **Verifica con `pwd`** antes de usar `rm -rf`
5. **Lee mensajes de error** (primera línea suele indicar el problema)
6. **Google el error** (copia-pega mensaje, busca en inglés)
7. **Documenta comandos** que usas (en archivo .txt)

---

> **Recuerda**: No necesitas memorizar todo. Ten este cheatsheet abierto y consúltalo cuando lo necesites. Con la práctica, los comandos más comunes se quedarán en tu memoria. 🚀
