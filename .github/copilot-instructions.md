# Copilot Instructions - Bootcamp Implantación de Software

## Contexto del Bootcamp

Este bootcamp de 9 semanas está diseñado para desarrollar la competencia de **Implantación de Software**, con sesiones semanales de 6 horas. El enfoque principal es capacitar a los participantes para planear y ejecutar actividades de implantación de software de acuerdo con las condiciones del sistema.

### Público Objetivo

**Aprendices de Análisis y Desarrollo de Software (ADSO)** del Centro de Gestión de Mercados, Logística y Tecnologías de la Información (CGMLTI) - Regional Distrito Capital, SENA Colombia.

## Resultado de Aprendizaje

**PLANEAR ACTIVIDADES DE IMPLANTACIÓN DEL SOFTWARE DE ACUERDO CON LAS CONDICIONES DEL SISTEMA**

## Estructura del Bootcamp

Cada semana sigue esta estructura de carpetas:

- `1-teoria/` - Material teórico y conceptual
- `2-practicas/` - Ejercicios prácticos y laboratorios
- `3-recursos/` - Material complementario (documentación, herramientas, plantillas)
- `4-asignación_dominios/` - Asignaciones y tareas específicas
- `README.md` - Resumen y objetivos de la semana

## Distribución de Contenidos (9 Semanas)

### Semana 1-2: Fundamentos de Hardware y Plataformas

- Hardware de servidores (RACK, BLADE, arreglos de discos)
- Características mínimas de hardware para software
- Preparación de plataforma tecnológica

### Semana 3-4: Sistemas Operativos de Servidor

- Linux Server (instalación, configuración, requisitos)
- Windows Server (instalación, configuración, licenciamiento)
- Selección de SO según condiciones del sistema

### Semana 5: Software de Servidores y Contenedores

- Docker y contenedores (concepto, instalación, uso)
- Docker Compose para orquestación
- PostgreSQL 15+ en contenedores
- Nginx como reverse proxy
- Gestión de volúmenes y redes
- Máquinas virtuales (solo conocimiento general)

### Semana 6: Hosting, Dominios y Transferencia de Archivos

- Tipos de hosting y configuraciones
- Gestión de dominios
- FTP y transferencia segura de archivos
- Gestores de contenidos (CMS)

### Semana 7: Migración y Respaldo de Datos

- Planes de migración de datos
- Estrategias de backup
- Procesos de restauración
- Mitigación de riesgos

### Semana 8: Planificación de Instalación

- Elaboración del plan de instalación
- Verificación de requisitos
- Coordinación de actividades
- Documentación de procesos

### Semana 9: Integración y Práctica Final

- Proyecto integrador
- Implantación completa de un sistema
- Evaluación de todos los criterios

## Criterios de Evaluación

Al generar contenido, asegúrate de que los participantes puedan:

1. **Preparar la plataforma tecnológica**, con base en las características del sistema operativo seleccionado
2. **Verificar el cumplimiento** de las características mínimas de hardware requeridas para el software desarrollado
3. **Diseñar el plan de migración** de datos de acuerdo con las condiciones de implementación
4. **Diseñar el plan de respaldo** de los datos para mitigar riesgos
5. **Elaborar el plan de instalación** de acuerdo con las características del software a implantar

## Guías para Generación de Contenido

### Material Teórico (1-teoria/)

- Usa lenguaje claro y técnico apropiado
- Incluye diagramas y ejemplos visuales cuando sea posible
- Referencia casos de uso reales del mundo empresarial
- Divide contenido en secciones digestibles (máximo 45 minutos de lectura)
- Incluye preguntas de autoevaluación al final

### Prácticas (2-practicas/)

- Proporciona instrucciones paso a paso
- Incluye comandos completos y scripts cuando sea necesario
- Añade capturas de pantalla o resultados esperados
- Establece tiempos estimados de realización
- Incluye sección de "Troubleshooting" para problemas comunes
- Proporciona criterios de éxito claros
- **Todo código debe estar comentado siguiendo el formato educativo: ¿Qué? ¿Para qué? ¿Cómo?**

### Recursos (3-recursos/)

- Lista herramientas necesarias con enlaces de descarga
- Incluye documentación oficial relevante
- Proporciona plantillas reutilizables (checklists, formatos de planes)
- Añade tutoriales complementarios en video si están disponibles
- Referencias a normativas y mejores prácticas de la industria

### Asignaciones (4-asignación_dominios/)

- Define objetivos de aprendizaje específicos
- Establece criterios de evaluación medibles
- Proporciona rúbricas de evaluación
- Incluye fecha de entrega y formato esperado
- Ofrece ejemplos de entregas satisfactorias

## Saberes Esenciales

### Conceptos y Principios (Prioriza estos temas):

