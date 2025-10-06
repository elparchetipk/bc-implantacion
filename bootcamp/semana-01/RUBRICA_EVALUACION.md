# Rúbrica de Evaluación - Semana 1

**Competencia**: Planear actividades de implantación del software de acuerdo con las condiciones del sistema  
**Bootcamp**: Implantación de Software  
**Institución**: SENA - CGMLTI - Regional Distrito Capital  
**Programa**: Análisis y Desarrollo de Software (ADSO)  
**Semana**: 1 - Fundamentos de Hardware, Docker y PostgreSQL  
**Duración**: 6 horas presenciales + 4 horas autónomas (total 10 horas)

---

## 📋 Estructura de la Evaluación

### Ponderación General

| Componente                  | Peso | Descripción                    |
| --------------------------- | ---- | ------------------------------ |
| Conocimientos Teóricos      | 30%  | Quiz y preguntas conceptuales  |
| Prácticas de Laboratorio    | 50%  | Ejercicios técnicos evaluables |
| Proyecto Personal (Dominio) | 15%  | Adaptación a dominio asignado  |
| Participación y Actitud     | 5%   | Colaboración y compromiso      |

---

## 📊 Escala de Valoración SENA

Según el modelo pedagógico del SENA, se utilizan los siguientes juicios evaluativos:

| Escala        | Significado       | Criterio                                        |
| ------------- | ----------------- | ----------------------------------------------- |
| **5.0 - 4.5** | **EXCELENTE**     | Supera ampliamente los criterios de evaluación  |
| **4.4 - 4.0** | **SOBRESALIENTE** | Supera los criterios de evaluación              |
| **3.9 - 3.5** | **ACEPTABLE**     | Cumple satisfactoriamente los criterios         |
| **3.4 - 3.0** | **MÍNIMO**        | Cumple los criterios mínimos requeridos         |
| **< 3.0**     | **INSUFICIENTE**  | No cumple con los criterios (requiere refuerzo) |

**Nota Mínima Aprobatoria**: 3.0

---

## 🎯 Criterios de Evaluación por Componente

### 1. CONOCIMIENTOS TEÓRICOS (30%)

#### 1.1 Conceptos de Implantación de Software (10%)

| Criterio                                    | Excelente (5.0)                                                     | Sobresaliente (4.0)                   | Aceptable (3.5)                         | Insuficiente (<3.0)                 |
| ------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------- | --------------------------------------- | ----------------------------------- |
| **Comprensión del proceso de implantación** | Define claramente las 5 fases y explica su importancia con ejemplos | Define las 5 fases correctamente      | Identifica al menos 3 fases del proceso | No identifica las fases del proceso |
| **Identificación de roles**                 | Explica claramente los roles y sus responsabilidades                | Identifica roles principales          | Menciona algunos roles                  | No identifica roles                 |
| **Riesgos y mitigación**                    | Identifica 5+ riesgos con estrategias de mitigación                 | Identifica 3-4 riesgos con mitigación | Identifica 2 riesgos básicos            | No identifica riesgos               |

**Instrumentos de evaluación:**

- Quiz escrito (10 preguntas de selección múltiple)
- Preguntas abiertas (2 preguntas de análisis)

---

#### 1.2 Hardware de Servidores (10%)

| Criterio                  | Excelente (5.0)                                                         | Sobresaliente (4.0)                | Aceptable (3.5)               | Insuficiente (<3.0)         |
| ------------------------- | ----------------------------------------------------------------------- | ---------------------------------- | ----------------------------- | --------------------------- |
| **Tipos de servidores**   | Diferencia claramente RACK, BLADE, Tower con ventajas/desventajas       | Diferencia los tipos de servidores | Identifica al menos 2 tipos   | No diferencia tipos         |
| **Componentes críticos**  | Explica CPU, RAM, Storage, Red con especificaciones técnicas            | Identifica componentes principales | Menciona 2-3 componentes      | No identifica componentes   |
| **Niveles RAID**          | Explica RAID 0,1,5,10 con casos de uso específicos                      | Explica RAID 0,1,5                 | Menciona al menos 2 niveles   | No comprende RAID           |
| **Cálculo de requisitos** | Calcula correctamente requisitos para aplicación dada con justificación | Calcula requisitos básicos         | Estima requisitos aproximados | No puede estimar requisitos |

