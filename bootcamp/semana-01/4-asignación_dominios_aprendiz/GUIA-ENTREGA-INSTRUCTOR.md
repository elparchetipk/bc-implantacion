# Guía de Entrega de Dominios - Para el Instructor

**Bootcamp**: Implantación de Software  
**Ficha**: 3147234  
**Fecha**: 5 de octubre de 2025

---

## 🎯 Objetivo

Esta guía explica cómo entregar los dominios asignados a cada aprendiz de forma individual y confidencial.

---

## 📋 Preparación Previa (1 hora)

### 1. Verificar Asignaciones

✅ Confirmar que el script generó correctamente las 29 carpetas:

```bash
cd bootcamp/semana-01/4-asignación_dominios_aprendiz/
ls -1d aprendiz-* | wc -l
# Debe mostrar: 29
```

✅ Verificar que cada carpeta tiene 2 archivos:

```bash
find aprendiz-* -name "*.md" | wc -l
# Debe mostrar: 58 (29 × 2)
```

### 2. Revisar Contenido

✅ Abrir una muestra de archivos para verificar:

```bash
# Ver ejemplo del aprendiz 001
cat aprendiz-001-arias-rendon-james-david/dominio.md
cat aprendiz-001-arias-rendon-james-david/asignacion-semana-01.md
```

✅ Verificar que:

- El nombre del aprendiz está correcto
- El dominio asignado es único
- Los archivos están bien formateados
- No hay errores de sintaxis

---

## 📧 Método de Entrega Recomendado

### Opción 1: Email Individual (Recomendado)

**Ventajas**:

- ✅ Privacidad garantizada
- ✅ Cada aprendiz solo ve su dominio
- ✅ Registro de entrega
- ✅ Puede leer en cualquier momento

**Proceso**:

1. **Obtener lista de emails** de los aprendices

   - Desde Sofia Plus o sistema SENA
   - Crear archivo CSV: `aprendiz, email`

2. **Para cada aprendiz**, enviar email con:

   **Asunto**: `[Bootcamp Implantación] Tu Dominio Asignado - Confidencial`

   **Cuerpo**:

   ```
   Hola [NOMBRE_APRENDIZ],

   Bienvenido/a al Bootcamp de Implantación de Software, Ficha 3147234.

   Como parte de nuestra metodología de aprendizaje personalizado,
   se te ha asignado un dominio de negocio único sobre el cual
   desarrollarás todos los ejercicios del bootcamp.

   TU DOMINIO ASIGNADO: [NOMBRE_DOMINIO]

   Adjunto encontrarás dos archivos:
   1. dominio.md - Descripción completa de tu dominio
   2. asignacion-semana-01.md - Tareas de la primera semana

   IMPORTANTE:
   - Este dominio es ÚNICO y PERSONAL
   - NO lo compartas con tus compañeros
   - Todas tus entregas deben reflejar este dominio
   - Lee cuidadosamente los archivos adjuntos

   Si tienes dudas sobre cómo adaptar los ejercicios a tu dominio,
   pregunta en clase o escríbeme a este correo.

   ¡Éxito en tu aprendizaje!

   [Tu nombre]
   Instructor - Bootcamp Implantación de Software
   SENA CGMLTI - Regional Distrito Capital
   ```

   **Adjuntos**:

   - `dominio.md` (de la carpeta del aprendiz)
   - `asignacion-semana-01.md` (de la carpeta del aprendiz)

3. **Llevar registro**:
   - Crear hoja de cálculo: `aprendiz | email | fecha_envío | estado`
   - Marcar como enviado al completar

---

### Opción 2: Plataforma LMS (Sofia Plus / Moodle)

**Ventajas**:

- ✅ Integrado con sistema SENA
- ✅ Los aprendices acceden con sus credenciales
- ✅ Notificaciones automáticas

**Proceso**:

1. **Crear carpeta privada por aprendiz** en la plataforma
2. **Subir archivos individuales** a cada carpeta
3. **Configurar permisos**: Solo el aprendiz ve su carpeta
4. **Notificar** a través de la plataforma

