# Práctica 2: Despliegue de Proyecto en Servidor Remoto

## 🎯 Objetivos

Al completar esta práctica podrás:

- ✅ Transferir archivos de forma segura a un servidor remoto
- ✅ Configurar variables de entorno para producción
- ✅ Desplegar aplicación con Docker Compose en servidor
- ✅ Configurar acceso público a través de firewall
- ✅ Verificar funcionamiento correcto en producción
- ✅ Documentar proceso de despliegue

## 📋 Pre-requisitos

Antes de comenzar, verifica que tienes:

- [x] Práctica 1 completada (servidor configurado)
- [x] Proyecto de Semana 2 funcionando localmente
- [x] Acceso SSH al servidor
- [x] Docker y Docker Compose instalados en servidor

## ⏱️ Tiempo Estimado

**90 minutos** (distribución):

- 15 min: Preparar proyecto local
- 20 min: Transferir archivos al servidor
- 15 min: Configurar variables de entorno
- 20 min: Desplegar con Docker Compose
- 10 min: Configurar acceso público
- 10 min: Verificación y pruebas

## 🗂️ Estructura de la Práctica

```
1. Preparar proyecto localmente
2. Transferir archivos al servidor
3. Configurar .env para producción
4. Desplegar con Docker Compose
5. Configurar firewall para acceso público
6. Verificar funcionamiento
7. Documentar proceso
```

---

## Paso 1: Preparar Proyecto Local

### 1.1 Verificar Proyecto Funciona

```bash
# ¿Qué? - Ir a directorio del proyecto
cd ~/ruta/proyecto-semana-2

# ¿Qué? - Verificar estructura de archivos
ls -la

# Debes ver:
# - docker-compose.yml
# - .env
# - database/init.sql
# - frontend/ (con index.html)
```

```bash
# ¿Qué? - Probar proyecto localmente
docker compose up -d

# ¿Para qué? - Asegurar que funciona antes de transferir
docker compose ps

# Todos deben estar "Up"

# ¿Qué? - Acceder en navegador
# Abre: http://localhost:3000

# ¿Qué? - Detener después de verificar
docker compose down
```

**✅ Resultado esperado:**

- Proyecto inicia sin errores
- Frontend accesible
- Base de datos funcional

### 1.2 Limpiar Archivos Innecesarios

```bash
# ¿Qué? - Ver tamaño del proyecto
du -sh .

# ¿Para qué? - Saber cuánto transferir

# ¿Qué? - Eliminar archivos temporales (si existen)
rm -rf node_modules/
rm -rf __pycache__/
rm -f *.log
rm -f .DS_Store

# ¿Para qué? - Reducir tiempo de transferencia
```

### 1.3 Verificar docker-compose.yml

```bash
# ¿Qué? - Ver contenido del archivo
cat docker-compose.yml
```

**Verifica que tenga:**

```yaml
services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - '${POSTGRES_PORT}:5432'

  adminer:
    image: adminer:latest
    ports:
      - '${ADMINER_PORT}:8080'
    depends_on:
      - postgres

  frontend:
    image: nginx:alpine
    volumes:
      - ./frontend:/usr/share/nginx/html
    ports:
      - '${FRONTEND_PORT}:80'
    depends_on:
      - postgres

volumes:
  postgres_data:
```

**✅ Checklist:**

- [ ] Usa variables de entorno (${VARIABLE})
- [ ] Define volumen para persistencia (postgres_data)
- [ ] Puertos mapeados correctamente
- [ ] depends_on configurado

---

## Paso 2: Transferir Archivos al Servidor

### Opción A: Usando SCP (Simple)

**2.1 Comprimir proyecto (opcional pero recomendado):**

```bash
# ¿Qué? - Crear archivo comprimido del proyecto
# ¿Para qué? - Transferir más rápido (un solo archivo)

# DESDE TU MÁQUINA LOCAL:
cd ~/ruta/
tar -czf proyecto.tar.gz proyecto-semana-2/

# Verificar tamaño
ls -lh proyecto.tar.gz
```

