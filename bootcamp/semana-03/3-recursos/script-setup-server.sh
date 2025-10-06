#!/bin/bash

# ============================================================================
# Script de Configuración Automática de Servidor Ubuntu
# ============================================================================
#
# ¿Qué? - Script que configura servidor Ubuntu para despliegue de aplicaciones
# ¿Para qué? - Automatizar instalación de Docker, firewall y configuración básica
# ¿Cómo? - Ejecutar: sudo bash script-setup-server.sh
#
# Autor: Bootcamp Implantación - SENA CGMLTI
# Versión: 1.0
# Última actualización: 2025-10-06
#
# ============================================================================

set -e  # Detener en caso de error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funciones de utilidad
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[⚠]${NC} $1"
}

log_error() {
    echo -e "${RED}[✗]${NC} $1"
}

# Banner
echo ""
echo "============================================"
echo "  🚀 Setup Servidor Ubuntu para Docker"
echo "============================================"
echo ""

# Verificar que se ejecuta como root
if [ "$EUID" -ne 0 ]; then 
    log_error "Este script debe ejecutarse como root (usa sudo)"
    exit 1
fi

log_info "Iniciando configuración del servidor..."
echo ""

# ============================================================================
# 1. ACTUALIZAR SISTEMA
# ============================================================================
log_info "Paso 1/6: Actualizando sistema operativo..."

# ¿Qué? - Actualizar lista de paquetes disponibles
# ¿Para qué? - Obtener información de últimas versiones
apt update -qq

log_success "Lista de paquetes actualizada"

# ¿Qué? - Actualizar paquetes instalados
# ¿Para qué? - Aplicar parches de seguridad
log_info "Instalando actualizaciones (puede tardar 2-3 minutos)..."
DEBIAN_FRONTEND=noninteractive apt upgrade -y -qq

log_success "Sistema actualizado"
echo ""

# ============================================================================
# 2. INSTALAR DEPENDENCIAS
# ============================================================================
log_info "Paso 2/6: Instalando herramientas básicas..."

# ¿Qué? - Instalar paquetes esenciales
# ¿Para qué? - Herramientas necesarias para administración
apt install -y -qq \
    curl \
    wget \
    git \
    nano \
    htop \
    net-tools \
    ca-certificates \
    gnupg \
    lsb-release

log_success "Herramientas básicas instaladas"
echo ""

# ============================================================================
# 3. INSTALAR DOCKER
# ============================================================================
log_info "Paso 3/6: Instalando Docker..."

# ¿Qué? - Descargar script oficial de instalación de Docker
# ¿Para qué? - Método recomendado por Docker Inc.
if [ ! -f get-docker.sh ]; then
    curl -fsSL https://get.docker.com -o get-docker.sh
fi

# ¿Qué? - Ejecutar script de instalación
# ¿Para qué? - Instalar Docker Engine + Docker Compose v2
sh get-docker.sh > /dev/null 2>&1

# ¿Qué? - Limpiar archivo descargado
rm get-docker.sh

log_success "Docker instalado correctamente"

# Verificar versión
DOCKER_VERSION=$(docker --version | cut -d' ' -f3 | cut -d',' -f1)
log_info "Docker versión: $DOCKER_VERSION"

COMPOSE_VERSION=$(docker compose version | cut -d' ' -f4)
log_info "Docker Compose versión: $COMPOSE_VERSION"

# ¿Qué? - Habilitar Docker para que inicie con el sistema
# ¿Para qué? - Contenedores arrancan automáticamente tras reinicio
systemctl enable docker > /dev/null 2>&1

log_success "Docker habilitado al inicio"
echo ""

# ============================================================================
# 4. CONFIGURAR USUARIO NO-ROOT
# ============================================================================
log_info "Paso 4/6: Configurando usuarios..."

# ¿Qué? - Obtener usuario que invocó sudo
# ¿Para qué? - Agregar permisos de Docker al usuario real
REAL_USER=${SUDO_USER:-$USER}

if [ "$REAL_USER" != "root" ]; then
    # ¿Qué? - Agregar usuario al grupo docker
    # ¿Para qué? - Permitir ejecutar docker sin sudo
    usermod -aG docker "$REAL_USER"
    log_success "Usuario '$REAL_USER' agregado al grupo docker"
    log_warning "Cierra sesión y vuelve a conectar para aplicar cambios"
else
    log_warning "Ejecutado como root - considera crear usuario no-root"
fi

