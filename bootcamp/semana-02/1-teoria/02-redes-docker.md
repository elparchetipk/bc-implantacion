# Redes Docker: Comunicación entre Contenedores

## 🎯 Objetivo

Comprender cómo funcionan las redes en Docker, los diferentes tipos de redes disponibles, y cómo configurarlas para permitir comunicación segura y eficiente entre contenedores.

**Tiempo estimado**: 30 minutos (lectura + ejemplos)

---

## 🌐 ¿Qué son las Redes en Docker?

**Las redes Docker** permiten que los contenedores se comuniquen entre sí y con el mundo exterior de forma controlada y segura.

**Definición simple**:  
Una red Docker es como una **red local virtual** donde los contenedores pueden encontrarse y comunicarse usando nombres en lugar de direcciones IP.

**Analogía del mundo real**:  
Es como tener una oficina donde cada empleado (contenedor) tiene una extensión telefónica (nombre del servicio). En lugar de memorizar números (IPs), simplemente marcas "ventas" o "soporte" para comunicarte.

---

## 🔌 ¿Por qué son importantes las redes?

### Problema sin redes configuradas:

```bash
# ¿Qué? Ejecutar API sin red específica
docker run -d --name api mi-api:1.0

# ¿Qué? Ejecutar PostgreSQL sin red específica
docker run -d --name db postgres:15

# ❌ PROBLEMA: La API NO puede conectarse a la base de datos
# Cada contenedor está en su propia red aislada
```

### Solución con redes:

```bash
# ¿Qué? Crear una red personalizada
docker network create mi-red

# ¿Qué? Ejecutar ambos contenedores en la misma red
docker run -d --name db --network mi-red postgres:15
docker run -d --name api --network mi-red mi-api:1.0

# ✅ AHORA: La API puede conectarse a "db:5432"
# Docker proporciona DNS interno automático
```

---

## 📊 Tipos de Redes en Docker

Docker ofrece 4 tipos principales de redes:

| Tipo        | Uso Principal       | Comunicación Externa | DNS Interno |
| ----------- | ------------------- | -------------------- | ----------- |
| **bridge**  | Desarrollo local    | ✅ Sí (con `-p`)     | ✅ Sí       |
| **host**    | Performance crítico | ✅ Directo           | ❌ No       |
| **overlay** | Swarm/multi-host    | ✅ Sí                | ✅ Sí       |
| **none**    | Aislamiento total   | ❌ No                | ❌ No       |

---

## 🌉 1. Red Bridge (Por Defecto)

**¿Qué es?**  
Una red privada interna en el host. Es la red por defecto cuando creas un contenedor.

**¿Para qué?**  
Permitir que contenedores se comuniquen entre sí en el mismo host.

**Características**:

- ✅ Aislamiento del host
- ✅ DNS interno automático
- ✅ Comunicación entre contenedores
- ✅ Puerto forwarding para acceso externo

### Red Bridge por Defecto

```bash
# ¿Qué? Ejecutar contenedor sin especificar red
docker run -d --name web nginx:alpine

# ¿Cómo? Usa automáticamente la red "bridge" por defecto
docker network inspect bridge
```

**⚠️ Limitación**: En la red `bridge` por defecto, los contenedores NO pueden usar DNS (nombres), solo IPs.

---

### Red Bridge Personalizada (RECOMENDADO)

```bash
# ¿Qué? Crear red bridge personalizada
# ¿Para qué? Habilitar DNS automático entre contenedores
docker network create mi-red-app

# ¿Qué? Ejecutar contenedores en la red personalizada
docker run -d --name db --network mi-red-app postgres:15
docker run -d --name api --network mi-red-app mi-api:1.0

# ✅ Ahora la API puede conectarse usando: postgresql://db:5432
# Docker resuelve "db" automáticamente a la IP del contenedor
```

**Ventajas**:

- ✅ DNS automático (usar nombres en lugar de IPs)
- ✅ Mejor aislamiento (separar proyectos)
- ✅ Fácil de gestionar

---

### Ejemplo con Docker Compose

```yaml
# ¿Qué? Docker Compose crea automáticamente una red bridge
services:
  db:
    image: postgres:15
    # ¿Qué? Se une automáticamente a la red del proyecto

  api:
    image: mi-api:1.0
    environment:
      # ¿Cómo? Usa el nombre del servicio para conectarse
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
# No necesitas especificar "networks", Docker Compose lo hace automáticamente
```

**¿Cómo funciona?**