**2.2 Transferir con SCP:**

```bash
# ¿Qué? - Copiar archivo al servidor
# Sintaxis: scp archivo usuario@servidor:destino

# DESDE TU MÁQUINA LOCAL:
scp proyecto.tar.gz usuario@IP_SERVIDOR:/home/usuario/

# Ejemplo real:
# scp proyecto.tar.gz ubuntu@34.123.45.67:/home/ubuntu/

# Esperarás ver:
# proyecto.tar.gz    100%   15MB   2.5MB/s   00:06
```

**2.3 Descomprimir en servidor:**

```bash
# ¿Qué? - Conectar al servidor
ssh usuario@IP_SERVIDOR

# YA EN EL SERVIDOR:
ls -lh proyecto.tar.gz

# ¿Qué? - Descomprimir archivo
tar -xzf proyecto.tar.gz

# ¿Qué? - Ver contenido
ls -la proyecto-semana-2/

# ¿Qué? - Renombrar carpeta (opcional)
mv proyecto-semana-2 proyecto

# ¿Qué? - Limpiar archivo comprimido
rm proyecto.tar.gz
```

### Opción B: Usando RSYNC (Recomendado para actualizaciones)

**2.1 Primera transferencia (todo):**

```bash
# ¿Qué? - Sincronizar carpeta local con servidor
# ¿Para qué? - Transferir todo el proyecto

# DESDE TU MÁQUINA LOCAL:
rsync -avz --progress proyecto-semana-2/ usuario@IP_SERVIDOR:/home/usuario/proyecto/

# Banderas:
# -a = modo archivo (preserva permisos)
# -v = verbose (muestra progreso)
# -z = comprime durante transferencia
# --progress = barra de progreso
```

**Verás salida como:**

```
sending incremental file list
./
docker-compose.yml
      1,234 100%    0.00kB/s    0:00:00
.env
        123 100%    0.00kB/s    0:00:00
database/
database/init.sql
      5,678 100%    0.00kB/s    0:00:00
...
sent 123.45K bytes  received 456 bytes  12.34K bytes/sec
total size is 789.01K  speedup is 6.37
```

**2.2 Actualizaciones futuras (solo cambios):**

```bash
# ¿Qué? - Sincronizar solo archivos modificados
# ¿Para qué? - Más rápido en actualizaciones

# DESDE TU MÁQUINA LOCAL:
rsync -avz --progress --delete proyecto-semana-2/ usuario@IP_SERVIDOR:/home/usuario/proyecto/

# --delete = elimina archivos en destino que no existen en origen
```

### Opción C: Usando Git (Mejor para desarrollo)

**2.1 Hacer push desde local:**

```bash
# DESDE TU MÁQUINA LOCAL:
cd proyecto-semana-2

# Verificar que .env NO esté en Git
cat .gitignore
# Debe contener: .env

git add .
git commit -m "Preparar para deploy"
git push origin main
```

**2.2 Clonar en servidor:**

```bash
# CONECTAR AL SERVIDOR:
ssh usuario@IP_SERVIDOR

# EN EL SERVIDOR:
git clone https://github.com/tu-usuario/tu-repo.git proyecto
cd proyecto
```

**⚠️ Importante con Git:**

- NO incluir `.env` en repositorio
- Crear `.env` manualmente en servidor
- Usar archivo `.env.example` como referencia

### ✅ Verificación de Transferencia

```bash
# EN EL SERVIDOR:
cd proyecto

# Verificar estructura completa
tree -L 2
# O si no tienes tree:
find . -maxdepth 2 -type f

# Verificar archivos críticos
ls -la docker-compose.yml
ls -la .env
ls -la database/init.sql
ls -la frontend/index.html

# Verificar contenido
cat docker-compose.yml | head -20
```

**✅ Resultado esperado:**

- Todos los archivos presentes
- Estructura de carpetas correcta
- docker-compose.yml completo

---

## Paso 3: Configurar Variables de Entorno

