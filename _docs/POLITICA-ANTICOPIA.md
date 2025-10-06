# Política Anticopia: Asignación de Dominios Únicos

## 📋 Resumen Ejecutivo

Esta política establece un sistema de asignación de **dominios únicos y aleatorios** a cada aprendiz para garantizar:

1. ✅ **Comprensión real** del contenido (no copia-pega)
2. ✅ **Aprendizaje personalizado** contextualizado
3. ✅ **Integridad académica** del bootcamp
4. ✅ **Evaluación justa** e individual

---

## 🎯 Problema que Resuelve

### Escenario Tradicional (Sin la Política)

**Problema**: Aprendiz A completa la práctica, comparte el código con Aprendices B, C, D...

**Resultado**:
- ❌ Código idéntico entre múltiples aprendices
- ❌ No hay evidencia de comprensión real
- ❌ Aprendices aprueban sin aprender
- ❌ Dificultad para detectar copias
- ❌ Injusticia para quien sí estudia

**Ejemplo real**:
```sql
-- Todos entregan exactamente esto:
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);
```

---

### Con Política de Dominios Únicos

**Solución**: Cada aprendiz trabaja sobre un dominio de negocio diferente.

**Resultado**:
- ✅ Código único por aprendiz (diferente contexto)
- ✅ Evidencia clara de comprensión
- ✅ Imposible copiar sin adaptar (requiere entender)
- ✅ Detección automática de copias
- ✅ Evaluación justa

**Ejemplo con dominios**:

**Aprendiz A (Restaurante)**:
```sql
-- ¿Qué? Tabla para platos del menú
-- ¿Para qué? Gestionar catálogo de comidas
CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    nombre_plato VARCHAR(100),
    precio DECIMAL(10,2)
);
```

**Aprendiz B (Biblioteca)**:
```sql
-- ¿Qué? Tabla para libros del catálogo
-- ¿Para qué? Gestionar inventario de libros
CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100)
);
```

**Aprendiz C (Gimnasio)**:
```sql
-- ¿Qué? Tabla para miembros del gimnasio
-- ¿Para qué? Gestionar inscripciones
CREATE TABLE miembros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    membresia VARCHAR(50)
);
```

**Detección**: Si dos aprendices entregan código idéntico, es **copia evidente**.

---

## 🏗️ Arquitectura del Sistema

### 1. Pool de Dominios (50+ únicos)

Categorías de dominios:

#### A. Comercio y Retail
- Restaurante, Cafetería, Panadería
- Tienda de Ropa, Zapatería, Joyería
- Supermercado, Farmacia, Ferretería

#### B. Servicios Profesionales
- Clínica Veterinaria, Consultorio Médico, Clínica Dental
- Bufete de Abogados, Notaría, Agencia de Seguros
- Salón de Belleza, Spa, Barbería

#### C. Educación y Cultura
- Biblioteca, Academia de Música, Centro Educativo
- Museo, Galería de Arte, Teatro

#### D. Entretenimiento y Deporte
- Gimnasio, Club Deportivo, Escuela de Natación
- Cine, Bolera, Arcade

#### E. Inmobiliario y Automotriz
- Inmobiliaria, Constructora, Arquitectos
- Taller Mecánico, Concesionario, Parqueadero

#### F. Logística y Turismo
- Agencia de Viajes, Hotel, Hostal
- Agencia de Mudanzas, Courier, Almacén

**Total**: 50+ dominios únicos garantizando **cero repeticiones** por cohorte.

---

### 2. Asignación Aleatoria

**Proceso**:

```bash
# Pseudocódigo del proceso de asignación

1. Leer lista de aprendices (APRENDICES-3147234.md)
2. Generar lista de dominios disponibles
3. Para cada aprendiz:
   a. Seleccionar dominio aleatorio (sin repetir)
   b. Crear carpeta: 4-asignación_dominios_aprendiz/aprendiz-XXX-[nombre]/
   c. Generar dominio.md con contexto detallado
   d. Generar asignaciones semanales contextualizadas
4. Marcar dominios como asignados
5. Generar reporte de asignaciones (solo para instructor)
```

**Garantías**:
- ✅ Un dominio = Un aprendiz
- ✅ Aleatorio (no hay favoritismos)
- ✅ Registrado y auditable
- ✅ Inmutable durante el bootcamp

---

### 3. Estructura de Asignación Individual

