# Scripts - Bootcamp Implantación de Software

## 📁 Contenido

Esta carpeta contiene scripts de utilidad para automatizar tareas durante el bootcamp.

### 1. auto-commit.sh

**¿Qué es?** Script de autocommit con formato de Conventional Commits.

**¿Para qué sirve?** Realizar commits automáticos cada 5 minutos para preservar el trabajo en progreso.

**¿Cómo funciona?**

- Detecta cambios en el repositorio
- Clasifica automáticamente el tipo de commit (feat, docs, chore, etc.)
- Determina el scope basado en las carpetas modificadas
- Genera mensaje descriptivo con formato: What? For? Impact?
- Realiza commit y push automático

**Tipos de commit detectados:**

- `feat`: Nuevas funcionalidades en prácticas/teoría
- `docs`: Cambios en documentación y archivos .md
- `style`: Recursos visuales (SVG, imágenes)
- `test`: Archivos de prueba
- `chore`: Configuración, scripts, Docker
- `build`: Dependencias (package.json, requirements.txt)

**Uso:**

```bash
# Ejecutar manualmente
./scripts/auto-commit.sh

# Ver log de ejecuciones
tail -f .autocommit.log
```

### 2. cron-setup.md

**¿Qué es?** Documentación completa para configurar el cron job en Fedora 42.

**¿Para qué sirve?** Guía paso a paso para instalar y configurar el autocommit automático.

**¿Cómo usarlo?**

1. Leer la documentación completa
2. Actualizar REPO_PATH en auto-commit.sh
3. Configurar crontab según instrucciones
4. Monitorear logs para verificar funcionamiento

## 🚀 Instalación Rápida

```bash
# 1. Dar permisos de ejecución
chmod +x scripts/auto-commit.sh

# 2. Editar el script y actualizar REPO_PATH
nano scripts/auto-commit.sh

# 3. Probar el script manualmente
./scripts/auto-commit.sh

# 4. Instalar cron job
crontab -e

# 5. Agregar esta línea:
*/5 * * * * /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/scripts/auto-commit.sh >> /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion/.autocommit.log 2>&1

# 6. Verificar instalación
crontab -l
```

## 📊 Monitoreo

```bash
# Ver últimas ejecuciones
tail -n 50 .autocommit.log

# Monitoreo en tiempo real
tail -f .autocommit.log

# Ver commits recientes
git log --oneline -10

# Ver solo autocommits
git log --oneline --grep="auto-save"
```

## ⚠️ Consideraciones Importantes

### Seguridad

- El script respeta .gitignore y no commitea archivos sensibles
- Se recomienda usar SSH keys para git push automático
- Los logs contienen información de debug pero no datos sensibles

### Mejores Prácticas

- **Revisar commits periódicamente**: Los autocommits son WIP (work in progress)
- **Squash antes de merge**: Combinar autocommits en commits significativos
- **Usar feature branches**: No hacer autocommits directamente en main
- **Hacer commits manuales**: Los autocommits son backup, no reemplazan commits apropiados

### Limpieza de Historial

```bash
# Ver últimos 20 commits
git log --oneline -20

# Squash últimos N commits interactivamente
git rebase -i HEAD~N

# En el editor, cambiar 'pick' a 'squash' o 's' para combinar commits
```

## 🔧 Troubleshooting

### El cron no se ejecuta

```bash
# Verificar que crond está activo
systemctl status crond

# Activar crond si está inactivo
sudo systemctl enable --now crond

# Ver logs del sistema
journalctl -u crond -f
```

### El script falla

```bash
# Verificar permisos
ls -la scripts/auto-commit.sh

# Verificar ruta del repositorio
cd /home/epti/Documentos/epti-dev/bc-channel/bc-implantacion && pwd

# Ejecutar con bash explícito
bash -x scripts/auto-commit.sh
```

### No se hace push

```bash
# Verificar configuración de remote
git remote -v

# Verificar credenciales
git config --list | grep user

# Configurar SSH keys (recomendado)
ssh-keygen -t ed25519 -C "your.email@example.com"
cat ~/.ssh/id_ed25519.pub  # Agregar a GitHub/GitLab
```

## 📝 Formato de Commits

Los autocommits siguen el formato de [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

What: <descripción de qué cambió>
For: <propósito del cambio>
Impact: <impacto del cambio>

Note: Automated commit by cron job
```

**Ejemplo:**

```
feat(week-01): auto-save progress

What: Automated commit of 3 changed file(s)
For: Preserve work-in-progress and maintain backup
Impact: Incremental progress saved at 2025-10-05 20:30

Note: Automated commit by cron job
```

## 🎯 Próximas Mejoras

- [ ] Soporte para múltiples ramas
- [ ] Detección inteligente de cambios significativos vs triviales
- [ ] Integración con notificaciones del sistema
- [ ] Generación de reportes de productividad
- [ ] Backup automático a storage externo

---

**Nota**: Estos scripts son herramientas de apoyo para el bootcamp. Siempre revisa y valida los commits antes de compartirlos o hacer merge a ramas principales.