### 3.1 Revisar .env Actual

```bash
# EN EL SERVIDOR:
cd proyecto

# ¿Qué? - Ver contenido de .env
cat .env
```

Verás algo como:

```env
# PostgreSQL
POSTGRES_USER=usuario_db
POSTGRES_PASSWORD=contraseña123
POSTGRES_DB=mi_base_datos
POSTGRES_PORT=5432

# Adminer
ADMINER_PORT=8080

# Frontend
FRONTEND_PORT=3000
```

### 3.2 Ajustar para Producción

```bash
# ¿Qué? - Editar archivo .env
nano .env
```

**Cambios importantes:**

#### A. Contraseñas Seguras

```env
# ❌ MAL (contraseña débil)
POSTGRES_PASSWORD=123456

# ✅ BIEN (contraseña fuerte)
POSTGRES_PASSWORD=Prod#2025$Db!SecurePass
```

**Generar contraseña segura:**

```bash
# En el servidor
openssl rand -base64 32
```

#### B. Puertos (verificar disponibilidad)

```bash
# ¿Qué? - Ver puertos en uso
ss -tulpn | grep LISTEN

# Si puerto 3000 está ocupado, cambiar:
# FRONTEND_PORT=3001
# O usar 8081, 8082, etc.
```

#### C. Nombres de Base de Datos

```env
# Usar nombre descriptivo + tu usuario
POSTGRES_DB=restaurante_jgarcia
# O tu dominio asignado
```

**Archivo .env completo para producción:**

```env
# PostgreSQL
POSTGRES_USER=admin_prod
POSTGRES_PASSWORD=Prod#2025$Db!SecurePass
POSTGRES_DB=proyecto_produccion
POSTGRES_PORT=5433

# Adminer
ADMINER_PORT=8080

# Frontend
FRONTEND_PORT=3000
```

**Guardar y salir:**

- `Ctrl + O` (guardar)
- `Enter` (confirmar)
- `Ctrl + X` (salir)

### 3.3 Verificar Sintaxis

```bash
# ¿Qué? - Validar configuración de Docker Compose
docker compose config

# ¿Para qué? - Detectar errores antes de desplegar

# Si hay errores, aparecerán aquí
# Si está bien, verás el archivo expandido
```

**✅ Resultado esperado:**

- Sin errores de sintaxis
- Variables correctamente sustituidas

---

## Paso 4: Desplegar con Docker Compose

### 4.1 Descargar Imágenes

```bash
# ¿Qué? - Descargar imágenes de Docker Hub
# ¿Para qué? - Evitar timeout durante despliegue

docker compose pull

# Verás:
# [+] Pulling 16/16
#  ✔ postgres Pulled
#  ✔ adminer Pulled
#  ✔ nginx Pulled
```

### 4.2 Iniciar Stack

```bash
# ¿Qué? - Levantar todos los servicios
docker compose up -d

# Banderas:
# -d = modo detached (segundo plano)

# Salida esperada:
# [+] Running 4/4
#  ✔ Network proyecto_default       Created
#  ✔ Container proyecto-postgres-1  Started
#  ✔ Container proyecto-adminer-1   Started
#  ✔ Container proyecto-frontend-1  Started
```

### 4.3 Verificar Estado

```bash
# ¿Qué? - Ver contenedores corriendo
docker compose ps

# Esperado:
# NAME                   STATUS    PORTS
# proyecto-postgres-1    Up        0.0.0.0:5433->5432/tcp
# proyecto-adminer-1     Up        0.0.0.0:8080->8080/tcp
# proyecto-frontend-1    Up        0.0.0.0:3000->80/tcp
```

**✅ Todos deben estar "Up"**

### 4.4 Ver Logs

```bash
# ¿Qué? - Ver logs de todos los servicios
docker compose logs

# ¿Qué? - Seguir logs en tiempo real
docker compose logs -f

# (Ctrl+C para salir)

# ¿Qué? - Ver solo logs de PostgreSQL
docker compose logs postgres

# Buscar línea:
# "database system is ready to accept connections"
```