**Instrumentos de evaluación:**

- Quiz técnico (10 preguntas)
- Ejercicio de dimensionamiento de hardware

---

#### 1.3 Docker y Contenedores (10%)

| Criterio                    | Excelente (5.0)                                                    | Sobresaliente (4.0)                     | Aceptable (3.5)                  | Insuficiente (<3.0)       |
| --------------------------- | ------------------------------------------------------------------ | --------------------------------------- | -------------------------------- | ------------------------- |
| **Conceptos fundamentales** | Explica contenedores vs VM, ventajas, arquitectura Docker completa | Explica contenedores vs VM con claridad | Define qué es un contenedor      | No comprende contenedores |
| **Componentes Docker**      | Diferencia imagen, contenedor, volumen, red con ejemplos           | Identifica componentes principales      | Menciona imágenes y contenedores | No identifica componentes |
| **Docker Compose**          | Explica orquestación, sintaxis YAML, networking entre servicios    | Explica Docker Compose básico           | Menciona Docker Compose          | No conoce Docker Compose  |

**Instrumentos de evaluación:**

- Quiz conceptual (10 preguntas)
- Análisis de Dockerfile y docker-compose.yml

---

### 2. PRÁCTICAS DE LABORATORIO (50%)

#### 2.1 Instalación y Configuración de Docker (20%)

| Criterio                  | Excelente (5.0)                                                    | Sobresaliente (4.0)              | Aceptable (3.5)                 | Insuficiente (<3.0) |
| ------------------------- | ------------------------------------------------------------------ | -------------------------------- | ------------------------------- | ------------------- |
| **Instalación correcta**  | Instala Docker y Docker Compose sin asistencia, verifica versiones | Instala con mínima asistencia    | Instala con asistencia moderada | No logra instalar   |
| **Configuración inicial** | Configura usuario no-root, inicia servicios, valida funcionamiento | Configura elementos básicos      | Logra iniciar Docker            | No configura        |
| **Verificación**          | Ejecuta comandos de verificación y explica resultados              | Ejecuta comandos de verificación | Verifica instalación básica     | No verifica         |
| **Documentación**         | Documenta cada paso con capturas, comandos y explicaciones         | Documenta pasos principales      | Documenta instalación básica    | No documenta        |

**Entregables:**

- ✅ Captura de pantalla: `docker --version` y `docker compose version`
- ✅ Captura de pantalla: `docker run hello-world` exitoso
- ✅ Documento con pasos de instalación adaptados al SO usado
- ✅ Captura de pantalla: `docker ps` mostrando contenedor hello-world

**Peso**: 20% de la nota total

---

#### 2.2 Despliegue de PostgreSQL con Docker (30%)

| Criterio                           | Excelente (5.0)                                                                  | Sobresaliente (4.0)                          | Aceptable (3.5)              | Insuficiente (<3.0)      |
| ---------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------- | ------------------------ |
| **Creación de docker-compose.yml** | Archivo completo, comentado educativamente, con variables de entorno seguras     | Archivo funcional con comentarios básicos    | Archivo funcional mínimo     | Archivo no funcional     |
| **Configuración de volúmenes**     | Configura volúmenes nombrados, explica persistencia                              | Configura volúmenes básicos                  | Menciona volúmenes           | No usa volúmenes         |
| **Configuración de red**           | Configura red personalizada, explica aislamiento                                 | Usa red por defecto correctamente            | Red funcional                | Red no configurada       |
| **Conexión a PostgreSQL**          | Se conecta con múltiples métodos (CLI, pgAdmin, script), ejecuta queries         | Se conecta con psql, ejecuta queries básicas | Logra conexión básica        | No logra conectarse      |
| **Verificación de datos**          | Crea tablas, inserta datos, verifica persistencia tras restart                   | Crea tabla y datos básicos                   | Ejecuta comandos SQL básicos | No manipula datos        |
| **Adaptación a dominio**           | Adapta completamente el ejercicio a su dominio asignado (nombres, tablas, datos) | Adapta parcialmente a su dominio             | Usa nombres genéricos        | Copia exacto del ejemplo |