1. Hardware de servidores: RACK, BLADE, arreglos de discos
2. Software de servidores: tipos, características, licenciamiento, máquinas virtuales (VMware), servidores de bases de datos
3. Sistemas operativos de servidores: concepto, características, tipos (Linux, Windows Server), licenciamiento, requisitos mínimos
4. Migración de datos: concepto, planes, copias de seguridad, procesos de restauración
5. Hosting y dominio: tipos, configuraciones, gestores de contenidos
6. FTP: concepto, transferencia de archivos

### Procesos (Enfatiza estas habilidades prácticas):

1. Preparar la plataforma tecnológica
2. Verificar el cumplimiento de características mínimas de hardware
3. Diseñar el plan de migración de datos
4. Diseñar el plan de respaldo de los datos
5. Elaborar el plan de instalación

## Formato de Sesiones (6 horas semanales)

Estructura sugerida:

- **Hora 1-2**: Teoría y conceptos fundamentales (con ejemplos)
- **Hora 3-4**: Demostración práctica y laboratorio guiado
- **Hora 5**: Práctica independiente con apoyo
- **Hora 6**: Revisión, Q&A, y presentación de asignación semanal

## Estilo de Comunicación

- Usa lenguaje profesional pero accesible
- Proporciona contexto del mundo real para cada concepto
- Enfatiza la importancia de la planificación y documentación
- Menciona consideraciones de seguridad y mejores prácticas
- Fomenta el pensamiento crítico sobre decisiones de implantación

## Tecnologías y Herramientas Recomendadas

### Stack Tecnológico Principal

- **Contenedores**: Docker y Docker Compose v2 (método principal de despliegue)
  - **IMPORTANTE**: Usar sintaxis `docker compose` (v2) en lugar de `docker-compose` (v1)
  - Versión instalada: Docker Compose v2.39.4+
  - Comandos: `docker compose up`, `docker compose down`, etc.
- **Base de Datos**: PostgreSQL 15+
- **Servidor Web**: Nginx
- **API**: REST API
- **Sistemas Operativos**: Ubuntu Server, Rocky Linux (para conocimiento general)
- **Virtualización**: VirtualBox, VMware (solo para conocimiento general, NO como método principal)

### Herramientas Complementarias

- **Transferencia de Archivos**: SFTP, SCP, rsync
- **Hosting/Cloud**:
  - Google Cloud Platform (GCP) - Free tier y Always Free products (recomendado)
  - AWS Free Tier
  - Azure for Students
  - DigitalOcean
- **Backup**: rsync, pg_dump/pg_restore, Docker volumes backup
- **Documentación**: Markdown, SVG para diagramas
- **Orquestación**: Docker Compose, introducción a Kubernetes (opcional)

## Consideraciones Especiales

- **Público Objetivo**: Aprendices de Análisis y Desarrollo de Software (ADSO) del Centro de Gestión de Mercados, Logística y Tecnologías de la Información (CGMLTI) - Regional Distrito Capital, SENA Colombia
- **Ambientes de práctica**: Prioriza uso de contenedores Docker para entornos reproducibles y seguros
- **Cloud para prácticas**: Google Cloud Platform (GCP) es la opción recomendada por su generosa capa gratuita y productos Always Free (incluye Compute Engine f1-micro, Cloud Storage, Cloud Functions)
- **Licenciamiento**: Usa tecnologías open source (Docker, PostgreSQL, Nginx) para evitar costos
- **Escalabilidad**: Los ejemplos deben ser escalables de pequeñas a grandes implementaciones usando contenedores
- **Portabilidad**: Enfatiza la portabilidad entre ambientes (dev, staging, production) con Docker
- **Seguridad**: Siempre incluye consideraciones de seguridad en planes de implantación
- **Infraestructura como Código**: Usa docker-compose.yml y Dockerfiles versionados
- **Recursos Gráficos**: Todos los diagramas deben estar en formato SVG con tema dark y sin degradados. Los archivos deben nombrarse con un número según el orden de aparición (ej: `1-proceso-implantacion.svg`, `2-hardware-servidores.svg`)
- **Código Educativo**: Todo código debe incluir comentarios explicativos con la estructura:
  - **¿Qué?** - Describe qué hace el código
  - **¿Para qué?** - Explica el propósito o razón
  - **¿Cómo?** - Detalla el funcionamiento o impacto (cuando sea relevante)

## Evaluación Continua

Cada semana debe incluir:

- Quiz de conocimientos teóricos (10-15 preguntas)
- Laboratorio práctico evaluable
- Documentación técnica de procesos realizados
- Participación en discusiones de casos de estudio

## Proyecto Final (Semana 9)

Los participantes deben demostrar capacidad para:

- Analizar requisitos de un sistema completo
- Planificar la infraestructura necesaria
- Diseñar planes de migración y respaldo
- Ejecutar instalación y configuración
- Documentar todo el proceso de implantación
- Presentar y defender decisiones técnicas tomadas

---

**Nota para GitHub Copilot**: Al generar contenido para este bootcamp, siempre contextualiza dentro de los saberes esenciales y criterios de evaluación. Prioriza la aplicación práctica sobre teoría abstracta, y asegura que cada actividad contribuya al resultado de aprendizaje principal.
