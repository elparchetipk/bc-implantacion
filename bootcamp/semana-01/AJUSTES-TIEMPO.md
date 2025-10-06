# Ajustes de Tiempo - Semana 1

## 📊 Análisis Realizado

**Fecha**: 6 de octubre de 2025  
**Tiempo disponible**: 5.5 horas efectivas (6 horas totales - 30 min break)

---

## ⚠️ Problemas Identificados (Versión Original)

### 1. Sobrecarga de Contenido Teórico

- **Teoría Docker original**: 45 minutos (946 líneas, ~30 páginas)
- **Problema**: Contenido muy extenso para primera sesión
- **Riesgo**: Estudiantes abrumados, poco tiempo para práctica

### 2. Tiempo de Instalación Subestimado

- **Estimado original**: 30-45 minutos
- **Realidad observada**:
  - Linux: 15-20 min ✅
  - Windows (Docker Desktop + WSL2): 40-60 min ⚠️
  - macOS: 20-30 min ✅
  - Troubleshooting: +15-30 min adicionales 🔴
- **Problema**: 30-40% de estudiantes con Windows requieren más tiempo

### 3. Práctica PostgreSQL Compleja

- **Original**: 3 partes (docker run, volúmenes, Docker Compose)
- **Tiempo real**: 60-75 minutos
- **Problema**: Docker Compose es tema avanzado para Semana 1

---

## ✅ Ajustes Implementados

### Ajuste 1: Teoría Docker Simplificada

**Antes**: 946 líneas (45 min estimados)  
**Ahora**: ~450 líneas (25 min reales)

**Contenido removido** (movido a Semana 2):

- Docker Compose completo
- Dockerfile avanzado
- Redes complejas
- Ejemplos multi-contenedor
- Mejores prácticas avanzadas

**Contenido mantenido** (esencial):

- ¿Qué es Docker? ¿Para qué?
- Contenedores vs VMs
- Conceptos: imagen, contenedor, volumen
- Comandos básicos

**Impacto**: ✅ Libera 20 minutos

---

### Ajuste 2: Tiempo Realista para Instalación

**Antes**: 30-45 min (optimista)  
**Ahora**: 50 min + 20 min troubleshooting = 70 min total

**Estrategia**:

- Bloque 2 completo (2 horas) dedicado a instalación
- Hora 3: Teoría (25 min) + inicio instalación (30 min)
- Hora 4: Instalación continuada (50 min) + troubleshooting (20 min)

**Medidas de contingencia**:

- ✅ Instaladores offline en USB (Windows, Mac, Linux)
- ✅ Imágenes Docker pre-descargadas (hello-world, postgres:15)
- ✅ Aprendices con instalación exitosa ayudan a compañeros

**Impacto**: ✅ Realista para 80-90% de estudiantes

---

### Ajuste 3: Práctica PostgreSQL Simplificada

**Antes**:

- Parte 1: docker run básico
- Parte 2: Volúmenes
- Parte 3: Docker Compose (completo)
- **Tiempo**: 60-75 minutos

**Ahora**:

- Parte 1: docker run básico (15 min)
- Parte 2: Volúmenes y persistencia (25 min)
- **Tiempo**: 40 minutos

**Contenido removido** (movido a Semana 2):

- Docker Compose completo
- Adminer (GUI web)
- Scripts de inicialización
- Health checks
- Configuraciones avanzadas

**Contenido mantenido**:

- Ejecutar PostgreSQL
- Conectar con psql
- Crear tabla y datos
- Probar persistencia (volúmenes)

**Impacto**: ✅ Libera 20-35 minutos

---

## 📅 Distribución Final (5.5 horas)

| Bloque       | Tiempo     | Actividad                       | Minutos     |
| ------------ | ---------- | ------------------------------- | ----------- |
| **Bloque 1** | 2:00 h     | Teoría: Implantación + Hardware | 120 min     |
|              |            | - Bienvenida + dominios         | 10 min      |
|              |            | - Proceso implantación          | 45 min      |
|              |            | - Hardware servidores           | 40 min      |
|              |            | - Q&A + transición              | 5 min       |
|              |            | - Buffer                        | 20 min      |
| **BREAK**    | 0:30 h     | Descanso                        | 30 min      |
| **Bloque 2** | 2:00 h     | Docker: Teoría + Instalación    | 120 min     |
|              |            | - Teoría Docker (esencial)      | 25 min      |
|              |            | - Demo + preparación            | 5 min       |
|              |            | - Instalación guiada            | 50 min      |
|              |            | - Troubleshooting               | 20 min      |
|              |            | - Verificación final            | 10 min      |
|              |            | - Buffer                        | 10 min      |
| **Bloque 3** | 1:30 h     | Práctica: PostgreSQL            | 90 min      |
|              |            | - Hello World                   | 10 min      |
|              |            | - PostgreSQL básico             | 15 min      |
|              |            | - PostgreSQL + volúmenes        | 25 min      |
|              |            | - Resumen comandos              | 20 min      |
|              |            | - Explicar asignación           | 10 min      |
|              |            | - Q&A final                     | 10 min      |
| **TOTAL**    | **6:00 h** |                                 | **360 min** |
| **Efectivo** | **5:30 h** | (sin break)                     | **330 min** |

---

## 🎯 Resultados Esperados

### Escenario Realista (80% estudiantes)