```
4-asignación_dominios_aprendiz/
├── README.md (política y guía)
├── .gitkeep
└── aprendiz-001-[nombre]/
    ├── dominio.md                    # Contexto del negocio
    ├── asignacion-semana-01.md       # Requisitos semana 1
    ├── asignacion-semana-02.md       # Requisitos semana 2
    ├── ...
    ├── asignacion-semana-09.md       # Requisitos semana 9
    └── rubrica-general.md            # Criterios de evaluación
```

---

### 4. Ejemplo Completo de Dominio

**Archivo: `dominio.md`**

```markdown
# Dominio Asignado: Restaurante "La Trattoria"

## Contexto de Negocio

**Tipo**: Restaurante de comida italiana  
**Ubicación**: Bogotá, Zona T  
**Tamaño**: 15 mesas (60 personas capacidad)  
**Horario**: Martes a Domingo, 12:00 - 22:00  

## Descripción

La Trattoria es un restaurante familiar que ofrece comida italiana 
auténtica. Cuenta con un menú de 40 platos entre entradas, pastas, 
pizzas, carnes y postres. El restaurante tiene 8 empleados y atiende 
aproximadamente 100 clientes al día.

## Entidades Principales

### 1. Mesas
- Atributos: numero, capacidad, ubicacion, estado
- Relaciones: pedidos, reservas

### 2. Menu
- Atributos: nombre, categoria, precio, ingredientes, disponible
- Categorías: entradas, pastas, pizzas, carnes, postres, bebidas

### 3. Empleados
- Atributos: nombre, puesto, turno, salario, fecha_ingreso
- Puestos: chef, sous_chef, mesero, cajero, hostess

### 4. Pedidos
- Atributos: mesa_id, empleado_id, items, total, estado, fecha
- Estados: pendiente, en_preparacion, servido, pagado

### 5. Reservas
- Atributos: cliente_nombre, telefono, mesa_id, fecha_hora, personas

### 6. Inventario
- Atributos: ingrediente, cantidad, unidad, minimo_stock, proveedor

## Datos de Ejemplo

### Menu (10 platos)
1. Bruschetta al Pomodoro - Entrada - $18,000
2. Carpaccio di Manzo - Entrada - $25,000
3. Spaghetti Carbonara - Pasta - $32,000
4. Fettuccine Alfredo - Pasta - $30,000
5. Pizza Margherita - Pizza - $28,000
6. Pizza Quattro Stagioni - Pizza - $35,000
7. Osso Buco - Carne - $48,000
8. Saltimbocca - Carne - $42,000
9. Tiramisu - Postre - $15,000
10. Panna Cotta - Postre - $14,000

### Empleados (8 personas)
1. Giovanni Rossi - Chef - Tiempo Completo
2. Marco Bianchi - Sous Chef - Tiempo Completo
3. Laura Conti - Mesera - Medio Tiempo (Cena)
4. Sofia Marino - Mesera - Medio Tiempo (Almuerzo)
5. Luca Romano - Mesero - Tiempo Completo
6. Giulia Ferrari - Cajera - Tiempo Completo
7. Alessandro Ricci - Mesero - Medio Tiempo (Cena)
8. Francesca Greco - Hostess - Tiempo Completo

## Requisitos Técnicos (Constantes para todos)

- Docker con PostgreSQL 15+
- Nginx como reverse proxy
- API REST (Node.js o Python)
- Persistencia con volúmenes
- Backup diario automatizado

## Adaptación Semanal

### Semana 1: Hardware e Instalación
- Documentar hardware necesario para "La Trattoria"
- Instalar Docker
- Crear BD con tablas del restaurante

### Semana 2: Docker Compose
- Stack completo (DB + API + Web)
- Datos de ejemplo del restaurante

### Semana 3: Migración
- Plan de migración desde sistema antiguo
- Scripts de transformación de datos

### Semana 4: Respaldo
- Estrategia de backup del restaurante
- Restauración de datos

### Semana 5-9: Continuación según bootcamp
```

---

## 📊 Evaluación con Dominios

### Rúbrica Adaptada

| Criterio | Peso | Evaluación |
|----------|------|------------|
| **Requisitos Técnicos** | 40% | Funciona Docker, PostgreSQL, volúmenes |
| **Adaptación al Dominio** | 30% | Nombres coherentes, datos realistas |
| **Comprensión Demostrada** | 20% | Comentarios apropiados, explicación |
| **Originalidad** | 10% | No es copia de otro aprendiz |

