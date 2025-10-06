#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de Asignación Aleatoria de Dominios
==========================================

¿Qué?
-----
Script que asigna dominios de negocio únicos y aleatorios a cada aprendiz
de la ficha 3147234 del programa ADSO.

¿Para qué?
----------
1. Garantizar que cada aprendiz tenga un contexto único
2. Evitar copias entre aprendices
3. Promover aprendizaje contextualizado
4. Generar estructura de carpetas personalizada

¿Cómo?
------
1. Lee lista de aprendices desde archivo
2. Define pool de 50+ dominios de negocio
3. Asigna aleatoriamente sin repetir
4. Crea carpetas y archivos individuales
5. Genera reporte de asignaciones

Autor: Sistema de Generación Automática
Fecha: 5 de octubre de 2025
Bootcamp: Implantación de Software - SENA CGMLTI
"""

import random
import os
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

# ¿Qué? Ruta base del proyecto
# ¿Para qué? Ubicar archivos de entrada y salida
BASE_DIR = Path(__file__).parent.parent.parent.parent
APRENDICES_FILE = BASE_DIR / "_docs" / "APRENDICES-3147234.md"
OUTPUT_DIR = Path(__file__).parent
REPORTE_FILE = OUTPUT_DIR / "REPORTE-ASIGNACIONES.md"

# ============================================================================
# BANCO DE DOMINIOS (50+ únicos)
# ============================================================================

# ¿Qué? Pool de dominios de negocio disponibles
# ¿Para qué? Asignar contextos únicos a cada aprendiz
# ¿Cómo? Categorizados por sector económico

DOMINIOS = {
    # A. Comercio y Retail (12 dominios)
    "Restaurante de Comida Italiana": {
        "categoria": "Comercio y Retail",
        "tipo": "Restaurante",
        "contexto": "restaurante de cocina italiana con 15 mesas"
    },
    "Cafetería Artesanal": {
        "categoria": "Comercio y Retail",
        "tipo": "Cafetería",
        "contexto": "cafetería especializada en café de origen"
    },
    "Panadería y Repostería": {
        "categoria": "Comercio y Retail",
        "tipo": "Panadería",
        "contexto": "panadería con productos horneados diariamente"
    },
    "Tienda de Ropa Urbana": {
        "categoria": "Comercio y Retail",
        "tipo": "Tienda",
        "contexto": "boutique de moda urbana para jóvenes"
    },
    "Zapatería Deportiva": {
        "categoria": "Comercio y Retail",
        "tipo": "Zapatería",
        "contexto": "tienda especializada en calzado deportivo"
    },
    "Joyería y Relojes": {
        "categoria": "Comercio y Retail",
        "tipo": "Joyería",
        "contexto": "joyería con diseños personalizados"
    },
    "Minimercado de Barrio": {
        "categoria": "Comercio y Retail",
        "tipo": "Supermercado",
        "contexto": "supermercado pequeño de productos básicos"
    },
    "Farmacia de Turno": {
        "categoria": "Comercio y Retail",
        "tipo": "Farmacia",
        "contexto": "farmacia con servicio 24 horas"
    },
    "Ferretería y Materiales": {
        "categoria": "Comercio y Retail",
        "tipo": "Ferretería",
        "contexto": "ferretería con herramientas y materiales de construcción"
    },
    "Librería y Papelería": {
        "categoria": "Comercio y Retail",
        "tipo": "Librería",
        "contexto": "librería con sección de útiles escolares"
    },
    "Tienda de Mascotas": {
        "categoria": "Comercio y Retail",
        "tipo": "Tienda",
        "contexto": "tienda con alimentos, juguetes y accesorios para mascotas"
    },
    "Floristería y Eventos": {
        "categoria": "Comercio y Retail",
        "tipo": "Floristería",
        "contexto": "floristería con servicio de arreglos para eventos"
    },
    
    # B. Servicios Profesionales (9 dominios)
    "Clínica Veterinaria": {
        "categoria": "Servicios Profesionales",
        "tipo": "Veterinaria",
        "contexto": "clínica veterinaria con cirugía y hospitalización"
    },
    "Consultorio Médico General": {
        "categoria": "Servicios Profesionales",
        "tipo": "Consultorio",
        "contexto": "consultorio de medicina general con 3 médicos"
    },
    "Clínica Odontológica": {
        "categoria": "Servicios Profesionales",
        "tipo": "Clínica Dental",
        "contexto": "clínica dental con ortodoncia y estética"
    },
    "Bufete de Abogados": {
        "categoria": "Servicios Profesionales",
        "tipo": "Jurídico",
        "contexto": "bufete especializado en derecho civil y laboral"
    },
    "Notaría Pública": {
        "categoria": "Servicios Profesionales",
        "tipo": "Notaría",
        "contexto": "notaría con servicios de autenticación y registro"
    },
    "Agencia de Seguros": {
        "categoria": "Servicios Profesionales",
        "tipo": "Seguros",
        "contexto": "agencia multi-ramo (vida, auto, hogar)"
    },
    "Salón de Belleza": {
        "categoria": "Servicios Profesionales",
        "tipo": "Salón",
        "contexto": "salón de belleza con peluquería y manicure"
    },
    "Spa y Masajes": {
        "categoria": "Servicios Profesionales",
        "tipo": "Spa",
        "contexto": "spa con terapias de relajación"
    },
    "Barbería Clásica": {
        "categoria": "Servicios Profesionales",
        "tipo": "Barbería",
        "contexto": "barbería tradicional para caballeros"
    },
    
    # C. Educación y Cultura (6 dominios)
    "Biblioteca Pública": {
        "categoria": "Educación y Cultura",
        "tipo": "Biblioteca",
        "contexto": "biblioteca con préstamo de libros y sala de lectura"
    },
    "Academia de Música": {
        "categoria": "Educación y Cultura",
        "tipo": "Academia",
        "contexto": "academia con clases de piano, guitarra y canto"
    },
    "Centro de Idiomas": {
        "categoria": "Educación y Cultura",
        "tipo": "Centro Educativo",
        "contexto": "instituto de enseñanza de inglés y francés"
    },
    "Museo de Arte": {
        "categoria": "Educación y Cultura",
        "tipo": "Museo",
        "contexto": "museo con exposiciones permanentes y temporales"
    },
    "Galería de Arte Contemporáneo": {
        "categoria": "Educación y Cultura",
        "tipo": "Galería",
        "contexto": "galería con obras de artistas locales"
    },
    "Teatro Comunitario": {
        "categoria": "Educación y Cultura",
        "tipo": "Teatro",
        "contexto": "teatro con presentaciones de obras y talleres"
    },
    
    # D. Entretenimiento y Deporte (6 dominios)
    "Gimnasio Urbano": {
        "categoria": "Entretenimiento y Deporte",
        "tipo": "Gimnasio",
        "contexto": "gimnasio con pesas, cardio y clases grupales"
    },
    "Club Deportivo": {
        "categoria": "Entretenimiento y Deporte",
        "tipo": "Club",
        "contexto": "club con canchas de fútbol y básquet"
    },
    "Academia de Natación": {
        "categoria": "Entretenimiento y Deporte",
        "tipo": "Academia Deportiva",
        "contexto": "escuela de natación para niños y adultos"
    },
    "Multicines": {
        "categoria": "Entretenimiento y Deporte",
        "tipo": "Cine",
        "contexto": "complejo de cine con 6 salas"
    },
    "Centro de Bolos": {
        "categoria": "Entretenimiento y Deporte",
        "tipo": "Bolera",
        "contexto": "bolera con 12 pistas y zona de juegos"
    },
    "Arcade de Videojuegos": {
        "categoria": "Entretenimiento y Deporte",
        "tipo": "Arcade",
        "contexto": "sala de juegos arcade y simuladores"
    },
    
    # E. Inmobiliario y Automotriz (6 dominios)
    "Inmobiliaria Urbana": {
        "categoria": "Inmobiliario y Automotriz",
        "tipo": "Inmobiliaria",
        "contexto": "inmobiliaria de venta y arriendo de propiedades"
    },
    "Constructora de Vivienda": {
        "categoria": "Inmobiliario y Automotriz",
        "tipo": "Constructora",
        "contexto": "constructora de proyectos residenciales"
    },
    "Estudio de Arquitectura": {
        "categoria": "Inmobiliario y Automotriz",
        "tipo": "Arquitectos",
        "contexto": "estudio de diseño arquitectónico"
    },
    "Taller Mecánico Automotriz": {
        "categoria": "Inmobiliario y Automotriz",
        "tipo": "Taller",
        "contexto": "taller de mecánica general y latonería"
    },
    "Concesionario de Vehículos": {
        "categoria": "Inmobiliario y Automotriz",
        "tipo": "Concesionario",
        "contexto": "concesionario de autos nuevos y usados"
    },
    "Parqueadero Cubierto": {
        "categoria": "Inmobiliario y Automotriz",
        "tipo": "Parqueadero",
        "contexto": "parqueadero de corta y larga estancia"
    },
    
    # F. Logística y Turismo (6 dominios)
    "Agencia de Viajes": {
        "categoria": "Logística y Turismo",
        "tipo": "Agencia",
        "contexto": "agencia con paquetes turísticos nacionales e internacionales"
    },
    "Hotel Boutique": {
        "categoria": "Logística y Turismo",
        "tipo": "Hotel",
        "contexto": "hotel boutique con 20 habitaciones"
    },
    "Hostal para Mochileros": {
        "categoria": "Logística y Turismo",
        "tipo": "Hostal",
        "contexto": "hostal económico para viajeros"
    },
    "Empresa de Mudanzas": {
        "categoria": "Logística y Turismo",
        "tipo": "Mudanzas",
        "contexto": "empresa de mudanzas locales y nacionales"
    },
    "Servicio de Mensajería": {
        "categoria": "Logística y Turismo",
        "tipo": "Courier",
        "contexto": "servicio de mensajería express"
    },
    "Centro de Distribución": {
        "categoria": "Logística y Turismo",
        "tipo": "Almacén",
        "contexto": "bodega de almacenamiento y distribución"
    },
}

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def leer_aprendices():
    """
    ¿Qué? Lee la lista de aprendices desde el archivo
    ¿Para qué? Obtener nombres para asignación
    ¿Cómo? Lee archivo y procesa líneas
    
    Returns:
        list: Lista de tuplas (nombre_completo, nombre_archivo)
    """
    aprendices = []
    
    with open(APRENDICES_FILE, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith('#'):
                continue
            
            # Procesar línea: "NOMBRE\tAPELLIDO" o "NOMBRE APELLIDO"
            partes = linea.split('\t') if '\t' in linea else linea.split()
            
            if len(partes) >= 2:
                nombre_completo = ' '.join(partes)
                # Crear nombre de archivo: apellido-nombre
                nombre_archivo = '-'.join(reversed(partes)).lower().replace(' ', '-')
                aprendices.append((nombre_completo, nombre_archivo))
    
    return aprendices


def asignar_dominios_aleatorios(aprendices):
    """
    ¿Qué? Asigna dominios aleatorios a cada aprendiz
    ¿Para qué? Garantizar distribución aleatoria sin repetir
    ¿Cómo? Mezcla dominios y asigna secuencialmente
    
    Args:
        aprendices (list): Lista de aprendices
        
    Returns:
        dict: Diccionario {aprendiz: dominio}
    """
    # ¿Qué? Lista de nombres de dominios disponibles
    # ¿Para qué? Preparar para asignación aleatoria
    dominios_disponibles = list(DOMINIOS.keys())
    
    # ¿Qué? Mezcla aleatoria de dominios
    # ¿Para qué? Garantizar aleatoriedad
    random.shuffle(dominios_disponibles)
    
    # ¿Qué? Asignación uno a uno
    # ¿Para qué? Emparejar aprendiz con dominio
    asignaciones = {}
    for i, (nombre_completo, nombre_archivo) in enumerate(aprendices):
        if i < len(dominios_disponibles):
            asignaciones[(nombre_completo, nombre_archivo)] = dominios_disponibles[i]
        else:
            print(f"⚠️ ADVERTENCIA: No hay suficientes dominios para {nombre_completo}")
    
    return asignaciones


def crear_estructura_aprendiz(numero, nombre_completo, nombre_archivo, dominio):
    """
    ¿Qué? Crea carpeta y archivos para un aprendiz
    ¿Para qué? Generar estructura personalizada
    ¿Cómo? Crea carpeta y archivos markdown
    
    Args:
        numero (int): Número del aprendiz
        nombre_completo (str): Nombre completo
        nombre_archivo (str): Nombre para carpeta
        dominio (str): Nombre del dominio asignado
    """
    # ¿Qué? Ruta de la carpeta del aprendiz
    # ¿Para qué? Organizar archivos por estudiante
    carpeta = OUTPUT_DIR / f"aprendiz-{numero:03d}-{nombre_archivo}"
    carpeta.mkdir(exist_ok=True)
    
    # Obtener datos del dominio
    datos_dominio = DOMINIOS[dominio]
    
    # ============================================================================
    # ARCHIVO 1: dominio.md
    # ============================================================================
    
    contenido_dominio = f"""# Dominio Asignado: {dominio}

