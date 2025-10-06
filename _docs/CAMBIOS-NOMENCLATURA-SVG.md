# Cambios en Nomenclatura de Archivos SVG

**Fecha**: 5 de octubre de 2025  
**Autor**: Sistema automatizado  
**Tipo**: Refactorización de nomenclatura

---

## 📋 Resumen

Se han renombrado todos los archivos SVG de recursos gráficos para incluir un **número de secuencia** que refleja el orden de aparición en la documentación del bootcamp.

---

## 🔄 Cambios Realizados

### Archivos Renombrados

| Nombre Anterior                 | Nombre Nuevo                      | Orden |
| ------------------------------- | --------------------------------- | ----- |
| `proceso-implantacion.svg`      | `1-proceso-implantacion.svg`      | 1°    |
| `hardware-servidores.svg`       | `2-hardware-servidores.svg`       | 2°    |
| `arquitectura-docker-stack.svg` | `3-arquitectura-docker-stack.svg` | 3°    |
| `red-docker.svg`                | `4-red-docker.svg`                | 4°    |
| `docker-compose-workflow.svg`   | `5-docker-compose-workflow.svg`   | 5°    |
| `respaldo-migracion.svg`        | `6-respaldo-migracion.svg`        | 6°    |

---

## 📁 Ubicación de Archivos

```
bootcamp/
└── semana-01/
    └── assets/
        ├── 1-proceso-implantacion.svg
        ├── 2-hardware-servidores.svg
        ├── 3-arquitectura-docker-stack.svg
        ├── 4-red-docker.svg
        ├── 5-docker-compose-workflow.svg
        ├── 6-respaldo-migracion.svg
        └── README.md (actualizado)
```

---

## 📝 Orden Lógico de Presentación

### 1. Proceso de Implantación (1-proceso-implantacion.svg)

- **Objetivo**: Introducir el concepto completo del proceso de implantación
- **Contenido**: 5 fases del proceso (Planificación → Preparación → Implementación → Validación → Documentación)
- **Uso**: Presentación inicial del bootcamp, marco conceptual

### 2. Hardware de Servidores (2-hardware-servidores.svg)

- **Objetivo**: Explicar fundamentos de infraestructura física
- **Contenido**: Tipos de servidores (RACK, BLADE), arreglos de discos, especificaciones por ambiente
- **Uso**: Semana 1-2 (Fundamentos de Hardware y Plataformas)

### 3. Arquitectura Docker Stack (3-arquitectura-docker-stack.svg)

- **Objetivo**: Mostrar stack tecnológico preferido del bootcamp
- **Contenido**: Nginx + REST API + PostgreSQL 15+ con Docker Compose
- **Uso**: Semana 5 (Introducción a contenedores y stack tecnológico)

### 4. Red Docker (4-red-docker.svg)

- **Objetivo**: Explicar networking en entornos containerizados
- **Contenido**: Redes bridge, IPs internas, puertos expuestos, comunicación entre servicios
- **Uso**: Semana 5 (Gestión de redes y volúmenes en Docker)

### 5. Docker Compose Workflow (5-docker-compose-workflow.svg)

- **Objetivo**: Enseñar el ciclo de vida de aplicaciones con Docker Compose
- **Contenido**: Comandos principales, estados de contenedores, gestión de volúmenes
- **Uso**: Semana 5 (Práctica de orquestación con docker-compose)

### 6. Respaldo y Migración (6-respaldo-migracion.svg)

- **Objetivo**: Planificar estrategias de datos y migración
- **Contenido**: Sistema origen/destino, proceso de respaldo, ubicaciones, cronograma, mejores prácticas
- **Uso**: Semana 7 (Migración y Respaldo de Datos)

---

## 📚 Documentación Actualizada

### Archivos Modificados:

1. **`bootcamp/semana-01/assets/README.md`**

   - ✅ Actualizado con nuevos nombres de archivos
   - ✅ Reorganizado según orden de presentación
   - ✅ Agregado contenido completo de `5-docker-compose-workflow.svg`
   - ✅ Corregida sección "Uso en Markdown" con todos los diagramas

