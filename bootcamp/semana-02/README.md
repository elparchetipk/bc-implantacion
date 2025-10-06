# Semana 2: Docker Compose para Implantación

## 📋 Información General

- **Duración**: 6 horas (5.5 horas efectivas + 30 min break)
- **Modalidad**: Presencial
- **Prerequisitos**: Semana 1 completada (Docker instalado y conceptos básicos)

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, los aprendices serán capaces de:

1. **Usar** Docker Compose para definir aplicaciones multi-contenedor
2. **Configurar** servicios, volúmenes y variables de entorno
3. **Conectar** contenedores entre sí usando nombres de servicios
4. **Persistir** datos con volúmenes nombrados
5. **Desplegar** un stack completo (Frontend + Base de Datos)
6. **Adaptar** un proyecto a su dominio de negocio asignado

---

## 📚 Contenido

### Teoría (1-teoria/)

- **docker-compose-implantacion.md** (45 min) - Todo lo esencial de Docker Compose en UN archivo
  - ¿Por qué Docker Compose?
  - Sintaxis YAML básica (services, volumes, environment)
  - Comandos esenciales
  - Ejemplo completo PostgreSQL + Adminer

> 📝 **Simplificación**: Todo el contenido teórico consolidado en un solo archivo enfocado en lo práctico

### Prácticas (2-practicas/)

- **01-stack-basico.md** (45 min) - PostgreSQL + Adminer con Docker Compose

  - Crear docker-compose.yml desde cero
  - Usar variables .env
  - Probar persistencia de datos
  - Scripts SQL de inicialización

- **02-proyecto-dominio.md** (60 min) - Adaptación a dominio asignado
  - Diseñar base de datos para tu dominio
  - Crear frontend personalizado
  - Stack completo (Frontend + BD + Adminer)
  - Documentación del proyecto

### Recursos (3-recursos/)

- Templates Docker Compose (básico, con frontend, producción)
- Cheatsheet de comandos
- Troubleshooting común
- Ejemplos de dominios

---

## ⏰ Distribución del Tiempo (6 horas)

> 💡 **Enfoque**: Simplicidad y práctica. Menos teoría, más hands-on.

### Bloque 1: Teoría Docker Compose (2 horas)

- **Hora 1 (0:00 - 1:00)** | Introducción y Conceptos

  - 0:00 - 0:10 | Bienvenida y recordatorio Semana 1
  - 0:10 - 0:25 | ¿Por qué Docker Compose? Antes vs Después
  - 0:25 - 0:50 | Sintaxis YAML: services, volumes, environment, ports
  - 0:50 - 1:00 | Q&A

- **Hora 2 (1:00 - 2:00)** | Ejemplo Completo y Demo

  - 1:00 - 1:30 | Ejemplo PostgreSQL + Adminer (paso a paso)
  - 1:30 - 1:50 | Comandos esenciales (up, down, logs, exec)
  - 1:50 - 2:00 | Q&A y preparación para break

---

### ☕ BREAK (30 min - 2:00 - 2:30)

---

### Bloque 2: Práctica 1 - Stack Básico (2 horas)

- **Hora 3 (2:30 - 3:30)** | Crear Stack Básico

  - 2:30 - 2:40 | Crear estructura del proyecto
  - 2:40 - 3:00 | Crear docker-compose.yml y .env
  - 3:00 - 3:20 | Script SQL de inicialización
  - 3:20 - 3:30 | Levantar servicios y verificar

- **Hora 4 (3:30 - 4:30)** | Probar y Explorar

  - 3:30 - 4:00 | Conectar con Adminer, explorar datos
  - 4:00 - 4:20 | Probar persistencia (down/up)
  - 4:20 - 4:30 | Troubleshooting y Q&A

---

### Bloque 3: Práctica 2 - Proyecto Dominio (1.5 horas)

- **Hora 5 (4:30 - 5:30)** | Adaptar a Dominio

  - 4:30 - 4:45 | Diseñar entidades de base de datos
  - 4:45 - 5:10 | Crear script SQL personalizado
  - 5:10 - 5:30 | Crear frontend básico (HTML)

- **Hora 6 (5:30 - 6:00)** | Despliegue y Cierre

  - 5:30 - 5:45 | Levantar stack completo, probar
  - 5:45 - 5:55 | Presentación voluntaria (2-3 proyectos)
  - 5:55 - 6:00 | Resumen y asignación semanal

---

## 📊 Evaluación

### Criterios de Evaluación