**✅ Sin errores críticos en logs**

---

## Paso 5: Configurar Firewall para Acceso Público

### 5.1 Verificar Estado del Firewall

```bash
# ¿Qué? - Ver reglas actuales
sudo ufw status numbered

# Verás:
# Status: active
# [1] 22/tcp    ALLOW IN    Anywhere
# [2] 80/tcp    ALLOW IN    Anywhere
# [3] 443/tcp   ALLOW IN    Anywhere
```

### 5.2 Abrir Puertos de Aplicación

```bash
# ¿Qué? - Permitir puerto del frontend
sudo ufw allow 3000/tcp

# ¿Para qué? - Acceso público a la aplicación

# ¿Qué? - Permitir puerto de Adminer
sudo ufw allow 8080/tcp

# Salida:
# Rule added
# Rule added (v6)
```

### 5.3 Verificar Reglas

```bash
# ¿Qué? - Ver reglas actualizadas
sudo ufw status numbered

# Ahora verás:
# [4] 3000/tcp  ALLOW IN    Anywhere
# [5] 8080/tcp  ALLOW IN    Anywhere
```

### 5.4 Verificar Puertos Escuchando

```bash
# ¿Qué? - Ver puertos en LISTEN
ss -tulpn | grep LISTEN

# Debes ver:
# tcp   LISTEN   0.0.0.0:3000
# tcp   LISTEN   0.0.0.0:8080
# tcp   LISTEN   0.0.0.0:5433
```

### 5.5 Configurar Firewall de GCP (Si Aplica)

**Si usas Google Cloud:**

1. Ve a: **VPC Network** → **Firewall**
2. Click **"CREATE FIREWALL RULE"**
3. Configuración:
   ```
   Name: allow-app-ports
   Direction: Ingress
   Action on match: Allow
   Targets: All instances in the network
   Source IP ranges: 0.0.0.0/0
   Protocols and ports: tcp:3000,8080
   ```
4. Click **"CREATE"**

**O desde terminal local:**

```bash
# DESDE TU MÁQUINA LOCAL (no en el servidor):
gcloud compute firewall-rules create allow-app-ports \
    --allow tcp:3000,tcp:8080 \
    --source-ranges 0.0.0.0/0 \
    --description "Allow application and Adminer ports"
```

---

## Paso 6: Verificación de Funcionamiento

### 6.1 Verificación Local (Servidor)

```bash
# EN EL SERVIDOR:

# ¿Qué? - Probar frontend localmente
curl http://localhost:3000

# Debe devolver HTML (no error)

# ¿Qué? - Probar Adminer localmente
curl -I http://localhost:8080

# Debe devolver: HTTP/1.1 200 OK
```

### 6.2 Verificación Remota (Navegador)

**Abre navegador en tu máquina local:**

#### A. Frontend

```
http://IP_EXTERNA:3000
```

**Ejemplo:**

```
http://34.123.45.67:3000
```

**✅ Debe mostrar:**

- Tu página HTML
- Sin errores 404
- Contenido cargando correctamente

#### B. Adminer

```
http://IP_EXTERNA:8080
```

**✅ Debe mostrar:**

- Pantalla de login de Adminer
- Sin errores de conexión

**Toma screenshot de ambas URL funcionando**

### 6.3 Verificación de Base de Datos

**En Adminer (navegador):**

1. **System**: PostgreSQL
2. **Server**: `postgres` (nombre del contenedor)
3. **Username**: (tu POSTGRES_USER del .env)
4. **Password**: (tu POSTGRES_PASSWORD del .env)
5. **Database**: (tu POSTGRES_DB del .env)
6. Click **"Login"**

**✅ Resultado esperado:**

- Login exitoso
- Ver listado de tablas
- Poder ejecutar queries

**Probar query:**

```sql
SELECT * FROM tu_tabla LIMIT 5;
```

**Toma screenshot del resultado**

### 6.4 Verificación de Persistencia