# ¿Qué? - Crear usuario 'deploy' si no existe
# ¿Para qué? - Usuario dedicado para despliegues (opcional)
if ! id "deploy" &>/dev/null; then
    log_info "¿Deseas crear usuario 'deploy'? (y/n)"
    read -r CREATE_DEPLOY
    
    if [ "$CREATE_DEPLOY" = "y" ]; then
        adduser --disabled-password --gecos "" deploy
        usermod -aG sudo,docker deploy
        log_success "Usuario 'deploy' creado (recuerda configurar contraseña)"
    fi
fi

echo ""

# ============================================================================
# 5. CONFIGURAR FIREWALL (UFW)
# ============================================================================
log_info "Paso 5/6: Configurando firewall (UFW)..."

# ¿Qué? - Instalar UFW si no está
if ! command -v ufw &> /dev/null; then
    apt install -y -qq ufw
fi

# ¿Qué? - Permitir SSH (puerto 22)
# ¿Para qué? - Mantener acceso remoto
ufw allow 22/tcp > /dev/null 2>&1
log_success "Puerto 22 (SSH) permitido"

# ¿Qué? - Permitir HTTP (puerto 80)
ufw allow 80/tcp > /dev/null 2>&1
log_success "Puerto 80 (HTTP) permitido"

# ¿Qué? - Permitir HTTPS (puerto 443)
ufw allow 443/tcp > /dev/null 2>&1
log_success "Puerto 443 (HTTPS) permitido"

# ¿Qué? - Permitir puertos comunes de aplicaciones
log_info "¿Deseas abrir puertos adicionales? (ej: 3000, 8080)"
log_info "Ingresa puertos separados por espacio, o Enter para omitir:"
read -r EXTRA_PORTS

if [ -n "$EXTRA_PORTS" ]; then
    for port in $EXTRA_PORTS; do
        ufw allow "$port"/tcp > /dev/null 2>&1
        log_success "Puerto $port permitido"
    done
fi

# ¿Qué? - Activar firewall
# ¿Para qué? - Aplicar reglas de seguridad
log_info "Activando firewall..."
ufw --force enable > /dev/null 2>&1

log_success "Firewall configurado y activo"
echo ""

# ============================================================================
# 6. VERIFICACIONES FINALES
# ============================================================================
log_info "Paso 6/6: Verificando instalación..."

# Verificar Docker
if docker ps > /dev/null 2>&1; then
    log_success "Docker funciona correctamente"
else
    log_error "Docker no está funcionando"
fi

# Verificar Docker Compose
if docker compose version > /dev/null 2>&1; then
    log_success "Docker Compose funciona correctamente"
else
    log_error "Docker Compose no está funcionando"
fi

# Verificar UFW
if ufw status | grep -q "Status: active"; then
    log_success "Firewall está activo"
else
    log_warning "Firewall no está activo"
fi

echo ""

# ============================================================================
# RESUMEN
# ============================================================================
echo "============================================"
echo "  ✅ Configuración Completada"
echo "============================================"
echo ""
echo "📊 Resumen de Recursos:"
echo "  • RAM disponible: $(free -h | awk '/^Mem:/ {print $4}')"
echo "  • Disco disponible: $(df -h / | awk 'NR==2 {print $4}')"
echo "  • Docker: $DOCKER_VERSION"
echo "  • Docker Compose: $COMPOSE_VERSION"
echo ""
echo "🔥 Firewall (UFW):"
ufw status numbered | grep -E "^\[|^Status"
echo ""
echo "📝 Próximos Pasos:"
echo "  1. Cierra sesión y vuelve a conectar:"
echo "     exit"
echo "     ssh $REAL_USER@\$(hostname -I | awk '{print \$1}')"
echo ""
echo "  2. Verifica que Docker funciona sin sudo:"
echo "     docker ps"
echo ""
echo "  3. Despliega tu primera aplicación:"
echo "     docker compose up -d"
echo ""
echo "============================================"
echo ""

# Preguntar si reiniciar (si actualizó kernel)
if [ -f /var/run/reboot-required ]; then
    log_warning "Se requiere reinicio para aplicar todas las actualizaciones"
    log_info "¿Deseas reiniciar ahora? (y/n)"
    read -r REBOOT
    
    if [ "$REBOOT" = "y" ]; then
        log_info "Reiniciando en 5 segundos..."
        sleep 5
        reboot
    else
        log_info "Recuerda reiniciar más tarde: sudo reboot"
    fi
fi

log_success "¡Configuración exitosa! 🚀"
echo ""

# ============================================================================
# FIN DEL SCRIPT
# ============================================================================