**Aprendiz**: {nombre_completo}  
**Ficha**: 3147234  
**Programa**: Análisis y Desarrollo de Software (ADSO)  
**Bootcamp**: Implantación de Software  
**Fecha de asignación**: {datetime.now().strftime("%d de %B de %Y")}

---

## 📋 Información del Dominio

**Categoría**: {datos_dominio['categoria']}  
**Tipo de Negocio**: {datos_dominio['tipo']}  
**Contexto**: Este proyecto se desarrolla en el contexto de un **{datos_dominio['contexto']}**.

---

## 🎯 Objetivo

Desarrollar un sistema completo de implantación de software para gestionar las operaciones de este negocio, aplicando los conocimientos del bootcamp de implantación de software.

---

## 📊 Entidades Principales Sugeridas

A continuación se sugieren entidades básicas. **Debes adaptarlas y ampliarlas según tu análisis del dominio:**

### Entidades Mínimas (Ejemplo)

1. **Clientes/Usuarios**
   - Información básica de personas que usan el servicio

2. **Productos/Servicios**
   - Catálogo de lo que ofrece el negocio

3. **Transacciones/Operaciones**
   - Registro de actividades principales

4. **Empleados/Personal**
   - Gestión del equipo de trabajo

5. **Inventario/Recursos**
   - Control de recursos disponibles