- Docker Compose crea una red llamada `<nombre_carpeta>_default`
- Todos los servicios se unen a esa red
- DNS interno: cada servicio es accesible por su nombre

---

## 🖥️ 2. Red Host

**¿Qué es?**  
El contenedor usa directamente la red del host, sin aislamiento.

**¿Para qué?**  
Aplicaciones que necesitan máximo performance de red (sin overhead de NAT).

```bash
# ¿Qué? Ejecutar contenedor en red host
# ¿Para qué? El contenedor usa directamente las interfaces del host
docker run -d --network host nginx:alpine

# ✅ Ahora nginx escucha en el puerto 80 del HOST directamente
# No necesitas "-p 80:80" porque no hay mapeo
```

**Ventajas**:

- ⚡ Mejor performance (sin NAT)
- ⚡ Sin overhead de red

**Desventajas**:

- ❌ Sin aislamiento de red
- ❌ Puede causar conflictos de puertos
- ❌ Solo funciona en Linux
- ❌ Sin DNS entre contenedores

**¿Cuándo usarla?**

- Aplicaciones de monitoreo (Prometheus, Grafana)
- Herramientas de diagnóstico de red
- Casos donde el performance es crítico

---

## 🔗 3. Red Overlay

**¿Qué es?**  
Red que permite comunicación entre contenedores en **diferentes hosts** (servidores físicos).

**¿Para qué?**  
Aplicaciones distribuidas con Docker Swarm o Kubernetes.

```bash
# ¿Qué? Crear red overlay (requiere Swarm)
docker network create --driver overlay mi-red-distribuida

# ¿Para qué? Contenedores en Server1 pueden comunicarse con Server2
```

**Características**:

- 🌐 Multi-host (varios servidores)
- 🔐 Encriptación opcional
- 🎯 Service discovery automático

**Nota**: Este bootcamp se enfoca en desarrollo local. Overlay se verá en Semana 8-9 (Orquestación avanzada).

---

## 🚫 4. Red None

**¿Qué es?**  
Desactiva completamente la red del contenedor.

**¿Para qué?**  
Contenedores que no necesitan red (procesamiento offline, tests).

```bash
# ¿Qué? Contenedor sin red
docker run -d --network none mi-app:1.0

# ❌ No puede conectarse a internet ni a otros contenedores
```

**¿Cuándo usarla?**

- Procesamiento de datos locales
- Contenedores de solo cómputo
- Tests que no requieren red

---

## 🎨 DNS Interno de Docker

Una de las características más poderosas de las redes Docker es el **DNS automático**.

### ¿Cómo funciona?

```yaml
services:
  db:
    image: postgres:15
    # ¿Qué? Este servicio es accesible como "db"

  api:
    image: mi-api:1.0
    environment:
      # ¿Cómo? Docker resuelve "db" a la IP del contenedor
      DB_HOST: db
      DB_PORT: 5432
```

**Proceso**:

1. La API intenta conectarse a `db:5432`
2. Docker DNS resuelve `db` → `172.18.0.2` (IP interna del contenedor)
3. La conexión se establece

**Ventajas**:

- ✅ No necesitas conocer IPs (cambian al reiniciar)
- ✅ Código independiente del ambiente
- ✅ Fácil mantenimiento

---

## 🔧 Comandos de Redes Docker

### Listar Redes

```bash
# ¿Qué? Listar todas las redes
docker network ls

# Salida típica:
# NETWORK ID     NAME      DRIVER    SCOPE
# abc123...      bridge    bridge    local
# def456...      host      host      local
# ghi789...      none      null      local
```

---

### Crear Red

```bash
# ¿Qué? Crear red bridge personalizada
docker network create mi-red

# ¿Qué? Crear red con subnet específica
docker network create --subnet=172.20.0.0/16 mi-red-custom

# ¿Qué? Crear red con driver específico
docker network create --driver bridge mi-red-bridge
```

---

### Inspeccionar Red

```bash
# ¿Qué? Ver detalles de una red
# ¿Para qué? Ver qué contenedores están conectados, configuración, subnet
docker network inspect mi-red

# Salida incluye:
# - Subnet (rango de IPs)
# - Gateway
# - Contenedores conectados con sus IPs
```

---

### Conectar Contenedor a Red

```bash
# ¿Qué? Conectar contenedor existente a una red
docker network connect mi-red mi-contenedor

# ¿Qué? Conectar con alias
# ¿Para qué? El contenedor es accesible con múltiples nombres
docker network connect --alias db-master mi-red postgres-container
```

---

