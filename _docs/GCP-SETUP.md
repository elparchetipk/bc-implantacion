# Google Cloud Platform (GCP) para Prácticas del Bootcamp

## 📋 Descripción General

Google Cloud Platform (GCP) es la opción **recomendada** para las prácticas del bootcamp debido a su generosa capa gratuita y productos Always Free.

---

## 🆓 GCP Free Tier

### Capa Gratuita (Free Trial)

GCP ofrece **$300 USD de crédito** válido por **90 días** para nuevos usuarios.

**Requisitos**:

- Cuenta de Google
- Tarjeta de crédito/débito (solo verificación, no se cobra automáticamente)
- No haber usado GCP Free Trial anteriormente

### Always Free Products

Estos productos son **gratuitos para siempre** (no requieren créditos):

#### Compute Engine

- **1 VM f1-micro** por mes
  - 0.6 GB de memoria
  - Regiones elegibles: us-west1, us-central1, us-east1
  - 30 GB de disco HDD por mes

#### Cloud Storage

- **5 GB** de almacenamiento Regional
- 5000 operaciones Class A por mes
- 50000 operaciones Class B por mes
- 1 GB de tráfico de salida a Norteamérica por mes

#### Cloud Functions

- **2 millones** de invocaciones por mes
- 400,000 GB-segundos de tiempo de computación
- 200,000 GHz-segundos de tiempo de computación
- 5 GB de tráfico de salida

#### Cloud Run

- **2 millones** de solicitudes por mes
- 360,000 GB-segundos de memoria
- 180,000 vCPU-segundos

#### Otros Servicios Always Free

- **Cloud SQL**: 1 instancia db-f1-micro (sin cargo)
- **Cloud Build**: 120 minutos de build por día
- **Cloud Shell**: 5 GB de almacenamiento persistente
- **BigQuery**: 1 TB de consultas por mes
- **Cloud Pub/Sub**: 10 GB de mensajes por mes

---

## 🎓 Casos de Uso para el Bootcamp

### Semana 1-2: Fundamentos de Hardware

- **Compute Engine**: Crear VMs para entender especificaciones de hardware
- **Cloud Console**: Familiarizarse con gestión de recursos

### Semana 3-4: Sistemas Operativos

- **Compute Engine f1-micro**: Instalar y configurar Ubuntu Server
- **SSH**: Conexión remota y gestión

### Semana 5: Docker y Contenedores

- **Compute Engine**: Desplegar Docker y Docker Compose
- **Container Registry**: Almacenar imágenes Docker
- **Cloud Run**: Desplegar contenedores sin gestionar infraestructura

### Semana 6: Hosting y Dominios

- **Cloud DNS**: Gestión de dominios
- **Cloud Load Balancing**: Distribución de tráfico
- **Cloud CDN**: Distribución de contenido estático

### Semana 7: Respaldo y Migración

- **Cloud Storage**: Almacenar backups
- **Cloud SQL**: Migración de bases de datos PostgreSQL
- **Persistent Disks**: Snapshots de discos

### Semana 8-9: Proyecto Final

- **Stack completo**: VM + Docker + PostgreSQL + Nginx
- **Cloud Monitoring**: Monitoreo de aplicación
- **Cloud Logging**: Registros centralizados

---

## 🚀 Configuración Inicial

### 1. Crear Cuenta GCP

```bash
# 1. Visitar
https://cloud.google.com/free

# 2. Hacer clic en "Comenzar gratis"
# 3. Iniciar sesión con cuenta de Google
# 4. Completar información de verificación
# 5. Ingresar datos de tarjeta (solo verificación)
```

### 2. Crear Proyecto

```bash
# En Cloud Console
1. Hacer clic en selector de proyectos (arriba)
2. "Nuevo Proyecto"
3. Nombre: "bootcamp-implantacion-sena"
4. Crear
```

### 3. Activar APIs Necesarias

```bash
# Compute Engine API
gcloud services enable compute.googleapis.com

# Cloud Storage API
gcloud services enable storage.googleapis.com

# Cloud SQL API
gcloud services enable sqladmin.googleapis.com

# Container Registry API
gcloud services enable containerregistry.googleapis.com
```

### 4. Instalar Google Cloud SDK

#### Linux (Debian/Ubuntu)

```bash
# ¿Qué?: Agregar repositorio de Google Cloud SDK
# ¿Para qué?: Instalar herramientas de línea de comandos de GCP
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# ¿Qué?: Importar clave GPG
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

# ¿Qué?: Instalar Google Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

#### Fedora/RHEL

```bash
# ¿Qué?: Agregar repositorio de Google Cloud SDK
sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

