# Asignaciones Personalizadas - Semana 3

> **⚠️ CONFIDENCIAL**: Esta carpeta contiene las asignaciones individuales de cada aprendiz con sus dominios únicos.

## 🎯 Propósito

Esta carpeta almacena las asignaciones personalizadas que se generan para cada aprendiz del bootcamp. Cada aprendiz recibe un dominio único y aleatorio sobre el cual debe trabajar en todas sus prácticas.

## 📁 Estructura

```
4-asignación_dominios_aprendiz/
├── README.md (este archivo)
├── lista-dominios.txt (dominios disponibles)
├── asignaciones/ (carpeta con archivos individuales)
│   ├── apellido-nombre.md
│   ├── garcia-juan.md
│   ├── martinez-maria.md
│   └── ...
└── plantilla-asignacion.md (template para generar)
```

## 🔒 Política Anticopia

### Objetivo

**Evitar que los aprendices copien y peguen código sin entender.**

### Estrategia

1. **Cada aprendiz = 1 dominio único** (no se repiten)
2. **Todo adaptado al dominio**: nombres de tablas, variables, rutas, etc.
3. **Sin ejemplos genéricos** en asignaciones individuales
4. **Evaluación personalizada**: instructor verifica coherencia con dominio

### Beneficios

- ✅ **Imposible copiar directamente** entre compañeros
- ✅ **Obliga a entender** para adaptar
- ✅ **Fomenta creatividad** en la implementación
- ✅ **Evidencia real** de aprendizaje

## 📝 Cómo Funciona

### Proceso de Asignación

1. **Instructor genera lista** de aprendices
2. **Sistema asigna dominio aleatorio** a cada uno
3. **Se genera archivo personalizado** con nombre-apellido.md
4. **Se entrega individualmente** (no compartido con grupo)
5. **Aprendiz desarrolla** prácticas según su dominio
6. **Instructor evalúa** coherencia y comprensión

### Ejemplo

**Aprendiz:** García, Juan
**Dominio:** Restaurante

**Su asignación contiene:**

- Base de datos: `restaurante_jgarcia`
- Tablas: `mesas`, `pedidos`, `platos`, `empleados`
- Variables de ejemplo: `nombrePlato`, `numeroMesa`, `precioTotal`
- Casos de uso: "Sistema para gestionar pedidos de mesas"

**Aprendiz:** Martínez, María
**Dominio:** Biblioteca

**Su asignación contiene:**

- Base de datos: `biblioteca_mmartinez`
- Tablas: `libros`, `prestamos`, `usuarios`, `multas`
- Variables de ejemplo: `tituloLibro`, `fechaPrestamo`, `montoMulta`
- Casos de uso: "Sistema para gestionar préstamos de libros"

## 🎲 Dominios Disponibles

Los dominios se seleccionan de una lista pre-definida y NO se repiten en la misma cohorte.

**Categorías:**

### Negocios

- Restaurante
- Cafetería
- Panadería
- Floristería
- Joyería
- Tienda de ropa
- Tienda de electrónicos
- Librería

### Servicios

- Peluquería/Barbería
- Lavandería
- Gimnasio
- Spa/Salón de belleza
- Taller mecánico
- Taller de bicicletas
- Veterinaria
- Clínica médica

### Entretenimiento

- Cine
- Teatro
- Museo
- Galería de arte
- Estudio de fotografía
- Academia de música
- Academia de danza
- Centro de yoga

### Educación

- Academia de idiomas
- Centro de tutorías
- Jardín infantil
- Biblioteca
- Centro de capacitación

### Turismo y Hotelería

- Hotel
- Hostal
- Agencia de viajes
- Rent a car
- Parque temático

### Tecnología

- Tienda de computadores
- Centro de reparación
- Cibercafé
- Tienda de videojuegos

### Inmobiliaria

- Inmobiliaria
- Arrendadora
- Administradora de propiedades

