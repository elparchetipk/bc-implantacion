# Semana 2: Docker Compose, Redes y Aplicaciones Multi-Contenedor

## 📋 Información General

- **Duración**: 6 horas (5.5 horas efectivas + 30 min break)
- **Modalidad**: Presencial
- **Prerequisitos**:
  - Docker instalado y funcionando (Semana 1)
  - Conocimientos básicos de contenedores
  - Haber completado práctica de PostgreSQL básico

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, los aprendices serán capaces de:

1. **Comprender** Docker Compose y su sintaxis YAML
2. **Crear** aplicaciones multi-contenedor con Docker Compose
3. **Configurar** redes Docker para comunicación entre contenedores
4. **Gestionar** volúmenes nombrados para persistencia de datos
5. **Implementar** stacks completos (PostgreSQL + Adminer + Nginx)
6. **Aplicar** mejores prácticas de seguridad y configuración

---

## 📚 Contenido

### Teoría (1-teoria/)

- **01-docker-compose-fundamentos.md** (35 min) - Docker Compose v2, sintaxis YAML, servicios
- **02-redes-docker.md** (30 min) - Tipos de redes, comunicación entre contenedores
- **03-volumenes-avanzados.md** (20 min) - Named volumes, bind mounts, tmpfs
- **04-mejores-practicas-docker.md** (25 min) - Seguridad, .dockerignore, health checks

### Prácticas (2-practicas/)

- **01-primer-docker-compose.md** (40 min) - Stack PostgreSQL + Adminer
- **02-aplicacion-multicapa.md** (50 min) - API + Base de datos + Reverse proxy
- **03-proyecto-integrador.md** (60 min) - Sistema completo con tu dominio asignado

### Recursos (3-recursos/)

- Plantillas de docker-compose.yml
- Scripts de inicialización SQL
- Configuraciones de Nginx
- Cheatsheet de comandos Docker Compose

### Asignación (4-asignación_dominios_aprendiz/)

- Implementar stack completo para tu dominio asignado
- Documentar arquitectura y componentes
- Demostrar persistencia y comunicación entre servicios

---

## ⏰ Distribución del Tiempo (6 horas)

> 💡 **Aprendizajes de Semana 1**: Tiempo realista para instalaciones, troubleshooting incluido, buffers explícitos.

### Bloque 1: Docker Compose Fundamentos (2 horas)

- **Hora 1 (0:00 - 1:00)** | Teoría: Docker Compose

  - 0:00 - 0:10 | Revisión Semana 1, verificación Docker instalado
  - 0:10 - 0:45 | Docker Compose: ¿Qué es? Sintaxis YAML, servicios, volúmenes, redes
  - 0:45 - 1:00 | Demo en vivo: PostgreSQL + Adminer

- **Hora 2 (1:00 - 2:00)** | Práctica: Primer Docker Compose

  - 1:00 - 1:40 | Práctica guiada: Crear stack PostgreSQL + Adminer
  - 1:40 - 2:00 | Exploración: Adminer GUI, comandos `docker compose`

---

### ☕ BREAK (30 min - 2:00 - 2:30)

---

### Bloque 2: Redes y Volúmenes (2 horas)

- **Hora 3 (2:30 - 3:30)** | Teoría: Redes y Volúmenes

  - 2:30 - 3:00 | Redes Docker: tipos, comunicación, DNS interno
  - 3:00 - 3:20 | Volúmenes avanzados: named vs bind mounts
  - 3:20 - 3:30 | Mejores prácticas: .env, secrets, .dockerignore

- **Hora 4 (3:30 - 4:30)** | Práctica: Aplicación Multi-Capa

  - 3:30 - 4:20 | Stack completo: API + PostgreSQL + Nginx
  - 4:20 - 4:30 | Verificación y troubleshooting

---

### Bloque 3: Proyecto Integrador (1.5 horas)

- **Hora 5 (4:30 - 5:30)** | Proyecto: Tu Dominio Asignado

  - 4:30 - 4:40 | Presentación del proyecto integrador
  - 4:40 - 5:30 | Trabajo individual: Implementar stack para tu dominio