### Detección de Copia

**Señales de alerta**:
- ❌ Nombres de tablas/variables idénticos entre aprendices de diferentes dominios
- ❌ Comentarios palabra por palabra iguales
- ❌ Estructura de código idéntica (incluso con nombres cambiados)
- ❌ Errores idénticos en múltiples entregas

**Acción**: Entrevista individual para verificar comprensión.

---

## 🔒 Confidencialidad

### Archivo de Aprendices

**Ubicación**: `_docs/APRENDICES-3147234.md`

**Contenido**:
```markdown
# Aprendices Ficha 3147234

## Cohorte 2025-2

| ID | Nombre Completo | Dominio Asignado | Email |
|----|----------------|------------------|-------|
| 001 | [Nombre] | Restaurante | email@sena.edu.co |
| 002 | [Nombre] | Biblioteca | email@sena.edu.co |
| 003 | [Nombre] | Gimnasio | email@sena.edu.co |
| ... | ... | ... | ... |
```

**Seguridad**:
- ❌ Ignorado en git (`.gitignore`)
- ✅ Visible en proyecto (acceso local)
- 🔐 Solo instructor tiene acceso
- 📝 Usado para generar asignaciones

---

## 🚫 Reglas Estrictas

### Material Compartido (Teoría y Prácticas)

#### ✅ PERMITIDO:
- Ejemplos genéricos: "Sistema de gestión", "Aplicación empresarial"
- Tablas abstractas: `entidades`, `items`, `registros`
- Conceptos universales: usuario, producto, transacción

#### ❌ PROHIBIDO:
- Mencionar nombres de aprendices: "Como hizo Juan..."
- Mencionar dominios específicos: "Para el restaurante..."
- Dar ejemplos de dominios asignados
- Mostrar código de entregas anteriores con contexto

### Comunicación con Aprendices

**Correcto**:
> "Adapta este ejemplo a tu dominio de negocio. Donde dice 'entidades', 
> usa el nombre correspondiente de tu contexto (ej: si tu dominio es 
> una tienda, podría ser 'productos')."

**Incorrecto**:
> "Pedro, en tu restaurante debes crear la tabla 'menu'..."  
> *(Expone el dominio de Pedro a otros aprendices)*

---

## 🎓 Beneficios Pedagógicos

### Para el Aprendiz

1. **Aprendizaje Activo**: Debe entender para adaptar
2. **Contextualización**: Conecta con realidad empresarial
3. **Portfolio Único**: Proyecto diferenciado
4. **Pensamiento Crítico**: Resuelve problemas específicos
5. **Preparación Laboral**: Simula proyecto real

### Para el Instructor

1. **Detección Fácil**: Copias son evidentes
2. **Evaluación Justa**: Cada quien según su trabajo
3. **Retroalimentación**: Específica al contexto
4. **Seguimiento**: Evolución individual clara
5. **Calidad Educativa**: Garantizada

### Para el SENA

1. **Integridad Académica**: Protegida
2. **Reputación**: Formación seria y rigurosa
3. **Egresados Competentes**: Saben hacer, no copiar
4. **Innovación Pedagógica**: Metodología diferenciadora
5. **Trazabilidad**: Auditable y demostrable

---

## 📈 Métricas de Éxito

### Indicadores

- **Tasa de originalidad**: > 95% (< 5% copias detectadas)
- **Comprensión demostrada**: > 85% aprendices explican su código
- **Satisfacción del aprendiz**: > 4.0/5.0 (sienten que aprenden de verdad)
- **Empleabilidad**: Portfolio personalizado aumenta contratación

### Seguimiento

- Semana 3: Primera verificación (instalación Docker)
- Semana 6: Verificación media (stack completo)
- Semana 9: Evaluación final (proyecto integrador)

---

## 🔄 Proceso de Implementación

### Fase 1: Preparación (Antes del bootcamp)

1. ✅ Generar pool de 50+ dominios
2. ✅ Obtener lista de aprendices
3. ✅ Asignar dominios aleatoriamente
4. ✅ Crear carpetas individuales
5. ✅ Generar documentos de contexto

### Fase 2: Inducción (Día 1)

1. ✅ Explicar la política a los aprendices
2. ✅ Entregar dominio individual a cada uno
3. ✅ Aclarar beneficios y reglas
4. ✅ Responder preguntas

### Fase 3: Seguimiento (Semanas 1-9)

