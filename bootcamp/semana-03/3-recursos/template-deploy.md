# Template: Checklist de Despliegue

> **Propósito**: Lista de verificación y comandos para desplegar aplicaciones en servidor Linux de forma ordenada y sin olvidar pasos críticos.

## 📋 Pre-Despliegue

### Verificaciones Locales

- [ ] **Proyecto funciona localmente**

  ```bash
  cd /ruta/proyecto
  docker compose up -d
  docker compose ps  # Todos deben estar "Up"
  # Acceder: http://localhost:PUERTO
  docker compose down
  ```

- [ ] **Archivos necesarios presentes**

  - [ ] `docker-compose.yml`
  - [ ] `.env` (con variables correctas)
  - [ ] `database/init.sql` (si aplica)
  - [ ] `frontend/` (HTML/CSS/JS)
  - [ ] `README.md` (documentación)

- [ ] **Sin archivos innecesarios**
  - [ ] Sin `node_modules/`
  - [ ] Sin `.git/` (o incluir en .dockerignore)
  - [ ] Sin archivos temporales (`.log`, `__pycache__`, etc.)

---

## 🚀 Despliegue

### 1. Preparar Servidor

- [ ] **Servidor accesible**

  ```bash
  # Probar conexión SSH
  ssh usuario@ip-servidor

  # Si funciona, salir
  exit
  ```

- [ ] **Recursos suficientes**

  ```bash
  # Conectar al servidor
  ssh usuario@ip-servidor

  # Verificar RAM disponible
  free -h
  # Debe tener al menos 500 MB libres

  # Verificar espacio en disco
  df -h
  # Debe tener al menos 5 GB libres

  # Verificar Docker funciona
  docker ps
  ```

### 2. Transferir Archivos

**Opción A: SCP**

```bash
# DESDE TU MÁQUINA LOCAL (no en el servidor):

# Comprimir proyecto (opcional, más rápido)
tar -czf proyecto.tar.gz proyecto/

# Transferir al servidor
scp proyecto.tar.gz usuario@ip-servidor:/home/usuario/

# Conectar al servidor
ssh usuario@ip-servidor

# Descomprimir
tar -xzf proyecto.tar.gz
cd proyecto/
```

**Opción B: RSYNC (Recomendado)**

```bash
# DESDE TU MÁQUINA LOCAL:

# Primera vez (todo)
rsync -avz --progress proyecto/ usuario@ip-servidor:/home/usuario/proyecto/

# Actualizaciones (solo cambios)
rsync -avz --progress --delete proyecto/ usuario@ip-servidor:/home/usuario/proyecto/
```

**Opción C: Git**

```bash
# DESDE TU MÁQUINA LOCAL:
git push

# EN EL SERVIDOR:
ssh usuario@ip-servidor
git clone https://github.com/tu-usuario/repo.git proyecto
cd proyecto/
```

- [ ] **Archivos transferidos correctamente**
  ```bash
  # EN EL SERVIDOR:
  ls -la proyecto/
  cat proyecto/docker-compose.yml  # Verificar contenido
  ```

### 3. Configurar Variables

- [ ] **Editar .env para producción**

  ```bash
  # EN EL SERVIDOR:
  cd proyecto/
  nano .env

  # Verificar/Cambiar:
  # - Contraseñas (usar seguras)
  # - Puertos (si hay conflictos)
  # - Nombres de BD
  # - URLs (usar IP del servidor, no localhost)
  ```

- [ ] **Variables críticas configuradas**
  - [ ] `POSTGRES_PASSWORD` (segura)
  - [ ] `POSTGRES_USER`
  - [ ] `POSTGRES_DB`
  - [ ] Puertos no conflictivos

### 4. Configurar Firewall

- [ ] **Puertos necesarios abiertos en UFW**

  ```bash
  # EN EL SERVIDOR:

  # Ver estado actual
  sudo ufw status

  # Abrir puerto de aplicación (ejemplo: 3000)
  sudo ufw allow 3000/tcp

  # Abrir Adminer (ejemplo: 8080)
  sudo ufw allow 8080/tcp

  # Verificar
  sudo ufw status numbered
  ```

