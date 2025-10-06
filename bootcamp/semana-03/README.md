# Semana 3: Linux Server y Despliegue Remoto

## 🎯 Objetivo de Aprendizaje

**Preparar la plataforma tecnológica con Linux Server para despliegue de aplicaciones, considerando requisitos mínimos de hardware y conectividad remota segura.**

## 📋 Contenido de la Semana

### 1. Teoría
- **Archivo**: `1-teoria/linux-server-implantacion.md`
- **Duración**: ~60 minutos de lectura
- **Temas**:
  - ¿Por qué Linux Server?
  - Distribuciones (Ubuntu Server, Rocky Linux)
  - Requisitos de hardware
  - SSH: Acceso remoto seguro
  - Usuarios y permisos
  - Comandos esenciales
  - Firewall (UFW)
  - Gestión de servicios (systemctl)

### 2. Prácticas

#### Práctica 1: Setup Inicial de Servidor
- **Archivo**: `2-practicas/01-setup-servidor-cloud.md`
- **Duración**: ~60 minutos
- **Objetivo**: Crear y configurar Ubuntu Server en Google Cloud
- **Entregable**: Servidor funcional con Docker instalado

#### Práctica 2: Despliegue Remoto
- **Archivo**: `2-practicas/02-deploy-proyecto-remoto.md`
- **Duración**: ~90 minutos
- **Objetivo**: Desplegar proyecto de Semana 2 en servidor remoto
- **Entregable**: Aplicación accesible públicamente + documentación

### 3. Recursos de Apoyo

Carpeta `3-recursos/` con:
- `README.md` - Índice y guía de uso
- `cheatsheet-linux-server.md` - Comandos esenciales
- `troubleshooting-linux.md` - Solución a problemas comunes
- `guia-gcp-free-tier.md` - Crear VM gratuita en Google Cloud
- `script-setup-server.sh` - Script automatizado de configuración
- `template-deploy.md` - Checklist de despliegue

## ⏱️ Distribución de Tiempo (6 horas)

### Bloque 1: Teoría y Demos (2 horas)
- **00:00 - 01:00**: Lectura de teoría + Explicación del instructor
- **01:00 - 01:30**: Demo: Crear VM en Google Cloud
- **01:30 - 02:00**: Demo: Conexión SSH + Setup básico

### Descanso (30 minutos)
- **02:00 - 02:30**: ☕ Receso

### Bloque 2: Práctica 1 (1.5 horas)
- **02:30 - 03:00**: Crear y configurar VM propia
- **03:00 - 03:30**: Instalar Docker + configurar firewall
- **03:30 - 04:00**: Verificaciones y troubleshooting

### Bloque 3: Práctica 2 (2 horas)
- **04:00 - 04:30**: Transferir proyecto de Semana 2
- **04:30 - 05:30**: Desplegar stack en servidor
- **05:30 - 06:00**: Testing, documentación, cleanup

## 📊 Comparación: ANTES vs DESPUÉS

### Antes de esta semana
- ✅ Hardware de servidores (teoría)
- ✅ Docker Compose (local)
- ❌ Despliegue en servidor remoto
- ❌ Administración Linux
- ❌ SSH y transferencia de archivos

### Después de esta semana
- ✅ Servidor Linux configurado
- ✅ Acceso remoto seguro (SSH)
- ✅ Aplicación desplegada en la nube
- ✅ Firewall configurado
- ✅ Comandos esenciales dominados

## 🎯 Criterios de Éxito

### Teoría (Bloque 1)
- [ ] 100% comprenden ¿por qué Linux Server?
- [ ] 90%+ pueden conectarse vía SSH
- [ ] 85%+ conocen 10 comandos esenciales

### Práctica 1 (Bloque 2)
- [ ] 90%+ crean VM exitosamente en GCP
- [ ] 85%+ instalan Docker correctamente
- [ ] 80%+ configuran firewall básico

### Práctica 2 (Bloque 3)
- [ ] 75%+ despliegan stack en servidor remoto
- [ ] 70%+ pueden acceder remotamente a su aplicación
- [ ] 60%+ documentan el proceso completo

### Autonomía
- [ ] 80%+ resuelven problemas SSH/permisos sin ayuda
- [ ] 70%+ usan cheatsheet como referencia
- [ ] 60%+ pueden replicar el proceso en otro servidor

## 📈 Indicadores de Logro

### Durante la Clase
- **Participación activa** en demos SSH
- **Completación** de Práctica 1 en tiempo estimado
- **Consulta de recursos** (cheatsheet, troubleshooting)
- **Autonomía** en resolución de errores comunes

### Después de la Clase
- **Entrega** de Práctica 2 con documentación
- **Calidad** del despliegue (aplicación accesible públicamente)
- **Originalidad** (adaptación a su dominio de Semana 2)
- **Documentación** clara del proceso seguido

## 🚀 Para el Instructor

### Preparación Pre-Clase

**1 semana antes:**
- [ ] Enviar email a estudiantes para crear cuenta GCP (requiere tarjeta, pero no cobra)
- [ ] Compartir guía `3-recursos/guia-gcp-free-tier.md`
- [ ] Verificar que todos tienen cuenta GCP activa

**1 día antes:**
- [ ] Revisar cheatsheet y troubleshooting
- [ ] Probar script de setup en VM limpia
- [ ] Preparar VM de demo
- [ ] Verificar conectividad SSH desde red institucional