- ✅ Crea docker-compose.yml funcional
- ✅ Usa variables .env para secretos
- ✅ Configura volúmenes para persistencia
- ✅ Adapta proyecto a dominio asignado
- ✅ Frontend personalizado funcional
- ✅ Documenta el proyecto (README.md)

### Productos Esperados

1. **Stack básico funcionando** (PostgreSQL + Adminer)
2. **Proyecto personalizado** adaptado a dominio
3. **Documentación** (README.md con instrucciones)
4. **Capturas de pantalla** (frontend, adminer, terminal)

---

## 🎯 Enfoque Pedagógico

### Simplificación vs Semana Original

| Aspecto            | Versión Original          | Versión Simplificada    |
| ------------------ | ------------------------- | ----------------------- |
| **Teoría**         | 4 archivos (~3000 líneas) | 1 archivo (~700 líneas) |
| **Tiempo lectura** | 110 min                   | 45 min                  |
| **Prácticas**      | 3 complejas               | 2 enfocadas             |
| **Total semana**   | ~5-5.5h                   | ~2.5-3h                 |

### ¿Qué Eliminamos?

❌ Multi-stage builds (muy avanzado)  
❌ tmpfs mounts (caso específico)  
❌ Redes overlay/host (solo bridge básico)  
❌ Health checks detallados  
❌ Sección completa "Mejores Prácticas"

### ¿Qué Mantenemos?

✅ Docker Compose esencial (services, volumes, environment)  
✅ Variables .env (seguridad)  
✅ Named volumes (persistencia)  
✅ Comunicación entre contenedores  
✅ Comandos básicos (up, down, logs)

---

## 📹 Video Complementario

**Duración**: 60-75 minutos

**Estructura**:

- 0-10 min: ¿Por qué Docker Compose?
- 10-30 min: Sintaxis YAML (services, volumes, env)
- 30-50 min: Demo completa (PostgreSQL + Adminer)
- 50-60 min: Comandos y troubleshooting

> 💡 Los estudiantes pueden elegir: estudiar con texto o con video (o ambos)

---

## 🛠️ Recursos de Apoyo

### Templates (3-recursos/)

- **template-basico.yml** - Stack mínimo (DB + Adminer)
- **template-frontend.yml** - Con Nginx y HTML
- **template-completo.yml** - Para proyectos finales

### Cheatsheet

```bash
# Los 5 comandos esenciales
docker compose up -d        # Levantar
docker compose down         # Detener
docker compose ps           # Ver estado
docker compose logs         # Ver logs
docker compose restart      # Reiniciar
```

---

## 💡 Notas para el Instructor

### Preparación Previa

1. **Verificar instalaciones**: Todos deben tener Docker de Semana 1
2. **Entregar dominios**: Cada estudiante tiene su dominio asignado
3. **Tener templates**: Listos para compartir si hay problemas
4. **Ambiente de demo**: Tu máquina con ejemplos funcionando

### Puntos Clave a Enfatizar

1. **docker-compose.yml = receta completa** de la aplicación
2. **Nombres de servicios = hostnames** (no usar localhost)
3. **Volúmenes nombrados = persistencia** (no se pierden datos)
4. **.env = secretos** (nunca hardcodear contraseñas)

### Posibles Problemas

| Problema           | Solución Rápida                                  |
| ------------------ | ------------------------------------------------ |
| Puerto ocupado     | Cambiar en docker-compose.yml: `5433:5432`       |
| .env no se lee     | `docker compose down && up -d --force-recreate`  |
| No conecta a DB    | Verificar que usan nombre servicio, no localhost |
| Cambios no aplican | Forzar recreación: `--force-recreate`            |

---

## 🔗 Referencias

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [PostgreSQL Docker Image](https://hub.docker.com/_/postgres)
- [Adminer](https://www.adminer.org/)

---

## 📌 Próximos Pasos (Semana 3)

En la siguiente semana agregarás:

- API REST (Backend con Node.js o Python)
- Nginx como reverse proxy
- Comunicación Frontend → API → Database

---

## ✅ Indicadores de Éxito

Esta semana es exitosa si:

- [ ] 80%+ estudiantes completan stack básico
- [ ] 70%+ adaptan proyecto a su dominio
- [ ] Todos entienden docker-compose.yml
- [ ] Pueden explicar persistencia de datos
- [ ] Saben conectar contenedores por nombre
- [ ] Documentan su proyecto

**Tiempo objetivo**: 2.5-3 horas de trabajo efectivo (vs 5-5.5h original)

---

_Semana simplificada - Enfoque en lo esencial para implantar software_