- [ ] **Puertos abiertos en GCP (si aplica)**
  - Ve a: VPC Network → Firewall → Create Firewall Rule
  - Name: `allow-app-port-3000`
  - Source IP: `0.0.0.0/0`
  - Protocols: `tcp:3000`

### 5. Desplegar Stack

- [ ] **Descargar imágenes**

  ```bash
  # EN EL SERVIDOR:
  cd proyecto/
  docker compose pull
  ```

- [ ] **Verificar configuración**

  ```bash
  # Validar sintaxis YAML
  docker compose config

  # Si hay errores, corregir en docker-compose.yml
  ```

- [ ] **Levantar servicios**

  ```bash
  # Iniciar en segundo plano
  docker compose up -d
  ```

- [ ] **Verificar estado**

  ```bash
  # Ver servicios corriendo
  docker compose ps
  # Todos deben estar "Up"

  # Ver logs
  docker compose logs

  # Seguir logs en tiempo real (Ctrl+C para salir)
  docker compose logs -f
  ```

---

## ✅ Verificación Post-Despliegue

### 1. Verificación Local (Servidor)

- [ ] **Contenedores corriendo**

  ```bash
  docker compose ps
  # STATUS debe ser "Up" para todos
  ```

- [ ] **Puertos escuchando**

  ```bash
  ss -tulpn | grep LISTEN

  # Debes ver tus puertos:
  # 0.0.0.0:3000
  # 0.0.0.0:8080
  # 0.0.0.0:5432 (si expones PostgreSQL)
  ```

- [ ] **Aplicación responde localmente**

  ```bash
  curl http://localhost:3000
  # Debe devolver HTML (no error)

  curl -I http://localhost:8080
  # HTTP/1.1 200 OK
  ```

### 2. Verificación Remota (Tu Máquina)

- [ ] **Aplicación accesible desde navegador**

  - Abre: `http://IP_EXTERNA:3000`
  - Debe cargar tu aplicación

- [ ] **Adminer accesible**
  - Abre: `http://IP_EXTERNA:8080`
  - Debe mostrar login de Adminer

### 3. Verificación de Base de Datos

- [ ] **Conectar a Adminer**

  - System: PostgreSQL
  - Server: `postgres` (nombre del contenedor)
  - Username: (tu .env)
  - Password: (tu .env)
  - Database: (tu .env)

- [ ] **Tablas creadas correctamente**
  - Navega a: SQL command
  - Ejecuta: `SELECT * FROM nombre_tabla LIMIT 5;`
  - Debe mostrar datos

### 4. Verificación de Persistencia

- [ ] **Datos persisten tras reinicio**

  ```bash
  # EN EL SERVIDOR:

  # 1. Insertar dato de prueba en Adminer
  # INSERT INTO tabla VALUES (...)

  # 2. Reiniciar contenedor PostgreSQL
  docker compose restart postgres

  # 3. Esperar 10 segundos
  sleep 10

  # 4. Verificar dato sigue ahí (Adminer)
  # SELECT * FROM tabla
  ```

### 5. Verificación de Logs

- [ ] **Sin errores críticos en logs**

  ```bash
  docker compose logs --tail=50

  # Buscar:
  # ✅ "database system is ready to accept connections"
  # ✅ "server started"
  # ❌ "ERROR", "FATAL", "panic"
  ```

---

## 📝 Documentación

### Crear archivo DEPLOY.md

```bash
# EN EL SERVIDOR:
cd proyecto/
nano DEPLOY.md
```

**Contenido mínimo:**

````markdown
# Despliegue en Producción

## Información del Servidor

- **IP Pública**: 34.123.45.67
- **Proveedor**: Google Cloud Platform
- **Sistema Operativo**: Ubuntu 22.04 LTS
- **Usuario SSH**: ubuntu

## URLs de Acceso

- **Aplicación**: http://34.123.45.67:3000
- **Adminer**: http://34.123.45.67:8080

## Puertos Abiertos (UFW)

- 22/tcp (SSH)
- 80/tcp (HTTP)
- 443/tcp (HTTPS)
- 3000/tcp (Aplicación)
- 8080/tcp (Adminer)

## Comandos Útiles

### Ver estado

```bash
docker compose ps
docker compose logs -f
```
````