```bash
# EN EL SERVIDOR:

# 1. Insertar dato de prueba (en Adminer)
# INSERT INTO tabla VALUES (...);

# 2. Reiniciar contenedor de PostgreSQL
docker compose restart postgres

# 3. Esperar 10 segundos
sleep 10

# 4. Verificar dato sigue ahí (Adminer)
# SELECT * FROM tabla;
```

**✅ Dato debe seguir presente (volumen funciona)**

### 6.5 Verificación de Logs Sin Errores

```bash
# EN EL SERVIDOR:

# ¿Qué? - Ver últimas 50 líneas de logs
docker compose logs --tail=50

# Buscar:
# ✅ "database system is ready"
# ✅ "server started"
# ❌ NO debe haber "ERROR", "FATAL", "panic"
```

---

## Paso 7: Documentación del Proceso

### 7.1 Crear Archivo DEPLOY.md

```bash
# EN EL SERVIDOR:
cd proyecto
nano DEPLOY.md
```

**Contenido mínimo:**

````markdown
# Información de Despliegue

## Servidor

- **IP Pública**: 34.123.45.67
- **Proveedor**: Google Cloud Platform
- **Sistema Operativo**: Ubuntu 22.04 LTS
- **Usuario SSH**: ubuntu

## URLs de Acceso

- **Frontend**: http://34.123.45.67:3000
- **Adminer**: http://34.123.45.67:8080

## Puertos Configurados (UFW)

- 22/tcp (SSH)
- 80/tcp (HTTP)
- 443/tcp (HTTPS)
- 3000/tcp (Frontend)
- 8080/tcp (Adminer)

## Variables de Entorno

Ver archivo `.env` (no incluido en Git)

## Comandos Útiles

### Ver estado

```bash
docker compose ps
docker compose logs -f
```
````

### Reiniciar servicios

```bash
docker compose restart
docker compose restart postgres
```

### Detener

```bash
docker compose down
```

### Actualizar código

```bash
# Desde máquina local:
rsync -avz proyecto/ usuario@34.123.45.67:/home/usuario/proyecto/

# En servidor:
cd proyecto
docker compose up -d --build
```

## Problemas Encontrados

### Puerto 80 requería permisos root

**Solución:** Cambié puerto a 3000 en .env

### PostgreSQL no iniciaba

**Solución:** Puerto 5432 ocupado, cambié a 5433

## Fecha de Despliegue

2025-10-06

## Desplegado por

[Tu Nombre]

````

**Guardar:** `Ctrl+O`, `Enter`, `Ctrl+X`

### 7.2 Tomar Screenshots

**Capturas necesarias:**

1. **Terminal con docker compose ps:**
   ```bash
   docker compose ps
````

- Mostrar todos los contenedores "Up"

2. **Frontend en navegador:**

   - URL visible: `http://IP:3000`
   - Contenido cargando

3. **Adminer con login exitoso:**

   - Pantalla de tablas
   - Query ejecutado

4. **Firewall configurado:**
   ```bash
   sudo ufw status numbered
   ```

### 7.3 Crear README en Servidor

```bash
# EN EL SERVIDOR:
cd proyecto
nano README-SERVIDOR.md
```

**Contenido:**

````markdown
# Proyecto Desplegado en Servidor

## Acceso Rápido

**SSH:**

```bash
ssh usuario@34.123.45.67
cd proyecto
```
````

**Ver estado:**

```bash
docker compose ps
```

**Ver logs:**

```bash
docker compose logs -f
```

## Mantenimiento

**Reiniciar todo:**

```bash
docker compose restart
```

**Backup de BD:**

```bash
docker compose exec postgres pg_dump -U admin_prod proyecto_produccion > backup_$(date +%Y%m%d).sql
```

**Restaurar BD:**

```bash
docker compose exec -T postgres psql -U admin_prod proyecto_produccion < backup_20251006.sql
```

## Monitoreo

**Uso de recursos:**

```bash
docker stats
htop
```

**Espacio en disco:**

```bash
df -h
du -sh proyecto/
```

