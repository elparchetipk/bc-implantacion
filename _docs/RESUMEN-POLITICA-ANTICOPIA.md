# Resumen: Política Anticopia Implementada

**Fecha**: 5 de octubre de 2025  
**Bootcamp**: Implantación de Software - SENA CGMLTI  
**Objetivo**: Evitar copia entre aprendices garantizando aprendizaje real

---

## 📋 Cambios Realizados

### 1. Documentación Actualizada

#### `.github/copilot-instructions.md`

**Sección agregada**: "Política Anticopia y Asignación de Dominios"

**Contenido clave**:

- Cada aprendiz recibe un dominio único y aleatorio
- No hay dominios repetidos entre aprendices
- El dominio es el contexto para todos los ejemplos
- NUNCA mencionar nombres de aprendices ni dominios asignados
- Usar ejemplos genéricos en material compartido
- Los aprendices adaptan cada práctica a su dominio

**Impacto**: GitHub Copilot ahora conoce la política y la aplica al generar contenido.

---

#### `_docs/POLITICA-ANTICOPIA.md` (NUEVO - 19 KB)

**Contenido completo**:

1. **Resumen ejecutivo** del problema y la solución
2. **Pool de 50+ dominios** únicos categorizados
3. **Proceso de asignación** aleatoria
4. **Estructura de carpetas** individuales
5. **Ejemplos completos** de dominio (Restaurante "La Trattoria")
6. **Rúbrica adaptada** para evaluación con dominios
7. **Detección de copias** - señales de alerta
8. **Reglas estrictas** para material compartido
9. **Casos de uso** con ejemplos reales
10. **Scripts de soporte** (Python)
11. **Métricas de éxito** e indicadores
12. **Proceso de implementación** en 4 fases

**Impacto**: Documentación completa y exhaustiva de la política para referencia del instructor.

---

#### `bootcamp/semana-01/4-asignación_dominios_aprendiz/README.md` (NUEVO)

**Contenido**:

- Explicación de la política anticopia
- Estructura de asignaciones individuales
- Ejemplos de adaptación por dominio
- Criterios de evaluación
- Pool de 50+ dominios disponibles
- Proceso de asignación
- Beneficios pedagógicos

**Archivos adicionales**:

- `.gitkeep` - Mantiene la carpeta en el proyecto

**Impacto**: Guía clara para el instructor sobre cómo gestionar asignaciones individuales.

---

### 2. Configuración de Privacidad

#### `.gitignore` (MODIFICADO)

**Reglas agregadas**:

```gitignore
# Asignaciones individuales por aprendiz
**/4-asignación_dominios_aprendiz/aprendiz-*/
!**/4-asignación_dominios_aprendiz/README.md
!**/4-asignación_dominios_aprendiz/.gitkeep

# Archivo de listado de aprendices
_docs/APRENDICES-3147234.md
```

**Comportamiento**:

- ✅ Carpeta `4-asignación_dominios_aprendiz/` **visible en el proyecto**
- ✅ Archivos `README.md` y `.gitkeep` **versionados en git**
- ❌ Subcarpetas `aprendiz-*/` **ignoradas en git** (no se suben)
- ❌ Archivo `APRENDICES-3147234.md` **ignorado en git** (no se sube)

**Resultado**: Instructor tiene acceso local a asignaciones personalizadas, pero no se exponen públicamente.

---

### 3. Corrección de Horarios

#### `bootcamp/semana-01/README.md` (MODIFICADO)

**Cambio principal**: Eliminada división "Sesión Mañana / Sesión Tarde"

**Nueva distribución** (6 horas totales):

```
Bloque 1: Introducción y Fundamentos (2h)
  - Hora 1 (0:00-1:00): Proceso de implantación
  - Hora 2 (1:00-2:00): Hardware de servidores

☕ BREAK (30 min)

Bloque 2: Contenedores y Docker (2h)
  - Hora 3 (2:30-3:30): Introducción a Docker
  - Hora 4 (3:30-4:30): Instalación de Docker

Bloque 3: Práctica Aplicada (1.5h)
  - Hora 5 (4:30-5:30): Primeros contenedores
  - Hora 6 (5:30-6:00): PostgreSQL y cierre
```

**Impacto**: Distribución flexible sin asumir jornada específica (puede ser mañana, tarde, o mixta según el centro de formación).

---

## 🎯 Política en Resumen

### Funcionamiento

1. **Asignación**: Cada aprendiz recibe un dominio único al inicio
2. **Desarrollo**: Adapta todos los ejemplos a su dominio
3. **Entrega**: Código personalizado con su contexto
4. **Evaluación**: Instructor verifica comprensión y originalidad