### Otros

- Funeraria
- Ferretería
- Vivero/Jardín
- Tienda de mascotas
- Granja orgánica

## 📄 Plantilla de Asignación

Ver archivo: `plantilla-asignacion.md`

Incluye:

- Objetivos específicos
- Contexto del dominio
- Requisitos técnicos adaptados
- Criterios de evaluación
- Entregables personalizados

## 🔐 Seguridad

### .gitignore

Esta carpeta está configurada en `.gitignore` para:

- ✅ NO subir a GitHub las asignaciones personalizadas
- ✅ Mantener privacidad de aprendices
- ✅ Evitar que vean asignaciones de otros

### Archivos Públicos

Solo estos archivos son compartidos:

- `README.md` (este archivo)
- `lista-dominios.txt` (lista genérica de dominios)
- `plantilla-asignacion.md` (template sin datos)

### Archivos Privados

Estos NO se comparten:

- `asignaciones/*.md` (archivos individuales)
- Cualquier archivo con nombres de aprendices

## 🎓 Evaluación

### Criterios de Verificación

El instructor verifica:

1. **Coherencia con dominio**

   - ✅ Nombres de tablas relacionados con dominio
   - ✅ Variables con nombres del contexto
   - ✅ Casos de uso realistas

2. **Comprensión técnica**

   - ✅ Código comentado correctamente
   - ✅ Decisiones técnicas justificadas
   - ✅ Solución de problemas documentada

3. **Originalidad**

   - ✅ No es copia directa de ejemplos
   - ✅ Adaptación creativa al dominio
   - ✅ Personalización evidente

4. **Completitud**
   - ✅ Todos los requisitos cumplidos
   - ✅ Entregables presentes
   - ✅ Documentación adecuada

### Rúbrica

| Criterio                  | Insuficiente (0-3) | Básico (3-4)          | Competente (4-4.5)     | Sobresaliente (4.5-5)         |
| ------------------------- | ------------------ | --------------------- | ---------------------- | ----------------------------- |
| **Adaptación al dominio** | No relacionado     | Parcialmente adaptado | Bien adaptado          | Perfectamente contextualizado |
| **Comprensión técnica**   | No funciona        | Funciona con errores  | Funciona correctamente | Funciona + optimizado         |
| **Código comentado**      | Sin comentarios    | Comentarios básicos   | Bien comentado         | Comentarios educativos        |
| **Documentación**         | Ausente o mínima   | Básica                | Completa               | Excepcional                   |

## 📊 Uso de Esta Carpeta

### Para el Instructor

1. **Generar asignaciones**

   ```bash
   cd semana-03/4-asignación_dominios_aprendiz/
   python3 generar-asignaciones.py lista-aprendices.txt
   ```

2. **Distribuir individualmente**

   - Enviar por correo o plataforma LMS
   - NO compartir en grupo o repositorio público

3. **Evaluar entregas**
   - Abrir archivo del aprendiz
   - Comparar entrega con requisitos personalizados
   - Verificar coherencia con dominio

### Para Desarrollo (Copilot)

Al generar contenido:

- ❌ **NO mencionar** nombres de aprendices específicos
- ❌ **NO incluir** dominios específicos en ejemplos públicos
- ✅ **SÍ usar** placeholders genéricos (`[TU_DOMINIO]`, `[NOMBRE_TABLA]`)
- ✅ **SÍ describir** requisitos adaptables

## 📝 Notas Adicionales

- Cada cohorte tiene dominios diferentes (rotar lista)
- Si hay más aprendices que dominios, crear combinaciones (ej: "Restaurante italiano", "Restaurante vegetariano")
- Mantener registro de asignaciones previas para no repetir en futuras cohortes
- Actualizar lista de dominios según retroalimentación de aprendices

---

> **Recordatorio:** Esta carpeta es CONFIDENCIAL. No compartir contenido personalizado con otros aprendices.