---

### Opción 3: Google Drive con Carpetas Compartidas

**Ventajas**:

- ✅ Fácil de gestionar
- ✅ Compartir enlaces individuales
- ✅ Historial de accesos

**Proceso**:

1. **Crear carpeta principal**: `Dominios-Bootcamp-3147234`
2. **Por cada aprendiz**:
   - Crear subcarpeta: `[Número]-[Apellido]-[Nombre]`
   - Subir 2 archivos (dominio.md y asignacion-semana-01.md)
   - Compartir SOLO con el email del aprendiz
   - Establecer permisos: "Puede ver"
3. **Enviar enlace** individual a cada aprendiz

---

## 🎓 Presentación en Clase (30 minutos)

### Momento 1: Explicación General (10 min)

**Diapositivas sugeridas**:

**Slide 1: Título**

```
POLÍTICA ANTICOPIA
Dominios Únicos por Aprendiz
```

**Slide 2: ¿Por qué?**

```
❌ Problema: Copiar código sin entender
✅ Solución: Cada uno trabaja en un contexto único

Beneficios:
• Aprendizaje real
• Portfolio personalizado
• Evaluación justa
• Preparación profesional
```

**Slide 3: ¿Cómo funciona?**

```
1. Cada aprendiz recibe UN dominio único
2. Todos los ejercicios se adaptan a ESE dominio
3. No hay dos dominios iguales
4. El código debe reflejar tu contexto

Ejemplos:
• Aprendiz A → Restaurante (tablas: platos, pedidos, mesas)
• Aprendiz B → Biblioteca (tablas: libros, prestamos, usuarios)
• Aprendiz C → Gimnasio (tablas: miembros, rutinas, equipos)
```

**Slide 4: Reglas**

```
✅ PERMITIDO:
• Discutir conceptos generales
• Ayudarse con errores técnicos
• Compartir recursos de aprendizaje

❌ NO PERMITIDO:
• Copiar código de compañeros
• Usar el dominio de otro aprendiz
• Entregar trabajo idéntico
```

**Slide 5: Evaluación**

```
Se califica:
1. Funcionalidad técnica (40%)
2. Adaptación al dominio (30%)
3. Comprensión (20%)
4. Documentación (10%)

Si dos entregas son idénticas = COPIA EVIDENTE
```

### Momento 2: Entrega Individual (15 min)

**Opciones**:

A. **Si enviaste por email previo**:

```
"Revisen su correo electrónico. Cada uno recibió
un email con su dominio asignado y los archivos necesarios."
```

B. **Si entregas en el momento**:

- Llamar a cada aprendiz individualmente
- Entregar sobre cerrado con sus archivos impresos
- O enviar link de Google Drive personal

C. **Si usas plataforma LMS**:

```
"Ingresen a Sofia Plus. En la sección 'Mi Dominio'
encontrarán sus archivos personales."
```

### Momento 3: Preguntas y Aclaraciones (5 min)

**Preguntas frecuentes esperadas**:

**P: ¿Puedo cambiar de dominio?**  
R: No. El dominio asignado es fijo durante todo el bootcamp.

**P: ¿Qué pasa si no sé sobre mi dominio?**  
R: Debes investigar. Parte del ejercicio es conocer ese tipo de negocio.

**P: ¿Puedo ver el dominio de mis compañeros?**  
R: No. Cada dominio es confidencial.

**P: ¿Y si mi código es similar al de un compañero?**  
R: El código puede ser similar técnicamente, pero los NOMBRES deben reflejar tu dominio.

**P: ¿Cómo sé qué tablas crear?**  
R: Investiga tu tipo de negocio. Los archivos que recibiste tienen sugerencias.

---

## 📝 Plantilla de Email

Copia y pega esta plantilla, ajustando los campos `[...]`:

```
Asunto: [Bootcamp Implantación] Tu Dominio Asignado - Confidencial

Hola [NOMBRE_COMPLETO],

Bienvenido/a al Bootcamp de Implantación de Software (Ficha 3147234).

Como parte de nuestra metodología pedagógica centrada en el aprendizaje
real y significativo, se te ha asignado un DOMINIO DE NEGOCIO ÚNICO sobre
el cual desarrollarás todos los ejercicios y prácticas del bootcamp.

═══════════════════════════════════════════════════════════════
TU DOMINIO ASIGNADO: [NOMBRE_DEL_DOMINIO]
═══════════════════════════════════════════════════════════════

En los archivos adjuntos encontrarás:

📄 dominio.md
   - Descripción completa de tu dominio
   - Contexto del negocio
   - Entidades sugeridas
   - Criterios de adaptación
   - Recursos para investigar

📄 asignacion-semana-01.md
   - Actividades de la primera semana
   - Adaptaciones específicas a tu dominio
   - Entregables requeridos
   - Criterios de evaluación

══════════════════════════════════════════════════════════════
REGLAS IMPORTANTES
══════════════════════════════════════════════════════════════

✅ HACER:
• Investigar tu tipo de negocio
• Adaptar TODOS los ejercicios a tu dominio
• Usar nombres específicos (tablas, variables, etc.)
• Documentar tus decisiones

❌ NO HACER:
• Copiar código de compañeros
• Compartir tu dominio con otros aprendices
• Usar nombres genéricos (tabla1, datos, test)
• Entregar trabajo sin adaptarlo

══════════════════════════════════════════════════════════════
¿POR QUÉ ESTA METODOLOGÍA?
══════════════════════════════════════════════════════════════

1. APRENDIZAJE REAL: Comprendes conceptos, no copias código
2. PORTFOLIO ÚNICO: Tendrás un proyecto personalizado
3. EVALUACIÓN JUSTA: Tu trabajo refleja TU comprensión
4. PREPARACIÓN PROFESIONAL: Contextos diversos = más habilidades

══════════════════════════════════════════════════════════════
SOPORTE
══════════════════════════════════════════════════════════════

Si tienes dudas sobre:
• Cómo adaptar ejercicios a tu dominio → Pregunta en clase
• Aspectos técnicos de Docker/PostgreSQL → Pregunta en clase
• Tu dominio específico → Investiga online, luego pregúntame

Recuerda: Tu dominio es CONFIDENCIAL. No lo compartas con compañeros.

¡Éxito en tu aprendizaje! 🚀

═══════════════════════════════════════════════════════════════

[Tu Nombre]
Instructor - Bootcamp Implantación de Software
Análisis y Desarrollo de Software (ADSO)
SENA - Centro de Gestión de Mercados, Logística y Tecnologías de la Información
Regional Distrito Capital

Email: [tu-email@sena.edu.co]
Teléfono: [tu-teléfono]
Horario de atención: Lunes a Viernes, 8:00 AM - 5:00 PM
```

---

## 🔍 Verificación Post-Entrega

### Día 1 (Después de la clase)

✅ **Verificar recepción**:

- Enviar mensaje de confirmación a todos
- Pedir que respondan si recibieron su dominio
- Atender consultas individuales

### Día 3 (Mitad de semana)

✅ **Recordatorio**:

```
Asunto: Recordatorio - Asignación Semana 1

Hola a todos,

Recordatorio sobre la primera entrega:
• Fecha límite: Viernes 11:59 PM
• Deben adaptar TODOS los ejercicios a su dominio
• Incluir capturas de pantalla
• Documentar el proceso

Revisen los archivos que les envié el día 1.

Saludos,
[Tu nombre]
```

### Día 5 (Antes de la entrega)

✅ **Última llamada**:

- Recordar fecha límite
- Ofrecer horario de consultas
- Aclarar dudas comunes

---

## 📊 Seguimiento y Evaluación

### Al Recibir Primera Entrega

✅ **Verificar adaptación**:

```python
# Checklist por aprendiz:
□ Nombre de BD refleja el dominio
□ Nombres de tablas son específicos
□ Datos de ejemplo son realistas
□ Comentarios mencionan el contexto
□ No es copia evidente de otro aprendiz
```