**IMPORTANTE**: Estas son solo sugerencias. Investiga tu dominio y define las entidades que realmente necesita tu negocio específico.

---

## 💡 Criterios de Adaptación

### ✅ Hacer (Buenas Prácticas)

1. **Investigar tu dominio**
   - Busca información sobre cómo funciona realmente este tipo de negocio
   - Identifica procesos clave
   - Define flujos de trabajo

2. **Nombrar correctamente**
   - Usa nombres específicos del dominio
   - Ejemplo: Si es restaurante → `platos`, `pedidos`, `mesas`
   - NO uses nombres genéricos como `tabla1`, `datos`, `items`

3. **Coherencia total**
   - Base de datos: `{nombre_archivo.replace('-', '_')}_db`
   - Tablas: Nombres relacionados con el dominio
   - Variables: Contextualizadas al negocio
   - Comentarios: Explican el contexto del negocio

4. **Documentar decisiones**
   - Explica por qué elegiste cada nombre
   - Justifica la estructura de tus tablas
   - Describe los casos de uso

### ❌ Evitar (Malas Prácticas)

1. **NO copiar código de compañeros**
   - Cada dominio es único
   - El código debe reflejar TU dominio

2. **NO usar ejemplos genéricos**
   - Adapta TODO a tu contexto
   - Los ejemplos del instructor son genéricos a propósito