| Actividad                    | Tiempo Real   |
| ---------------------------- | ------------- |
| Teoría Bloque 1              | 1:45 h        |
| Teoría Docker                | 0:25 h        |
| Instalación Docker           | 0:50 h        |
| Troubleshooting              | 0:20 h        |
| PostgreSQL práctica          | 0:40 h        |
| Overhead (Q&A, transiciones) | 0:40 h        |
| **TOTAL**                    | **5:20 h** ✅ |

**Margen**: 10 minutos ✅

---

### Escenario Ideal (20% estudiantes avanzados)

| Actividad           | Tiempo Real   |
| ------------------- | ------------- |
| Teoría Bloque 1     | 1:30 h        |
| Teoría Docker       | 0:25 h        |
| Instalación Docker  | 0:20 h        |
| PostgreSQL práctica | 0:35 h        |
| Overhead            | 0:30 h        |
| **TOTAL**           | **3:20 h** ✅ |

**Margen**: 2 horas 10 minutos (pueden profundizar) ✅

---

### Escenario Problemático (5-10% estudiantes)

| Actividad           | Tiempo Real   |
| ------------------- | ------------- |
| Teoría Bloque 1     | 2:00 h        |
| Teoría Docker       | 0:25 h        |
| Instalación Docker  | 1:10 h        |
| Troubleshooting     | 0:30 h        |
| PostgreSQL práctica | 0:50 h        |
| Overhead            | 0:45 h        |
| **TOTAL**           | **6:20 h** 🔴 |

**Déficit**: 20 minutos

**Solución**: Completar instalación como tarea, seguir con demo del instructor

---

## 🛡️ Medidas de Contingencia

### Si la instalación toma más de 70 minutos:

1. **Prioridad 1**: Lograr que al menos 60% instalen correctamente
2. **Resto del grupo**: Demo con máquina del instructor (proyector)
3. **Tarea**: Completar instalación en casa con soporte virtual

### Si hay problemas de conectividad:

1. **USB con instaladores**: Windows, Mac, Linux
2. **Imágenes Docker pre-descargadas**: `hello-world`, `postgres:15`
3. **Comando**: `docker load -i postgres-15.tar`

### Si PostgreSQL no da tiempo:

1. **Mínimo viable**: Ejecutar `hello-world`
2. **Demo**: Instructor muestra PostgreSQL (proyector)
3. **Tarea**: Replicar en casa y documentar con capturas

---

## 📈 Indicadores de Éxito

### Mínimos Aceptables (80% estudiantes):

- ✅ Docker instalado y `docker --version` funciona
- ✅ Ejecutaron al menos `hello-world`
- ✅ Entienden concepto de contenedor vs VM
- ✅ Conocen para qué sirven los volúmenes

### Óptimos (60% estudiantes):

- ✅ PostgreSQL ejecutándose en contenedor
- ✅ Conectaron con psql
- ✅ Crearon tabla y datos
- ✅ Probaron persistencia con volúmenes

### Sobresalientes (20% estudiantes):

- ✅ Todo lo anterior
- ✅ Documentaron proceso completo
- ✅ Experimentaron con comandos adicionales
- ✅ Ayudaron a compañeros

---

## 📝 Cambios en Archivos

### Archivos Modificados:

1. **`README.md`**:

   - ❌ Eliminada tarea previa opcional
   - ✅ Distribución de tiempo ajustada a realidad
   - ✅ Medidas de contingencia documentadas
   - ✅ Buffer de tiempo explícito

2. **`1-teoria/03-introduccion-docker.md`**:

   - ✅ Reducido de 946 a ~450 líneas
   - ✅ Tiempo estimado: 45 min → 25 min
   - ✅ Docker Compose movido a Semana 2
   - ✅ Nota clara sobre contenido dividido

3. **`2-practicas/02-primer-contenedor-postgresql.md`**:
   - ✅ Eliminada Parte 3 (Docker Compose)
   - ✅ Tiempo estimado: 45 min → 40 min
   - ✅ Enfoque en lo esencial
   - ✅ Nota sobre contenido avanzado en Semana 2

---

## 🚀 Preparación para Semana 2

### Contenido que se verá la próxima semana:

- ✅ Docker Compose (archivo YAML completo)
- ✅ Aplicaciones multi-contenedor
- ✅ Redes Docker avanzadas
- ✅ Adminer (GUI web para PostgreSQL)
- ✅ Scripts de inicialización
- ✅ Health checks y restart policies
- ✅ Mejores prácticas de producción

---

## ✅ Conclusión

**Ajustes realizados**:

1. ✅ Teoría Docker reducida 20 minutos
2. ✅ Tiempo de instalación aumentado 25 minutos (realista)
3. ✅ Práctica PostgreSQL simplificada 20 minutos
4. ✅ Eliminada tarea previa (no contar con plata ajena)
5. ✅ Buffer explícito de 10-20 minutos

**Resultado**:

- 80-90% de estudiantes completarán todas las actividades en 5.5 horas ✅
- 5-10% pueden necesitar completar instalación en casa (aceptable) ⚠️
- Preparación crítica: USB con instaladores + imágenes offline 🔴

**Veredicto final**: ⚠️ **AJUSTADO - Viable con preparación adecuada**

---

**Última revisión**: 6 de octubre de 2025  
**Responsable**: Instructor - Bootcamp Implantación ADSO 3147234
