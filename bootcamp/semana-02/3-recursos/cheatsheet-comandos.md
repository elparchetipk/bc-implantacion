# 📋 Cheatsheet - Comandos Esenciales Docker Compose

> **Propósito**: Referencia rápida de 1 página con los comandos más usados  
> **Audiencia**: Tecnólogos ADSO - Implantación de software  
> **Versión**: Docker Compose v2 (sintaxis `docker compose`, no `docker-compose`)

---

## 🚀 Comandos Básicos (Los 5 Esenciales)

### 1️⃣ **Iniciar servicios** (crear y arrancar contenedores)

```bash
docker compose up -d
```

**¿Qué hace?** - Crea e inicia todos los servicios definidos en `docker-compose.yml`  
**¿Para qué?** - Levantar la aplicación completa con un solo comando  
**¿Cómo funciona?** - Lee el archivo YAML, descarga imágenes si no existen, crea volúmenes, redes y contenedores

**Opciones útiles**:

- `docker compose up` → Inicia en primer plano (ver logs en tiempo real)
- `docker compose up -d` → Inicia en segundo plano (detached mode) ✅ **Recomendado**
- `docker compose up --build` → Reconstruye imágenes antes de iniciar

---

### 2️⃣ **Detener servicios** (parar sin eliminar contenedores)

```bash
docker compose stop
```

**¿Qué hace?** - Detiene los contenedores pero NO los elimina  
**¿Para qué?** - Pausar temporalmente la aplicación manteniendo la configuración  
**¿Cómo funciona?** - Los datos persisten en volúmenes, puedes reiniciar con `up`

---

### 3️⃣ **Detener y eliminar** (limpiar todo excepto volúmenes)

```bash
docker compose down
```

**¿Qué hace?** - Detiene y elimina contenedores, redes creadas  
**¿Para qué?** - Limpiar el entorno, empezar desde cero (sin perder datos en volúmenes)  
**¿Cómo funciona?** - Los volúmenes con datos persisten por defecto

**Opciones útiles**:

- `docker compose down -v` → Elimina también los volúmenes (⚠️ **BORRA DATOS**)
- `docker compose down --remove-orphans` → Elimina contenedores huérfanos

---

### 4️⃣ **Ver estado de servicios** (¿qué está corriendo?)

```bash
docker compose ps
```

**¿Qué hace?** - Lista el estado de todos los servicios del proyecto  
**¿Para qué?** - Verificar qué contenedores están activos, detenidos o con errores  
**¿Cómo funciona?** - Muestra nombre, estado, puertos expuestos

**Salida típica**:

```
NAME                IMAGE               STATUS          PORTS
proyecto_db         postgres:15-alpine  Up 2 minutes    0.0.0.0:5432->5432/tcp
proyecto_adminer    adminer:latest      Up 2 minutes    0.0.0.0:8080->8080/tcp
```

---

### 5️⃣ **Ver logs** (depurar errores y monitorear)

```bash
docker compose logs -f
```

**¿Qué hace?** - Muestra los logs de todos los servicios  
**¿Para qué?** - Depurar errores, ver qué está pasando dentro de los contenedores  
**¿Cómo funciona?** - `-f` hace seguimiento en tiempo real (como `tail -f`)

**Opciones útiles**:

- `docker compose logs` → Ver todos los logs (histórico)
- `docker compose logs -f` → Seguimiento en tiempo real ✅ **Recomendado**
- `docker compose logs -f db` → Ver logs solo del servicio `db`
- `docker compose logs --tail=50 backend` → Ver últimas 50 líneas del servicio `backend`

---

## 🔧 Comandos Complementarios (Útiles pero no críticos)

### 📦 **Ejecutar comandos dentro de un contenedor**

```bash
docker compose exec <servicio> <comando>
```

**Ejemplos**:

```bash
# Abrir shell en PostgreSQL
docker compose exec db psql -U admin -d mi_base_datos

# Abrir bash en el contenedor
docker compose exec db bash

# Ver variables de entorno
docker compose exec db env
```