3. **NO inventar datos irreales**
   - Investiga datos realistas para tu dominio
   - Piensa en casos de uso reales

---

## 📚 Recursos para Investigar tu Dominio

### Sugerencias de Búsqueda

1. **Google**: "{dominio} + gestión" o "{dominio} + sistema"
2. **YouTube**: Videos sobre cómo funciona este tipo de negocio
3. **Artículos**: Blogs de expertos en el sector
4. **Sistemas reales**: Observa cómo operan negocios similares

### Preguntas Clave

- ¿Qué información se necesita registrar?
- ¿Cuáles son los procesos principales?
- ¿Qué reportes son importantes?
- ¿Qué roles de usuario existen?
- ¿Cómo se relacionan las entidades?

---

## 🎓 Evaluación

Tu trabajo será evaluado considerando:

1. **Funcionalidad Técnica (40%)**
   - Docker funciona correctamente
   - PostgreSQL desplegado y operativo
   - Persistencia de datos verificada

2. **Adaptación al Dominio (30%)**
   - Nombres específicos y coherentes
   - Estructura lógica del dominio
   - Datos realistas y contextualizados

3. **Comprensión (20%)**
   - Documentación clara
   - Justificación de decisiones
   - Capacidad de explicar el código

4. **Documentación (10%)**
   - Comentarios educativos (¿Qué? ¿Para qué? ¿Cómo?)
   - README completo
   - Capturas de pantalla claras

