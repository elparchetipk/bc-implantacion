# Recursos de Apoyo - Semana 3

> **Propósito**: Materiales de referencia rápida, guías paso a paso y herramientas para facilitar el aprendizaje autónomo de Linux Server y despliegue remoto.

## 📦 Contenido de esta Carpeta

### 1. Referencia Rápida

- **`cheatsheet-linux-server.md`**: Comandos esenciales de Linux para implantación (los 15 más usados)

### 2. Solución de Problemas

- **`troubleshooting-linux.md`**: Guía de resolución de problemas comunes (SSH, permisos, firewall, Docker)

### 3. Guías Paso a Paso

- **`guia-gcp-free-tier.md`**: Crear VM gratuita en Google Cloud Platform

### 4. Automatización

- **`script-setup-server.sh`**: Script para configurar servidor automáticamente

### 5. Plantillas

- **`template-deploy.md`**: Checklist y comandos para despliegue

---

## 🎯 ¿Cuándo Usar Cada Recurso?

### Durante Teoría (Bloque 1)

📖 **Lectura recomendada:**

- `cheatsheet-linux-server.md` → Tener abierto como referencia

### Durante Práctica 1 (Setup Servidor)

🔧 **Recursos útiles:**

1. `guia-gcp-free-tier.md` → Crear VM paso a paso
2. `script-setup-server.sh` → Automatizar configuración
3. `troubleshooting-linux.md` → Si hay problemas SSH o permisos

### Durante Práctica 2 (Despliegue)

🚀 **Recursos útiles:**

1. `template-deploy.md` → Checklist de verificación
2. `cheatsheet-linux-server.md` → Comandos de transferencia (scp, rsync)
3. `troubleshooting-linux.md` → Problemas de firewall o Docker

### Después de Clase

📚 **Para profundizar:**

- Repasar `cheatsheet-linux-server.md`
- Practicar comandos en servidor de prueba

---

## 📊 Comparación de Recursos

| Recurso                      | Tipo       | Tiempo lectura | Mejor para           |
| ---------------------------- | ---------- | -------------- | -------------------- |
| `cheatsheet-linux-server.md` | Referencia | 5 min          | Consulta rápida      |
| `troubleshooting-linux.md`   | Guía       | 10-15 min      | Resolver errores     |
| `guia-gcp-free-tier.md`      | Tutorial   | 15 min         | Primera vez GCP      |
| `script-setup-server.sh`     | Script     | 2 min          | Automatizar setup    |
| `template-deploy.md`         | Checklist  | 5 min          | Verificar despliegue |

---

## 💡 Tips de Uso

### DO's ✅

- ✅ Ten el cheatsheet abierto mientras trabajas
- ✅ Consulta troubleshooting ANTES de pedir ayuda
- ✅ Usa script de setup para ahorrar tiempo
- ✅ Sigue el template de deploy como checklist
- ✅ Adapta ejemplos a tu contexto específico

### DON'Ts ❌

- ❌ No copies-pega sin entender qué hace
- ❌ No ignores errores (busca en troubleshooting)
- ❌ No saltes pasos del checklist
- ❌ No modifiques el script sin leerlo primero
- ❌ No uses comandos `rm -rf` sin verificar ruta

---

## 🔍 Búsqueda Rápida

### "¿Cómo conecto por SSH?"

→ Ver: `cheatsheet-linux-server.md` → Sección SSH

### "Error: Permission denied"

→ Ver: `troubleshooting-linux.md` → Problema 1

### "¿Cómo abro un puerto?"

→ Ver: `cheatsheet-linux-server.md` → Sección Firewall (UFW)

### "¿Cómo transfiero archivos?"

→ Ver: `cheatsheet-linux-server.md` → Sección Transferencia de Archivos

### "Docker no inicia"

→ Ver: `troubleshooting-linux.md` → Problema 5

### "¿Cómo creo VM en GCP?"

→ Ver: `guia-gcp-free-tier.md`

---

## 📋 Checklist: Dominio del Tema

Usa este checklist para verificar tu aprendizaje:

### Nivel Básico (Semana 3)

- [ ] Puedo conectarme a un servidor por SSH
- [ ] Conozco 10+ comandos esenciales de Linux
- [ ] Puedo instalar Docker en Ubuntu Server
- [ ] Sé configurar firewall básico (UFW)
- [ ] Puedo transferir archivos con scp
- [ ] Puedo desplegar stack con docker compose

### Nivel Intermedio (Post Semana 3)

- [ ] Puedo crear y configurar VM en GCP sin guía
- [ ] Uso rsync para transferencias eficientes
- [ ] Configuro usuarios y permisos correctamente
- [ ] Resuelvo problemas comunes sin ayuda
- [ ] Documento mis despliegues adecuadamente

### Nivel Avanzado (Opcional)

- [ ] Automatizo setup con scripts bash
- [ ] Configuro backups automáticos
- [ ] Implemento monitoreo básico
- [ ] Uso SSH keys en lugar de contraseñas
- [ ] Optimizo configuración de firewall

---

## 🆘 ¿Aún Tienes Dudas?

### Durante Clase

1. Consulta el recurso relevante
2. Pregunta a compañeros cercanos
3. Levanta la mano para el instructor

### Fuera de Clase

1. Revisa troubleshooting completo
2. Busca error específico en Google (inglés)
3. Consulta foro del curso
4. Email al instructor con detalles (screenshots, comandos)

---

## 📚 Recursos Externos Complementarios

### Tutoriales Interactivos

- [Linux Journey](https://linuxjourney.com/) - Aprende Linux paso a paso
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) - Juego para practicar comandos

### Cheat Sheets

- [DevHints Linux](https://devhints.io/bash) - Bash scripting
- [ExplainShell](https://explainshell.com/) - Explica cualquier comando Linux

### Videos

- [NetworkChuck - Linux for Hackers](https://www.youtube.com/watch?v=ZtqBQ68cfJc)
- [LearnLinuxTV - Ubuntu Server](https://www.youtube.com/c/LearnLinuxtv)

---

## 🔄 Actualizaciones

Estos recursos se actualizan según:

- Feedback de estudiantes
- Problemas nuevos identificados
- Mejores prácticas emergentes

**Última actualización**: 2025-10-06

---

> **Recuerda**: Estos recursos son **herramientas**, no reemplazan la práctica. Úsalos como referencia mientras trabajas, pero la mejor forma de aprender es haciendo. 🚀