1. ✅ Verificar adaptación al dominio en entregas
2. ✅ Detectar posibles copias
3. ✅ Entrevistar si hay sospechas
4. ✅ Retroalimentación contextualizada

### Fase 4: Evaluación Final (Semana 9)

1. ✅ Proyecto completo en dominio asignado
2. ✅ Presentación y defensa
3. ✅ Verificación de comprensión
4. ✅ Certificación

---

## 🛠️ Herramientas de Soporte

### Script de Asignación

```python
# asignar_dominios.py
# ¿Qué? Script para asignar dominios aleatorios
# ¿Para qué? Automatizar el proceso de asignación

import random
import os

# Lista de dominios disponibles
dominios = [
    "Restaurante", "Biblioteca", "Gimnasio",
    "Inmobiliaria", "Clínica Veterinaria",
    # ... 50+ dominios
]

# Leer lista de aprendices
with open("_docs/APRENDICES-3147234.md", "r") as f:
    aprendices = [line.strip() for line in f if line.strip()]

# Asignar aleatoriamente
random.shuffle(dominios)
asignaciones = {}

for i, aprendiz in enumerate(aprendices):
    if i < len(dominios):
        asignaciones[aprendiz] = dominios[i]
        # Crear carpeta individual
        carpeta = f"bootcamp/semana-01/4-asignación_dominios_aprendiz/aprendiz-{i+1:03d}-{aprendiz}"
        os.makedirs(carpeta, exist_ok=True)
        # Generar archivos...

print("Asignaciones completadas!")
```

### Detector de Similitud

```python
# detectar_copias.py
# ¿Qué? Herramienta para detectar código similar
# ¿Para qué? Identificar posibles copias entre aprendices

from difflib import SequenceMatcher

def similitud(texto1, texto2):
    return SequenceMatcher(None, texto1, texto2).ratio()

# Comparar entregas de aprendices
umbral = 0.85  # 85% de similitud = sospechoso

# Lógica de comparación...
```

---

## 📚 Casos de Uso

### Caso 1: Aprendiz Intenta Copiar

**Situación**: Aprendiz A (Restaurante) copia código de Aprendiz B (Biblioteca).

**Resultado**:
```sql
-- Aprendiz A entrega (supuestamente Restaurante):
CREATE TABLE libros (  -- ❌ No tiene sentido en un restaurante
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100)
);
```

**Detección**: Inmediata (tabla "libros" en contexto de restaurante).

**Acción**: 
1. Conversación individual
2. Oportunidad de rehacer
3. Si persiste, sanción académica

---

### Caso 2: Aprendiz Comparte Código

**Situación**: Aprendiz C ayuda a Aprendiz D mostrando su código.

**Resultado**: Aprendiz D debe **adaptar** el código a su dominio.

**Ejemplo**:

**Código de C (Gimnasio)**:
```sql
CREATE TABLE miembros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);
```

**Código de D (Farmacia)** - Adaptado correctamente:
```sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);
```

**Evaluación**: ✅ Permitido. D entendió y adaptó.

---

### Caso 3: Material del Instructor

**Situación**: Instructor muestra ejemplo en clase.

**Correcto** (genérico):
```sql
-- Ejemplo genérico en clase
CREATE TABLE entidades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);
```

**Aprendiz E (Hotel)** adapta:
```sql
-- ¿Qué? Tabla para habitaciones del hotel
-- ¿Para qué? Gestionar inventario de cuartos
CREATE TABLE habitaciones (
    id SERIAL PRIMARY KEY,
    numero VARCHAR(10),
    tipo VARCHAR(50),
    precio DECIMAL(10,2)
);
```

**Evaluación**: ✅ Excelente adaptación.

---

## 🎯 Conclusión

Esta política garantiza:

1. ✅ **Aprendizaje real** sobre memorización
2. ✅ **Integridad académica** del bootcamp
3. ✅ **Preparación profesional** de los egresados
4. ✅ **Diferenciación** del programa SENA
5. ✅ **Evaluación justa** e individual

**Resultado final**: Aprendices ADSO con habilidades reales de implantación de software, portfolios únicos, y capacidad demostrada de resolver problemas en contextos diversos.

---

**Última actualización**: 5 de octubre de 2025  
**Bootcamp**: Implantación de Software  
**Institución**: SENA - CGMLTI - Regional Distrito Capital  
**Ficha**: 3147234
