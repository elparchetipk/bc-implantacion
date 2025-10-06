# 🚀 Quick Start Guide - Bootcamp Implantación

## Configuración Inicial del Sistema de Autocommits

### Opción 1: Instalación Automática (Recomendada) ⚡

```bash
# Ejecutar desde la raíz del proyecto
./scripts/install-cron.sh

# O con intervalo personalizado (en minutos)
./scripts/install-cron.sh 10  # cada 10 minutos
```

El script automáticamente:

- ✅ Verifica configuración de Git
- ✅ Actualiza la ruta del repositorio
- ✅ Instala el cron job
- ✅ Prueba el funcionamiento
- ✅ Muestra resumen de instalación

---

### Opción 2: Instalación Manual 📝

#### 1. Configurar Git (si no está configurado)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

#### 2. Actualizar ruta del repositorio

```bash
# Editar scripts/auto-commit.sh
nano scripts/auto-commit.sh

# Cambiar la línea:
REPO_PATH="/home/epti/Documentos/epti-dev/bc-channel/bc-implantacion"
# Por tu ruta real
```

#### 3. Hacer ejecutable el script

```bash
chmod +x scripts/auto-commit.sh
```

#### 4. Probar manualmente

```bash
./scripts/auto-commit.sh
# Debería crear un commit si hay cambios
```

#### 5. Instalar cron job

```bash
# Editar crontab
crontab -e

# Agregar esta línea (actualizar la ruta):
*/5 * * * * /ruta/completa/scripts/auto-commit.sh >> /ruta/completa/.autocommit.log 2>&1

# Guardar y salir (ESC + :wq en vim, Ctrl+X en nano)
```

#### 6. Verificar instalación

```bash
# Ver cron jobs instalados
crontab -l

# Verificar que crond está activo
systemctl status crond
```

---

## Monitoreo y Verificación 📊

### Ver el log en tiempo real

```bash
tail -f .autocommit.log
```

### Ver últimas 50 líneas del log

```bash
tail -n 50 .autocommit.log
```

### Ver commits recientes

```bash
# Últimos 20 commits
git log --oneline -20

# Solo autocommits
git log --oneline --grep="auto-save"

# Ver commits de hoy
git log --oneline --since="today"
```

### Verificar estado del cron

```bash
# Ver si crond está corriendo
systemctl status crond

# Ver logs del sistema de cron
journalctl -u crond -f
```

---

## Gestión de Commits 🔄

### Limpiar autocommits (Squash)

```bash
# Ver últimos 20 commits
git log --oneline -20

# Hacer rebase interactivo de últimos N commits
git rebase -i HEAD~10

# En el editor:
# - Dejar el primero como "pick"
# - Cambiar los demás de "pick" a "squash" o "s"
# - Guardar y salir
# - Editar el mensaje de commit combinado
```

### Deshacer último autocommit (si es necesario)

```bash
# Deshacer último commit pero mantener cambios
git reset --soft HEAD~1

# Ver estado
git status
```

---

## Desinstalación 🗑️

### Remover cron job

```bash
# Editar crontab
crontab -e

# Comentar o eliminar la línea de auto-commit.sh
# Guardar y salir
```

### O remover todos los cron jobs del usuario

```bash
# ⚠️ CUIDADO: Esto elimina TODOS los cron jobs
crontab -r
```

---

## Troubleshooting 🔧

### El cron no se ejecuta

**Verificar crond:**

```bash
systemctl status crond
sudo systemctl enable --now crond
```

**Verificar sintaxis del cron:**

```bash
crontab -l
# La línea debe verse así:
# */5 * * * * /ruta/completa/script.sh >> /ruta/completa/log 2>&1
```

**Ver errores del sistema:**

```bash
journalctl -u crond -f
```

### El script falla

**Ejecutar con debug:**

```bash
bash -x scripts/auto-commit.sh
```

**Verificar permisos:**