**Inicio de clase:**
- [ ] Explicar estructura de `3-recursos/`
- [ ] Enfatizar importancia de SSH keys (seguridad)
- [ ] Advertir sobre costos (Free Tier, shutdown VMs)
- [ ] Mostrar cómo usar cheatsheet y troubleshooting

### Durante Teoría (Bloque 1)
- [ ] Referencia constante al cheatsheet
- [ ] Demo en vivo (no solo slides)
- [ ] Mostrar errores comunes y soluciones
- [ ] Enfatizar diferencia: desarrollo local vs producción

### Durante Práctica 1 (Bloque 2)
- [ ] Circular por el aula verificando progreso
- [ ] Identificar quiénes tienen problemas SSH
- [ ] Remitir a troubleshooting antes de responder
- [ ] Ayudar con autenticación GCP si es necesario

### Durante Práctica 2 (Bloque 3)
- [ ] Verificar que usan proyecto de Semana 2
- [ ] Validar configuración de firewall (puertos abiertos)
- [ ] Ayudar con transferencia de archivos (scp/rsync)
- [ ] Verificar acceso público a aplicaciones

### Al Finalizar
- [ ] Resumir comandos esenciales (top 10)
- [ ] Recordar shutdown VMs para evitar costos
- [ ] Asignar documentación como tarea
- [ ] Anunciar: Semana 4 = Networking y Nginx

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Estudiantes sin cuenta GCP | Alto | Guía pre-clase, alternativa VirtualBox local |
| Problemas SSH institucional | Alto | Web console GCP, SSH desde casa |
| Confusión comandos Linux | Medio | Cheatsheet robusto, comparación con Windows |
| Transferencia archivos falla | Medio | Múltiples métodos (scp, rsync, git) |
| Costos inesperados cloud | Bajo | Énfasis en Free Tier, alarmas presupuesto |
| Tiempo insuficiente | Medio | Script setup automatizado, templates |

## 🔗 Conexión con Otras Semanas

### Semana 1 → Semana 3
- **Antes**: Teoría de hardware de servidores
- **Ahora**: Verificar requisitos en servidor real

### Semana 2 → Semana 3
- **Antes**: Docker Compose funcionando localmente
- **Ahora**: Desplegar en servidor Linux remoto

### Semana 3 → Semana 4
- **Ahora**: Aplicación corriendo en servidor
- **Siguiente**: Configurar dominio y Nginx como reverse proxy

## 📝 Entregables de la Semana

### Práctica 1 (Opcional - completada en clase)
- Screenshot de VM corriendo en GCP
- Output de `docker --version`
- Output de `sudo ufw status`

### Práctica 2 (Obligatorio - tarea)
1. **Código**:
   - Proyecto desplegado en servidor
   - URL pública de la aplicación

2. **Documentación** (README.md):
   - IP pública del servidor
   - Puertos abiertos (firewall)
   - Comandos usados para desplegar
   - Screenshot de la aplicación funcionando
   - Problemas encontrados y cómo los resolviste

3. **Rúbrica** (100 puntos):
   - Aplicación accesible públicamente (40 pts)
   - Firewall correctamente configurado (20 pts)
   - Documentación completa y clara (20 pts)
   - Código organizado y comentado (10 pts)
   - Originalidad (adaptado a dominio) (10 pts)

## 💡 Tips para Estudiantes

### Antes de Empezar
- ✅ Crea cuenta GCP con anticipación
- ✅ Lee la teoría completa antes de clase
- ✅ Ten a mano el proyecto de Semana 2
- ✅ Familiarízate con el cheatsheet

### Durante la Práctica
- ✅ Usa cheatsheet como referencia constante
- ✅ Ante un error, busca primero en troubleshooting
- ✅ Documenta comandos que usas (copiar en archivo .txt)
- ✅ No copies-pega sin entender (adapta a tu dominio)
- ✅ Shutdown VM al terminar sesión (evitar costos)

### Después de Clase
- ✅ Completa Práctica 2 en las próximas 48 horas
- ✅ Documenta problemas y soluciones
- ✅ Prueba acceso desde diferentes dispositivos
- ✅ Mantén servidor corriendo para demostración

## 📚 Recursos Externos Recomendados

### Tutoriales
- [Linux Journey](https://linuxjourney.com/) - Tutorial interactivo de Linux
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) - Practicar comandos Linux (juego)
- [Google Cloud Free Tier](https://cloud.google.com/free) - Documentación oficial

### Cheat Sheets
- [Linux Command Cheat Sheet](https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/)
- [SSH Cheat Sheet](https://www.ssh.com/academy/ssh/command)
- [UFW Essentials](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)

### Videos
- [Ubuntu Server Setup](https://www.youtube.com/results?search_query=ubuntu+server+setup)
- [SSH Basics](https://www.youtube.com/results?search_query=ssh+tutorial+beginners)

## 🆘 Soporte

### ¿Problemas durante la clase?
1. Consulta `3-recursos/troubleshooting-linux.md`
2. Pregunta a compañeros cercanos
3. Levanta la mano para el instructor

### ¿Problemas después de clase?
1. Revisa troubleshooting nuevamente
2. Busca error específico en Google (en inglés)
3. Consulta en foro del curso
4. Email al instructor (con screenshots y comandos usados)

---

**¡Éxito en tu primera experiencia con Linux Server! 🚀**

> Recuerda: El objetivo no es ser un experto en Linux, sino tener las habilidades básicas para **implantar software de forma segura y eficiente**.
