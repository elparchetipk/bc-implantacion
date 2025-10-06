# Práctica 2: Primer Contenedor PostgreSQL (Simplificada para Semana 1)

## 🎯 Objetivos

- Ejecutar PostgreSQL en un contenedor Docker
- Conectarse a la base de datos desde el host
- Crear una tabla y datos de prueba
- Entender persistencia básica de datos

**Tiempo estimado**: 40 minutos

> 📝 **Nota**: Esta es una versión simplificada. En Semana 2 veremos Docker Compose y configuraciones avanzadas.

---

## 📋 Requisitos Previos

- ✅ Docker instalado (Práctica 1 completada)
- ✅ Docker Compose v2 funcional
- Cliente de PostgreSQL (opcional pero recomendado)

---

## 📦 Parte 1: PostgreSQL con docker run

### Paso 1: Ejecutar PostgreSQL básico

```bash
# ¿Qué? Ejecuta PostgreSQL 15 en un contenedor
# ¿Para qué? Tener una base de datos lista en segundos
# ¿Cómo?
#   -d = detached (segundo plano)
#   --name = nombre del contenedor
#   -e = variables de ambiente
#   -p = mapeo de puertos (host:contenedor)
docker run -d \
  --name postgres-dev \
  -e POSTGRES_PASSWORD=devpassword \
  -e POSTGRES_USER=devuser \
  -e POSTGRES_DB=devdb \
  -p 5432:5432 \
  postgres:15
```

**Explicación de parámetros**:

- `POSTGRES_PASSWORD`: Contraseña del usuario postgres
- `POSTGRES_USER`: Crea un usuario adicional (por defecto es "postgres")
- `POSTGRES_DB`: Crea una base de datos automáticamente
- `-p 5432:5432`: Expone el puerto de PostgreSQL al host

---

### Paso 2: Verificar que está corriendo

```bash
# ¿Qué? Lista contenedores en ejecución
docker ps

# Salida esperada:
# CONTAINER ID   IMAGE          PORTS                    NAMES
# abc123...      postgres:15    0.0.0.0:5432->5432/tcp   postgres-dev
```

---

### Paso 3: Ver logs de inicialización

```bash
# ¿Qué? Muestra los últimos 50 logs del contenedor
# ¿Para qué? Verificar que PostgreSQL inició correctamente
docker logs postgres-dev --tail 50

# Buscar líneas como:
# "database system is ready to accept connections"
# "PostgreSQL init process complete; ready for start up"
```

---

### Paso 4: Conectarse a PostgreSQL (Método 1: psql en el contenedor)

```bash
# ¿Qué? Ejecuta psql dentro del contenedor
# ¿Para qué? Acceder a la línea de comandos de PostgreSQL
# ¿Cómo? -it = interactivo, -U = usuario
docker exec -it postgres-dev psql -U devuser -d devdb
```

**Comandos básicos de psql**:

```sql
-- ¿Qué? Listar todas las bases de datos
\l

-- ¿Qué? Listar todas las tablas de la BD actual
\dt

-- ¿Qué? Ver información de la conexión actual
\conninfo

-- ¿Qué? Salir de psql
\q
```

---

### Paso 5: Crear una tabla y datos de prueba

```sql
-- Dentro de psql:

-- ¿Qué? Crear una tabla de usuarios
-- ¿Para qué? Probar que la base de datos funciona
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT NOW()
);

-- ¿Qué? Insertar datos de prueba
INSERT INTO usuarios (nombre, email) VALUES
('Juan Pérez', 'juan@example.com'),
('María García', 'maria@example.com'),
('Carlos López', 'carlos@example.com');

-- ¿Qué? Consultar los datos insertados
SELECT * FROM usuarios;

-- Salida esperada:
--  id |    nombre     |        email        |     fecha_registro
-- ----+---------------+---------------------+------------------------
--   1 | Juan Pérez    | juan@example.com    | 2025-10-05 20:45:12
--   2 | María García  | maria@example.com   | 2025-10-05 20:45:12
--   3 | Carlos López  | carlos@example.com  | 2025-10-05 20:45:12
```

---

### Paso 6: Detener y eliminar el contenedor