**Logs del sistema:**

```bash
journalctl -u docker -f
```

```

---

## 📦 Entregables de la Práctica

### Archivos

- [ ] **DEPLOY.md** (en servidor)
- [ ] **README-SERVIDOR.md** (en servidor)
- [ ] **Screenshots** (4 mínimo):
  - docker compose ps
  - Frontend funcionando
  - Adminer con tablas
  - UFW configurado

### Documentación Adicional

- [ ] Archivo local con datos de acceso:
```

servidor-acceso.txt:
IP: 34.123.45.67
Usuario: ubuntu
Comando SSH: ssh ubuntu@34.123.45.67
Frontend: http://34.123.45.67:3000
Adminer: http://34.123.45.67:8080

````

- [ ] Problemas encontrados y soluciones (en DEPLOY.md)

### Verificación Final

- [ ] Aplicación accesible desde cualquier navegador
- [ ] Base de datos funcional (Adminer conecta)
- [ ] Datos persisten tras reinicio
- [ ] Logs sin errores críticos
- [ ] Firewall configurado correctamente
- [ ] Documentación completa

---

## 🔧 Mantenimiento Post-Despliegue

### Actualizar Código

**Método 1: RSYNC**
```bash
# Desde máquina local:
rsync -avz --progress proyecto/ usuario@servidor:/home/usuario/proyecto/

# En servidor:
ssh usuario@servidor
cd proyecto
docker compose up -d --build
````

**Método 2: Git**

```bash
# En servidor:
ssh usuario@servidor
cd proyecto
git pull origin main
docker compose up -d --build
```

### Ver Uso de Recursos

```bash
# CPU, RAM, I/O de contenedores
docker stats

# CPU, RAM del sistema
htop

# Espacio en disco
df -h
du -sh /home/usuario/proyecto
```

### Backup de Base de Datos

```bash
# Crear backup
docker compose exec postgres pg_dump -U admin_prod proyecto_produccion > backup_$(date +%Y%m%d).sql

# Verificar backup
ls -lh backup_*.sql

# Comprimir (opcional)
gzip backup_20251006.sql
```

### Limpiar Docker

```bash
# Eliminar contenedores detenidos
docker container prune

# Eliminar imágenes no usadas
docker image prune

# Eliminar volúmenes huérfanos
docker volume prune

# Limpiar todo (⚠️ cuidado)
docker system prune -a
```

---

## 🚨 Troubleshooting

### Problema 1: No puedo acceder desde navegador

**Síntomas:**

- `http://IP:3000` no carga
- Error: "Connection refused" o timeout

**Verificar:**

```bash
# 1. Contenedor corriendo
docker compose ps

# 2. Puerto escuchando
ss -tulpn | grep 3000

# 3. Firewall permite tráfico
sudo ufw status | grep 3000

# 4. Regla en GCP (si aplica)
gcloud compute firewall-rules list | grep 3000
```

**Soluciones:**

1. **Contenedor no está corriendo:**

   ```bash
   docker compose up -d
   ```

2. **Firewall bloqueando:**

   ```bash
   sudo ufw allow 3000/tcp
   ```

3. **Regla GCP faltante:**
   - Crear regla en consola GCP

### Problema 2: PostgreSQL no inicia

**Síntomas:**

- `docker compose ps` muestra postgres "Restarting"
- Logs muestran error de inicialización

**Ver logs:**

```bash
docker compose logs postgres
```

**Causas comunes:**

1. **Puerto ocupado:**

   ```bash
   ss -tulpn | grep 5432
   # Cambiar POSTGRES_PORT en .env
   ```

2. **Permisos de volumen:**

   ```bash
   docker compose down -v  # Eliminar volumen
   docker compose up -d     # Recrear
   ```

3. **Sintaxis en init.sql:**
   ```bash
   cat database/init.sql
   # Verificar SQL válido
   ```

### Problema 3: "Cannot connect to database" en Adminer

**Verificar:**

