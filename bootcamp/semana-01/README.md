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

- Introducción a la implantación de software
- Proceso de implantación en 5 fases
- Hardware de servidores (RACK, BLADE, arreglos de discos)
- Especificaciones de hardware por ambiente
- Introducción a contenedores y Docker

### Prácticas (2-practicas/)

- Instalación de Docker y Docker Compose v2
- Configuración de ambiente de desarrollo
- Primer contenedor: Hello World
- Exploración de imágenes y contenedores

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

## ⏰ Distribución del Tiempo (6 horas)

### Bloque 1: Introducción y Fundamentos (2 horas)

- **Hora 1 (0:00 - 1:00)** | Bienvenida y Teoría: Proceso de implantación de software

  - 0:00 - 0:15 | Bienvenida y presentación del bootcamp
  - 0:15 - 1:00 | Proceso de implantación en 5 fases

- **Hora 2 (1:00 - 2:00)** | Teoría: Hardware de Servidores
  - 1:00 - 1:30 | Tipos de servidores (RACK, BLADE, Tower)
  - 1:30 - 2:00 | Arreglos de discos (RAID) y especificaciones

---

### ☕ BREAK (30 min)

---

### Bloque 2: Contenedores y Docker (2 horas)

- **Hora 3 (2:30 - 3:30)** | Teoría: Introducción a Docker

  - 2:30 - 3:00 | ¿Qué son contenedores? Docker vs VMs
  - 3:00 - 3:30 | Conceptos: imágenes, contenedores, volúmenes, redes

- **Hora 4 (3:30 - 4:30)** | Demo y Práctica: Instalación de Docker
  - 3:30 - 4:00 | Demostración de instalación en diferentes sistemas
  - 4:00 - 4:30 | Práctica guiada: Instalar Docker en máquina personal

---

### Bloque 3: Práctica Aplicada (1.5 horas)

- **Hora 5 (4:30 - 5:30)** | Práctica: Primeros Contenedores

  - 4:30 - 5:00 | Primer contenedor: Hello World
  - 5:00 - 5:30 | Explorar Docker (images, containers, ps, logs)

- **Hora 6 (5:30 - 6:00)** | Práctica: PostgreSQL y Cierre
  - 5:30 - 5:45 | Desplegar PostgreSQL en contenedor
  - 5:45 - 6:00 | Presentación de asignación semanal y Q&A

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
