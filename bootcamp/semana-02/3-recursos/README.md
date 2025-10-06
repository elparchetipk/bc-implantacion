# 📦 Recursos - Semana 2

> **Propósito**: Material de apoyo para la práctica de Docker Compose  
> **Audiencia**: Tecnólogos ADSO - Implantación de software  
> **Uso**: Consulta rápida, copy-paste, inspiración para proyectos

---

## 📂 Contenido de esta Carpeta

### 🎯 [cheatsheet-comandos.md](./cheatsheet-comandos.md)

**Referencia rápida de 1 página con los 5 comandos esenciales**

- ¿Qué? - Guía de consulta rápida con sintaxis y ejemplos
- ¿Para qué? - Tener a mano los comandos más usados durante la práctica
- ¿Cómo usar? - Abrir en una pestaña separada como referencia

**Comandos incluidos**:

- `docker compose up -d` - Iniciar servicios
- `docker compose down` - Detener y limpiar
- `docker compose ps` - Ver estado
- `docker compose logs -f` - Ver logs en tiempo real
- `docker compose restart` - Reiniciar servicios

---

### 🔧 [troubleshooting.md](./troubleshooting.md)

**Solución de 12 problemas más comunes**

- ¿Qué? - Guía de resolución de problemas paso a paso
- ¿Para qué? - Depurar errores sin perder tiempo
- ¿Cómo usar? - Buscar tu error en el índice, seguir los pasos

**Problemas cubiertos**:

1. Puerto ya está en uso
2. Conexión rechazada (localhost vs nombre de servicio)
3. Adminer no conecta a PostgreSQL
4. Cambios en .env no aplican
5. Contenedor se reinicia constantemente
6. Permisos denegados en volúmenes
7. init.sql no se ejecuta
8. Frontend 403 Forbidden
9. Servicio "unhealthy"
10. Datos se pierden al reiniciar
11. Error de sintaxis YAML
12. No se puede descargar imagen

---

### 📋 [templates/](./templates/)

**Plantillas docker-compose.yml listas para copiar**

#### 1. `template-basico.yml`

- **Stack**: PostgreSQL + Adminer
- **Uso**: Proyectos simples con solo base de datos
- **Tiempo de setup**: 5 minutos
- **Ideal para**: Primera práctica, proyectos de aprendizaje

#### 2. `template-frontend.yml`

- **Stack**: Nginx + PostgreSQL + Adminer
- **Uso**: Proyectos con interfaz web (HTML/CSS/JS)
- **Tiempo de setup**: 10 minutos
- **Ideal para**: Práctica 2 (adaptación al dominio)

#### 3. `template-completo.yml`

- **Stack**: Frontend + Backend API + PostgreSQL + Adminer
- **Uso**: Proyectos de múltiples capas (3-tier)
- **Tiempo de setup**: 20-30 minutos
- **Ideal para**: Proyectos finales, aplicaciones reales

**Características**:

- ✅ Completamente comentados (¿Qué? ¿Para qué? ¿Cómo?)
- ✅ Variables de entorno con .env
- ✅ Healthchecks configurados
- ✅ Volúmenes para persistencia
- ✅ Instrucciones de uso incluidas
- ✅ Troubleshooting integrado

---

### 💡 [ejemplos-dominios/](./ejemplos-dominios/)

**Proyectos completos de ejemplo por dominio de negocio**

#### 1. [restaurante.md](./ejemplos-dominios/restaurante.md)

**Sistema de gestión de restaurante**

- **Tablas**: categorias, platos, mesas, clientes, pedidos, detalle_pedidos, empleados
- **Casos de uso**: Gestionar menú, tomar pedidos, controlar mesas
- **Incluye**: SQL completo, docker-compose.yml, frontend HTML/CSS, README
- **Adaptable a**: Cafetería, hotel, catering, eventos

**Características destacadas**:

- 7 tablas relacionadas
- 3 empleados, 5 mesas, 8 platos en el menú
- Frontend con estadísticas del día
- Consultas SQL útiles incluidas

#### 2. [biblioteca.md](./ejemplos-dominios/biblioteca.md)

**Sistema de gestión de biblioteca**

- **Tablas**: categorias_libros, autores, libros, libros_autores (M:M), usuarios, prestamos, multas, empleados
- **Casos de uso**: Préstamos de libros, control de devoluciones, gestión de multas
- **Incluye**: SQL completo, docker-compose.yml, frontend simplificado
- **Adaptable a**: Videoteca, ludoteca, centro de documentación, archivo

**Características destacadas**:

- 8 tablas con relaciones M:M
- 7 libros, 5 autores, 4 usuarios
- Sistema de multas por retraso
- Préstamos activos y vencidos

---

## 🎯 ¿Cómo Usar estos Recursos?

### Durante la Teoría (Bloque 1 - 2 horas):

- Tener abierto el **cheatsheet** para referenciar comandos
- Consultar **troubleshooting** si aparecen errores en las demos

### Durante Práctica 1 (Bloque 2 - 2 horas):

1. Abrir `template-basico.yml`
2. Copiar y pegar en tu proyecto
3. Adaptar nombres y credenciales
4. Seguir las instrucciones del template

### Durante Práctica 2 (Bloque 3 - 1.5 horas):

1. Elegir tu dominio asignado (restaurante, biblioteca, gimnasio, etc.)
2. Abrir el ejemplo más similar en `ejemplos-dominios/`
3. **NO copiar literalmente** - usar como inspiración
4. Adaptar las tablas a tu dominio específico
5. Personalizar el frontend con tu contexto
6. Usar `template-frontend.yml` como base

### Al Encontrar Errores:

1. **NO entrar en pánico** 😌
2. Copiar el mensaje de error completo
3. Buscar en `troubleshooting.md` (Ctrl+F)
4. Seguir los pasos de la solución
5. Si persiste, preguntar al instructor

---

## 📊 Comparación de Templates

| Template     | Servicios                         | Complejidad | Tiempo Setup | Uso Recomendado                           |
| ------------ | --------------------------------- | ----------- | ------------ | ----------------------------------------- |
| **Básico**   | DB + Adminer                      | ⭐ Baja     | 5 min        | Primera práctica, aprender Docker Compose |
| **Frontend** | Nginx + DB + Adminer              | ⭐⭐ Media  | 10 min       | Práctica 2, proyectos con interfaz web    |
| **Completo** | Frontend + Backend + DB + Adminer | ⭐⭐⭐ Alta | 30 min       | Proyectos finales, aplicaciones reales    |

---

## 💡 Tips para Estudiantes

### ✅ DO's (Hacer):

1. **Leer los comentarios** en los templates (explican cada sección)
2. **Probar primero** el template básico antes del completo
3. **Consultar troubleshooting** antes de preguntar (autonomía)
4. **Adaptar** los ejemplos de dominios, no copiarlos literalmente
5. **Guardar** estos archivos como referencia futura

### ❌ DON'Ts (Evitar):

1. **NO copiar** sin entender (no aprenderás)
2. **NO usar** contraseñas débiles como "123456"
3. **NO ignorar** los mensajes de error (leer con atención)
4. **NO mezclar** contenido de diferentes templates sin comprender
5. **NO olvidar** el archivo `.env` (es crítico)

---

## 🔍 Búsqueda Rápida

**¿Necesitas encontrar algo?**

| Busco...                         | Archivo                           | Sección                  |
| -------------------------------- | --------------------------------- | ------------------------ |
| Comando para iniciar servicios   | `cheatsheet-comandos.md`          | Comandos Básicos #1      |
| Error "port already allocated"   | `troubleshooting.md`              | Problema #1              |
| Template con frontend            | `templates/template-frontend.yml` | -                        |
| Ejemplo de tablas relacionadas   | `ejemplos-dominios/biblioteca.md` | Base de Datos            |
| Cómo conectar desde backend a DB | `troubleshooting.md`              | Problema #2              |
| Sintaxis de volumes en YAML      | `templates/template-basico.yml`   | Comentarios en volúmenes |

---

## 📚 Orden de Lectura Recomendado

### Para principiantes absolutos:

1. `cheatsheet-comandos.md` - Sección "Comandos Básicos"
2. `template-basico.yml` - Leer todos los comentarios
3. `troubleshooting.md` - Índice rápido (solo saber que existe)
4. Intentar Práctica 1
5. `ejemplos-dominios/restaurante.md` - Como inspiración para Práctica 2

### Para quienes ya conocen Docker:

1. `template-frontend.yml` - Para proyectos web
2. `ejemplos-dominios/` - Elegir dominio similar al tuyo
3. `troubleshooting.md` - Marcar como referencia
4. `template-completo.yml` - Para proyectos avanzados

---

## 🎓 Principios de Aprendizaje

Estos recursos están diseñados siguiendo el principio **80/20**:

- **20% de conceptos** esenciales de Docker Compose
- **80% de capacidad** para implantar software con contenedores

**No necesitas**:

- Ser experto en Docker para usar estos recursos
- Memorizar todos los comandos (tienes el cheatsheet)
- Entender todos los parámetros avanzados (solo lo esencial)

**Sí necesitas**:

- Leer los comentarios en los templates
- Probar los ejemplos modificando valores
- Consultar troubleshooting cuando algo falle
- Adaptar los ejemplos a tu dominio asignado

---

## 🆘 ¿Sigues Atascado?

Si después de consultar estos recursos aún tienes problemas:

1. **Verifica que seguiste todos los pasos** del troubleshooting
2. **Revisa los logs**: `docker compose logs -f <servicio>`
3. **Valida el YAML**: `docker compose config`
4. **Pregunta al instructor** con contexto:
   - ¿Qué intentabas hacer?
   - ¿Qué comando ejecutaste?
   - ¿Qué error apareció? (mensaje completo)
   - ¿Qué has intentado ya?

---

## 📖 Recursos Externos Recomendados

- **Documentación oficial Docker Compose**: https://docs.docker.com/compose/
- **Docker Hub (imágenes)**: https://hub.docker.com/
- **PostgreSQL Docs**: https://www.postgresql.org/docs/
- **Nginx Docs**: https://nginx.org/en/docs/

---

## ✅ Checklist: ¿Dominas los Recursos?

Marca ✅ cuando puedas hacer esto sin ayuda:

- [ ] Iniciar un stack con `docker compose up -d`
- [ ] Identificar el estado de los servicios con `docker compose ps`
- [ ] Ver logs de un servicio específico
- [ ] Conectar Adminer a PostgreSQL usando el nombre del servicio
- [ ] Solucionar error "port already allocated"
- [ ] Crear un `docker-compose.yml` desde cero usando un template
- [ ] Adaptar el ejemplo de restaurante a tu dominio
- [ ] Ejecutar consultas SQL en Adminer
- [ ] Verificar persistencia de datos tras `docker compose down`
- [ ] Explicar la diferencia entre `down` y `down -v`

**Si marcaste 8+ ✅**: Estás listo para proyectos reales 🎉  
**Si marcaste 5-7 ✅**: Sigue practicando con los templates  
**Si marcaste <5 ✅**: Revisa nuevamente la teoría y haz Práctica 1

---

**Última actualización**: Semana 2 - Bootcamp Implantación de Software SENA CGMLTI  
**Versión**: Docker Compose v2.39.4+  
**Mantenedor**: Instructor del bootcamp