**Entregables:**

- ✅ Archivo `docker-compose.yml` comentado y funcional
- ✅ Captura de pantalla: `docker compose up -d` exitoso
- ✅ Captura de pantalla: `docker ps` mostrando PostgreSQL corriendo
- ✅ Captura de pantalla: Conexión a PostgreSQL (`\l` listando databases)
- ✅ Script SQL con creación de tablas adaptadas al dominio
- ✅ Captura de pantalla: Datos insertados en tablas
- ✅ Documento explicando la persistencia de datos (¿qué?, ¿para qué?, ¿cómo?)
- ✅ Captura de pantalla: Verificación de datos tras `docker compose down` y `up`

**Peso**: 30% de la nota total

---

### 3. PROYECTO PERSONAL - DOMINIO ASIGNADO (15%)

#### 3.1 Adaptación Creativa a Dominio (15%)

| Criterio                     | Excelente (5.0)                                                                | Sobresaliente (4.0)                   | Aceptable (3.5)             | Insuficiente (<3.0)          |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------------------------------- | --------------------------- | ---------------------------- |
| **Consistencia con dominio** | Todos los elementos reflejan el dominio (nombres DB, tablas, variables, datos) | Mayoría de elementos reflejan dominio | Algunos elementos adaptados | Copia literal sin adaptación |
| **Originalidad**             | Implementación única, creativa, con lógica de negocio coherente                | Implementación propia coherente       | Adaptación básica           | Copia de otro aprendiz       |
| **Comprensión**              | Explica claramente por qué eligió cada nombre y estructura                     | Explica decisiones principales        | Justifica elementos básicos | No justifica decisiones      |
| **Nomenclatura**             | Nombres técnicamente correctos (snake_case, plurales, etc.) según dominio      | Nombres correctos                     | Nombres aceptables          | Nombres incorrectos          |

**Ejemplos de Adaptación:**

**Dominio: Restaurante**

- Base de datos: `restaurante_db`
- Tablas: `platos`, `pedidos`, `mesas`, `empleados`
- Usuario: `chef_admin`

**Dominio: Biblioteca**

- Base de datos: `biblioteca_db`
- Tablas: `libros`, `prestamos`, `usuarios`, `multas`
- Usuario: `bibliotecario_admin`

**Dominio: Clínica Veterinaria**

- Base de datos: `veterinaria_db`
- Tablas: `mascotas`, `duenos`, `citas`, `tratamientos`
- Usuario: `veterinario_admin`

**Entregables:**

- ✅ Documento explicando el dominio asignado
- ✅ Diagrama ER (opcional pero valorado) de las tablas creadas
- ✅ Justificación de nomenclatura y decisiones técnicas
- ✅ Evidencia de comprensión (no copia)

**Peso**: 15% de la nota total

---

### 4. PARTICIPACIÓN Y ACTITUD (5%)

| Criterio                     | Excelente (5.0)                                                | Sobresaliente (4.0)             | Aceptable (3.5)             | Insuficiente (<3.0)      |
| ---------------------------- | -------------------------------------------------------------- | ------------------------------- | --------------------------- | ------------------------ |
| **Asistencia y puntualidad** | 100% asistencia, puntual, preparado                            | Asistencia completa             | Asistencia aceptable (>80%) | Inasistencias frecuentes |
| **Participación activa**     | Pregunta, responde, colabora constantemente                    | Participa regularmente          | Participa ocasionalmente    | No participa             |
| **Respeto y colaboración**   | Ayuda a compañeros, respeta opiniones, propone soluciones      | Colabora con compañeros         | Trabaja individualmente     | Actitud negativa         |
| **Trabajo autónomo**         | Completa prácticas fuera de clase, investiga por cuenta propia | Realiza trabajo autónomo básico | Cumple mínimo               | No trabaja autónomamente |