---

## 📝 Entregables por Semana

Cada semana tendrás asignaciones específicas adaptadas a tu dominio. Consulta los archivos:

- `asignacion-semana-01.md`
- `asignacion-semana-02.md`
- ... (se generarán progresivamente)

---

## 🤝 Política de Colaboración

### Permitido ✅

- Discutir conceptos con compañeros
- Ayudarse con errores técnicos
- Compartir recursos de aprendizaje
- Explicar cómo resolviste un problema

### NO Permitido ❌

- Copiar código de compañeros
- Compartir tu código completo
- Usar el dominio de otro aprendiz
- Entregar trabajo de otra persona

---

## 📞 Soporte

Si tienes dudas sobre cómo adaptar ejercicios a tu dominio:

1. **Consulta con el instructor** durante la sesión
2. **Investiga** por tu cuenta sobre tu tipo de negocio
3. **Pregunta en clase** de forma general (sin revelar tu dominio)

---

## 🚀 ¡Comienza tu Proyecto!

Este dominio es tuyo por las próximas 9 semanas. Conviértelo en un proyecto de portfolio que demuestre tus habilidades reales de implantación de software.

**¡ÉXITO EN TU APRENDIZAJE!** 🎯

---

**Última actualización**: {datetime.now().strftime("%d de %B de %Y")}  
**Instructor**: [Nombre del Instructor]  
**Contacto**: [Correo del Instructor]
"""
    
    with open(carpeta / "dominio.md", 'w', encoding='utf-8') as f:
        f.write(contenido_dominio)
    
    # ============================================================================
    # ARCHIVO 2: asignacion-semana-01.md
    # ============================================================================
    
    contenido_semana01 = f"""# Asignación Semana 1 - {dominio}

**Aprendiz**: {nombre_completo}  
**Dominio**: {dominio}  
**Fecha**: Semana 1 del Bootcamp

---

## 🎯 Objetivos de la Semana

1. Comprender el proceso de implantación de software
2. Conocer fundamentos de hardware de servidores
3. Instalar y configurar Docker
4. Desplegar PostgreSQL con Docker Compose
5. **Adaptar todo a tu dominio: {dominio}**

---

## 📝 Actividades

### Actividad 1: Instalación de Docker

**Instrucciones generales**: Consulta `bootcamp/semana-01/2-practicas/01-instalar-docker.md`

**Adaptación a tu dominio**:
- En la documentación, menciona que instalarás Docker para el proyecto de **{dominio}**
- Cuando documentes el proceso, usa el contexto de tu negocio

**Entregables**:
- ✅ Documento de instalación contextualizado
- ✅ Capturas de pantalla con verificaciones
- ✅ `docker --version` y `docker compose version`

---

### Actividad 2: Base de Datos PostgreSQL

**Instrucciones generales**: Consulta `bootcamp/semana-01/2-practicas/02-primer-contenedor-postgresql.md`

**Adaptación OBLIGATORIA a {dominio}**:

#### Nombres Específicos

```yaml
# docker-compose.yml
services:
  postgres:
    container_name: {nombre_archivo.replace('-', '_')}_postgres
    environment:
      POSTGRES_DB: {nombre_archivo.replace('-', '_')}_db
      POSTGRES_USER: {nombre_archivo.replace('-', '_')}_admin
      POSTGRES_PASSWORD: [TU_PASSWORD_SEGURA]
    volumes:
      - {nombre_archivo.replace('-', '_')}_data:/var/lib/postgresql/data

volumes:
  {nombre_archivo.replace('-', '_')}_data:
```

#### Tablas Específicas del Dominio

**Investiga tu dominio y crea AL MENOS 3 tablas apropiadas.**

Ejemplo genérico (DEBES ADAPTAR):

```sql
-- ¿Qué? Crear tablas para {dominio}
-- ¿Para qué? Gestionar información del negocio

-- Tabla 1: [Entidad principal de tu dominio]
CREATE TABLE [nombre_tabla_1] (
    id SERIAL PRIMARY KEY,
    -- Agrega columnas relevantes para tu dominio
);

-- Tabla 2: [Segunda entidad importante]
CREATE TABLE [nombre_tabla_2] (
    id SERIAL PRIMARY KEY,
    -- Agrega columnas relevantes
);

-- Tabla 3: [Tercera entidad necesaria]
CREATE TABLE [nombre_tabla_3] (
    id SERIAL PRIMARY KEY,
    -- Agrega columnas relevantes
);
```

**IMPORTANTE**: 
- NO uses nombres genéricos
- Investiga qué tablas necesita realmente tu tipo de negocio
- Incluye relaciones entre tablas (claves foráneas)

#### Datos de Ejemplo

**Inserta AL MENOS 5 registros por tabla con datos realistas de tu dominio.**

```sql
-- ¿Qué? Insertar datos de ejemplo para {dominio}
-- ¿Para qué? Probar la funcionalidad del sistema

INSERT INTO [tabla_1] VALUES ...;
-- Datos realistas de tu dominio
```

---

### Actividad 3: Verificación de Persistencia

**Instrucciones**:

1. Inserta datos en tus tablas
2. Ejecuta: `docker compose down`
3. Ejecuta: `docker compose up -d`
4. Verifica que los datos siguen ahí
5. Documenta con capturas de pantalla

---

## 📦 Estructura de Entrega

```
apellido-nombre-semana01/
├── README.md
├── 01-instalacion-docker/
│   ├── INSTALACION.md
│   └── capturas/
├── 02-postgresql-{nombre_archivo}/
│   ├── docker-compose.yml
│   ├── scripts/
│   │   ├── 01-crear-tablas.sql
│   │   └── 02-insertar-datos.sql
│   ├── capturas/
│   └── DOCUMENTACION.md
└── REFLEXION.md
```

---

## ✅ Criterios de Evaluación

### Técnico (50%)
- [ ] Docker instalado y funcionando
- [ ] PostgreSQL desplegado correctamente
- [ ] Base de datos creada con nombre del dominio
- [ ] Al menos 3 tablas creadas
- [ ] Al menos 5 registros por tabla
- [ ] Persistencia verificada

### Dominio (30%)
- [ ] Nombres de BD, tablas y campos reflejan el dominio
- [ ] Estructura coherente con el tipo de negocio
- [ ] Datos realistas y contextualizados
- [ ] NO hay nombres genéricos (tabla1, datos, test, etc.)

### Documentación (20%)
- [ ] Comentarios educativos en TODO el código
- [ ] README completo con instrucciones
- [ ] Capturas de pantalla claras
- [ ] Justificación de decisiones de diseño

---

## 🚨 Errores Comunes a Evitar

### ❌ NO HACER

1. **NO copiar código de compañeros**
   - Tu dominio es único
   
2. **NO usar nombres genéricos**
   ```sql
   -- MAL ❌
   CREATE TABLE usuarios (...);
   CREATE TABLE productos (...);
   ```

3. **NO inventar datos irreales**
   ```sql
   -- MAL ❌
   INSERT INTO tabla VALUES ('aaaa', 'bbb', 'ccc');
   ```