# ¿Qué?: Instalar Google Cloud SDK
sudo dnf install google-cloud-sdk
```

#### Verificar Instalación

```bash
# ¿Qué?: Verificar que gcloud está instalado
gcloud version
```

### 5. Inicializar gcloud

```bash
# ¿Qué?: Inicializar configuración de gcloud
# ¿Para qué?: Autenticar y configurar proyecto por defecto
gcloud init

# Seguir los pasos:
# 1. Iniciar sesión con cuenta de Google
# 2. Seleccionar proyecto "bootcamp-implantacion-sena"
# 3. Configurar región por defecto: us-central1
# 4. Configurar zona por defecto: us-central1-a
```

---

## 💻 Ejemplo Práctico: VM con Docker

### Crear VM Always Free

```bash
# ¿Qué?: Crear VM f1-micro con Ubuntu 22.04
# ¿Para qué?: Tener un servidor gratuito para prácticas
# ¿Cómo?: Usa recursos Always Free de GCP
gcloud compute instances create bootcamp-vm \
  --machine-type=f1-micro \
  --zone=us-central1-a \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=30GB \
  --boot-disk-type=pd-standard \
  --tags=http-server,https-server

# Permitir tráfico HTTP/HTTPS
gcloud compute firewall-rules create allow-http \
  --allow tcp:80,tcp:443 \
  --target-tags http-server,https-server
```

### Conectar a la VM

```bash
# ¿Qué?: Conectar por SSH a la VM
gcloud compute ssh bootcamp-vm --zone=us-central1-a
```

### Instalar Docker

```bash
# ¿Qué?: Script de instalación de Docker en Ubuntu
# ¿Para qué?: Preparar ambiente de contenedores
# ¿Cómo?: Instala Docker Engine y Docker Compose v2

# Actualizar sistema
sudo apt-get update && sudo apt-get upgrade -y

# Instalar dependencias
sudo apt-get install -y \
  ca-certificates \
  curl \
  gnupg \
  lsb-release

# Agregar clave GPG de Docker
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Agregar repositorio
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Verificar instalación
docker --version
docker compose version
```

### Desplegar Stack (Nginx + API + PostgreSQL)

```bash
# ¿Qué?: Crear estructura de proyecto
mkdir -p ~/bootcamp-stack
cd ~/bootcamp-stack

# ¿Qué?: Crear docker-compose.yml
# ¿Para qué?: Definir stack de aplicación completo
cat > docker-compose.yml << 'EOF'
# ¿Qué?: Archivo de orquestación Docker Compose
# ¿Para qué?: Definir servicios de la aplicación (Nginx + API + DB)
services:
  # ¿Qué?: Servicio de base de datos PostgreSQL 15
  # ¿Para qué?: Almacenar datos de la aplicación
  database:
    image: postgres:15-alpine
    container_name: postgres-db
    environment:
      POSTGRES_DB: bootcamp_db
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secure_password_123
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network
    restart: unless-stopped

  # ¿Qué?: Servicio Nginx como reverse proxy
  # ¿Para qué?: Servir contenido estático y redireccionar a API
  nginx:
    image: nginx:alpine
    container_name: nginx-server
    ports:
      - "80:80"
    networks:
      - app-network
    restart: unless-stopped

# ¿Qué?: Definición de volúmenes persistentes
# ¿Para qué?: Mantener datos entre reinicios de contenedores
volumes:
  postgres_data:

# ¿Qué?: Definición de red interna
# ¿Para qué?: Comunicación entre contenedores
networks:
  app-network:
    driver: bridge
EOF

# ¿Qué?: Levantar servicios
# ¿Para qué?: Iniciar stack completo en modo detached
docker compose up -d

# Verificar servicios
docker compose ps
docker compose logs -f
```

---

## 📊 Monitoreo de Uso y Costos

### Ver Uso de Free Tier

```bash
# En Cloud Console
1. Ir a "Facturación" → "Informes"
2. Filtrar por "Nivel gratuito"
3. Ver consumo de recursos
```

### Configurar Alertas de Presupuesto

```bash
# En Cloud Console
1. "Facturación" → "Presupuestos y alertas"
2. "Crear presupuesto"
3. Configurar límite: $5 USD
4. Alertas: 50%, 90%, 100%
5. Notificaciones por email
```

### Comandos de Monitoreo

```bash
# Listar todas las VMs
gcloud compute instances list

