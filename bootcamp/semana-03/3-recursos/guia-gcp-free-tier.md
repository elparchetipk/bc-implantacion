# Guía: Crear VM Gratuita en Google Cloud Platform

> **Objetivo**: Crear y configurar una máquina virtual Ubuntu Server en Google Cloud usando el Free Tier (sin costo inicial).

## 📋 Tabla de Contenidos

1. [Antes de Empezar](#antes-de-empezar)
2. [Crear Cuenta GCP](#crear-cuenta-gcp)
3. [Crear Máquina Virtual](#crear-máquina-virtual)
4. [Configurar Acceso SSH](#configurar-acceso-ssh)
5. [Configurar Firewall](#configurar-firewall)
6. [Verificación](#verificación)
7. [Gestión de Costos](#gestión-de-costos)

**⏱️ Tiempo estimado**: 15 minutos

---

## Antes de Empezar

### ¿Qué Necesitas?

- [ ] Cuenta de Google (Gmail)
- [ ] Tarjeta de crédito o débito (para verificación)
- [ ] 15 minutos de tiempo

### ¿Por Qué GCP?

**Ventajas:**

- ✅ **$300 USD en créditos** (válidos 90 días)
- ✅ **Always Free tier** (no expira)
- ✅ **f1-micro** incluida en Free tier
- ✅ **Fácil de usar** (interfaz intuitiva)
- ✅ **Buen rendimiento** para aprendizaje

**Always Free incluye:**

- 1 VM f1-micro (EE.UU. - regiones específicas)
- 30 GB almacenamiento HDD
- 1 GB tráfico de red saliente/mes
- 5 GB Cloud Storage

### ⚠️ Importante Sobre Costos

**No se cobra SI:**

- ✅ Usas f1-micro en regiones permitidas (us-west1, us-central1, us-east1)
- ✅ No excedes 30 GB de disco
- ✅ Apagas VM cuando no la uses

**Se cobra SI:**

- ❌ Usas e2-micro u otros tipos (no Free)
- ❌ Usas regiones fuera de EE.UU.
- ❌ Dejas VM corriendo 24/7 sin necesidad

---

## Crear Cuenta GCP

### Paso 1: Registrarse

1. Ve a: [https://cloud.google.com/free](https://cloud.google.com/free)
2. Click en **"Comenzar gratis"** o **"Get started for free"**
3. Inicia sesión con tu cuenta de Google

### Paso 2: Completar Formulario

**Información solicitada:**

- **País**: Colombia
- **Tipo de cuenta**: Individual
- **Términos**: Lee y acepta

### Paso 3: Verificar Identidad

**Información de tarjeta:**

- Nombre del titular
- Número de tarjeta
- Fecha de vencimiento
- CVV

**⚠️ Importante:**

- Solo es para **verificación de identidad**
- No se realizará ningún cargo sin tu autorización
- Puedes cancelar después del período de prueba

### Paso 4: Confirmar

1. Revisa la información
2. Click en **"Start my free trial"**
3. Espera confirmación (30 segundos)

**✅ Resultado:** Deberías ver el panel de GCP con tus $300 en créditos.

---

## Crear Máquina Virtual

### Paso 1: Ir a Compute Engine

1. En el menú (☰), ve a: **Compute Engine** → **VM instances**
2. Si es la primera vez, espera que se active la API (1-2 minutos)
3. Click en **"CREATE INSTANCE"** o **"CREAR INSTANCIA"**

### Paso 2: Configuración Básica

**Name (Nombre):**

```
ubuntu-bootcamp
```

**Region (Región):**

```
us-central1 (Iowa)
```

**⚠️ IMPORTANTE: Debe ser una región de EE.UU. para Free Tier**

Regiones Always Free:

- `us-west1` (Oregon)
- `us-central1` (Iowa)
- `us-east1` (South Carolina)

**Zone (Zona):**

```
us-central1-a
```

(O cualquier zona con sufijo `-a`)

### Paso 3: Machine Configuration

**Series:**

```
E2
```

**Machine type:**

Para **FREE TIER** (100% gratis):

```
f1-micro
- 1 vCPU (compartida)
- 614 MB RAM
- Costo: $0.00/mes
```

Para **mejor rendimiento** (~$7/mes):

```
e2-micro
- 2 vCPU
- 1 GB RAM
- Costo: ~$6-7/mes
```

**💡 Recomendación para bootcamp:** Usa **e2-micro** (mejor experiencia, bajo costo)

### Paso 4: Boot Disk (Disco de Arranque)

Click en **"CHANGE"** (Cambiar):

**Operating system:**

```
Ubuntu
```

**Version:**

```
Ubuntu 22.04 LTS x86/64
```

**⚠️ IMPORTANTE: Selecciona 22.04 LTS, no otras versiones**

**Boot disk type:**

```
Balanced persistent disk
```

**Size (GB):**

```
20 GB
```

(Mínimo: 10 GB, Recomendado: 20 GB)

Click en **"SELECT"** (Seleccionar)

### Paso 5: Firewall

**Marcar AMBAS casillas:**

- ☑ **Allow HTTP traffic** (puerto 80)
- ☑ **Allow HTTPS traffic** (puerto 443)

### Paso 6: Expandir Opciones Avanzadas (Opcional)

Click en **"Advanced options"** → **"Networking"**

**External IPv4 address:**

```
Ephemeral
```

(O puedes reservar una IP estática - cuesta $)

### Paso 7: Revisar Costo Estimado

**En el panel derecho verás:**

- f1-micro: **$0.00/month** (Free Tier)
- e2-micro: **~$6.50/month** (sin Free Tier)

### Paso 8: Crear

1. Revisa toda la configuración
2. Click en **"CREATE"** (abajo de la página)
3. Espera 30-60 segundos

**✅ Resultado:** VM con estado **Running** y IP externa asignada

---

## Configurar Acceso SSH

### Opción A: SSH desde Navegador (Más Fácil)

1. En la lista de VMs, encuentra tu instancia
2. Click en **"SSH"** (botón en la fila)
3. Se abre ventana nueva con terminal

**✅ Ventajas:**

- No requiere configuración
- Funciona desde cualquier lugar

**❌ Desventajas:**

- No puedes transferir archivos fácilmente
- Depende del navegador

### Opción B: SSH desde Terminal Local (Recomendado)

#### Paso 1: Obtener IP Externa

En la lista de VMs, copia la **External IP**

Ejemplo: `34.123.45.67`

#### Paso 2: Obtener tu Username

**Método 1: Desde GCP Console**

1. Click en **"SSH"** (se abre ventana)
2. El username aparece en el prompt:
   ```
   tu_usuario@ubuntu-bootcamp:~$
   ```

**Método 2: Calcular**

- Si tu email es `juan.perez@gmail.com`
- Tu username es: `juan_perez` (reemplaza `.` por `_`)

#### Paso 3: Conectar desde Terminal

```bash
# Sintaxis
ssh USUARIO@IP_EXTERNA

# Ejemplo
ssh juan_perez@34.123.45.67

# Primera vez preguntará:
# Are you sure you want to continue connecting (yes/no)?
# Escribe: yes
```

#### Paso 4: Configurar SSH Keys (Opcional pero Recomendado)

**En tu máquina local:**

```bash
# 1. Generar clave SSH (si no tienes)
ssh-keygen -t rsa -b 4096 -C "tu-email@gmail.com"
# Presiona Enter 3 veces (usa defaults)

# 2. Ver tu clave pública
cat ~/.ssh/id_rsa.pub
# Copia el contenido completo
```

**En GCP Console:**

1. Ve a: **Compute Engine** → **Metadata** → **SSH Keys**
2. Click **"ADD SSH KEY"**
3. Pega tu clave pública completa
4. Click **"SAVE"**

**Ahora puedes conectar sin contraseña:**

```bash
ssh usuario@ip-externa
```

---

## Configurar Firewall

### Firewall de GCP (Reglas de Red)

Por defecto, GCP permite:

- ✅ Puerto 22 (SSH)
- ✅ Puerto 80 (HTTP) - si marcaste la casilla
- ✅ Puerto 443 (HTTPS) - si marcaste la casilla

### Agregar Puertos Personalizados

**Ejemplo: Permitir puerto 3000 (para aplicación)**

1. Ve a: **VPC Network** → **Firewall** → **CREATE FIREWALL RULE**

2. Configuración:

   ```
   Name: allow-app-port-3000
   Direction of traffic: Ingress
   Action on match: Allow
   Targets: All instances in the network
   Source IP ranges: 0.0.0.0/0
   Protocols and ports: tcp:3000
   ```

3. Click **"CREATE"**

**Puertos comunes a abrir:**

- `3000` - Frontend (React, Vue)
- `5000` - Backend (Flask, Express)
- `8080` - Adminer, Jenkins
- `5432` - PostgreSQL (solo si necesitas acceso externo)

### Desde gcloud CLI (Alternativa)

```bash
gcloud compute firewall-rules create allow-app-port-3000 \
    --allow tcp:3000 \
    --source-ranges 0.0.0.0/0 \
    --description "Allow app on port 3000"
```

---

## Verificación

### Checklist de Verificación

```bash
# 1. Conectar por SSH
ssh usuario@ip-externa

# 2. Verificar sistema operativo
cat /etc/os-release

# Debe mostrar:
# NAME="Ubuntu"
# VERSION="22.04.x LTS (Jammy Jellyfish)"

# 3. Verificar RAM
free -h

# Debe mostrar:
# f1-micro: ~600 MB
# e2-micro: ~1 GB

# 4. Verificar disco
df -h

# Debe mostrar ~20 GB total

# 5. Verificar conectividad
ping -c 3 google.com

# Debe funcionar (3 paquetes enviados/recibidos)

# 6. Actualizar sistema
sudo apt update

# Debe completarse sin errores
```

### Test de Rendimiento (Opcional)

```bash
# Ver información del CPU
lscpu

# Ver uso de recursos
htop
# (Instalar si no existe: sudo apt install htop)
```

---

## Gestión de Costos

### Monitorear Créditos

1. Ve a: **Billing** → **Overview**
2. Verás:
   - Créditos restantes ($300)
   - Días restantes (90)
   - Gasto actual

### Configurar Alarma de Presupuesto

1. Ve a: **Billing** → **Budgets & alerts**
2. Click **"CREATE BUDGET"**
3. Configuración:
   ```
   Name: Alerta de Gasto
   Budget amount: $10
   Threshold rules: 50%, 75%, 100%
   Email notifications: tu-email@gmail.com
   ```
4. Click **"FINISH"**

**Recibirás email cuando:**

- Gastes $5 (50%)
- Gastes $7.50 (75%)
- Gastes $10 (100%)

### Detener VM (Evitar Costos)

**Cuando termines de trabajar:**

```bash
# Opción 1: Desde GCP Console
# VM instances → ⋮ (junto a tu VM) → Stop

# Opción 2: Desde terminal
gcloud compute instances stop ubuntu-bootcamp --zone=us-central1-a

# Opción 3: Desde SSH (dentro de la VM)
sudo shutdown -h now
```

**Para volver a encenderla:**

```bash
# Desde GCP Console
# VM instances → ⋮ → Start

# O desde terminal
gcloud compute instances start ubuntu-bootcamp --zone=us-central1-a
```

**⚠️ Importante:**

- VM detenida: $0/hora (solo pagas disco: ~$0.04/día)
- VM corriendo: $0.00/hora (f1-micro) o $0.01/hora (e2-micro)

### Eliminar VM (Cuando Ya No la Necesites)

```bash
# Opción 1: Desde GCP Console
# VM instances → ☑ (marca tu VM) → DELETE

# Opción 2: Desde terminal
gcloud compute instances delete ubuntu-bootcamp --zone=us-central1-a
```

**⚠️ Esto eliminará:**

- La VM
- El disco (⚠️ PERDERÁS DATOS)
- La IP externa

### Mejores Prácticas de Costos

1. **Detén VM cuando no la uses**

   - Fin de clase: Stop
   - Fin de semana: Stop
   - Solo enciende cuando vayas a trabajar

2. **Usa f1-micro para pruebas**

   - 100% gratis
   - Suficiente para aprendizaje

3. **Elimina recursos no usados**

   - Discos huérfanos
   - IPs estáticas no asignadas
   - Snapshots viejos

4. **Monitorea semanalmente**
   - Revisa **Billing** → **Reports**
   - Verifica que gastos sean $0 o mínimos

---

## Solución de Problemas

### "No puedo crear VM - quota exceeded"

**Causa:** Límite de Free Trial alcanzado

**Solución:**

1. Ve a: **IAM & Admin** → **Quotas**
2. Busca: "CPUs"
3. Solicita aumento de cuota (gratis)

### "La IP externa cambia cada vez"

**Causa:** Usas IP efímera (por defecto)

**Solución: Reservar IP estática**

1. Ve a: **VPC Network** → **External IP addresses**
2. Encuentra tu IP → Type: **Static**
3. Costo: ~$0.01/hora cuando no está asignada

### "Me están cobrando"

**Verifica:**

1. ¿Usas f1-micro en región permitida?
2. ¿Dejaste VM corriendo 24/7?
3. ¿Tienes recursos adicionales? (IPs, discos)

**Solución:**

- Detén o elimina recursos no necesarios
- Contacta soporte de GCP si crees que es error

---

## Comandos Útiles de gcloud

### Instalar gcloud CLI (Opcional)

```bash
# Linux
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Inicializar
gcloud init
```

### Comandos Básicos

```bash
# Listar VMs
gcloud compute instances list

# Ver detalles de VM
gcloud compute instances describe ubuntu-bootcamp --zone=us-central1-a

# SSH a VM
gcloud compute ssh ubuntu-bootcamp --zone=us-central1-a

# Detener VM
gcloud compute instances stop ubuntu-bootcamp --zone=us-central1-a

# Iniciar VM
gcloud compute instances start ubuntu-bootcamp --zone=us-central1-a

# Eliminar VM
gcloud compute instances delete ubuntu-bootcamp --zone=us-central1-a
```

---

## Checklist Final

Antes de dar por completada la configuración:

- [ ] VM creada y corriendo (estado: Running)
- [ ] Puedes conectar por SSH
- [ ] Sistema actualizado (`sudo apt update && sudo apt upgrade`)
- [ ] Firewall configurado (puertos necesarios abiertos)
- [ ] Alarma de presupuesto configurada
- [ ] IP externa anotada
- [ ] Username anotado

---

## Próximos Pasos

✅ VM lista para usar!

**Ahora puedes:**

1. Continuar con [Práctica 1](../../2-practicas/01-setup-servidor-cloud.md)
2. Instalar Docker
3. Desplegar tu primera aplicación

**No olvides:**

- 🛑 **Detener VM** cuando termines
- 💰 **Monitorear costos** semanalmente
- 📝 **Anotar IP y usuario** para futuras conexiones

---

> **Tip:** Crea un archivo local con tus datos de acceso:
>
> ```
> IP: 34.123.45.67
> Usuario: juan_perez
> Comando: ssh juan_perez@34.123.45.67
> ```

¡Éxito con tu primer servidor en la nube! ☁️🚀
