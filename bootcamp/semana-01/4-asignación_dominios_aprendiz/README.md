# Asignaciones Individuales por Dominio

## ⚠️ Política Anticopia

Esta carpeta contiene las **asignaciones personalizadas** para cada aprendiz. Cada estudiante trabaja sobre un **dominio único y aleatorio** para garantizar la comprensión individual y evitar la copia.

---

## 🎯 Objetivo de la Política

1. **Evitar copia-pega** entre aprendices
2. **Fomentar comprensión real** del código y conceptos
3. **Personalizar el aprendizaje** según contexto específico
4. **Desarrollar pensamiento crítico** al adaptar soluciones

---

## 📋 Estructura de Dominios

Cada aprendiz recibe:

- ✅ **Dominio único** (ej: Restaurante, Biblioteca, Clínica Veterinaria)
- ✅ **Contexto de negocio** específico con entidades y relaciones
- ✅ **Requisitos funcionales** adaptados al dominio
- ✅ **Entregables técnicos** idénticos para todos (misma rúbrica)

---

## 🔒 Confidencialidad

### Esta carpeta está:

- ❌ **Ignorada en git** (`.gitignore`)
- ✅ **Visible en el proyecto** (no en `.git/info/exclude`)
- 🔐 **Accesible solo por el instructor**

### Contenido de asignaciones individuales:

```
4-asignación_dominios_aprendiz/
├── README.md (este archivo)
├── aprendiz-001-[nombre]/
│   ├── dominio.md
│   ├── asignacion-semana-01.md
│   └── rubrica.md
├── aprendiz-002-[nombre]/
│   ├── dominio.md
│   ├── asignacion-semana-01.md
│   └── rubrica.md
└── ...
```

---

## 📝 Ejemplo de Dominio

### Aprendiz: [Nombre Aleatorio 001]

**Dominio Asignado**: **Restaurante**

**Contexto**:

- Restaurante de comida italiana con 15 mesas
- Menú con 40 platos (entradas, platos fuertes, postres)
- 8 empleados (meseros, cocineros, cajero)
- Sistema de reservas y pedidos

**Entidades principales**:

- `mesas` (id, numero, capacidad, ubicacion)
- `menu` (id, nombre, categoria, precio, ingredientes)
- `empleados` (id, nombre, puesto, turno, salario)
- `pedidos` (id, mesa_id, empleado_id, fecha, total, estado)
- `reservas` (id, cliente_nombre, mesa_id, fecha_hora, personas)

**Asignación Semana 1**:

1. Documentar especificaciones de hardware para este restaurante
2. Instalar Docker y crear contenedor PostgreSQL
3. Crear las tablas del dominio "Restaurante"
4. Insertar 10 registros de ejemplo en cada tabla

---

## ✅ Criterios de Evaluación

### El instructor verifica:

1. **Código refleja el dominio**

   - Nombres de tablas coherentes con dominio asignado
   - Variables con nomenclatura del contexto
   - Datos de ejemplo realistas

2. **Comprensión demostrada**

   - Comentarios explicativos (¿Qué? ¿Para qué? ¿Cómo?)
   - Adaptación inteligente de ejemplos generales
   - Resolución de problemas contextualizados

3. **Requisitos técnicos cumplidos**

   - Docker instalado y funcionando
   - PostgreSQL corriendo en contenedor
   - Persistencia con volúmenes
   - Capturas de pantalla evidenciando trabajo

4. **Originalidad**
   - No hay código idéntico entre aprendices
   - Cada implementación es única al dominio

---

## 🚫 Reglas para Material Compartido

### En material teórico y prácticas generales:

1. ❌ **NUNCA mencionar nombres de aprendices**
2. ❌ **NUNCA mencionar dominios específicos asignados**
3. ✅ **Usar ejemplos genéricos** (Sistema de gestión, Aplicación empresarial)
4. ✅ **Proporcionar plantillas adaptables**
5. ✅ **Los aprendices contextualizan** según su dominio