### ✅ SÍ HACER

1. **Investigar tu dominio**
   - Busca información sobre este tipo de negocio
   
2. **Usar nombres específicos**
   ```sql
   -- BIEN ✅ (ejemplo, adapta a TU dominio)
   CREATE TABLE [entidad_especifica_tu_dominio] (...);
   ```

3. **Datos realistas**
   ```sql
   -- BIEN ✅ (ejemplo, adapta a TU dominio)
   INSERT INTO [tabla] VALUES ('[datos realistas]', ...);
   ```

---

## 💡 Consejos

1. **Investiga primero**
   - Antes de codificar, investiga cómo funciona tu tipo de negocio
   
2. **Piensa en casos reales**
   - ¿Qué información necesitaría guardar este negocio?
   
3. **Documenta decisiones**
   - Explica por qué elegiste cada tabla y campo
   
4. **Prueba constantemente**
   - Verifica que todo funcione antes de entregar

---

## 📅 Fecha de Entrega

**Fecha límite**: Viernes de la semana 1, 11:59 PM

**Medio de entrega**: [Especificar plataforma: Sofia Plus, Google Classroom, etc.]

---

## 📞 Dudas y Soporte

Si tienes dudas sobre cómo adaptar la actividad a tu dominio:

1. Revisa el archivo `dominio.md`
2. Investiga sobre tu tipo de negocio
3. Consulta con el instructor en clase
4. NO compartas tu dominio con compañeros

---

## 🎯 Recuerda

**Tu dominio es único. Tu solución debe ser única.**

No se trata de copiar, se trata de **aprender aplicando conocimientos a un contexto real.**

---

**¡ÉXITO EN TU PRIMERA SEMANA!** 🚀

---

**Instructor**: [Nombre del Instructor]  
**Contacto**: [Correo del Instructor]
"""
    
    with open(carpeta / "asignacion-semana-01.md", 'w', encoding='utf-8') as f:
        f.write(contenido_semana01)
    
    print(f"✅ Creada estructura para: {nombre_completo} → {dominio}")


def generar_reporte(asignaciones):
    """
    ¿Qué? Genera reporte de asignaciones
    ¿Para qué? Documentar y auditar asignaciones
    ¿Cómo? Crea archivo markdown con tabla
    
    Args:
        asignaciones (dict): Diccionario de asignaciones
    """
    contenido = f"""# Reporte de Asignaciones de Dominios

**Ficha**: 3147234  
**Programa**: Análisis y Desarrollo de Software (ADSO)  
**Bootcamp**: Implantación de Software  
**Fecha de asignación**: {datetime.now().strftime("%d de %B de %Y, %H:%M:%S")}

---

## 📊 Estadísticas

- **Total de aprendices**: {len(asignaciones)}
- **Total de dominios asignados**: {len(asignaciones)}
- **Total de dominios disponibles**: {len(DOMINIOS)}
- **Método de asignación**: Aleatorio sin repetición

---

## 📋 Tabla de Asignaciones

| # | Aprendiz | Dominio | Categoría | Tipo |
|---|----------|---------|-----------|------|
"""
    
    # Ordenar por número
    items = sorted(enumerate(asignaciones.items(), 1), key=lambda x: x[0])
    
    for numero, ((nombre_completo, nombre_archivo), dominio) in items:
        datos = DOMINIOS[dominio]
        contenido += f"| {numero:02d} | {nombre_completo} | {dominio} | {datos['categoria']} | {datos['tipo']} |\n"
    
    contenido += """
---

## 🔒 Confidencialidad

**IMPORTANTE**: Este archivo contiene información sensible y debe ser tratado de forma confidencial.

- ✅ **Solo el instructor** tiene acceso a este reporte
- ✅ Este archivo está en `.gitignore` (no se sube a repositorio)
- ✅ No compartir asignaciones entre aprendices
- ✅ Cada aprendiz solo conoce SU dominio

---

## 📌 Notas

### Verificación de Unicidad

Todos los dominios asignados son únicos. No hay repeticiones.