```bash
# Salir de psql:
\q

# ¿Qué? Detiene el contenedor
docker stop postgres-dev

# ¿Qué? Elimina el contenedor
docker rm postgres-dev
```

**⚠️ PROBLEMA**: Al eliminar el contenedor, **perdemos todos los datos** (los 3 usuarios).

**Solución**: Usar volúmenes para persistencia.

---

## 💾 Parte 2: PostgreSQL con Persistencia (Volúmenes)

### Paso 1: Crear un volumen nombrado

```bash
# ¿Qué? Crea un volumen para almacenar datos de PostgreSQL
# ¿Para qué? Los datos sobreviven aunque eliminemos el contenedor
docker volume create postgres_data
```

---

### Paso 2: Ejecutar PostgreSQL con volumen

```bash
# ¿Qué? Ejecuta PostgreSQL con volumen montado
# ¿Para qué? Persistir datos fuera del contenedor
# ¿Cómo? -v = mapeo de volumen (volumen:ruta_contenedor)
docker run -d \
  --name postgres-persistent \
  -e POSTGRES_PASSWORD=securepassword \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=productiondb \
  -p 5433:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15
```

**Nota**: Usamos puerto 5433 en el host para evitar conflictos.

---

### Paso 3: Insertar datos de prueba

```bash
# Conectarse:
docker exec -it postgres-persistent psql -U admin -d productiondb
```

```sql
-- Crear tabla y datos:
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop Dell', 1200.00, 15),
('Mouse Logitech', 25.50, 50),
('Teclado Mecánico', 89.99, 30),
('Monitor 24"', 350.00, 20);

SELECT * FROM productos;

\q
```

---

### Paso 4: Entender qué pasó (IMPORTANTE)

**Sin volumen**:

```
Contenedor creado → Datos guardados → Contenedor eliminado → ❌ Datos perdidos
```

**Con volumen**:

```
Contenedor creado → Datos guardados en volumen → Contenedor eliminado → ✅ Datos persisten
Nuevo contenedor → Monta el mismo volumen → ✅ Datos disponibles
```

---

## � Parte 2: PostgreSQL con Persistencia (Volúmenes)

Ahora vamos a hacer lo mismo pero con **persistencia de datos**.

### Paso 1: Crear un volumen nombrado

```bash
# ¿Qué? Crea un volumen para almacenar datos de PostgreSQL
# ¿Para qué? Los datos sobreviven aunque eliminemos el contenedor
docker volume create mi_postgres_data

# ¿Qué? Ver el volumen creado
docker volume ls | grep mi_postgres
```

---

### Paso 2: Ejecutar PostgreSQL con volumen

```bash
# ¿Qué? Ejecuta PostgreSQL con volumen montado
# ¿Para qué? Persistir datos fuera del contenedor
# ¿Cómo? -v mapea el volumen a la carpeta de datos de PostgreSQL
docker run -d \
  --name postgres-persistente \
  -e POSTGRES_PASSWORD=mipassword123 \
  -e POSTGRES_USER=miusuario \
  -e POSTGRES_DB=mibasededatos \
  -p 5432:5432 \
  -v mi_postgres_data:/var/lib/postgresql/data \
  postgres:15

# ¿Qué? Ver que está corriendo
docker ps
```

---

### Paso 3: Crear tabla y datos de prueba

```bash
# ¿Qué? Conectarse a PostgreSQL
docker exec -it postgres-persistente psql -U miusuario -d mibasededatos
```

```sql
-- Dentro de psql:

-- ¿Qué? Crear tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0
);

-- ¿Qué? Insertar datos de prueba
INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop', 1200.00, 10),
('Mouse', 25.50, 50),
('Teclado', 89.99, 30);

-- ¿Qué? Consultar los datos
SELECT * FROM productos;

-- Salir:
\q
```

---

### Paso 4: Probar la persistencia (¡MOMENTO CLAVE!)