**Peso**: 5% de la nota total

---

## 📝 Instrumentos de Evaluación Detallados

### QUIZ 1: Conceptos de Implantación (10 preguntas)

**Formato**: Selección múltiple con única respuesta  
**Duración**: 20 minutos  
**Nota**: 30% del componente teórico

**Temas evaluados:**

1. Fases del proceso de implantación (3 preguntas)
2. Roles y responsabilidades (2 preguntas)
3. Riesgos y mitigación (2 preguntas)
4. Planificación de actividades (3 preguntas)

---

### QUIZ 2: Hardware de Servidores (10 preguntas)

**Formato**: Selección múltiple + 1 pregunta abierta  
**Duración**: 25 minutos  
**Nota**: 30% del componente teórico

**Temas evaluados:**

1. Tipos de servidores (2 preguntas)
2. Componentes de hardware (3 preguntas)
3. RAID (2 preguntas)
4. Especificaciones técnicas (2 preguntas)
5. Dimensionamiento (1 pregunta abierta)

---

### QUIZ 3: Docker y Contenedores (10 preguntas)

**Formato**: Selección múltiple + análisis de código  
**Duración**: 30 minutos  
**Nota**: 40% del componente teórico

**Temas evaluados:**

1. Conceptos fundamentales (3 preguntas)
2. Componentes Docker (3 preguntas)
3. Docker Compose (2 preguntas)
4. Análisis de Dockerfile (1 ejercicio)
5. Análisis de docker-compose.yml (1 ejercicio)

---

### LAB 1: Instalación de Docker

**Formato**: Práctica guiada con entregables  
**Duración**: 1.5 horas  
**Nota**: 20% de la nota total

**Entregables requeridos:**

1. Documento con pasos de instalación (formato Markdown preferido)
2. Capturas de pantalla de comandos de verificación
3. Respuestas a preguntas de autoevaluación
4. Archivo de respaldos de comandos ejecutados

---

### LAB 2: PostgreSQL con Docker

**Formato**: Práctica independiente con supervisión  
**Duración**: 2 horas en clase + 2 horas autónomas  
**Nota**: 30% de la nota total

**Entregables requeridos:**

1. Archivo `docker-compose.yml` funcional y comentado
2. Script SQL con DDL adaptado al dominio
3. Documento explicativo del proceso (¿Qué? ¿Para qué? ¿Cómo?)
4. Conjunto completo de capturas de pantalla
5. Archivo de respaldos (.sql) de la base de datos
6. README.md explicando cómo replicar el ejercicio

---

### PROYECTO: Adaptación a Dominio

**Formato**: Trabajo individual continuo  
**Duración**: Durante toda la semana  
**Nota**: 15% de la nota total

**Entregables requeridos:**

1. Documento de análisis del dominio asignado
2. Modelo de datos (tablas, relaciones)
3. Nomenclatura justificada técnicamente
4. Implementación completa en PostgreSQL
5. Documento de reflexión sobre aprendizajes

---

## 🎯 Rúbrica Integrada por Actividad

### ACTIVIDAD 1: Quiz Teórico Integrado (30%)

| Componente   | Peso en Quiz | Criterio Excelente                          | Criterio Mínimo                         |
| ------------ | ------------ | ------------------------------------------- | --------------------------------------- |
| Implantación | 33%          | 9-10 respuestas correctas                   | 6-7 respuestas correctas                |
| Hardware     | 33%          | 9-10 correctas + dimensionamiento excelente | 6-7 correctas + dimensionamiento básico |
| Docker       | 34%          | 9-10 correctas + análisis profundo          | 6-7 correctas + análisis básico         |

**Nota mínima aprobatoria del quiz**: 6.0/10.0 (equivale a 3.0 en escala SENA)

---