### Desconectar Contenedor de Red

```bash
# ¿Qué? Desconectar contenedor de una red
docker network disconnect mi-red mi-contenedor
```

---

### Eliminar Red

```bash
# ¿Qué? Eliminar red (debe estar vacía)
docker network rm mi-red

# ¿Qué? Eliminar todas las redes no usadas
docker network prune
```

---

## 🎯 Ejemplo Completo: Arquitectura Multi-Capa con Redes

Vamos a crear una aplicación con **3 redes separadas** para seguridad:

```yaml
# ¿Qué? Aplicación con 3 capas y 3 redes
# ¿Para qué? Aislar frontend, backend y base de datos

services:
  # ¿Qué? Base de datos (solo en red backend)
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - backend # ¿Para qué? Solo backend puede acceder
    restart: unless-stopped

  # ¿Qué? API REST (en ambas redes)
  api:
    image: mi-api:1.0
    environment:
      DATABASE_URL: postgresql://postgres:${DB_PASSWORD}@db:5432/mydb
    networks:
      - backend # ¿Para qué? Conectarse a la base de datos
      - frontend # ¿Para qué? Recibir peticiones del frontend
    depends_on:
      - db
    restart: unless-stopped

  # ¿Qué? Frontend React (solo en red frontend)
  web:
    image: mi-frontend:1.0
    networks:
      - frontend # ¿Para qué? Comunicarse con API, no con DB
    restart: unless-stopped

  # ¿Qué? Nginx reverse proxy (frontend + expuesto al host)
  nginx:
    image: nginx:alpine
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks:
      - frontend # ¿Para qué? Enrutar a web y api
    depends_on:
      - web
      - api
    restart: unless-stopped

networks:
  # ¿Qué? Red para frontend (web, api, nginx)
  frontend:
    driver: bridge

  # ¿Qué? Red para backend (api, db)
  backend:
    driver: bridge

volumes:
  db_data:
```

**Ventajas de esta arquitectura**:

- 🔐 **Seguridad**: Frontend NO puede acceder directamente a la base de datos
- 🎯 **Separación de responsabilidades**: Cada capa en su red
- 🛡️ **Defensa en profundidad**: Si el frontend es comprometido, no puede acceder a DB

**Flujo de comunicación**:

```
Usuario
  ↓
Nginx (puerto 80/443) → frontend + frontend network
  ↓
Web (React) → frontend network
  ↓
API (REST) → frontend + backend networks
  ↓
DB (PostgreSQL) → backend network
```

---

## 🔒 Mejores Prácticas de Redes

### 1. **Usar Redes Personalizadas**

**❌ Mal**:

```bash
docker run -d --name db postgres:15
docker run -d --name api mi-api:1.0
# No pueden comunicarse (sin red común)
```

**✅ Bien**:

```bash
docker network create mi-app-red
docker run -d --name db --network mi-app-red postgres:15
docker run -d --name api --network mi-app-red mi-api:1.0
# Pueden comunicarse usando DNS
```

---

### 2. **Separar Redes por Capa**

```yaml
# ✅ Separar frontend y backend
networks:
  frontend: # Web pública
  backend: # Servicios internos
```

**¿Para qué?** Limitar acceso y mejorar seguridad.

---

### 3. **No Exponer Puertos Innecesarios**

**❌ Mal**:

```yaml
services:
  db:
    image: postgres:15
    ports:
      - '5432:5432' # ¿Para qué? ❌ Exponer DB al host
```

**✅ Bien**:

```yaml
services:
  db:
    image: postgres:15
    # Sin "ports" - solo accesible internamente en la red
```

**Regla**: Solo exponer puertos de servicios que necesitan acceso externo (nginx, adminer).

---

### 4. **Usar Nombres Descriptivos**

**❌ Mal**:

```bash
docker network create net1
docker network create net2
```

**✅ Bien**:

```bash
docker network create frontend-public
docker network create backend-private
```

---

### 5. **Documentar Arquitectura de Red**

```yaml
# ¿Qué? Documentar con comentarios
networks:
  frontend:
    # ¿Para qué? Red pública para nginx, web, api
    driver: bridge

  backend:
    # ¿Para qué? Red privada para api y base de datos
    driver: bridge
    internal: true # ¿Qué? Sin acceso a internet
```

---

## 🧪 Troubleshooting de Redes

### Problema 1: Contenedores no se comunican

**Síntoma**: Error de conexión entre contenedores

**Solución**:

```bash
# ¿Qué? Verificar que están en la misma red
docker network inspect mi-red

# ¿Qué? Ver redes de un contenedor específico
docker inspect mi-contenedor | grep Networks -A 10

# ¿Qué? Probar conectividad
docker exec api ping db
```

---

### Problema 2: DNS no resuelve nombres

**Síntoma**: Error "db: Name or service not known"

**Causa**: Usando red `bridge` por defecto (sin DNS)

**Solución**: Usar red personalizada

```bash
# ¿Qué? Crear red personalizada (con DNS)
docker network create mi-red

# ¿Qué? Conectar contenedores a la nueva red
docker network connect mi-red db
docker network connect mi-red api
```

---

### Problema 3: Conflicto de puertos

**Síntoma**: Error "port is already allocated"

**Solución**:

```bash
# ¿Qué? Verificar qué está usando el puerto
sudo lsof -i :80

# ¿Qué? Usar puerto diferente en el host
docker run -p 8080:80 nginx:alpine  # Host:Contenedor
```

---

### Problema 4: Contenedor no tiene acceso a internet

**Síntoma**: `curl google.com` falla dentro del contenedor

**Solución**:

```bash
# ¿Qué? Verificar configuración de red
docker network inspect bridge

# ¿Qué? Reiniciar Docker daemon
sudo systemctl restart docker

# ¿Qué? Verificar iptables/firewall del host
```

---

## 📊 Comparación de Estrategias de Red

| Escenario                     | Estrategia Recomendada                 |
| ----------------------------- | -------------------------------------- |
| Desarrollo local simple       | Red bridge personalizada única         |
| App multi-capa (3-tier)       | Múltiples redes (frontend/backend)     |
| Microservicios (5+ servicios) | Redes por funcionalidad + service mesh |
| Performance crítico           | Red host (solo Linux)                  |
| Máximo aislamiento            | Red none o redes separadas             |

---

## ✅ Autoevaluación

### Pregunta 1

¿Cuál es la diferencia entre la red `bridge` por defecto y una red `bridge` personalizada?

<details>
<summary>Ver respuesta</summary>

**Red bridge por defecto**:

- ❌ Sin DNS automático (contenedores solo por IP)
- ❌ Todos los contenedores comparten la misma red

**Red bridge personalizada**:

- ✅ DNS automático (contenedores accesibles por nombre)
- ✅ Mejor aislamiento (separar proyectos)
- ✅ Más control sobre configuración

**Recomendación**: Siempre usar redes personalizadas.

</details>

---

### Pregunta 2

¿Por qué es buena práctica separar frontend y backend en redes diferentes?

<details>
<summary>Ver respuesta</summary>

**Seguridad en capas**:

- 🔐 El frontend NO puede acceder directamente a la base de datos
- 🛡️ Si el frontend es comprometido, el atacante no tiene acceso directo a la DB
- 🎯 Principio de menor privilegio: cada capa solo accede a lo necesario

**Arquitectura típica**:

```
Frontend (React) → Red frontend
API (REST) → Red frontend + backend (puente)
DB (PostgreSQL) → Red backend (solo interna)
```

</details>

---

### Pregunta 3

¿Cuándo deberías exponer el puerto de un servicio con `ports` en docker-compose.yml?

<details>
<summary>Ver respuesta</summary>

**Exponer puerto (`ports`)** solo cuando:

- ✅ Necesitas acceder desde el **host** (tu máquina)
- ✅ Es un servicio **público** (nginx, adminer)
- ✅ Necesitas **debugging** (puerto temporal)

**NO exponer puerto** si:

- ❌ Solo comunicación **entre contenedores** (usar DNS interno)
- ❌ Servicio **privado** (base de datos, caché)
- ❌ Por razones de **seguridad**

**Ejemplo**:

```yaml
services:
  nginx:
    ports:
      - '80:80' # ✅ Necesita acceso externo

  db:
    # ❌ Sin ports - solo interno
```

</details>

---

## 🔗 Referencias

- [Docker Network Documentation](https://docs.docker.com/network/)
- [Docker Bridge Networks](https://docs.docker.com/network/bridge/)
- [Docker Compose Networking](https://docs.docker.com/compose/networking/)
- [Network Security Best Practices](https://docs.docker.com/network/network-tutorial-standalone/)

---

## 📌 Próximos Pasos

Ahora que entiendes las redes Docker, en la siguiente sección profundizaremos en **volúmenes avanzados** para gestión de datos persistentes.

**Continuar a**: [03-volumenes-avanzados.md](./03-volumenes-avanzados.md)