1. **Nombre del servidor:**

   - Debe ser: `postgres` (nombre del contenedor)
   - NO: `localhost` o `127.0.0.1`

2. **Credenciales:**

   ```bash
   cat .env
   # Verificar POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
   ```

3. **Contenedores en misma red:**
   ```bash
   docker compose ps
   # Ambos deben estar "Up"
   ```

### Problema 4: Cambios no se reflejan

**Si modificas código y no se ve:**

```bash
# 1. Reconstruir imágenes
docker compose up -d --build

# 2. Forzar recreación
docker compose up -d --force-recreate

# 3. Limpiar cache
docker compose down
docker compose build --no-cache
docker compose up -d
```

**Ver más problemas:** `../3-recursos/troubleshooting-linux.md`

---

## ✅ Checklist Final

Antes de considerar completada la práctica:

### Funcional

- [ ] Puedo acceder al frontend desde cualquier navegador
- [ ] Adminer conecta a PostgreSQL exitosamente
- [ ] Puedo ejecutar queries en Adminer
- [ ] Datos persisten después de reiniciar (docker compose restart)
- [ ] Logs no muestran errores críticos

### Seguridad

- [ ] Firewall UFW activo (`sudo ufw status`)
- [ ] Solo puertos necesarios abiertos (22, 80, 443, 3000, 8080)
- [ ] Contraseña de PostgreSQL es segura (no "123456")
- [ ] Puerto 5432 NO expuesto públicamente

### Documentación

- [ ] DEPLOY.md creado con información completa
- [ ] Screenshots tomados (mínimo 4)
- [ ] Archivo local con datos de acceso
- [ ] Problemas y soluciones documentados

### Conocimiento

- [ ] Entiendo cómo transferir archivos (scp/rsync)
- [ ] Entiendo cómo configurar variables (.env)
- [ ] Entiendo cómo abrir puertos (ufw)
- [ ] Sé cómo ver logs (docker compose logs)
- [ ] Sé cómo reiniciar servicios (docker compose restart)

---

## 🎯 Próximos Pasos

✅ **¡Felicitaciones! Tienes tu primera aplicación en producción.**

**Ahora puedes:**

1. **Compartir tu aplicación:**

   - Envía la URL: `http://TU_IP:3000`
   - Otros pueden acceder desde sus navegadores

2. **Seguir mejorando:**

   - Agregar más funcionalidad
   - Mejorar diseño del frontend
   - Optimizar queries de base de datos

3. **Aprender más:**
   - Configurar dominio propio (no solo IP)
   - Agregar HTTPS (certificado SSL)
   - Implementar CI/CD (deploy automático)

---

## 📝 Notas Adicionales

### Buenas Prácticas

1. **Siempre probar localmente primero**

   - Si no funciona local, no funcionará en servidor

2. **Hacer backup antes de cambios grandes**

   ```bash
   docker compose exec postgres pg_dump ... > backup.sql
   ```

3. **Documentar TODO lo que hagas**

   - Cambios en configuración
   - Problemas encontrados
   - Comandos útiles

4. **Monitorear recursos**
   - Revisar `docker stats` regularmente
   - Verificar espacio en disco (`df -h`)

### Recursos de Consulta

- **Cheatsheet de comandos**: `../3-recursos/cheatsheet-linux-server.md`
- **Troubleshooting**: `../3-recursos/troubleshooting-linux.md`
- **Template de deploy**: `../3-recursos/template-deploy.md`

### Comandos Útiles de Referencia Rápida

```bash
# Ver estado
docker compose ps

# Ver logs
docker compose logs -f

# Reiniciar
docker compose restart

# Detener
docker compose down

# Iniciar
docker compose up -d

# Reconstruir
docker compose up -d --build

# Ver recursos
docker stats
htop
df -h

# Backup BD
docker compose exec postgres pg_dump -U user db > backup.sql
```

---

**¡Éxito con tu despliegue!** 🚀

Si encuentras problemas, consulta la [guía de troubleshooting](../3-recursos/troubleshooting-linux.md).