```bash
# ¿Qué? Eliminar el contenedor (datos están en volumen)
docker rm -f postgres-persistente

# ¿Qué? Verificar que el contenedor fue eliminado
docker ps -a | grep postgres-persistente
# (no debe aparecer)

# ¿Qué? Crear un NUEVO contenedor con el MISMO volumen
docker run -d \
  --name postgres-nuevo \
  -e POSTGRES_PASSWORD=mipassword123 \
  -e POSTGRES_USER=miusuario \
  -e POSTGRES_DB=mibasededatos \
  -p 5432:5432 \
  -v mi_postgres_data:/var/lib/postgresql/data \
  postgres:15

# ¿Qué? Verificar que los datos siguen ahí
docker exec -it postgres-nuevo psql -U miusuario -d mibasededatos -c "SELECT * FROM productos;"
```

**✅ Resultado esperado**: Los 3 productos siguen en la base de datos.

**¡Persistencia lograda!** 🎉

---

## 🎯 Comandos Esenciales de PostgreSQL (Resumen)

### Dentro de psql:

```sql
\l              -- Listar todas las bases de datos
\dt             -- Listar todas las tablas
\d productos    -- Describir estructura de la tabla "productos"
\du             -- Listar usuarios
\conninfo       -- Ver información de la conexión actual
\q              -- Salir de psql
```

### Desde el host:

```bash
# ¿Qué? Ejecutar comando SQL directamente (sin entrar a psql)
docker exec -it postgres-nuevo psql -U miusuario -d mibasededatos -c "SELECT COUNT(*) FROM productos;"

# ¿Qué? Ver logs de PostgreSQL
docker logs postgres-nuevo

# ¿Qué? Ver logs en tiempo real
docker logs -f postgres-nuevo
```

---

## 🧹 Limpieza (Opcional)

```bash
# ¿Qué? Detener y eliminar contenedor
docker rm -f postgres-nuevo

# ¿Qué? Eliminar volumen (¡CUIDADO! esto borra los datos)
docker volume rm mi_postgres_data

# ¿Qué? Eliminar todos los contenedores detenidos
docker container prune -f

# ¿Qué? Eliminar volúmenes no usados
docker volume prune -f
```

---

## ✅ Verificación Final

**Has completado la práctica si**:

- ✅ Ejecutaste PostgreSQL en un contenedor
- ✅ Te conectaste con `psql`
- ✅ Creaste una tabla y datos
- ✅ Probaste la persistencia (eliminar y recrear contenedor)
- ✅ Los datos sobrevivieron

---

## 🚀 Próximos Pasos (Semana 2)

En la siguiente sesión aprenderás:

- **Docker Compose**: Gestionar PostgreSQL + otras aplicaciones con un archivo YAML
- **Redes Docker**: Conectar contenedores entre sí
- **Adminer**: GUI web para administrar PostgreSQL
- **Configuraciones avanzadas**: Health checks, restart policies, variables de ambiente desde archivos

---

## 📚 Recursos Adicionales

- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)
- [Docker Volumes Documentation](https://docs.docker.com/storage/volumes/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/15/)

---

## ❓ Troubleshooting

### Error: "port is already allocated"

```bash
# Problema: Puerto 5432 ya está en uso
# Solución: Usar otro puerto
docker run -d -p 5433:5432 ... # Usa 5433 en el host
```

### Error: "permission denied" al ejecutar docker

```bash
# Problema: Usuario no está en grupo docker
# Solución:
sudo usermod -aG docker $USER
newgrp docker
```

### No puedo conectarme a PostgreSQL

```bash
# ¿Qué? Verificar que el contenedor está corriendo
docker ps

# ¿Qué? Ver logs para identificar el error
docker logs nombre-contenedor

# ¿Qué? Verificar contraseña y usuario
docker exec -it nombre-contenedor env | grep POSTGRES
```

---

**Tiempo empleado**: ⏱️ ~40 minutos

**¡Excelente trabajo!** 🎉 Ahora tienes PostgreSQL corriendo en Docker con persistencia de datos.

**Abrir navegador**: [http://localhost:8082](http://localhost:8082)

**Credenciales**:

- **Sistema**: PostgreSQL
- **Servidor**: db
- **Usuario**: appuser
- **Contraseña**: supersecretpassword123 (del archivo .env)
- **Base de datos**: appdb

**Explorar**:

- Ver tablas `clientes` y `pedidos`
- Ejecutar consultas SQL
- Ver estructura de tablas
- Exportar/importar datos

---

### Paso 7: Consultas SQL desde la línea de comandos

```bash
# ¿Qué? Ejecutar consulta SQL directamente
# ¿Para qué? No necesitar entrar a psql interactivo
docker compose exec db psql -U appuser -d appdb -c "SELECT * FROM clientes;"

# Consulta compleja (JOIN):
docker compose exec db psql -U appuser -d appdb -c "
SELECT
    c.nombre,
    c.email,
    COUNT(p.id) as total_pedidos,
    SUM(p.total) as monto_total
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre, c.email
ORDER BY monto_total DESC;
"
```

---

### Paso 8: Backup de la base de datos

```bash
# ¿Qué? Crea un backup completo de la base de datos
# ¿Para qué? Tener una copia de seguridad antes de cambios importantes
# ¿Cómo? pg_dump exporta toda la BD a un archivo SQL
docker compose exec db pg_dump -U appuser appdb > backup-$(date +%Y%m%d).sql

# Ver el backup creado:
ls -lh backup-*.sql
```

---

### Paso 9: Restaurar desde backup

```bash
# ¿Qué? Restaura la base de datos desde un archivo backup
# ¿Para qué? Recuperar datos en caso de error o pérdida

# Primero, copiar el backup al contenedor:
docker compose cp backup-20251005.sql db:/tmp/backup.sql

# Restaurar:
docker compose exec db psql -U appuser -d appdb -f /tmp/backup.sql
```

---

## 📊 Parte 4: Monitoreo y Gestión

### Ver estadísticas de la base de datos

```bash
# ¿Qué? Conectarse a psql
docker compose exec db psql -U appuser -d appdb
```

```sql
-- ¿Qué? Ver tamaño de la base de datos
SELECT pg_size_pretty(pg_database_size('appdb')) as db_size;

-- ¿Qué? Ver tamaño de cada tabla
SELECT
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- ¿Qué? Ver conexiones activas
SELECT
    pid,
    usename,
    application_name,
    client_addr,
    state,
    query
FROM pg_stat_activity
WHERE datname = 'appdb';

-- ¿Qué? Ver índices de las tablas
\di

\q
```

---

### Ver uso de recursos del contenedor

```bash
# ¿Qué? Muestra estadísticas en tiempo real de CPU, RAM, red, disco
# ¿Para qué? Monitorear rendimiento del contenedor PostgreSQL
docker stats postgres-app

# Presionar Ctrl+C para salir
```

---

## 🔍 Parte 5: Conexión desde Aplicaciones

### Desde Python (psycopg2)

```python
# ¿Qué? Script Python para conectarse a PostgreSQL en Docker
# ¿Para qué? Mostrar cómo una aplicación externa se conecta

import psycopg2

# ¿Qué? Parámetros de conexión
# ¿Cómo? Usar el puerto del host (5434), no el del contenedor
conn = psycopg2.connect(
    host="localhost",      # Host donde corre Docker
    port=5434,             # Puerto mapeado en docker-compose.yml
    database="appdb",
    user="appuser",
    password="supersecretpassword123"
)

# ¿Qué? Crear cursor para ejecutar consultas
cur = conn.cursor()

# ¿Qué? Ejecutar consulta
cur.execute("SELECT * FROM clientes;")

# ¿Qué? Obtener resultados
clientes = cur.fetchall()

for cliente in clientes:
    print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}")

# Cerrar conexión
cur.close()
conn.close()
```

---

### Desde Node.js (pg)

```javascript
// ¿Qué? Script Node.js para conectarse a PostgreSQL en Docker

const { Client } = require('pg');

// ¿Qué? Configuración de conexión
const client = new Client({
  host: 'localhost',
  port: 5434,
  database: 'appdb',
  user: 'appuser',
  password: 'supersecretpassword123',
});

// ¿Qué? Conectar y ejecutar consulta
async function main() {
  await client.connect();

  const result = await client.query('SELECT * FROM clientes');

  console.log('Clientes:');
  result.rows.forEach((cliente) => {
    console.log(`${cliente.id}: ${cliente.nombre} - ${cliente.email}`);
  });

  await client.end();
}

main().catch(console.error);
```

---

### String de conexión (para ORMs)

```bash
# ¿Qué? URL de conexión estándar para PostgreSQL
# ¿Para qué? Usarla en frameworks como Django, Rails, Prisma

postgresql://appuser:supersecretpassword123@localhost:5434/appdb

# Formato:
# postgresql://[usuario]:[contraseña]@[host]:[puerto]/[base_de_datos]
```

---

## 🧹 Parte 6: Limpieza y Gestión

### Detener el stack

```bash
# ¿Qué? Detiene todos los servicios
# ¿Para qué? Liberar recursos sin eliminar datos
docker compose stop
```

---

### Iniciar el stack nuevamente

```bash
# ¿Qué? Inicia servicios previamente detenidos
docker compose start
```

---

### Eliminar stack (conservando volúmenes)

```bash
# ¿Qué? Elimina contenedores y redes, pero NO volúmenes
# ¿Para qué? Limpiar pero mantener los datos
docker compose down
```

---

### Eliminar stack completamente (incluyendo datos)

```bash
# ¿Qué? Elimina contenedores, redes Y volúmenes
# ¿Para qué? Limpieza completa (⚠️ pérdida de datos)
docker compose down -v
```

---

### Ver volúmenes de Docker

```bash
# ¿Qué? Lista todos los volúmenes
docker volume ls

# ¿Qué? Ver detalles de un volumen específico
docker volume inspect postgres_app_data

# ¿Qué? Eliminar un volumen específico (⚠️ elimina datos)
docker volume rm postgres_app_data
```

---

## 🐛 Solución de Problemas

### Problema 1: "port is already allocated"

**Causa**: Otro servicio está usando el puerto 5432/5433/5434.

**Solución**: Cambiar el puerto en docker-compose.yml:

```yaml
ports:
  - '5435:5432' # Usar un puerto diferente
```

---

### Problema 2: "password authentication failed"

**Causa**: Contraseña incorrecta o variables de ambiente mal configuradas.

**Solución**:

1. Verificar archivo `.env`
2. Recrear contenedor:

```bash
docker compose down -v  # ⚠️ Elimina datos
docker compose up -d
```

---

### Problema 3: Scripts de inicialización no se ejecutan

**Causa**: Los scripts solo se ejecutan en el **primer inicio** con un volumen vacío.

**Solución**:

```bash
# ¿Qué? Eliminar volumen y recrear
docker compose down -v
docker compose up -d
```

---

### Problema 4: "too many connections"

**Causa**: Límite de conexiones alcanzado (por defecto 100).

**Solución**: Aumentar límite en docker-compose.yml:

```yaml
services:
  db:
    command: postgres -c max_connections=200
```

---

## ✅ Checklist de Verificación

- [ ] PostgreSQL corriendo en contenedor
- [ ] Conexión exitosa con psql
- [ ] Tabla creada y datos insertados
- [ ] Volumen creado para persistencia
- [ ] Datos sobreviven después de eliminar contenedor
- [ ] Docker Compose funciona con stack completo
- [ ] Adminer accesible en http://localhost:8082
- [ ] Scripts de inicialización ejecutados
- [ ] Backup creado exitosamente
- [ ] Conexión desde host (Python o Node.js) funciona

---

## 📊 Entregable

**Documento PDF** con:

1. **Capturas de pantalla**:

   - `docker compose ps` mostrando servicios corriendo
   - Adminer mostrando tablas `clientes` y `pedidos`
   - Resultado de consulta SQL con JOIN
   - Listado de volúmenes con `docker volume ls`

2. **Archivo backup** (.sql) de tu base de datos

3. **Respuestas**:
   - ¿Qué sucede con los datos si eliminas el contenedor sin volumen?
   - ¿Para qué sirve el archivo `.env` en Docker Compose?
   - ¿Cuál es la diferencia entre `docker compose down` y `docker compose down -v`?

**Nombre**: `S01-P02-PostgreSQL-[TuNombre].pdf`

---

## 🔗 Referencias

- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/15/index.html)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Adminer](https://www.adminer.org/)

---

## 📌 Próximos Pasos

En la **Asignación de la Semana** aplicarás estos conceptos para documentar especificaciones de hardware y desplegar un stack completo para un caso de estudio real.

**Continuar a**: [../4-asignación_dominios_aprendiz/README.md](../4-asignación_dominios_aprendiz/README.md)
