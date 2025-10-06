# Linux Server para Implantación de Software

> **Objetivo**: Comprender las características fundamentales de Linux Server y preparar la plataforma tecnológica para despliegue de aplicaciones en entornos de producción.

## 📋 Tabla de Contenidos

1. [¿Por qué Linux Server?](#por-qué-linux-server)
2. [Distribuciones para Servidores](#distribuciones-para-servidores)
3. [Requisitos Mínimos de Hardware](#requisitos-mínimos-de-hardware)
4. [SSH: Acceso Remoto Seguro](#ssh-acceso-remoto-seguro)
5. [Usuarios y Permisos](#usuarios-y-permisos)
6. [Comandos Esenciales](#comandos-esenciales)
7. [Firewall Básico (UFW)](#firewall-básico-ufw)
8. [Gestión de Servicios](#gestión-de-servicios)
9. [Autoevaluación](#autoevaluación)

---

## ¿Por qué Linux Server?

### Comparación: Linux Server vs Desktop vs Windows Server

| Característica | Linux Server | Linux Desktop | Windows Server |
|----------------|--------------|---------------|----------------|
| **Interfaz gráfica** | No (solo terminal) | Sí | Sí (opcional) |
| **Consumo de recursos** | Muy bajo | Medio | Alto |
| **Costo** | Gratuito | Gratuito | Licencia costosa |
| **Estabilidad** | Excelente (uptime meses) | Buena | Buena |
| **Seguridad** | Muy alta | Alta | Media-Alta |
| **Actualizaciones** | Sin reinicio (mayoría) | Requiere reinicio | Requiere reinicio |
| **Ideal para** | Servidores web, BD, APIs | Desarrollo local | Apps empresariales |

### ¿Cuándo usar Linux Server?

✅ **Úsalo cuando:**
- Necesites desplegar aplicaciones web
- Trabajes con contenedores (Docker)
- Requieras alta disponibilidad
- Busques minimizar costos de licenciamiento
- Necesites control total del sistema

❌ **No lo uses cuando:**
- La aplicación es exclusiva de Windows (ej: .NET Framework antiguo)
- El equipo no tiene experiencia con terminal Linux
- Requieres software específico de Windows (ej: Active Directory)

### Ventajas para Implantación de Software

1. **Estabilidad**: Servidores Linux pueden funcionar meses sin reiniciar
2. **Seguridad**: Menos vulnerable a virus y malware
3. **Rendimiento**: Consume menos recursos (más espacio para aplicaciones)
4. **Automatización**: Todo es scriptable desde terminal
5. **Costo**: Sin licencias (ahorro significativo en producción)
6. **Comunidad**: Documentación extensa y soporte gratuito

---

## Distribuciones para Servidores

### Ubuntu Server 22.04 LTS (Recomendado para este bootcamp)

**¿Qué es?** La versión sin interfaz gráfica de Ubuntu, optimizada para servidores.

**¿Por qué?**
- ✅ LTS (Long Term Support): 5 años de actualizaciones
- ✅ Documentación extensa en español
- ✅ Gestor de paquetes APT (amigable)
- ✅ Compatible con Docker, PostgreSQL, Nginx
- ✅ Gran comunidad y tutoriales

**¿Para qué?** Despliegue de aplicaciones web, APIs, bases de datos.

**Requisitos mínimos:**
- CPU: 1 core
- RAM: 512 MB (mínimo), 2 GB (recomendado)
- Disco: 10 GB (mínimo), 20 GB (recomendado)

### Rocky Linux 9 (Alternativa empresarial)

**¿Qué es?** Reemplazo de CentOS, basado en Red Hat Enterprise Linux (RHEL).

**¿Por qué?**
- ✅ Muy estable (usado en grandes empresas)
- ✅ Soporte a largo plazo
- ✅ Compatible binariamente con RHEL
- ✅ Gestor de paquetes DNF/YUM

**¿Para qué?** Entornos empresariales que requieren compatibilidad RHEL.

**Nota:** En este bootcamp usaremos **Ubuntu Server** por su facilidad de uso.

### Comparación de Gestores de Paquetes

| Acción | Ubuntu Server (APT) | Rocky Linux (DNF/YUM) |
|--------|---------------------|------------------------|
| Actualizar lista | `sudo apt update` | `sudo dnf check-update` |
| Actualizar sistema | `sudo apt upgrade` | `sudo dnf upgrade` |
| Instalar paquete | `sudo apt install docker` | `sudo dnf install docker` |
| Buscar paquete | `apt search nginx` | `dnf search nginx` |
| Eliminar paquete | `sudo apt remove docker` | `sudo dnf remove docker` |

---

## Requisitos Mínimos de Hardware

### Para Desarrollo/Pruebas

```yaml
# ¿Qué? - Especificaciones mínimas para entorno de pruebas
# ¿Para qué? - Verificar que el servidor pueda ejecutar el stack básico

CPU: 1 core
RAM: 2 GB
Disco: 20 GB
Red: 1 Mbps

# ¿Cómo? - Stack que soporta:
- Ubuntu Server 22.04
- Docker + Docker Compose
- PostgreSQL (contenedor)
- Nginx (contenedor)
- Aplicación web pequeña
```

### Para Producción (Baja Escala)

```yaml
# ¿Qué? - Especificaciones recomendadas para producción pequeña
# ¿Para qué? - Garantizar rendimiento aceptable con usuarios reales

CPU: 2 cores
RAM: 4 GB
Disco: 40 GB SSD
Red: 10 Mbps
Backup: Mínimo semanal

# ¿Cómo? - Stack que soporta:
- Hasta 100 usuarios concurrentes
- Base de datos con ~10GB
- Logs y backups
```

### Para Producción (Media-Alta Escala)

```yaml
# ¿Qué? - Especificaciones para aplicaciones con mayor demanda
# ¿Para qué? - Soportar carga media-alta sin degradación

CPU: 4+ cores
RAM: 8+ GB
Disco: 100+ GB SSD
Red: 100 Mbps
Backup: Diario automático
Monitoreo: 24/7

# ¿Cómo? - Stack que soporta:
- 500+ usuarios concurrentes
- Base de datos con 50GB+
- Múltiples servicios (frontend, backend, BD)
```

### Verificar Hardware del Servidor

```bash
# ¿Qué? - Comandos para verificar recursos del servidor
# ¿Para qué? - Validar que cumple requisitos mínimos

# CPU (cantidad de cores)
nproc

# RAM total
free -h

# Espacio en disco
df -h

# Información completa del sistema
lscpu
cat /proc/meminfo
```

---

## SSH: Acceso Remoto Seguro

### ¿Qué es SSH?

**SSH (Secure Shell)** es un protocolo que permite acceder de forma segura a un servidor remoto a través de una terminal. Es la forma estándar de administrar servidores Linux.

### ¿Por qué usar SSH?

- ✅ **Seguro**: Todo el tráfico está cifrado
- ✅ **Eficiente**: No requiere interfaz gráfica (menos recursos)
- ✅ **Remoto**: Administra el servidor desde cualquier lugar
- ✅ **Scriptable**: Automatiza tareas con comandos

### Anatomía de una Conexión SSH

```bash
# ¿Qué? - Comando para conectarse a un servidor remoto
# ¿Para qué? - Acceder a la terminal del servidor desde tu máquina local
# ¿Cómo? - SSH establece conexión cifrada en el puerto 22

ssh usuario@direccion-ip

# Ejemplo real:
ssh ubuntu@34.123.45.67

# Con puerto personalizado:
ssh -p 2222 usuario@servidor.com
```

**Componentes:**
- `ssh`: El comando
- `usuario`: Cuenta en el servidor remoto
- `@`: Separador
- `direccion-ip`: IP pública del servidor (o dominio)

### Autenticación por Contraseña vs Clave SSH

| Método | Seguridad | Facilidad | Recomendado |
|--------|-----------|-----------|-------------|
| **Contraseña** | Media | Alta | Solo para inicio |
| **Clave SSH** | Muy alta | Media | Producción ✅ |

### Generar y Usar Claves SSH

```bash
# ¿Qué? - Generar par de claves SSH (privada + pública)
# ¿Para qué? - Autenticación segura sin contraseñas
# ¿Cómo? - Genera archivo ~/.ssh/id_rsa (privada) y ~/.ssh/id_rsa.pub (pública)

# Paso 1: Generar par de claves en tu máquina LOCAL
ssh-keygen -t rsa -b 4096 -C "tu-email@ejemplo.com"

# Presiona Enter 3 veces (usa valores por defecto)
# Resultado: Se crean 2 archivos en ~/.ssh/
#   - id_rsa (clave PRIVADA - nunca compartir)
#   - id_rsa.pub (clave PÚBLICA - copiar al servidor)

# Paso 2: Copiar clave pública al servidor
ssh-copy-id usuario@servidor-ip

# Ejemplo:
ssh-copy-id ubuntu@34.123.45.67

# Paso 3: Conectar (ya no pedirá contraseña)
ssh ubuntu@34.123.45.67
```

### Comandos SSH Útiles

```bash
# ¿Qué? - Transferir archivo local al servidor
# ¿Para qué? - Subir código, configuraciones, datos
scp archivo.txt usuario@servidor:/ruta/destino/

# ¿Qué? - Descargar archivo del servidor
# ¿Para qué? - Bajar logs, backups, archivos generados
scp usuario@servidor:/ruta/archivo.txt ./

# ¿Qué? - Transferir carpeta completa (recursivo)
# ¿Para qué? - Subir proyecto completo
scp -r carpeta/ usuario@servidor:/home/ubuntu/

# ¿Qué? - Sincronizar carpetas (más eficiente que scp)
# ¿Para qué? - Solo transfiere archivos modificados
rsync -avz carpeta/ usuario@servidor:/home/ubuntu/carpeta/
```

---

## Usuarios y Permisos

### Tipos de Usuarios

1. **root**: Usuario administrador (poder total)
   - ⚠️ Peligroso usar directamente
   - ✅ Mejor: Usar `sudo` con usuario normal

2. **Usuario normal**: Usuario con permisos limitados
   - ✅ Seguro para operación diaria
   - ✅ Puede usar `sudo` para tareas administrativas

### Sistema de Permisos en Linux

Cada archivo/carpeta tiene 3 tipos de permisos para 3 grupos:

```bash
# ¿Qué? - Ver permisos de archivos
ls -l

# Resultado ejemplo:
# -rw-r--r-- 1 ubuntu ubuntu 1024 Oct 06 10:30 archivo.txt
# drwxr-xr-x 2 ubuntu ubuntu 4096 Oct 06 10:31 carpeta/

# Estructura: -rwxrwxrwx
#              │││││││││└─ Otros (other): pueden leer
#              ││││││││└── Otros: pueden escribir
#              │││││││└─── Otros: pueden ejecutar
#              ││││││└──── Grupo: pueden leer
#              │||||└───── Grupo: pueden escribir
#              ││││└────── Grupo: pueden ejecutar
#              │││└─────── Usuario: puede leer
#              ││└──────── Usuario: puede escribir
#              │└───────── Usuario: puede ejecutar
#              └────────── Tipo: - (archivo) o d (directorio)
```

**Permisos:**
- `r` (read): Leer el archivo
- `w` (write): Modificar el archivo
- `x` (execute): Ejecutar el archivo (si es script/programa)

### Cambiar Permisos

```bash
# ¿Qué? - Cambiar permisos con chmod
# ¿Para qué? - Controlar quién puede leer/escribir/ejecutar

# Hacer archivo ejecutable
chmod +x script.sh

# Dar permisos de lectura/escritura al usuario
chmod u+rw archivo.txt

# Quitar permisos de escritura a grupo y otros
chmod go-w archivo.txt

# Método numérico (más común):
# 7 = rwx (4+2+1)
# 6 = rw- (4+2)
# 5 = r-x (4+1)
# 4 = r-- (4)

# Ejemplo: rwxr-xr-x = 755
chmod 755 script.sh

# Ejemplo: rw-r--r-- = 644
chmod 644 archivo.txt
```

### Uso de sudo

```bash
# ¿Qué? - Ejecutar comando con privilegios de administrador
# ¿Para qué? - Realizar tareas que requieren permisos root

# Instalar software (requiere sudo)
sudo apt install docker

# Editar archivo del sistema (requiere sudo)
sudo nano /etc/hosts

# Ver logs del sistema (requiere sudo)
sudo tail -f /var/log/syslog

# Convertirse temporalmente en root (usar con precaución)
sudo su
```

### Crear Usuario No-Root

```bash
# ¿Qué? - Crear nuevo usuario en el servidor
# ¿Para qué? - No usar root directamente (seguridad)

# Paso 1: Crear usuario
sudo adduser deploy

# Paso 2: Agregar usuario al grupo sudo (puede usar sudo)
sudo usermod -aG sudo deploy

# Paso 3: Verificar grupos del usuario
groups deploy

# Paso 4: Cambiar a ese usuario
su - deploy
```

---

## Comandos Esenciales

### Navegación y Archivos

```bash
# ¿Qué? - Mostrar directorio actual
# ¿Para qué? - Saber dónde estás ubicado
pwd

# ¿Qué? - Listar archivos y carpetas
# ¿Para qué? - Ver contenido del directorio
ls        # Listado simple
ls -l     # Listado detallado (permisos, tamaño, fecha)
ls -lh    # Listado con tamaños legibles (KB, MB, GB)
ls -la    # Incluir archivos ocultos

# ¿Qué? - Cambiar de directorio
# ¿Para qué? - Navegar por el sistema de archivos
cd /home/ubuntu/proyecto    # Ir a ruta absoluta
cd ..                       # Subir un nivel
cd ~                        # Ir al home del usuario
cd -                        # Volver al directorio anterior

# ¿Qué? - Crear carpeta
# ¿Para qué? - Organizar archivos
mkdir proyecto
mkdir -p proyecto/src/components  # Crear estructura completa

# ¿Qué? - Crear archivo vacío
# ¿Para qué? - Inicializar archivo
touch archivo.txt

# ¿Qué? - Copiar archivos/carpetas
# ¿Para qué? - Duplicar contenido
cp origen.txt destino.txt
cp -r carpeta/ copia-carpeta/  # Copiar carpeta (recursivo)

# ¿Qué? - Mover/renombrar archivos
# ¿Para qué? - Reorganizar o cambiar nombres
mv viejo.txt nuevo.txt           # Renombrar
mv archivo.txt /otra/carpeta/    # Mover

# ¿Qué? - Eliminar archivos/carpetas
# ¿Para qué? - Liberar espacio, limpiar
rm archivo.txt
rm -r carpeta/        # Eliminar carpeta (recursivo)
rm -rf carpeta/       # Forzar eliminación (¡cuidado!)
```

### Visualización de Contenido

```bash
# ¿Qué? - Ver contenido completo de archivo
# ¿Para qué? - Leer archivos pequeños
cat archivo.txt

# ¿Qué? - Ver contenido con paginación
# ¿Para qué? - Leer archivos grandes
less archivo.log
# Controles: Espacio (página), q (salir), / (buscar)

# ¿Qué? - Ver primeras 10 líneas
# ¿Para qué? - Vista rápida del inicio
head archivo.txt
head -n 20 archivo.txt  # Primeras 20 líneas

# ¿Qué? - Ver últimas 10 líneas
# ¿Para qué? - Ver logs recientes
tail archivo.log
tail -n 50 archivo.log       # Últimas 50 líneas
tail -f archivo.log          # Seguir archivo en tiempo real (logs)
```

### Búsqueda

```bash
# ¿Qué? - Buscar archivos por nombre
# ¿Para qué? - Encontrar archivos en el sistema
find /home/ubuntu -name "*.txt"
find . -name "docker-compose.yml"

# ¿Qué? - Buscar texto dentro de archivos
# ¿Para qué? - Encontrar contenido específico
grep "error" archivo.log
grep -r "TODO" .              # Buscar recursivamente
grep -i "error" archivo.log   # Ignorar mayúsculas/minúsculas
```

### Información del Sistema

```bash
# ¿Qué? - Ver uso de disco
# ¿Para qué? - Verificar espacio disponible
df -h

# ¿Qué? - Ver uso de RAM
# ¿Para qué? - Monitorear memoria
free -h

# ¿Qué? - Ver procesos en ejecución
# ¿Para qué? - Monitorear aplicaciones activas
top           # Interactivo (presiona q para salir)
htop          # Versión mejorada (requiere instalación)
ps aux        # Listado completo

# ¿Qué? - Ver uso de CPU y RAM en tiempo real
# ¿Para qué? - Diagnóstico de rendimiento
htop

# ¿Qué? - Ver información de red
# ¿Para qué? - Verificar IP, puertos abiertos
ip addr       # Ver IPs del servidor
ss -tulpn     # Ver puertos abiertos (reemplaza netstat)
```

### Gestión de Paquetes (Ubuntu)

```bash
# ¿Qué? - Actualizar lista de paquetes disponibles
# ¿Para qué? - Obtener última información de repositorios
# ¿Cómo? - No instala nada, solo actualiza el índice
sudo apt update

# ¿Qué? - Actualizar paquetes instalados
# ¿Para qué? - Aplicar actualizaciones de seguridad y mejoras
sudo apt upgrade

# ¿Qué? - Instalar paquete
# ¿Para qué? - Agregar nuevo software
sudo apt install curl
sudo apt install -y docker.io  # -y = responder "yes" automáticamente

# ¿Qué? - Buscar paquete
# ¿Para qué? - Ver si está disponible en repositorios
apt search nginx

# ¿Qué? - Ver información de paquete
# ¿Para qué? - Conocer versión, dependencias
apt show docker.io

# ¿Qué? - Eliminar paquete
# ¿Para qué? - Desinstalar software
sudo apt remove paquete
sudo apt purge paquete        # Elimina también configuración
```

---

## Firewall Básico (UFW)

### ¿Qué es UFW?

**UFW (Uncomplicated Firewall)** es una interfaz simplificada para gestionar el firewall de Linux (iptables). Controla qué tráfico de red puede entrar o salir del servidor.

### ¿Por qué es importante?

- ✅ **Seguridad**: Solo permite tráfico autorizado
- ✅ **Protección**: Bloquea accesos no deseados
- ✅ **Control**: Define qué puertos están abiertos

### Comandos Esenciales de UFW

```bash
# ¿Qué? - Verificar estado del firewall
# ¿Para qué? - Saber si está activo y qué reglas tiene
sudo ufw status

# ¿Qué? - Ver reglas numeradas
# ¿Para qué? - Facilitar eliminación de reglas específicas
sudo ufw status numbered

# ¿Qué? - Activar firewall
# ¿Para qué? - Iniciar protección
sudo ufw enable

# ⚠️ IMPORTANTE: Antes de activar, permite SSH o perderás acceso
sudo ufw allow 22/tcp
sudo ufw enable

# ¿Qué? - Desactivar firewall
# ¿Para qué? - Solo para troubleshooting (no en producción)
sudo ufw disable
```

### Configuración Típica para Implantación Web

```bash
# ¿Qué? - Permitir SSH (puerto 22)
# ¿Para qué? - Mantener acceso remoto al servidor
# ¿Cómo? - Acepta conexiones TCP en puerto 22
sudo ufw allow 22/tcp

# ¿Qué? - Permitir HTTP (puerto 80)
# ¿Para qué? - Acceso web sin cifrado
sudo ufw allow 80/tcp

# ¿Qué? - Permitir HTTPS (puerto 443)
# ¿Para qué? - Acceso web cifrado (recomendado)
sudo ufw allow 443/tcp

# ¿Qué? - Permitir puerto personalizado (ej: 8080)
# ¿Para qué? - Aplicación corriendo en puerto específico
sudo ufw allow 8080/tcp

# ¿Qué? - Activar firewall
sudo ufw enable

# ¿Qué? - Verificar reglas
sudo ufw status
```

**Resultado esperado:**
```
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
8080/tcp                   ALLOW       Anywhere
```

### Gestión de Reglas

```bash
# ¿Qué? - Eliminar regla por número
# ¿Para qué? - Quitar permisos de puerto
sudo ufw status numbered  # Ver números
sudo ufw delete 3         # Eliminar regla #3

# ¿Qué? - Eliminar regla por especificación
sudo ufw delete allow 8080/tcp

# ¿Qué? - Permitir rango de puertos
# ¿Para qué? - Abrir múltiples puertos consecutivos
sudo ufw allow 3000:3010/tcp

# ¿Qué? - Permitir desde IP específica
# ¿Para qué? - Restringir acceso a IPs conocidas
sudo ufw allow from 192.168.1.100

# ¿Qué? - Denegar tráfico
# ¿Para qué? - Bloquear puerto o IP específica
sudo ufw deny 23/tcp      # Bloquear Telnet (inseguro)
```

### Reglas por Aplicación

```bash
# ¿Qué? - Ver aplicaciones disponibles
# ¿Para qué? - Usar perfiles predefinidos
sudo ufw app list

# ¿Qué? - Permitir aplicación (ej: Nginx)
# ¿Para qué? - Abrir puertos de forma simplificada
sudo ufw allow 'Nginx Full'  # Abre 80 y 443
sudo ufw allow 'OpenSSH'     # Abre 22
```

### Reset del Firewall

```bash
# ¿Qué? - Resetear firewall a estado inicial
# ¿Para qué? - Empezar de cero con configuración
# ⚠️ Cuidado: Perderás todas las reglas
sudo ufw reset
```

---

## Gestión de Servicios

### ¿Qué es systemd?

**systemd** es el sistema de inicio y gestión de servicios en Linux moderno. Controla qué aplicaciones arrancan automáticamente y permite iniciar/detener/reiniciar servicios.

### Comando systemctl

```bash
# ¿Qué? - Ver estado de un servicio
# ¿Para qué? - Saber si está corriendo, detenido, o con error
systemctl status docker
systemctl status nginx

# ¿Qué? - Iniciar servicio
# ¿Para qué? - Arrancar servicio detenido
sudo systemctl start docker

# ¿Qué? - Detener servicio
# ¿Para qué? - Apagar servicio en ejecución
sudo systemctl stop nginx

# ¿Qué? - Reiniciar servicio
# ¿Para qué? - Aplicar cambios de configuración
sudo systemctl restart docker

# ¿Qué? - Recargar configuración sin reiniciar
# ¿Para qué? - Cambios menores sin downtime
sudo systemctl reload nginx

# ¿Qué? - Habilitar servicio al inicio
# ¿Para qué? - Que arranque automáticamente al bootear servidor
sudo systemctl enable docker

# ¿Qué? - Deshabilitar servicio al inicio
# ¿Para qué? - Que NO arranque automáticamente
sudo systemctl disable servicio

# ¿Qué? - Ver servicios activos
# ¿Para qué? - Diagnóstico general del sistema
systemctl list-units --type=service --state=running
```

### Ejemplo: Gestionar Docker

```bash
# ¿Qué? - Verificar si Docker está corriendo
systemctl status docker

# Si no está corriendo:
# ¿Qué? - Iniciar Docker
sudo systemctl start docker

# ¿Qué? - Habilitar Docker para que inicie con el sistema
sudo systemctl enable docker

# ¿Qué? - Verificar que inicia correctamente
systemctl is-enabled docker
# Respuesta esperada: enabled
```

### Ver Logs de Servicios

```bash
# ¿Qué? - Ver logs de un servicio
# ¿Para qué? - Diagnosticar errores
journalctl -u docker

# ¿Qué? - Ver logs en tiempo real
# ¿Para qué? - Monitorear actividad del servicio
journalctl -u docker -f

# ¿Qué? - Ver últimas 50 líneas
journalctl -u docker -n 50

# ¿Qué? - Ver logs desde hoy
journalctl -u docker --since today
```

---

## Resumen: Flujo Típico de Implantación

### 1. Acceso Inicial

```bash
# Conectar al servidor
ssh ubuntu@servidor-ip

# Verificar recursos
free -h
df -h
```

### 2. Actualización del Sistema

```bash
# Actualizar lista de paquetes
sudo apt update

# Actualizar paquetes instalados
sudo apt upgrade -y
```

### 3. Configuración de Firewall

```bash
# Permitir puertos necesarios
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Activar firewall
sudo ufw enable

# Verificar
sudo ufw status
```

### 4. Instalación de Docker

```bash
# Instalar Docker (script oficial)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Agregar usuario al grupo docker (evita usar sudo)
sudo usermod -aG docker $USER

# Habilitar Docker al inicio
sudo systemctl enable docker

# Verificar instalación
docker --version
docker compose version
```

### 5. Transferir Proyecto

```bash
# Desde tu máquina LOCAL:
scp -r mi-proyecto/ ubuntu@servidor:/home/ubuntu/
```

### 6. Desplegar Aplicación

```bash
# En el servidor:
cd ~/mi-proyecto
docker compose up -d

# Verificar
docker compose ps
```

### 7. Verificación

```bash
# Ver logs
docker compose logs -f

# Verificar puertos abiertos
ss -tulpn | grep LISTEN

# Acceder desde navegador:
# http://servidor-ip:puerto
```

---

## Cheatsheet Rápido

### Top 15 Comandos para Implantación

```bash
# Navegación
pwd                          # Ubicación actual
ls -la                       # Listar archivos (incluye ocultos)
cd /ruta/carpeta             # Cambiar directorio

# Archivos
cat archivo.txt              # Ver contenido
tail -f archivo.log          # Seguir logs en tiempo real
nano archivo.txt             # Editar archivo

# Sistema
free -h                      # Ver RAM disponible
df -h                        # Ver espacio en disco
htop                         # Monitor de recursos (interactivo)

# Paquetes
sudo apt update              # Actualizar lista de paquetes
sudo apt install paquete     # Instalar software

# Firewall
sudo ufw status              # Ver reglas del firewall
sudo ufw allow 80/tcp        # Abrir puerto

# Servicios
systemctl status docker      # Ver estado de servicio
sudo systemctl restart docker # Reiniciar servicio
```

---

## Autoevaluación

### Pregunta 1: ¿Por qué Linux Server?

**¿Cuáles son las 3 principales ventajas de usar Linux Server para implantar aplicaciones web?**

<details>
<summary>Ver respuesta</summary>

1. **Costo**: Sin licencias (gratuito), ahorro significativo en producción
2. **Estabilidad**: Puede funcionar meses sin reiniciar, alta disponibilidad
3. **Rendimiento**: Consume menos recursos (sin interfaz gráfica), más RAM/CPU para aplicaciones

</details>

### Pregunta 2: SSH y Seguridad

**¿Qué comando usarías para conectarte a un servidor con IP 35.123.45.67 usando el usuario `deploy` y qué es mejor: autenticación por contraseña o clave SSH en producción?**

<details>
<summary>Ver respuesta</summary>

**Comando:**
```bash
ssh deploy@35.123.45.67
```

**Mejor método**: Clave SSH
- Más seguro (no se puede adivinar como una contraseña)
- Sin riesgo de ataques de fuerza bruta
- Permite automatización

</details>

### Pregunta 3: Firewall

**Tu aplicación web corre en el puerto 3000 y necesitas acceso SSH. ¿Qué comandos de UFW ejecutarías?**

<details>
<summary>Ver respuesta</summary>

```bash
# Permitir SSH (puerto 22)
sudo ufw allow 22/tcp

# Permitir aplicación (puerto 3000)
sudo ufw allow 3000/tcp

# Activar firewall
sudo ufw enable

# Verificar
sudo ufw status
```

**Importante**: Siempre permite SSH ANTES de activar UFW, o perderás acceso al servidor.

</details>

---

## Recursos Adicionales

### Documentación Oficial

- [Ubuntu Server Guide](https://ubuntu.com/server/docs)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)
- [SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)

### Práctica

- **Próximo paso**: Práctica 1 - Crear VM en Google Cloud
- **Recursos**: Revisa `3-recursos/cheatsheet-linux-server.md` para referencia rápida
- **Troubleshooting**: Consulta `3-recursos/troubleshooting-linux.md` ante problemas

---

> **Nota**: Este contenido está enfocado en lo **justo y necesario** para implantar software. No es un curso completo de administración de sistemas Linux, sino las habilidades prácticas para desplegar aplicaciones en producción.