### ACTIVIDAD 2: Laboratorio Docker + PostgreSQL (50%)

| Componente           | Peso | Criterio Excelente                                | Criterio Mínimo             |
| -------------------- | ---- | ------------------------------------------------- | --------------------------- |
| Instalación Docker   | 40%  | Instalado, configurado, documentado completamente | Instalado y funcional       |
| PostgreSQL Container | 40%  | Compose completo, persistente, bien documentado   | Contenedor funcional básico |
| Adaptación dominio   | 20%  | Totalmente adaptado, original, coherente          | Parcialmente adaptado       |

**Nota mínima aprobatoria del lab**: 3.0/5.0

---

### ACTIVIDAD 3: Proyecto de Dominio (15%)

| Componente    | Peso | Criterio Excelente            | Criterio Mínimo         |
| ------------- | ---- | ----------------------------- | ----------------------- |
| Consistencia  | 40%  | Todos los elementos adaptados | 50% elementos adaptados |
| Originalidad  | 30%  | Implementación única          | No es copia evidente    |
| Documentación | 30%  | Completa y justificada        | Básica pero presente    |

**Nota mínima aprobatoria**: 3.0/5.0

---

## 📊 Tabla de Conversión de Calificaciones

### De Puntos a Escala SENA

| Puntos (0-100) | Escala SENA (0-5.0) | Juicio        |
| -------------- | ------------------- | ------------- |
| 90 - 100       | 4.5 - 5.0           | Excelente     |
| 80 - 89        | 4.0 - 4.4           | Sobresaliente |
| 70 - 79        | 3.5 - 3.9           | Aceptable     |
| 60 - 69        | 3.0 - 3.4           | Mínimo        |
| 0 - 59         | 0.0 - 2.9           | Insuficiente  |

**Fórmula de conversión**: `Nota SENA = (Puntos / 100) × 5.0`

---

## 📅 Cronograma de Evaluación

| Actividad               | Momento                | Duración  | Peso |
| ----------------------- | ---------------------- | --------- | ---- |
| Quiz 1 (Implantación)   | Bloque 1 - Inicio      | 20 min    | 10%  |
| Quiz 2 (Hardware)       | Bloque 1 - Final       | 25 min    | 10%  |
| Lab 1 (Instalar Docker) | Bloque 2               | 1.5 h     | 20%  |
| Quiz 3 (Docker)         | Bloque 3 - Inicio      | 30 min    | 10%  |
| Lab 2 (PostgreSQL)      | Bloque 3 + Autónomo    | 2 h + 2 h | 30%  |
| Proyecto Dominio        | Durante toda la semana | Continuo  | 15%  |
| Participación           | Durante toda la sesión | 6 h       | 5%   |

**Fecha límite entrega Lab 2 y Proyecto**: Viernes 11:59 PM (5 días después de la sesión presencial)

---

## 📦 Formato de Entrega

### Estructura de Carpeta Requerida

```
apellido-nombre-semana01/
├── README.md                          # Índice general
├── 01-instalacion-docker/
│   ├── capturas/
│   │   ├── 01-docker-version.png
│   │   ├── 02-hello-world.png
│   │   └── 03-docker-ps.png
│   └── INSTALACION.md                 # Documentación del proceso
├── 02-postgresql-docker/
│   ├── docker-compose.yml             # Archivo principal
│   ├── scripts/
│   │   ├── 01-crear-tablas.sql       # DDL
│   │   └── 02-insertar-datos.sql     # DML
│   ├── capturas/
│   │   ├── 01-compose-up.png
│   │   ├── 02-docker-ps.png
│   │   ├── 03-conexion-psql.png
│   │   ├── 04-tablas-creadas.png
│   │   ├── 05-datos-insertados.png
│   │   └── 06-persistencia-verificada.png
│   ├── backup/
│   │   └── dominio-backup.sql         # Respaldo de BD
│   └── DOCUMENTACION.md               # Explicación completa
├── 03-proyecto-dominio/
│   ├── ANALISIS-DOMINIO.md            # Descripción del dominio
│   ├── MODELO-DATOS.md                # Diseño de tablas
│   ├── JUSTIFICACION.md               # Decisiones técnicas
│   └── diagrama-er.png                # Diagrama opcional
└── REFLEXION.md                       # Aprendizajes personales
```