---

## 📊 Ejemplo de Adaptación

### Material general (Teoría/Prácticas):

```sql
-- Crear tabla genérica de entidades
CREATE TABLE entidades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Aprendiz con dominio "Restaurante":

```sql
-- ¿Qué? Tabla para almacenar los platos del menú
-- ¿Para qué? Gestionar el catálogo de comidas del restaurante
CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),  -- ej: "Pasta Carbonara"
    descripcion TEXT,     -- ej: "Pasta con salsa de huevo y tocino"
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Aprendiz con dominio "Biblioteca":

```sql
-- ¿Qué? Tabla para almacenar libros de la biblioteca
-- ¿Para qué? Gestionar el catálogo de libros disponibles
CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),  -- ej: "Cien Años de Soledad"
    descripcion TEXT,     -- ej: "Novela de Gabriel García Márquez"
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🎓 Beneficios de esta Metodología

### Para el Aprendiz:

- ✅ Aprendizaje profundo (no superficial)
- ✅ Comprensión real de conceptos
- ✅ Capacidad de adaptación a contextos diferentes
- ✅ Portfolio personalizado

### Para el Instructor:

- ✅ Detección fácil de copias
- ✅ Evaluación justa e individual
- ✅ Evidencia de comprensión real
- ✅ Retroalimentación específica

### Para el Bootcamp:

- ✅ Integridad académica
- ✅ Calidad del aprendizaje
- ✅ Preparación para el mundo real
- ✅ Diferenciación del SENA

---

## 📚 Dominios Disponibles (Referencia Instructor)

Pool de 50+ dominios únicos:

1. Restaurante
2. Biblioteca
3. Clínica Veterinaria
4. Gimnasio
5. Inmobiliaria
6. Floristería
7. Taller Mecánico
8. Academia de Música
9. Agencia de Viajes
10. Tienda de Mascotas
11. Farmacia
12. Hotel
13. Salón de Belleza
14. Agencia de Seguros
15. Centro Educativo
16. Estudio Fotográfico
17. Tienda de Ropa
18. Panadería
19. Consultorio Médico
20. Agencia de Publicidad
21. Tienda de Deportes
22. Lavandería
23. Parqueadero
24. Centro de Copiado
25. Ferretería
26. Juguetería
27. Papelería
28. Óptica
29. Mueblería
30. Agencia de Empleos

_(Continuar hasta 50+ dominios únicos)_

---

## 🔄 Proceso de Asignación

1. **Instructor genera** lista de aprendices
2. **Sistema asigna** dominio aleatorio (sin repetir)
3. **Instructor crea** carpeta individual con asignación contextualizada
4. **Aprendiz recibe** su dominio al inicio del bootcamp
5. **Aprendiz desarrolla** todas las prácticas sobre ese dominio
6. **Instructor evalúa** considerando el contexto específico

---

## 📅 Gestión por Semanas

Cada semana, el aprendiz recibe:

- `asignacion-semana-XX.md` - Requisitos específicos
- Adapta ejemplos generales a su dominio
- Entrega evidencias personalizadas
- Recibe retroalimentación contextualizada

**Ejemplo**:

- Semana 1: Especificaciones de hardware + PostgreSQL con datos del dominio
- Semana 2: Docker Compose con servicios del dominio
- Semana 3: Migración de datos del sistema antiguo del dominio
- ...y así sucesivamente

---

## 🎯 Resultado Esperado

Al finalizar el bootcamp, cada aprendiz tiene:

✅ Un **proyecto completo** de implantación de software  
✅ **Contextualizado** en un dominio de negocio real  
✅ **Documentación** técnica profesional  
✅ **Portfolio** único y demostrable  
✅ **Comprensión profunda** de todos los conceptos

---

**Última actualización**: 5 de octubre de 2025  
**Bootcamp**: Implantación de Software - ADSO CGMLTI SENA  
**Instructor**: [Nombre del instructor]
