# Semana 1: Fundamentos de Implantación y Plataformas Tecnológicas

## 📋 Información General

- **Duración**: 6 horas (5.5 horas efectivas + 30 min break)
- **Modalidad**: Presencial
- **Prerequisitos**: Conocimientos básicos de sistemas operativos

> ⚠️ **TAREA PREVIA OPCIONAL** (48h antes de la sesión): Para optimizar el tiempo en clase, se recomienda intentar instalar Docker previamente. Ver [Guía de instalación previa](#-tarea-previa-opcional-recomendada) al final de este documento.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, los aprendices serán capaces de:

1. **Comprender** el proceso completo de implantación de software
2. **Identificar** los componentes de hardware necesarios para servidores
3. **Reconocer** las especificaciones mínimas de hardware según el ambiente
4. **Introducirse** al concepto de contenedores y Docker
5. **Preparar** el ambiente de desarrollo local

---

## 📚 Contenido

### Teoría (1-teoria/)

- **01-introduccion-implantacion.md** (45 min) - Proceso de implantación en 5 fases
- **02-hardware-servidores.md** (45 min) - Hardware de servidores (RACK, BLADE, arreglos de discos)
- **03-introduccion-docker.md** (30 min) - Fundamentos de contenedores y Docker

> 📝 **Nota**: La teoría de Docker se dividió en 2 partes. Parte 1 (fundamentos) en esta semana, Parte 2 (Docker Compose y avanzado) en Semana 2.

### Prácticas (2-practicas/)

- **01-instalar-docker.md** (30-45 min según SO) - Instalación de Docker y Docker Compose v2
- **02-primer-contenedor-postgresql.md** (45 min) - Primer contenedor y PostgreSQL con persistencia

> ⏱️ **Optimización de tiempo**: Si instalaste Docker previamente (tarea opcional), la Práctica 1 tomará solo 10-15 min de verificación.

### Recursos (3-recursos/)

- Glosario de términos
- Webgrafía
- Videografía
- E-books recomendados

### Asignación (4-asignación_dominios_aprendiz/)

- Documentar especificaciones de hardware para un caso de estudio
- Instalar y configurar Docker en máquina personal
- Crear primer contenedor PostgreSQL

---

## ⏰ Distribución del Tiempo (6 horas optimizadas)

> 💡 **Optimización realizada**: Teoría de Docker reducida a 30 min (lo esencial), contenido avanzado movido a Semana 2. Instalación previa opcional libera 30-40 min en clase.

### Bloque 1: Introducción y Fundamentos (2 horas)

- **Hora 1 (0:00 - 1:00)** | Bienvenida y Teoría: Proceso de implantación

  - 0:00 - 0:15 | Bienvenida, presentación del bootcamp, y **entrega de asignación de dominios**
  - 0:15 - 1:00 | Proceso de implantación en 5 fases (teoría + ejemplos)

- **Hora 2 (1:00 - 2:00)** | Teoría: Hardware de Servidores
  - 1:00 - 1:45 | Tipos de servidores (RACK, BLADE), RAID, especificaciones
  - 1:45 - 2:00 | Q&A y transición

---

### ☕ BREAK (30 min - 2:00 - 2:30)

---

### Bloque 2: Docker - Teoría y Práctica (2 horas)

- **Hora 3 (2:30 - 3:30)** | Teoría: Introducción a Docker (REDUCIDO)

  - 2:30 - 3:00 | ¿Qué son contenedores? Docker vs VMs, conceptos fundamentales
  - 3:00 - 3:10 | Q&A rápido
  - 3:10 - 3:30 | Transición y preparación para práctica

- **Hora 4 (3:30 - 4:30)** | Práctica: Instalación y Verificación Docker

  - 3:30 - 3:40 | **Verificación de instalaciones previas** (quienes hicieron tarea)
  - 3:40 - 4:10 | **Instalación guiada** para quienes NO instalaron previamente
  - 4:10 - 4:30 | Resolución de problemas técnicos (permisos, virtualización)

---

### Bloque 3: Práctica Aplicada con PostgreSQL (1.5 horas)

- **Hora 5 (4:30 - 5:30)** | Práctica: Primeros Contenedores

  - 4:30 - 4:45 | Hello World (verificación básica)
  - 4:45 - 5:30 | PostgreSQL: ejecutar, conectar, crear tabla (Parte 1 y 2)

- **Hora 6 (5:30 - 6:00)** | Persistencia y Cierre
  - 5:30 - 5:45 | PostgreSQL con volúmenes (persistencia)
  - 5:45 - 6:00 | Resumen de la sesión, recordatorio de asignación semanal, Q&A final

> ⏱️ **Buffer**: Con estas optimizaciones, hay ~15-20 min de margen para estudiantes que necesiten ayuda adicional.

---

## 📊 Evaluación

### Criterios de Evaluación

- ✅ Identifica correctamente las fases del proceso de implantación
- ✅ Reconoce tipos de hardware de servidores
- ✅ Define especificaciones mínimas según ambiente
- ✅ Instala Docker correctamente en su máquina
- ✅ Ejecuta contenedores básicos

### Productos Esperados

1. Docker instalado y funcionando
2. Capturas de pantalla de contenedores corriendo
3. Documento con especificaciones de hardware (caso de estudio)

Ver [RUBRICA_EVALUACION.md](./RUBRICA_EVALUACION.md) para detalles completos.

---

## 🎓 Recursos de Apoyo

### Diagramas SVG

- [1-proceso-implantacion.svg](./assets/1-proceso-implantacion.svg) - Proceso de 5 fases
- [2-hardware-servidores.svg](./assets/2-hardware-servidores.svg) - Tipos de servidores
- [3-arquitectura-docker-stack.svg](./assets/3-arquitectura-docker-stack.svg) - Stack Docker
- [4-red-docker.svg](./assets/4-red-docker.svg) - Redes en Docker
- [5-docker-compose-workflow.svg](./assets/5-docker-compose-workflow.svg) - Workflow
- [6-respaldo-migracion.svg](./assets/6-respaldo-migracion.svg) - Backup y migración

### Documentación Externa

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [PostgreSQL on Docker](https://hub.docker.com/_/postgres)

---

## 📝 Notas para el Instructor

### Preparación Previa

- [ ] Verificar proyector y conectividad
- [ ] Tener Docker instalado en máquina de demostración
- [ ] Preparar USB con instaladores de Docker (Windows/Mac)
- [ ] Revisar acceso a internet (descargas de imágenes)
- [ ] Imprimir o tener digital las rúbricas de evaluación

### Adaptaciones

- Si hay problemas de conectividad, usar imágenes Docker previamente descargadas
- Para aprendices con máquinas lentas, considerar uso de GCP Free Tier
- Tener ejemplos alternativos si PostgreSQL toma mucho tiempo

### Seguimiento

- Tomar asistencia al inicio
- Registro de dudas frecuentes para próxima sesión
- Identificar aprendices que requieren apoyo adicional

---

## 🚀 Preparación para Semana 2

### Requisitos para la próxima sesión

- Docker instalado y funcionando
- Cuenta de GCP creada (opcional pero recomendado)
- Lecturas previas sobre Linux Server (se enviará material)

---

**Última actualización**: 5 de octubre de 2025  
**Instructor**: [Nombre del instructor]  
**Cohorte**: ADSO - CGMLTI - SENA