```bash
ls -la scripts/auto-commit.sh
# Debe tener -rwxr-xr-x (ejecutable)
```

**Verificar ruta del repositorio:**

```bash
grep "REPO_PATH=" scripts/auto-commit.sh
# Debe coincidir con tu ruta real
```

### No se hace push al remoto

**Configurar SSH keys (recomendado):**

```bash
# Generar key
ssh-keygen -t ed25519 -C "tu.email@ejemplo.com"

# Ver la key pública
cat ~/.ssh/id_ed25519.pub

# Agregar a GitHub/GitLab en Settings > SSH Keys
```

**O usar HTTPS con credential helper:**

```bash
git config --global credential.helper store
# El siguiente push pedirá credenciales y las guardará
```

### Logs no se crean

**Verificar permisos del directorio:**

```bash
ls -la .autocommit.log
touch .autocommit.log  # Crear si no existe
```

**Verificar redirección en crontab:**

```bash
# Debe terminar con: >> /ruta/.autocommit.log 2>&1
crontab -l
```

---

## Mejores Prácticas 📌

### ✅ DO - Hacer

1. **Revisar autocommits regularmente**

   - Al final del día
   - Antes de hacer merge
   - Squash commits relacionados

2. **Usar branches para features**

   - No trabajar directo en main
   - Crear branch: `git checkout -b feature/nombre`
   - Merge después de limpiar commits

3. **Hacer commits manuales importantes**

   - Los autocommits son backup
   - Hacer commits con mensajes significativos
   - Usar conventional commits manualmente también

4. **Mantener el log limpio**

   - Rotar logs grandes: `echo "" > .autocommit.log`
   - Revisar errores periódicamente
   - Limpiar logs antiguos

5. **Probar cambios importantes**
   - Ejecutar script manualmente después de cambios
   - Verificar que el cron sigue funcionando
   - Revisar logs después de actualizaciones

### ❌ DON'T - Evitar

1. **No confiar solo en autocommits**

   - Siempre hacer commits manuales importantes
   - Los autocommits son complementarios

2. **No ignorar errores en logs**

   - Si falla, investigar por qué
   - No dejar problemas sin resolver

3. **No hacer merge directo de autocommits**

   - Siempre hacer squash primero
   - Limpiar el historial

4. **No exponer credenciales**

   - Nunca commitear .env o keys
   - Verificar .gitignore regularmente

5. **No usar en producción directamente**
   - Solo para desarrollo
   - En producción usar CI/CD apropiado

---

## Comandos Útiles Rápidos 💡

```bash
# Ver estado actual
git status

# Ver últimos 10 commits
git log --oneline -10

# Ver cambios no commiteados
git diff

# Ver log de autocommits
tail -f .autocommit.log

# Ver cron jobs
crontab -l

# Probar script manualmente
./scripts/auto-commit.sh

# Ver commits de hoy con autocommits
git log --since="today" --oneline

# Ver estadísticas de commits
git log --oneline | wc -l

# Squash últimos 5 commits
git rebase -i HEAD~5

# Ver tamaño del log
du -h .autocommit.log
```

---

## Recursos Adicionales 📚

- **Documentación completa**: `scripts/README.md`
- **Setup de cron detallado**: `scripts/cron-setup.md`
- **Ejemplo de código**: `_docs/ejemplo-codigo-comentado.yml`
- **Resumen de tareas**: `_docs/RESUMEN-TAREAS-COMPLETADAS.md`
- **Copilot instructions**: `.github/copilot-instructions.md`

---

## Soporte 🆘

Si encuentras problemas:

1. Revisar logs: `tail -f .autocommit.log`
2. Ejecutar con debug: `bash -x scripts/auto-commit.sh`
3. Verificar configuración: `crontab -l`
4. Consultar troubleshooting arriba
5. Revisar documentación completa en `scripts/`

---

**¡Listo para comenzar! El sistema hará backup automático cada 5 minutos. 🎉**