**¿Qué hace?** - Ejecuta comandos dentro de un contenedor en ejecución  
**¿Para qué?** - Acceder a la base de datos, depurar, ejecutar scripts

---

### 🔄 **Reiniciar servicios**

```bash
docker compose restart
```

**Ejemplos**:

```bash
# Reiniciar todos los servicios
docker compose restart

# Reiniciar solo un servicio específico
docker compose restart db
```

**¿Qué hace?** - Reinicia contenedores sin recrearlos  
**¿Para qué?** - Aplicar cambios en variables de entorno (`.env`)

---

### 🔍 **Validar sintaxis del archivo YAML**

```bash
docker compose config
```

**¿Qué hace?** - Valida y muestra la configuración final (con variables .env resueltas)  
**¿Para qué?** - Verificar errores de sintaxis antes de iniciar servicios

---

### 🛑 **Detener un servicio específico**

```bash
docker compose stop <servicio>
```

**Ejemplo**:

```bash
docker compose stop adminer
```

**¿Qué hace?** - Detiene solo un servicio sin afectar los demás  
**¿Para qué?** - Pausar temporalmente un servicio (ej: Adminer en producción)

---

### 📥 **Descargar imágenes sin iniciar**

```bash
docker compose pull
```

**¿Qué hace?** - Descarga todas las imágenes especificadas en el YAML  
**¿Para qué?** - Pre-descargar imágenes antes de iniciar (útil con conexión lenta)

---

## 🧹 Limpieza y Mantenimiento

### 🗑️ **Eliminar todo (contenedores, volúmenes, redes, imágenes)**

```bash
docker compose down -v --rmi all
```

**⚠️ CUIDADO**: Esto **BORRA TODO** del proyecto, incluidos los datos

**Opciones**:

- `docker compose down -v` → Elimina volúmenes (borra datos)
- `docker compose down --rmi local` → Elimina solo imágenes construidas localmente
- `docker compose down --rmi all` → Elimina todas las imágenes descargadas

---

### 🔍 **Ver volúmenes del proyecto**

```bash
docker volume ls
```

**Ver detalles de un volumen**:

```bash
docker volume inspect <nombre_volumen>
```

---

### 📊 **Ver uso de recursos (CPU, memoria)**

```bash
docker stats
```

**¿Qué hace?** - Muestra estadísticas en tiempo real de todos los contenedores  
**¿Para qué?** - Monitorear rendimiento, detectar fugas de memoria

---

## 📝 Flujo de Trabajo Típico

### 🆕 **Primera vez (Nuevo proyecto)**

```bash
# 1. Crear estructura de carpetas
mkdir mi-proyecto && cd mi-proyecto

# 2. Crear docker-compose.yml y .env
nano docker-compose.yml
nano .env

# 3. Descargar imágenes (opcional, acelera el primer inicio)
docker compose pull

# 4. Iniciar servicios
docker compose up -d

# 5. Verificar que todo esté corriendo
docker compose ps

# 6. Ver logs para confirmar
docker compose logs -f
```

---

### 🔄 **Desarrollo diario**

```bash
# Iniciar servicios
docker compose up -d

# Trabajar en el código...

# Ver logs si hay problemas
docker compose logs -f backend

# Reiniciar servicio si cambias .env
docker compose restart backend

# Detener al finalizar
docker compose stop
```

---

### 🧪 **Depuración (cuando algo falla)**

```bash
# 1. Ver estado de servicios
docker compose ps

# 2. Ver logs del servicio problemático
docker compose logs -f db

# 3. Entrar al contenedor para investigar
docker compose exec db bash

# 4. Reiniciar el servicio
docker compose restart db

# 5. Si persiste, recrear desde cero
docker compose down
docker compose up -d
```

---

### 🔁 **Actualizar código o configuración**