### Ejemplos de Dominios

- Restaurante, Biblioteca, Clínica Veterinaria
- Gimnasio, Inmobiliaria, Floristería
- Taller Mecánico, Academia de Música, Agencia de Viajes
- ...hasta 50+ dominios únicos

### Detección de Copia

**Señal de alerta**: Si aprendiz A (Restaurante) entrega:

```sql
CREATE TABLE libros (...)  -- ❌ No tiene sentido en restaurante
```

**Evidencia**: Copió de aprendiz con dominio "Biblioteca"

---

## ✅ Beneficios Logrados

### Para el Aprendiz

- ✅ Aprendizaje profundo (debe entender para adaptar)
- ✅ Portfolio personalizado y único
- ✅ Preparación para contextos reales
- ✅ Pensamiento crítico desarrollado

### Para el Instructor

- ✅ Detección fácil de copias (código idéntico = alerta)
- ✅ Evaluación justa e individual
- ✅ Evidencia clara de comprensión
- ✅ Retroalimentación contextualizada

### Para el SENA

- ✅ Integridad académica protegida
- ✅ Calidad educativa garantizada
- ✅ Egresados verdaderamente competentes
- ✅ Innovación pedagógica diferenciadora

---

## 📊 Archivos Creados/Modificados

| Archivo                                                       | Acción     | Tamaño     | Estado   |
| ------------------------------------------------------------- | ---------- | ---------- | -------- |
| `.github/copilot-instructions.md`                             | Modificado | +60 líneas | ✅ Listo |
| `_docs/POLITICA-ANTICOPIA.md`                                 | Creado     | 19 KB      | ✅ Listo |
| `bootcamp/semana-01/4-asignación_dominios_aprendiz/README.md` | Creado     | 6 KB       | ✅ Listo |
| `bootcamp/semana-01/4-asignación_dominios_aprendiz/.gitkeep`  | Creado     | -          | ✅ Listo |
| `.gitignore`                                                  | Modificado | +5 líneas  | ✅ Listo |
| `bootcamp/semana-01/README.md`                                | Modificado | Horarios   | ✅ Listo |

**Total**: 6 archivos (4 modificados, 2 creados)

---

## 🚀 Próximos Pasos

### Antes del Bootcamp (Preparación)

1. ✅ Política documentada (completado)
2. ⏳ Obtener lista de aprendices de la ficha 3147234
3. ⏳ Ejecutar script de asignación aleatoria de dominios
4. ⏳ Crear carpetas individuales con asignaciones personalizadas
5. ⏳ Revisar y aprobar asignaciones

### Día 1 del Bootcamp (Inducción)

1. ⏳ Explicar la política a los aprendices
2. ⏳ Entregar dominio individual a cada uno (privado)
3. ⏳ Aclarar beneficios y reglas
4. ⏳ Responder preguntas

### Durante el Bootcamp (Seguimiento)

1. ⏳ Verificar adaptación al dominio en cada entrega
2. ⏳ Detectar y actuar sobre posibles copias
3. ⏳ Retroalimentación contextualizada
4. ⏳ Registro de avances individuales

---

## 📝 Notas Importantes

### Confidencialidad

- 🔐 Archivo `_docs/APRENDICES-3147234.md` contiene datos personales
- 🔐 Carpetas `aprendiz-*/` contienen asignaciones individuales
- 🔐 Ambos ignorados en git pero visibles localmente
- 🔐 Solo instructor tiene acceso

### Reglas de Oro

1. ❌ **NUNCA** mencionar nombres de aprendices en ejemplos públicos
2. ❌ **NUNCA** mencionar dominios específicos asignados
3. ✅ **SIEMPRE** usar ejemplos genéricos en teoría/prácticas
4. ✅ **SIEMPRE** verificar adaptación al dominio en entregas

---

## 🎓 Impacto Esperado

### Métricas de Éxito

- **Originalidad**: > 95% de entregas únicas
- **Comprensión**: > 85% pueden explicar su código
- **Satisfacción**: > 4.0/5.0 en encuestas
- **Empleabilidad**: Portfolio personalizado aumenta contratación

### Diferenciación

Esta metodología posiciona al SENA como líder en:

- ✅ Innovación pedagógica
- ✅ Integridad académica
- ✅ Formación de calidad
- ✅ Preparación para el mercado laboral

---

**Estado**: ✅ Implementación completa  
**Listo para**: Asignar dominios a aprendices de la ficha 3147234  
**Última actualización**: 5 de octubre de 2025