### Si Detectas Copia

**Paso 1: Identificar**

- Comparar código entre entregas sospechosas
- Buscar nombres idénticos o muy similares
- Verificar timestamps de commits (si usan git)

**Paso 2: Conversación Individual**

- Llamar al aprendiz en privado
- Mostrar evidencias
- Dar oportunidad de explicar
- Ofrecer chance de rehacer

**Paso 3: Acción Pedagógica**

- Primera vez: Advertencia + rehacer
- Segunda vez: Penalización en nota
- Tercera vez: Sanción académica según reglamento SENA

---

## 💡 Consejos Prácticos

### Para Ti (Instructor)

1. **Mantén la confidencialidad**

   - No menciones dominios específicos en clase
   - Usa ejemplos genéricos en explicaciones
   - Si un aprendiz pregunta públicamente, responde en privado

2. **Fomenta la investigación**

   - Si preguntan "¿qué tablas crear?", responde "¿qué información guarda ese tipo de negocio?"
   - Orienta, no des respuestas directas

3. **Celebra la originalidad**
   - Cuando veas una adaptación creativa, felicita públicamente (sin revelar el dominio)
   - Comparte (anónimamente) buenos ejemplos de adaptación

### Para Los Aprendices

Comparte estos consejos en clase:

1. **Investiga tu dominio**

   - Busca en Google: "[tu dominio] + gestión"
   - Ve videos sobre ese tipo de negocio
   - Piensa en lugares reales similares

2. **Sé específico**

   - Mal: `usuarios`, `productos`, `transacciones`
   - Bien: Nombres específicos de tu dominio

3. **Documenta decisiones**

   - Explica por qué elegiste cada nombre
   - Justifica la estructura de tus tablas

4. **Pide ayuda correctamente**
   - Mal: "¿Me pasas tu código?"
   - Bien: "¿Cómo hiciste para que Docker persistiera los datos?"

---

## 📅 Cronograma Sugerido

| Cuándo                | Qué hacer                        | Tiempo  |
| --------------------- | -------------------------------- | ------- |
| **Día -1**            | Generar asignaciones con script  | 15 min  |
| **Día -1**            | Revisar asignaciones generadas   | 30 min  |
| **Día -1**            | Preparar emails o plataforma     | 30 min  |
| **Día 1 - Pre-clase** | Enviar dominios por email        | 1 hora  |
| **Día 1 - Clase**     | Explicar política (presentación) | 10 min  |
| **Día 1 - Clase**     | Confirmar recepción              | 5 min   |
| **Día 1 - Clase**     | Sesión de preguntas              | 15 min  |
| **Día 3**             | Recordatorio a aprendices        | 10 min  |
| **Día 5**             | Última llamada antes entrega     | 10 min  |
| **Día 7**             | Recibir y revisar entregas       | 3 horas |
| **Día 9**             | Retroalimentar individualmente   | 2 horas |

---

## ✅ Checklist Final

Antes de la clase, verifica:

- [ ] Script de asignación ejecutado correctamente
- [ ] 29 carpetas generadas (una por aprendiz)
- [ ] 58 archivos creados (2 por aprendiz)
- [ ] Nombres de aprendices correctos
- [ ] Dominios únicos (cero repeticiones)
- [ ] Archivos .gitignore configurados
- [ ] Presentación preparada
- [ ] Emails listos (o plataforma configurada)
- [ ] Plantilla de email personalizada
- [ ] Plan de seguimiento definido
- [ ] Criterios de evaluación claros

---

## 🎯 Resultado Esperado

Al final de este proceso:

✅ Cada aprendiz conoce su dominio único  
✅ Entienden la metodología y sus beneficios  
✅ Saben cómo adaptar ejercicios a su contexto  
✅ Tienen claro que no deben copiar  
✅ Están motivados para aprender de verdad

---

**¡Éxito con la implementación!** 🚀

---

**Documento**: Guía de Entrega de Dominios  
**Autor**: Sistema de Asignación Automática  
**Fecha**: 5 de octubre de 2025  
**Versión**: 1.0