```bash
# 1. Detener servicios
docker compose down

# 2. Modificar código o docker-compose.yml

# 3. Reconstruir imágenes si usas build
docker compose build

# 4. Iniciar con nueva configuración
docker compose up -d

# 5. Verificar cambios
docker compose logs -f
```

---

### 🗑️ **Empezar desde cero (borrar todo)**

```bash
# ⚠️ Esto BORRA TODO: contenedores, volúmenes, datos
docker compose down -v

# Iniciar limpio
docker compose up -d
```

---

## 💡 Tips y Mejores Prácticas

### ✅ **DO's (Hacer)**

1. **Siempre usar `-d`** para iniciar en segundo plano

   ```bash
   docker compose up -d
   ```

2. **Verificar estado antes de depurar**

   ```bash
   docker compose ps
   ```

3. **Ver logs con `-f` para seguimiento en tiempo real**

   ```bash
   docker compose logs -f
   ```

4. **Validar YAML antes de iniciar**

   ```bash
   docker compose config
   ```

5. **Usar nombres de servicios para comunicación interna**
   ```yaml
   # En backend, conectar a PostgreSQL:
   DB_HOST=db # ✅ Correcto (nombre del servicio)
   ```

---

### ❌ **DON'Ts (Evitar)**

1. **NO usar `docker-compose` (con guion)**

   ```bash
   docker-compose up  # ❌ Sintaxis antigua (v1)
   docker compose up  # ✅ Sintaxis correcta (v2)
   ```

2. **NO usar `localhost` dentro de contenedores**

   ```yaml
   # ❌ Incorrecto:
   DB_HOST=localhost

   # ✅ Correcto:
   DB_HOST=db  # Nombre del servicio
   ```

3. **NO olvidar `-d` (ocuparás la terminal)**

   ```bash
   docker compose up     # ❌ Ocupa terminal
   docker compose up -d  # ✅ Libera terminal
   ```

4. **NO usar `down -v` sin respaldar datos**

   ```bash
   docker compose down -v  # ⚠️ BORRA DATOS
   ```

5. **NO exponer puertos sensibles en producción**
   ```yaml
   # ❌ En producción:
   ports:
     - '5432:5432' # PostgreSQL expuesto al público
   ```

---

## 🆘 Solución Rápida de Errores Comunes

| ❌ Error                              | ✅ Solución                                           |
| ------------------------------------- | ----------------------------------------------------- |
| `port is already allocated`           | Cambiar puerto en `docker-compose.yml`: `"5433:5432"` |
| `connection refused`                  | Usar nombre del servicio (`db`), no `localhost`       |
| `Adminer no conecta`                  | Verificar credenciales en `.env`                      |
| `permission denied`                   | `chmod -R 755` en carpetas montadas                   |
| Cambios en `.env` no aplican          | `docker compose restart <servicio>`                   |
| `no such file or directory`           | Verificar rutas en `volumes:`                         |
| `unhealthy` en servicio               | Ver logs: `docker compose logs -f <servicio>`         |
| Contenedor se reinicia constantemente | Error en la aplicación, ver logs                      |

---

## 📚 Recursos Adicionales

- **Documentación oficial**: https://docs.docker.com/compose/
- **Referencia de YAML**: https://docs.docker.com/compose/compose-file/
- **Docker Hub (imágenes)**: https://hub.docker.com/

---

## 🎯 Resumen: Los Únicos 5 Comandos que Necesitas Memorizar

```bash
1. docker compose up -d      # Iniciar servicios
2. docker compose down       # Detener y limpiar
3. docker compose ps         # Ver estado
4. docker compose logs -f    # Ver logs en tiempo real
5. docker compose restart    # Reiniciar servicios
```

**Con estos 5 comandos puedes implantar cualquier aplicación con Docker Compose** 🚀

---

**Última actualización**: Semana 2 - Bootcamp Implantación de Software SENA CGMLTI  
**Versión**: Docker Compose v2.39.4+