- **Hora 6 (5:30 - 6:00)** | Presentaciones y Cierre

  - 5:30 - 5:50 | 3-4 presentaciones de proyectos (voluntarios)
  - 5:50 - 6:00 | Asignación semanal, Q&A, preparación Semana 3

---

## 📊 Evaluación

### Criterios de Evaluación

- ✅ Crea archivos docker-compose.yml válidos
- ✅ Configura servicios que se comunican entre sí
- ✅ Implementa persistencia de datos con volúmenes
- ✅ Usa variables de ambiente (.env)
- ✅ Documenta arquitectura de su aplicación

### Productos Esperados

1. **Stack PostgreSQL + Adminer funcionando**
2. **Aplicación multi-capa con 3+ servicios**
3. **Proyecto integrador personalizado a su dominio**
4. **Documentación técnica con capturas de pantalla**
5. **Archivo docker-compose.yml comentado**

Ver [RUBRICA_EVALUACION.md](./RUBRICA_EVALUACION.md) para detalles completos.

---

## 🎓 Recursos de Apoyo

### Diagramas SVG (a crear)

- `1-arquitectura-compose.svg` - Arquitectura de Docker Compose
- `2-redes-docker-detalle.svg` - Tipos de redes y comunicación
- `3-volumenes-tipos.svg` - Comparación de tipos de volúmenes
- `4-stack-multicapa.svg` - Ejemplo de stack completo

### Plantillas Incluidas

- `plantilla-compose-basico.yml`
- `plantilla-compose-avanzado.yml`
- `plantilla-env-example`
- `script-init-db.sql`

### Documentación Externa

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Docker Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Adminer](https://www.adminer.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)

---

## 📝 Notas para el Instructor

### Preparación Previa

- [ ] Verificar que todos tienen Docker funcionando desde Semana 1
- [ ] Preparar USB con imágenes Docker: `adminer`, `nginx:alpine`, `postgres:15`
- [ ] Tener proyector y laptop con demos preparadas
- [ ] Revisar carpetas de dominios asignados (cada aprendiz)
- [ ] Preparar ejemplos de docker-compose.yml para diferentes casos

### Adaptaciones

- **Si Docker no está instalado**: Ayudar durante break mientras otros avanzan
- **Para máquinas lentas**: Usar imágenes alpine (más ligeras)
- **Aprendices avanzados**: Proponer agregar Redis o servicios adicionales
- **Problemas de red**: Tener imágenes pre-descargadas en USB

### Puntos Críticos

⚠️ **Docker Compose v2**: Recordar que es `docker compose` (sin guion), no `docker-compose`  
⚠️ **Sintaxis YAML**: Indentación es crítica (espacios, no tabs)  
⚠️ **Puertos**: Explicar bien la diferencia entre puerto host y puerto contenedor  
⚠️ **Redes**: Por defecto Docker Compose crea una red, no necesitan crearla manualmente

---

## 🚀 Preparación para Semana 3

### Requisitos para la próxima sesión

- Stack Docker Compose funcionando
- Familiaridad con arquitecturas multi-contenedor
- Leer material previo sobre Sistemas Operativos de Servidor (se enviará)

### Temas Próxima Semana

- Linux Server (Ubuntu Server, Rocky Linux)
- Instalación y configuración de SO en servidor
- Gestión de usuarios y permisos
- SSH y acceso remoto

---

## 🎯 Conexión con Competencia SENA

Esta semana contribuye directamente a:

- **Planear actividades de implantación**: Definir arquitectura de servicios
- **Preparar la plataforma tecnológica**: Configurar contenedores y servicios
- **Verificar requisitos de hardware**: Entender recursos necesarios por servicio
- **Elaborar plan de instalación**: Documentar configuraciones y dependencias

---

**Última actualización**: 6 de octubre de 2025  
**Instructor**: [Nombre del instructor]  
**Cohorte**: ADSO Ficha 3147234 - CGMLTI - SENA
