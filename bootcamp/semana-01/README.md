# Semana 1: Fundamentos de Implantación y Plataformas Tecnológicas

## 📋 Información General

- **Duración**: 6 horas (5.5 horas efectivas + 30 min break)
- **Modalidad**: Presencial
- **Prerequisitos**: Conocimientos básicos de sistemas operativos

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
- **02-primer-contenedor-postgresql.md** (40 min - SIMPLIFICADA) - Primer contenedor y PostgreSQL básico

> 📝 **Nota**: La Práctica 2 fue simplificada para enfocarse en lo esencial: ejecutar PostgreSQL, conectar, y verificar persistencia básica.

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

## ⏰ Distribución del Tiempo (6 horas - ajustada para 5.5h efectivas)

> 💡 **Optimizaciones realizadas**:
>
> - Teoría de Docker reducida a 25 min (solo conceptos esenciales)
> - Práctica PostgreSQL simplificada (sin Docker Compose en Semana 1)
> - Contenido avanzado movido a Semana 2
> - Instalación Docker tiene tiempo realista (40-50 min considerando troubleshooting)

### Bloque 1: Introducción y Fundamentos (2 horas)

- **Hora 1 (0:00 - 1:00)** | Bienvenida y Teoría: Proceso de implantación

  - 0:00 - 0:10 | Bienvenida, presentación del bootcamp y **entrega de asignación de dominios**
  - 0:10 - 0:55 | Proceso de implantación en 5 fases (lectura guiada + ejemplos)
  - 0:55 - 1:00 | Q&A rápido

- **Hora 2 (1:00 - 2:00)** | Teoría: Hardware de Servidores
  - 1:00 - 1:40 | Tipos de servidores (RACK, BLADE), RAID, especificaciones por ambiente
  - 1:40 - 1:55 | Ejemplos prácticos y casos de uso
  - 1:55 - 2:00 | Q&A y preparación para break

---

### ☕ BREAK (30 min - 2:00 - 2:30)

---

### Bloque 2: Docker - Teoría y Práctica de Instalación (2 horas)

- **Hora 3 (2:30 - 3:30)** | Teoría Docker + Inicio de Instalación

  - 2:30 - 2:55 | **Teoría Docker (CONCENTRADA)**: ¿Qué es? ¿Para qué? Contenedores vs VMs, conceptos clave (imagen, contenedor, volumen)
  - 2:55 - 3:00 | Demostración rápida (Docker ya instalado en máquina instructor)
  - 3:00 - 3:30 | **Inicio de instalación guiada** (cada estudiante en su máquina)

- **Hora 4 (3:30 - 4:30)** | Continuación de Instalación y Troubleshooting

  - 3:30 - 4:20 | **Instalación y resolución de problemas**: permisos, virtualización, WSL2 (Windows), etc.
  - 4:20 - 4:30 | Verificación: todos deben tener `docker --version` funcionando

---

### Bloque 3: Práctica con Contenedores (1.5 horas)

- **Hora 5 (4:30 - 5:30)** | Primeros Contenedores PostgreSQL

  - 4:30 - 4:40 | Hello World (verificación rápida que Docker funciona)
  - 4:40 - 5:25 | **PostgreSQL básico**: ejecutar contenedor, conectar con psql, crear una tabla, verificar datos
  - 5:25 - 5:30 | Demostración de persistencia con volúmenes (solo demo del instructor)

- **Hora 6 (5:30 - 6:00)** | Cierre y Asignación
  - 5:30 - 5:50 | Resumen de conceptos clave, comandos esenciales de Docker
  - 5:50 - 6:00 | Explicación de asignación semanal, fechas de entrega, Q&A final

> ⚠️ **Importante**: No hay margen de tiempo. La instalación de Docker es el cuello de botella. Instructor debe tener preparados instaladores offline y estar listo para ayudar rápidamente.

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
- [ ] **CRÍTICO**: Preparar USB con instaladores de Docker (Windows/Mac/Linux)
- [ ] **CRÍTICO**: Descargar imágenes Docker básicas: `hello-world`, `postgres:15` (usar si hay problemas de red)
- [ ] Revisar acceso a internet (descargas de imágenes)
- [ ] Imprimir o tener digital las rúbricas de evaluación
- [ ] **Preparar carpetas con dominios asignados** para entregar a cada aprendiz

### Adaptaciones

- **Si hay problemas de conectividad**: Usar instaladores de Docker offline (preparar en USB)
- **Para máquinas lentas**: Priorizar que ejecuten contenedores en clase, documentación como tarea
- **Aprendices rezagados**: Continuar instalación mientras otros avanzan (aprendizaje entre pares)
- **Si instalación toma más tiempo**: Saltar "Hello World", ir directo a PostgreSQL (más práctico)

> ⚠️ **Crítico**: Tener instaladores offline de Docker para Windows, Mac y Linux en USB. La instalación es el mayor riesgo de tiempo.

### Seguimiento

- Tomar asistencia al inicio
- Registro de dudas frecuentes para próxima sesión
- Identificar aprendices que requieren apoyo adicional

---

## 🚀 Preparación para Semana 2

### Requisitos para la próxima sesión

- Docker instalado y funcionando (si no se logró en clase, completar como tarea)
- Familiarización con comandos básicos: `docker ps`, `docker images`, `docker run`
- Leer material previo sobre Docker Compose (se enviará por LMS)

---

**Última actualización**: 6 de octubre de 2025  
**Instructor**: [Nombre del instructor]  
**Cohorte**: ADSO Ficha 3147234 - CGMLTI - SENA