# Ver uso de disco de una VM
gcloud compute disks list

# Ver snapshots
gcloud compute snapshots list

# Ver uso de Cloud Storage
gsutil du -sh gs://mi-bucket

# Ver costos estimados del proyecto
gcloud billing accounts list
```

---

## 🛑 Detener Recursos para Ahorrar

### Detener VM (sin eliminar)

```bash
# ¿Qué?: Detener VM sin eliminarla
# ¿Para qué?: Ahorrar costos cuando no se usa (no se cobra por VM detenida)
gcloud compute instances stop bootcamp-vm --zone=us-central1-a

# Reiniciar cuando se necesite
gcloud compute instances start bootcamp-vm --zone=us-central1-a
```

### Eliminar Recursos

```bash
# Eliminar VM
gcloud compute instances delete bootcamp-vm --zone=us-central1-a

# Eliminar disco
gcloud compute disks delete bootcamp-vm --zone=us-central1-a

# Eliminar snapshot
gcloud compute snapshots delete my-snapshot
```

---

## 📚 Recursos Adicionales

### Documentación Oficial

- [GCP Free Tier](https://cloud.google.com/free)
- [Always Free Products](https://cloud.google.com/free/docs/gcp-free-tier#always-free)
- [Compute Engine Docs](https://cloud.google.com/compute/docs)
- [Cloud SDK Docs](https://cloud.google.com/sdk/docs)

### Tutoriales

- [Quickstart: Linux VMs](https://cloud.google.com/compute/docs/quickstart-linux)
- [Deploy Docker Containers](https://cloud.google.com/compute/docs/containers/deploying-containers)
- [Cloud Storage Tutorial](https://cloud.google.com/storage/docs/quickstart-console)

### Soporte

- [Stack Overflow: google-cloud-platform](https://stackoverflow.com/questions/tagged/google-cloud-platform)
- [GCP Community](https://www.googlecloudcommunity.com/)
- [Free Tier FAQ](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-faqs)

---

## ⚠️ Mejores Prácticas

### Seguridad

✅ **DO**:

- Usar SSH keys en lugar de contraseñas
- Configurar firewall rules restrictivas
- Rotar credenciales regularmente
- Habilitar 2FA en cuenta de Google
- Usar service accounts para aplicaciones

❌ **DON'T**:

- Exponer puertos innecesarios
- Usar contraseñas por defecto
- Compartir credenciales
- Dejar recursos corriendo sin usar

### Costos

✅ **DO**:

- Detener VMs cuando no se usan
- Usar preemptible VMs para pruebas
- Configurar alertas de presupuesto
- Revisar facturación semanalmente
- Limpiar recursos no usados

❌ **DON'T**:

- Dejar VMs corriendo 24/7
- Crear múltiples snapshots sin limpiar
- Usar tipos de máquina más grandes de lo necesario
- Olvidar eliminar recursos después de practicar

### Organización

✅ **DO**:

- Usar etiquetas (labels) en recursos
- Nombrar recursos descriptivamente
- Documentar configuraciones
- Usar proyectos separados para diferentes propósitos

---

## 🎯 Checklist para Aprendices

### Configuración Inicial

- [ ] Crear cuenta GCP con correo institucional del SENA
- [ ] Activar Free Trial ($300 USD)
- [ ] Crear proyecto "bootcamp-implantacion-sena"
- [ ] Instalar Google Cloud SDK en máquina local
- [ ] Configurar gcloud CLI
- [ ] Configurar alertas de presupuesto ($5 USD)

### Primera VM

- [ ] Crear VM f1-micro en us-central1
- [ ] Conectar por SSH
- [ ] Actualizar sistema operativo
- [ ] Instalar Docker y Docker Compose v2
- [ ] Verificar instalación: `docker compose version`

### Primer Despliegue

- [ ] Crear docker-compose.yml con PostgreSQL
- [ ] Levantar servicios: `docker compose up -d`
- [ ] Verificar logs: `docker compose logs -f`
- [ ] Conectar a base de datos
- [ ] Crear snapshot de disco como backup

### Limpieza

- [ ] Detener servicios: `docker compose down`
- [ ] Detener VM cuando no se use
- [ ] Revisar uso semanal de recursos
- [ ] Eliminar snapshots antiguos
- [ ] Al finalizar bootcamp: eliminar todos los recursos

---

**¡GCP es una excelente plataforma para aprender implantación de software sin costos!** 🚀

Última actualización: 5 de octubre de 2025