### Reiniciar

```bash
docker compose restart
```

### Actualizar

```bash
# En máquina local:
rsync -avz proyecto/ ubuntu@34.123.45.67:/home/ubuntu/proyecto/

# En servidor:
cd proyecto
docker compose up -d --build
```

## Problemas Encontrados

- [Fecha] Puerto 80 requiere root → Solución: Cambié a 3000
- [Fecha] PostgreSQL no iniciaba → Solución: Cambié puerto a 5433

## Fecha de Despliegue

2025-10-06

## Desplegado por

[Tu Nombre]

````

### Tomar Screenshots

- [ ] **Captura de aplicación funcionando**
  - URL visible en navegador
  - Contenido cargando correctamente

- [ ] **Captura de Adminer con login exitoso**
  - Tablas visibles
  - Datos presentes

- [ ] **Captura de terminal**
  - `docker compose ps` mostrando todos "Up"

---

## 🔧 Mantenimiento

### Comandos Post-Despliegue

**Ver uso de recursos:**
```bash
docker stats
htop
````

**Ver logs:**

```bash
docker compose logs -f
docker compose logs --tail=100 postgres
```

**Reiniciar servicios:**

```bash
docker compose restart
docker compose restart postgres
```

**Detener stack:**

```bash
docker compose down
```

**Actualizar código:**

```bash
# Desde máquina local:
rsync -avz proyecto/ usuario@servidor:/home/usuario/proyecto/

# En servidor:
cd proyecto
docker compose up -d --build
```

**Backup de base de datos:**

```bash
docker compose exec postgres pg_dump -U usuario base_datos > backup_$(date +%Y%m%d).sql
```

---

## ⚠️ Checklist de Seguridad

- [ ] **Contraseñas seguras** (no usar "123456" o "password")
- [ ] **Puerto PostgreSQL NO expuesto** (eliminar de ports: si no es necesario)
- [ ] **Firewall activo** (`sudo ufw status` → active)
- [ ] **Solo puertos necesarios abiertos**
- [ ] **SSH con keys** (no solo contraseña)
- [ ] **Usuario no-root** (no usar root directamente)
- [ ] **.env NO en Git** (agregar a .gitignore)

---

## 🚨 Si Algo Sale Mal

### Troubleshooting Rápido

1. **Ver logs primero**

   ```bash
   docker compose logs
   ```

2. **Verificar puertos**

   ```bash
   sudo ufw status
   ss -tulpn | grep LISTEN
   ```

3. **Verificar recursos**

   ```bash
   free -h
   df -h
   ```

4. **Reiniciar servicios**

   ```bash
   docker compose restart
   ```

5. **Consultar troubleshooting completo**
   - Ver: `../3-recursos/troubleshooting-linux.md`

---

## ✅ Checklist Final

Antes de considerar completado el despliegue:

### Funcionalidad

- [ ] Aplicación accesible desde internet
- [ ] Base de datos funcional
- [ ] Datos persisten tras reinicio
- [ ] Sin errores en logs

### Seguridad

- [ ] Firewall configurado
- [ ] Contraseñas seguras
- [ ] Solo puertos necesarios abiertos

### Documentación

- [ ] DEPLOY.md creado
- [ ] Screenshots tomados
- [ ] README.md actualizado
- [ ] Problemas y soluciones documentados

### Operación

- [ ] Conoces comandos de mantenimiento
- [ ] Sabes cómo actualizar
- [ ] Sabes cómo hacer backup
- [ ] Sabes cómo detener/iniciar

---

## 📊 Métricas de Éxito

| Métrica              | Objetivo   | Cómo Verificar              |
| -------------------- | ---------- | --------------------------- |
| Tiempo de despliegue | < 30 min   | Cronometrar proceso         |
| Uptime               | > 99%      | Monitorear con `uptime`     |
| Errores en logs      | 0 críticos | `docker compose logs`       |
| Tiempo de respuesta  | < 2 seg    | `curl -w "%{time_total}\n"` |
| Satisfacción         | Alta       | Funciona sin problemas      |

---

> **Tip:** Guarda este checklist y úsalo en cada despliegue. Con la práctica, el proceso será cada vez más rápido y natural. 🚀