2. **`.github/copilot-instructions.md`**
   - ✅ Agregada convención de nomenclatura en "Consideraciones Especiales"
   - ✅ Especifica formato: número + guión + nombre descriptivo

---

## 🎯 Convención de Nomenclatura

### Reglas Establecidas:

```
[número]-[nombre-descriptivo].svg

Donde:
- número: Orden de aparición en documentación (1, 2, 3, ...)
- nombre-descriptivo: kebab-case, descriptivo del contenido
- extensión: .svg (siempre)
```

### Ejemplos Válidos:

- ✅ `1-proceso-implantacion.svg`
- ✅ `2-hardware-servidores.svg`
- ✅ `10-arquitectura-microservicios.svg`

### Ejemplos Inválidos:

- ❌ `proceso-implantacion.svg` (sin número)
- ❌ `01-proceso-implantacion.svg` (número con cero inicial)
- ❌ `proceso_implantacion.svg` (snake_case en lugar de kebab-case)
- ❌ `ProcesoImplantacion.svg` (PascalCase)

---

## 🔍 Verificación

### Comandos para Verificar:

```bash
# Listar archivos SVG en orden
ls -1 bootcamp/semana-01/assets/*.svg

# Verificar que no queden archivos sin número
find bootcamp -name "*.svg" -not -name "[0-9]*-*.svg"

# Contar archivos SVG
find bootcamp/semana-01/assets -name "*.svg" | wc -l
```

### Resultado Esperado:

```
bootcamp/semana-01/assets/1-proceso-implantacion.svg
bootcamp/semana-01/assets/2-hardware-servidores.svg
bootcamp/semana-01/assets/3-arquitectura-docker-stack.svg
bootcamp/semana-01/assets/4-red-docker.svg
bootcamp/semana-01/assets/5-docker-compose-workflow.svg
bootcamp/semana-01/assets/6-respaldo-migracion.svg

Total: 6 archivos ✅
```

---

## 📊 Impacto del Cambio

### Ventajas:

1. **Orden Visual**: Los archivos se listan automáticamente en orden de uso
2. **Facilita Navegación**: Instructores y estudiantes pueden seguir secuencia lógica
3. **Escalabilidad**: Fácil agregar nuevos diagramas sin conflictos
4. **Consistencia**: Nomenclatura estándar para todo el bootcamp
5. **Documentación Clara**: El número indica claramente cuándo usar cada diagrama

### Consideraciones:

- Si se agregan diagramas intermedios, usar decimales (ej: `2.5-tema-intermedio.svg`) o renumerar
- Mantener coherencia entre semanas (cada semana sus propios números)
- Actualizar referencias en documentación cuando se agreguen nuevos diagramas

---

## 🚀 Próximos Pasos

### Para Semanas 2-9:

1. Crear directorio `bootcamp/semana-XX/assets/` para cada semana
2. Nombrar diagramas SVG con numeración desde 1 (relativo a la semana)
3. Crear `README.md` en cada directorio `assets/` documentando los diagramas
4. Seguir tema dark (#1e1e1e) y estilo flat (sin degradados)

### Ejemplo para Semana 2:

```
bootcamp/semana-02/assets/
├── 1-instalacion-linux-server.svg
├── 2-estructura-directorios-linux.svg
├── 3-gestion-paquetes.svg
└── README.md
```

---

## 📖 Referencias

- **Copilot Instructions**: `.github/copilot-instructions.md` → Sección "Consideraciones Especiales"
- **Documentación de Assets**: `bootcamp/semana-01/assets/README.md`
- **Guía de Estilo SVG**: Tema dark (#1e1e1e), flat design, sin degradados

---

## ✅ Checklist de Implementación

- [x] Renombrar 6 archivos SVG en `semana-01/assets/`
- [x] Actualizar `semana-01/assets/README.md` con nuevos nombres
- [x] Actualizar sección "Uso en Markdown" con todos los diagramas
- [x] Agregar convención a `.github/copilot-instructions.md`
- [x] Crear documentación de cambios (este archivo)
- [x] Verificar que no hay referencias rotas
- [ ] Aplicar convención a semanas futuras (2-9) cuando se creen

---

**Estado**: ✅ Completado  
**Versión**: 1.0  
**Última actualización**: 5 de octubre de 2025
