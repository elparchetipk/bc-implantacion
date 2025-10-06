# Guía de Contribución

¡Gracias por tu interés en contribuir al Bootcamp de Implantación de Software! 🎉

## 🎯 Sobre el Proyecto

Este bootcamp está diseñado para **Aprendices de Análisis y Desarrollo de Software (ADSO)** del Centro de Gestión de Mercados, Logística y Tecnologías de la Información (CGMLTI) - Regional Distrito Capital, SENA Colombia.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo Puedo Contribuir?](#cómo-puedo-contribuir)
- [Guías de Estilo](#guías-de-estilo)
- [Proceso de Revisión](#proceso-de-revisión)

---

## Código de Conducta

Este proyecto se adhiere a nuestro [Código de Conducta](./CODE_OF_CONDUCT.md). Al participar, se espera que mantengas este código.

---

## ¿Cómo Puedo Contribuir?

### 🐛 Reportar Bugs

Si encuentras un error:

1. **Verifica** que no exista un issue similar
2. **Crea un nuevo issue** usando la plantilla de bug report
3. **Incluye**:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Screenshots si aplica
   - Información del entorno (OS, versiones)

### 💡 Sugerir Mejoras

Para proponer nuevas características:

1. **Revisa** los issues existentes
2. **Crea un issue** con la etiqueta `enhancement`
3. **Describe**:
   - Problema que resuelve
   - Solución propuesta
   - Alternativas consideradas
   - Contexto adicional

### 📝 Mejorar Documentación

La documentación siempre puede mejorar:

- Corregir errores tipográficos
- Aclarar explicaciones confusas
- Agregar ejemplos
- Traducir contenido
- Crear diagramas adicionales

### 🎨 Contribuir con Contenido

Para agregar o mejorar contenido educativo:

1. **Contenido en español**, código en inglés
2. Seguir estructura de carpetas existente
3. Usar plantillas de código comentado
4. Incluir recursos gráficos SVG cuando sea apropiado
5. Agregar ejercicios prácticos

---

## Guías de Estilo

### 📁 Estructura de Archivos

```
bootcamp/
└── semana-XX/
    ├── 1-teoria/
    ├── 2-practicas/
    ├── 3-recursos/
    ├── 4-asignación_dominios_aprendiz/
    └── assets/
        └── N-nombre-descriptivo.svg
```

### 💻 Código

**Nomenclatura:**

- Variables, funciones, clases: `inglés` (camelCase o snake_case según lenguaje)
- Comentarios: `español` con formato educativo (¿Qué? ¿Para qué? ¿Cómo?)
- Archivos: `kebab-case` en inglés

**Ejemplo:**

```yaml
# docker-compose.yml

# ¿Qué?: Definición de servicios de la aplicación
# ¿Para qué?: Orquestar contenedores de forma reproducible
services:
  # ¿Qué?: Servicio de base de datos PostgreSQL
  # ¿Para qué?: Almacenar datos de la aplicación de forma persistente
  database:
    image: postgres:15-alpine
    # ...
```

### 🎨 Recursos Gráficos (SVG)

- **Formato**: SVG vectorial
- **Tema**: Dark (`#1e1e1e` background)
- **Estilo**: Flat design (sin degradados)
- **Nomenclatura**: `N-nombre-descriptivo.svg` (número + kebab-case)
- **Colores estándar**:
  - Azul `#58a6ff`: Elementos principales
  - Verde `#7ee787`: Estados exitosos
  - Naranja `#ffa657`: Advertencias
  - Púrpura `#d2a8ff`: Datos/almacenamiento
  - Rojo `#f78166`: Crítico
  - Gris `#8b949e`: Secundario

### 📝 Commits

Usar **Conventional Commits** en inglés:

```bash
# Tipos permitidos
feat:     # Nueva característica
fix:      # Corrección de bug
docs:     # Cambios en documentación
style:    # Formato, espacios, etc.
refactor: # Refactorización de código
test:     # Agregar o modificar tests
chore:    # Tareas de mantenimiento

# Formato
<type>(<scope>): <description>

# Ejemplos
feat(week-05): add docker compose tutorial
docs(readme): update installation instructions
fix(scripts): correct autocommit path resolution
```

### 📚 Documentación

- **Markdown** para todo
- **Español** para explicaciones
- **Inglés** para términos técnicos (Docker, Git, API, etc.)
- **Títulos descriptivos** y estructura jerárquica clara
- **Ejemplos prácticos** en todos los conceptos
- **TOC** (tabla de contenidos) en docs largos

---

## Proceso de Contribución

### 1. Fork y Clone

```bash
# Fork en GitHub, luego:
git clone https://github.com/TU-USUARIO/bc-implantacion.git
cd bc-implantacion
```

### 2. Crear Branch

```bash
# Nombre descriptivo en inglés
git checkout -b feature/add-week-03-content
git checkout -b fix/docker-compose-syntax
git checkout -b docs/improve-readme
```

### 3. Hacer Cambios

- Seguir guías de estilo
- Probar cambios localmente
- Agregar documentación si es necesario
- Actualizar tests si aplica

### 4. Commit

```bash
git add .
git commit -m "feat(week-03): add linux server installation guide"
```

### 5. Push y Pull Request

```bash
git push origin feature/add-week-03-content
```

Luego en GitHub:

1. Crear Pull Request
2. Describir cambios claramente
3. Referenciar issues relacionados
4. Esperar revisión

---

## Proceso de Revisión

### Para Revisores

- ✅ Verifica que siga guías de estilo
- ✅ Prueba cambios localmente
- ✅ Revisa claridad de documentación
- ✅ Verifica que el código funcione
- ✅ Da feedback constructivo

### Para Contribuidores

- 🔄 Responde a comentarios
- 🔧 Realiza cambios solicitados
- 📝 Mantén conversación profesional
- ⏰ Sé paciente con el proceso

---

## 🎓 Áreas de Contribución Prioritarias

### Alta Prioridad

- [ ] Contenido para semanas 2-9
- [ ] Ejercicios prácticos con Docker
- [ ] Casos de estudio reales
- [ ] Diagramas SVG adicionales
- [ ] Rúbricas de evaluación

### Prioridad Media

- [ ] Traducciones de recursos
- [ ] Videos tutoriales
- [ ] Quizzes interactivos
- [ ] Guías de troubleshooting
- [ ] Mejoras de documentación

### Prioridad Baja

- [ ] Optimización de scripts
- [ ] Mejoras estéticas
- [ ] Refactorización de código
- [ ] Tests adicionales

---

## 📞 ¿Tienes Preguntas?

- **Issues**: [GitHub Issues](../../issues)
- **Discusiones**: [GitHub Discussions](../../discussions)
- **Email**: [Contacto del equipo]

---

## 🙏 Reconocimientos

Todos los contribuidores serán agregados a [AUTHORS.md](./AUTHORS.md).

---

**¡Gracias por contribuir a la educación abierta!** 🎉
