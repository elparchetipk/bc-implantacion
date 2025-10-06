# Recursos Gráficos - Bootcamp Implantación de Software

Este directorio contiene recursos gráficos en formato SVG (tema dark, sin degradados) para apoyar el aprendizaje visual durante el bootcamp.

## Diagramas Disponibles

### 1-proceso-implantacion.svg

**Descripción**: Representa las 5 fases del proceso completo de implantación de software.

**Contenido**:

- **Fase 1 - Planificación**: Análisis de requisitos, selección de plataforma, planes de instalación/respaldo/migración
- **Fase 2 - Preparación**: Configuración de infraestructura, instalación de servicios base, seguridad
- **Fase 3 - Implementación**: Deploy de aplicación, migración de datos, configuración de dominios
- **Fase 4 - Validación**: Pruebas funcionales, rendimiento, seguridad, verificación de respaldos
- **Fase 5 - Documentación**: Documentación técnica y capacitación

**Uso**: Para explicar el flujo completo del proceso de implantación.

---

### 2-hardware-servidores.svg

**Descripción**: Ilustra los tipos de hardware de servidores y especificaciones mínimas.

**Contenido**:

- **Servidores RACK**: Montaje estándar 19", unidades 1U-3U
- **Servidores BLADE**: Alta densidad, múltiples blades en chasis
- **Arreglos de Discos**: RAID 5/10, discos de paridad y hot spare
- **Especificaciones mínimas** por ambiente:
  - Desarrollo: 2 cores, 4GB RAM, 40GB disco
  - Pruebas/QA: 4 cores, 8GB RAM, 100GB disco
  - Producción: 8+ cores, 16-32GB RAM, 500GB SSD
  - Alta Disponibilidad: 16+ cores, 64GB+ RAM, 1TB+ NVMe

**Uso**: Para explicar infraestructura física y requisitos de hardware.

---

### 3-arquitectura-docker-stack.svg

**Descripción**: Muestra la arquitectura completa de una aplicación containerizada con Docker.

**Contenido**:

- Stack tecnológico: Nginx + REST API + PostgreSQL 15+
- Configuración de red Docker (app-network)
- Volúmenes persistentes para datos
- Comunicación entre contenedores
- Orquestación con docker-compose.yml

**Uso**: Ideal para explicar la arquitectura de aplicaciones modernas usando contenedores.

---

### 4-red-docker.svg

**Descripción**: Detalla la configuración de red Docker para comunicación entre contenedores.

**Contenido**:

- Red externa / Internet
- Docker Host (servidor)
- Red bridge interna (app-network, subnet 172.20.0.0/16)
- Contenedores:
  - **nginx-container**: IP 172.20.0.2, puertos 80:80 y 443:443 (expuestos)
  - **api-container**: IP 172.20.0.3, puerto interno 3000
  - **postgres-container**: IP 172.20.0.4, puerto interno 5432
- Volúmenes y variables de ambiente
- Comunicación interna vs externa

**Uso**: Para explicar networking en Docker y comunicación entre servicios.

---

### 5-docker-compose-workflow.svg

**Descripción**: Flujo de trabajo completo usando Docker Compose.

**Contenido**:

- **Archivos de Configuración**: docker-compose.yml, Dockerfiles, .env
- **Comandos Principales**:
  - `docker-compose up -d`: Levantar servicios
  - `docker-compose ps`: Ver estado
  - `docker-compose logs -f`: Ver logs en vivo
  - `docker-compose down`: Detener servicios
  - `docker-compose exec`: Ejecutar comandos en contenedores
- **Ciclo de Vida**: Build → Run → Monitor → Update → Restart
- **Estados de Contenedores**: Created, Running, Paused, Stopped, Exited
- **Gestión de Volúmenes**: Backup, restore, inspect
- **Network Testing**: Verificar comunicación entre servicios

**Uso**: Para enseñar el ciclo de vida de una aplicación con Docker Compose.

---

### 6-respaldo-migracion.svg

**Descripción**: Muestra la estrategia completa de respaldo y migración de datos.

**Contenido**:

- **Sistema Origen**: Base de datos legacy, archivos, configuración
- **Proceso de Respaldo**: Export/dump, compresión, verificación, almacenamiento
- **Ubicaciones de Almacenamiento**: Local (Docker Volumes), Red (NAS), Nube (AWS S3/Azure), Offline
- **Sistema Nuevo**: PostgreSQL 15+ en contenedor, volúmenes Docker, config maps
- **Cronograma de Migración**: Timeline de 18 días desde planificación hasta Go Live
- **Mejores Prácticas**: Regla 3-2-1, automatización, testing de restauración

**Uso**: Para planificar estrategias de respaldo y procesos de migración.

---

## Características de los Diagramas

- ✅ **Formato**: SVG (escalable sin pérdida de calidad)
- ✅ **Tema**: Dark (#1e1e1e background)
- ✅ **Estilo**: Sin degradados (flat design)
- ✅ **Colores**:
  - Azul (#58a6ff): Elementos principales
  - Verde (#7ee787): Estados activos/exitosos
  - Naranja (#ffa657): Procesos/advertencias
  - Púrpura (#d2a8ff): Almacenamiento/datos
  - Rojo (#f78166): Crítico/migración
  - Gris (#8b949e): Texto secundario

## Uso en Markdown

Para incluir estos diagramas en documentación Markdown:

```markdown
![Proceso de Implantación](./assets/1-proceso-implantacion.svg)
![Hardware de Servidores](./assets/2-hardware-servidores.svg)
![Arquitectura Docker Stack](./assets/3-arquitectura-docker-stack.svg)
![Red Docker](./assets/4-red-docker.svg)
![Docker Compose Workflow](./assets/5-docker-compose-workflow.svg)
![Respaldo y Migración](./assets/6-respaldo-migracion.svg)
```

## Edición

Los archivos SVG son de texto plano y pueden editarse con:

- Editores de texto (VS Code con extensión SVG)
- Herramientas gráficas (Inkscape, Figma, etc.)
- Directamente en código SVG

---

**Nota**: Todos los diagramas están optimizados para visualización en pantallas y proyectores en presentaciones del bootcamp.