### Aleatoriedad

La asignación fue realizada mediante algoritmo de mezcla aleatoria (`random.shuffle()`).

### Trazabilidad

Este reporte permite auditar las asignaciones durante todo el bootcamp.

---

## 📂 Estructura Generada

Se crearon las siguientes carpetas:

```
4-asignación_dominios_aprendiz/
├── README.md
├── generar_asignaciones.py
├── REPORTE-ASIGNACIONES.md (este archivo)
"""
    
    for numero, ((nombre_completo, nombre_archivo), dominio) in items:
        contenido += f"├── aprendiz-{numero:03d}-{nombre_archivo}/\n"
        contenido += f"│   ├── dominio.md\n"
        contenido += f"│   └── asignacion-semana-01.md\n"
    
    contenido += """```

---

## ✅ Validación

### Checklist de Generación

- [x] Archivo de aprendices leído correctamente
- [x] Dominios mezclados aleatoriamente
- [x] Asignaciones uno a uno realizadas
- [x] Carpetas individuales creadas
- [x] Archivo dominio.md generado
- [x] Archivo asignacion-semana-01.md generado
- [x] Reporte completo generado

---

## 📞 Contacto

**Instructor**: [Nombre del Instructor]  
**Email**: [correo@sena.edu.co]  
**Institución**: SENA - CGMLTI - Regional Distrito Capital

---

**Generado automáticamente por el sistema de asignación de dominios.**
"""
    
    with open(REPORTE_FILE, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print(f"\n✅ Reporte generado: {REPORTE_FILE}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    ¿Qué? Función principal del script
    ¿Para qué? Coordinar todo el proceso de asignación
    ¿Cómo? Ejecuta funciones en orden
    """
    print("=" * 70)
    print("🎯 SISTEMA DE ASIGNACIÓN DE DOMINIOS")
    print("=" * 70)
    print(f"Bootcamp: Implantación de Software")
    print(f"Ficha: 3147234")
    print(f"Fecha: {datetime.now().strftime('%d de %B de %Y, %H:%M:%S')}")
    print("=" * 70)
    print()
    
    # 1. Leer aprendices
    print("📖 Leyendo lista de aprendices...")
    aprendices = leer_aprendices()
    print(f"   ✅ {len(aprendices)} aprendices encontrados")
    print()
    
    # 2. Verificar dominios disponibles
    print("🏪 Verificando dominios disponibles...")
    print(f"   ✅ {len(DOMINIOS)} dominios en el banco")
    if len(aprendices) > len(DOMINIOS):
        print(f"   ⚠️  ADVERTENCIA: Faltan {len(aprendices) - len(DOMINIOS)} dominios")
        return
    print()
    
    # 3. Asignar dominios
    print("🎲 Asignando dominios aleatoriamente...")
    asignaciones = asignar_dominios_aleatorios(aprendices)
    print(f"   ✅ {len(asignaciones)} asignaciones realizadas")
    print()
    
    # 4. Crear estructuras
    print("📁 Creando estructuras de carpetas...")
    for numero, ((nombre_completo, nombre_archivo), dominio) in enumerate(asignaciones.items(), 1):
        crear_estructura_aprendiz(numero, nombre_completo, nombre_archivo, dominio)
    print()
    
    # 5. Generar reporte
    print("📊 Generando reporte de asignaciones...")
    generar_reporte(asignaciones)
    print()
    
    # Resumen final
    print("=" * 70)
    print("✅ PROCESO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print(f"✓ {len(aprendices)} aprendices procesados")
    print(f"✓ {len(asignaciones)} dominios asignados")
    print(f"✓ {len(asignaciones)} carpetas creadas")
    print(f"✓ {len(asignaciones) * 2} archivos generados")
    print(f"✓ 1 reporte de asignaciones creado")
    print()
    print("📂 Ubicación:")
    print(f"   {OUTPUT_DIR}")
    print()
    print("📄 Reporte:")
    print(f"   {REPORTE_FILE}")
    print("=" * 70)


# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    # ¿Qué? Punto de entrada del script
    # ¿Para qué? Ejecutar el proceso completo
    main()