### Archivo README.md Principal

```markdown
# Entrega Semana 1 - [Tu Nombre]

**Programa**: Análisis y Desarrollo de Software (ADSO)  
**Bootcamp**: Implantación de Software  
**Instructor**: [Nombre del Instructor]  
**Fecha entrega**: [DD/MM/AAAA]  
**Dominio asignado**: [Tu Dominio]

## Contenido

1. [Instalación de Docker](01-instalacion-docker/INSTALACION.md)
2. [PostgreSQL con Docker](02-postgresql-docker/DOCUMENTACION.md)
3. [Proyecto de Dominio](03-proyecto-dominio/ANALISIS-DOMINIO.md)
4. [Reflexiones](REFLEXION.md)

## Verificación

- [x] Docker instalado y funcionando
- [x] PostgreSQL desplegado con Docker Compose
- [x] Datos persistentes verificados
- [x] Proyecto adaptado a dominio: [Tu Dominio]
- [x] Documentación completa
- [x] Capturas de pantalla incluidas
```

---

## ✅ Lista de Verificación de Entrega

### Antes de Enviar, Verificar:

**Técnico:**

- [ ] Docker funciona correctamente
- [ ] `docker compose up -d` inicia PostgreSQL sin errores
- [ ] Conexión a PostgreSQL exitosa
- [ ] Datos persisten después de `docker compose down` y `up`
- [ ] Todos los scripts SQL ejecutan sin errores

**Documentación:**

- [ ] Todos los archivos tienen comentarios educativos (¿Qué? ¿Para qué? ¿Cómo?)
- [ ] README.md principal completo
- [ ] Capturas de pantalla claras y legibles
- [ ] Nombres de archivos descriptivos y organizados

**Dominio:**

- [ ] Todos los nombres reflejan el dominio asignado
- [ ] No hay nombres genéricos (ej: "tabla1", "datos", "test")
- [ ] Nomenclatura técnicamente correcta
- [ ] Implementación original (no copiada)

**Formato:**

- [ ] Estructura de carpetas correcta
- [ ] Archivos .md en formato Markdown válido
- [ ] Imágenes en formato .png o .jpg
- [ ] Tamaño total < 50 MB

---

## 🚨 Causales de Pérdida de Puntos

### Penalizaciones Mayores (50-100% de la nota del ítem)

- ❌ **Plagio o copia**: Copia literal de otro aprendiz o fuente sin adaptación
- ❌ **No funciona**: Código que no ejecuta o genera errores
- ❌ **Entrega tardía**: Después de la fecha límite sin justificación
- ❌ **Dominio incorrecto**: No adaptado al dominio asignado

### Penalizaciones Moderadas (20-50% de la nota del ítem)

- ⚠️ **Documentación incompleta**: Faltan explicaciones o comentarios
- ⚠️ **Capturas ilegibles**: Imágenes borrosas o incompletas
- ⚠️ **Nomenclatura incorrecta**: Nombres mal escritos o no convencionales
- ⚠️ **Estructura desordenada**: Archivos mal organizados

### Penalizaciones Menores (5-20% de la nota del ítem)

- ⚠️ **Formato inconsistente**: Markdown mal formateado
- ⚠️ **Comentarios escasos**: Código poco comentado
- ⚠️ **README incompleto**: Falta información básica

---

## 🎓 Criterios de Aprobación

### Para Aprobar la Semana 1:

1. **Nota mínima general**: 3.0/5.0 (60%)
2. **Evidencia de comprensión**: No copia evidente
3. **Adaptación a dominio**: Al menos 50% adaptado
4. **Funcionalidad técnica**: Docker y PostgreSQL funcionales

### Para Excelencia:

1. **Nota**: 4.5+/5.0 (90%+)
2. **Originalidad**: Implementación única y creativa
3. **Documentación**: Completa y profesional
4. **Participación**: Activa y colaborativa

---

## 📞 Recursos de Apoyo

### Durante la Evaluación

- **Instructor disponible**: Durante las 6 horas de clase
- **Compañeros**: Colaboración permitida para conceptos (NO código)
- **Documentación oficial**: Consulta permitida y recomendada
- **Internet**: Búsqueda de información permitida

### No Permitido

- ❌ Copiar código de compañeros
- ❌ Compartir dominio asignado
- ❌ Usar código sin entender
- ❌ Entregar trabajo de otra persona

---

## 🔄 Plan de Mejoramiento

### Si la Nota es Insuficiente (<3.0):

1. **Reunión con instructor**: Agendar tutoría personalizada
2. **Identificar debilidades**: Análisis de componentes fallidos
3. **Plan de estudio**: Recursos adicionales y ejercicios
4. **Evaluación de recuperación**: Máximo 2 semanas después
5. **Nota máxima de recuperación**: 3.5/5.0

### Actividades de Recuperación:

- Repetir laboratorios con supervisión
- Quiz de recuperación sobre temas fallidos
- Proyecto adicional más simple
- Presentación oral explicando conceptos

---

## 📈 Retroalimentación

### Cuándo Recibirás Notas:

- **Quizzes**: Inmediatamente después (automático)
- **Lab 1**: 2 días después de la sesión
- **Lab 2 y Proyecto**: 5 días después de la fecha límite
- **Nota final Semana 1**: 7 días después de la entrega

### Formato de Retroalimentación:

- Nota numérica en escala SENA (0.0 - 5.0)
- Comentarios específicos por componente
- Fortalezas identificadas
- Áreas de mejora con sugerencias
- Recursos adicionales si es necesario

---

## 📝 Autoevaluación

### Antes de Entregar, Pregúntate:

1. ¿Entiendo qué hace cada línea de mi código?
2. ¿Puedo explicar por qué elegí estos nombres?
3. ¿Mi implementación es original?
4. ¿Funciona todo sin errores?
5. ¿La documentación es clara y completa?
6. ¿Refleja mi dominio asignado consistentemente?
7. ¿Estoy orgulloso de esta entrega?

**Si respondiste "NO" a alguna pregunta, revisa ese aspecto antes de entregar.**

---

## 🎯 Consejos para Obtener Excelencia

### Técnicos

- ✅ Prueba tu código múltiples veces
- ✅ Usa nombres descriptivos y consistentes
- ✅ Comenta TODO tu código educativamente
- ✅ Verifica persistencia de datos

### Documentación

- ✅ Escribe como si explicaras a alguien que no sabe nada
- ✅ Incluye capturas claras y descriptivas
- ✅ Usa formato Markdown correctamente
- ✅ Revisa ortografía y redacción

### Dominio

- ✅ Sé creativo pero coherente
- ✅ Investiga sobre tu dominio si no lo conoces
- ✅ Piensa en casos de uso reales
- ✅ Mantén consistencia en toda la entrega

### Actitud

- ✅ Participa activamente en clase
- ✅ Ayuda a compañeros (sin dar respuestas directas)
- ✅ Pregunta cuando no entiendas
- ✅ Investiga por cuenta propia

---

**Última actualización**: 5 de octubre de 2025  
**Bootcamp**: Implantación de Software - SENA CGMLTI  
**Versión**: 1.0

**Aprobado por**: [Nombre del Coordinador Académico]  
**Validado por**: [Nombre del Instructor]

---

## 📧 Contacto

**Dudas sobre la evaluación:**  
Correo: [correo-instructor@sena.edu.co]  
Horario de atención: Lunes a Viernes 8:00 AM - 5:00 PM

**Plataforma de entrega:**  
[Especificar: Sofia Plus, Google Classroom, etc.]

---

**¡ÉXITO EN TU APRENDIZAJE! 🚀**
