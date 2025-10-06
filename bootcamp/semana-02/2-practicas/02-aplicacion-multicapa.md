# Práctica 2: Aplicación Multicapa (Frontend + API + Database)

## 🎯 Objetivo

Construir una aplicación completa de 3 capas con Docker Compose:

- **Frontend**: Nginx sirviendo HTML
- **API**: Node.js con Express
- **Database**: PostgreSQL

**Tiempo estimado**: 50 minutos

---

## 📋 Pre-requisitos

```bash
# Verificar Docker Compose
docker compose version

# Verificar Node.js (para construir la API localmente antes)
node --version  # v18+ recomendado
```

---

## 📁 Estructura del Proyecto

```
app-multicapa/
├── docker-compose.yml
├── .env
├── .dockerignore
├── frontend/
│   └── index.html
├── api/
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── nginx/
│   └── nginx.conf
└── db/
    └── init.sql
```

---

## 🚀 Parte 1: Preparar el Proyecto

### Paso 1: Crear Estructura de Carpetas

```bash
# ¿Qué? Crear proyecto y carpetas
mkdir -p ~/bootcamp/app-multicapa/{frontend,api,nginx,db}
cd ~/bootcamp/app-multicapa
```

---

## 📱 Parte 2: Crear el Frontend

### Paso 2: Crear frontend/index.html

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0" />
    <title>Bootcamp - App Multicapa</title>
    <style>
      /* ¿Para qué? Estilos básicos para una interfaz limpia */
      body {
        font-family: Arial, sans-serif;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        background: #f5f5f5;
      }
      .container {
        background: white;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      }
      h1 {
        color: #2c3e50;
      }
      button {
        background: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        margin: 5px;
      }
      button:hover {
        background: #2980b9;
      }
      #resultado {
        margin-top: 20px;
        padding: 15px;
        background: #ecf0f1;
        border-radius: 4px;
      }
      .estudiante {
        padding: 10px;
        margin: 10px 0;
        background: #fff;
        border-left: 4px solid #3498db;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>🎓 Bootcamp - Aplicación Multicapa</h1>
      <p>
        Esta aplicación demuestra arquitectura de 3 capas con Docker Compose
      </p>

      <h2>Operaciones Disponibles</h2>
      <button onclick="obtenerEstudiantes()">📋 Ver Estudiantes</button>
      <button onclick="crearEstudiante()">➕ Crear Estudiante</button>
      <button onclick="verificarSalud()">🩺 Verificar Salud API</button>

      <div id="resultado"></div>
    </div>

    <script>
      // ¿Qué? URL de la API (proxy inverso de Nginx)
      // ¿Para qué? Frontend no se conecta directamente a la API
      const API_URL = '/api';

      // ¿Qué? Función para obtener lista de estudiantes
      async function obtenerEstudiantes() {
        try {
          // ¿Para qué? Realizar petición GET a la API
          const response = await fetch(`${API_URL}/estudiantes`);
          const data = await response.json();

          // ¿Qué? Construir HTML con los estudiantes
          let html = '<h3>Estudiantes Registrados:</h3>';
          data.forEach((est) => {
            html += `
                        <div class="estudiante">
                            <strong>${est.nombre} ${est.apellido}</strong><br>
                            Email: ${est.email}<br>
                            Registrado: ${new Date(
                              est.fecha_registro
                            ).toLocaleDateString()}
                        </div>
                    `;
          });

          document.getElementById('resultado').innerHTML = html;
        } catch (error) {
          document.getElementById(
            'resultado'
          ).innerHTML = `<p style="color: red;">❌ Error: ${error.message}</p>`;
        }
      }

      // ¿Qué? Función para crear estudiante de ejemplo
      async function crearEstudiante() {
        // ¿Para qué? Generar datos aleatorios
        const nombres = ['Ana', 'Luis', 'Pedro', 'Laura', 'Diego'];
        const apellidos = [
          'Martínez',
          'Rodríguez',
          'González',
          'Sánchez',
          'Torres',
        ];

        const nombre = nombres[Math.floor(Math.random() * nombres.length)];
        const apellido =
          apellidos[Math.floor(Math.random() * apellidos.length)];
        const email = `${nombre.toLowerCase()}.${apellido.toLowerCase()}@example.com`;

        try {
          // ¿Para qué? Enviar petición POST a la API
          const response = await fetch(`${API_URL}/estudiantes`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nombre, apellido, email }),
          });

          const data = await response.json();

          document.getElementById(
            'resultado'
          ).innerHTML = `<p style="color: green;">✅ Estudiante creado: ${data.nombre} ${data.apellido}</p>`;

          // ¿Para qué? Actualizar lista automáticamente
          setTimeout(obtenerEstudiantes, 500);
        } catch (error) {
          document.getElementById(
            'resultado'
          ).innerHTML = `<p style="color: red;">❌ Error: ${error.message}</p>`;
        }
      }

      // ¿Qué? Función para verificar salud de la API
      async function verificarSalud() {
        try {
          const response = await fetch(`${API_URL}/health`);
          const data = await response.json();

          document.getElementById('resultado').innerHTML = `
                    <h3>Estado de la API:</h3>
                    <p><strong>Estado:</strong> ${data.status}</p>
                    <p><strong>Tiempo activo:</strong> ${Math.floor(
                      data.uptime
                    )} segundos</p>
                    <p><strong>Timestamp:</strong> ${new Date(
                      data.timestamp
                    ).toLocaleString()}</p>
                `;
        } catch (error) {
          document.getElementById(
            'resultado'
          ).innerHTML = `<p style="color: red;">❌ Error: ${error.message}</p>`;
        }
      }

      // ¿Para qué? Cargar estudiantes automáticamente al abrir la página
      window.addEventListener('load', obtenerEstudiantes);
    </script>
  </body>
</html>
```

---

## 🖥️ Parte 3: Crear la API

### Paso 3: Crear api/package.json

```json
{
  "name": "bootcamp-api",
  "version": "1.0.0",
  "description": "API REST para aplicación multicapa",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.3",
    "cors": "^2.8.5"
  }
}
```

---

### Paso 4: Crear api/server.js

```javascript
// ¿Qué? Importar dependencias necesarias
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

// ¿Qué? Crear aplicación Express
const app = express();
const PORT = 3000;

// ¿Qué? Configurar middlewares
app.use(cors()); // ¿Para qué? Permitir peticiones desde el frontend
app.use(express.json()); // ¿Para qué? Parsear JSON en peticiones

// ¿Qué? Configurar pool de conexiones a PostgreSQL
// ¿Para qué? Gestionar conexiones de manera eficiente (reúso)
const pool = new Pool({
  host: process.env.DB_HOST || 'db',
  // ¿Por qué 'db'? Es el nombre del servicio en docker-compose.yml
  port: process.env.DB_PORT || 5432,
  user: process.env.DB_USER || 'admin_bootcamp',
  password: process.env.DB_PASSWORD || 'password123',
  database: process.env.DB_NAME || 'bootcamp_db',
  max: 20, // ¿Para qué? Máximo 20 conexiones simultáneas
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

// ¿Qué? Verificar conexión a la base de datos al iniciar
pool.connect((err, client, release) => {
  if (err) {
    console.error('❌ Error conectando a PostgreSQL:', err.stack);
  } else {
    console.log('✅ Conectado a PostgreSQL');
    release(); // ¿Para qué? Liberar la conexión de vuelta al pool
  }
});

// ===== ENDPOINTS =====

// ¿Qué? Endpoint de salud (health check)
// ¿Para qué? Verificar que la API y la BD funcionan
app.get('/health', async (req, res) => {
  try {
    // ¿Qué? Probar conexión a la base de datos
    const result = await pool.query('SELECT NOW()');

    res.json({
      status: 'healthy',
      timestamp: new Date().toISOString(),
      uptime: process.uptime(), // ¿Para qué? Tiempo que lleva corriendo la API
      database: 'connected',
    });
  } catch (error) {
    res.status(503).json({
      status: 'unhealthy',
      error: error.message,
    });
  }
});

// ¿Qué? GET /estudiantes - Obtener todos los estudiantes
app.get('/estudiantes', async (req, res) => {
  try {
    const result = await pool.query(
      'SELECT * FROM estudiantes ORDER BY fecha_registro DESC'
    );

    res.json(result.rows);
  } catch (error) {
    console.error('Error al obtener estudiantes:', error);
    res.status(500).json({ error: 'Error al obtener estudiantes' });
  }
});

// ¿Qué? GET /estudiantes/:id - Obtener un estudiante específico
app.get('/estudiantes/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query('SELECT * FROM estudiantes WHERE id = $1', [
      id,
    ]);

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Estudiante no encontrado' });
    }

    res.json(result.rows[0]);
  } catch (error) {
    console.error('Error al obtener estudiante:', error);
    res.status(500).json({ error: 'Error al obtener estudiante' });
  }
});

// ¿Qué? POST /estudiantes - Crear nuevo estudiante
app.post('/estudiantes', async (req, res) => {
  try {
    const { nombre, apellido, email } = req.body;

    // ¿Qué? Validar datos
    if (!nombre || !apellido || !email) {
      return res.status(400).json({
        error: 'Faltan campos requeridos: nombre, apellido, email',
      });
    }

    // ¿Qué? Insertar estudiante en la base de datos
    const result = await pool.query(
      'INSERT INTO estudiantes (nombre, apellido, email) VALUES ($1, $2, $3) RETURNING *',
      [nombre, apellido, email]
    );

    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.error('Error al crear estudiante:', error);

    // ¿Qué? Manejar error de email duplicado
    if (error.code === '23505') {
      // Código de PostgreSQL para violación de UNIQUE
      return res.status(409).json({ error: 'El email ya está registrado' });
    }

    res.status(500).json({ error: 'Error al crear estudiante' });
  }
});

// ¿Qué? Iniciar servidor
app.listen(PORT, () => {
  console.log(`🚀 API corriendo en http://localhost:${PORT}`);
});
```

---

### Paso 5: Crear api/Dockerfile

```dockerfile
# ¿Qué? Usar imagen de Node.js Alpine (ligera)
FROM node:20-alpine

# ¿Qué? Crear usuario no-root
RUN addgroup -g 1000 apiuser && \
    adduser -D -u 1000 -G apiuser apiuser

WORKDIR /app

# ¿Qué? Copiar archivos de dependencias primero
# ¿Para qué? Cachear la capa de npm install (más rápido)
COPY package*.json ./

# ¿Qué? Instalar solo dependencias de producción
RUN npm ci --only=production

# ¿Qué? Copiar código fuente
COPY server.js ./

# ¿Qué? Cambiar propietario
RUN chown -R apiuser:apiuser /app

# ¿Qué? Cambiar a usuario no-root
USER apiuser

# ¿Qué? Exponer puerto
EXPOSE 3000

# ¿Qué? Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# ¿Qué? Comando para iniciar la API
CMD ["node", "server.js"]
```

---

### Paso 6: Crear api/.dockerignore

```bash
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
```

---

## 🌐 Parte 4: Configurar Nginx

### Paso 7: Crear nginx/nginx.conf

```nginx
# ¿Qué? Configuración de Nginx como proxy inverso

events {
    worker_connections 1024;  # ¿Para qué? Máximo conexiones simultáneas
}

http {
    # ¿Qué? Configurar tipos MIME
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # ¿Qué? Servidor principal
    server {
        listen 80;  # ¿Para qué? Escuchar en puerto 80 (HTTP)

        # ¿Qué? Servir archivos estáticos (Frontend)
        location / {
            root /usr/share/nginx/html;
            index index.html;
            try_files $uri $uri/ /index.html;
            # ¿Para qué? Si no encuentra el archivo, devolver index.html
        }

        # ¿Qué? Proxy inverso para la API
        # ¿Para qué? Todas las peticiones a /api/* se reenvían al backend
        location /api/ {
            # ¿Qué? Reescribir URL (remover /api del path)
            rewrite ^/api/(.*) /$1 break;
            # Ejemplo: /api/estudiantes → /estudiantes

            # ¿Qué? Proxy hacia el servicio 'api'
            proxy_pass http://api:3000;
            # ¿Por qué 'api'? Es el nombre del servicio en docker-compose.yml

            # ¿Qué? Headers para el proxy
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            # ¿Qué? Timeouts
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }
    }
}
```

---

## 🗄️ Parte 5: Crear Script de Base de Datos

### Paso 8: Crear db/init.sql

```sql
-- ¿Qué? Script de inicialización de base de datos

-- ¿Qué? Crear tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ¿Qué? Índice para búsquedas rápidas por email
CREATE INDEX IF NOT EXISTS idx_estudiantes_email ON estudiantes(email);

-- ¿Qué? Insertar datos de ejemplo
INSERT INTO estudiantes (nombre, apellido, email) VALUES
    ('Juan', 'Pérez', 'juan.perez@example.com'),
    ('María', 'García', 'maria.garcia@example.com'),
    ('Carlos', 'López', 'carlos.lopez@example.com'),
    ('Ana', 'Martínez', 'ana.martinez@example.com'),
    ('Luis', 'Rodríguez', 'luis.rodriguez@example.com')
ON CONFLICT (email) DO NOTHING;
-- ¿Para qué? Si ya existen (por reiniciar), no duplicar
```

---

## 🐳 Parte 6: Crear Docker Compose

### Paso 9: Crear .env

```bash
# Variables de entorno para la aplicación
DB_USER=admin_bootcamp
DB_PASSWORD=Bootcamp2024Secure!
DB_NAME=bootcamp_db
DB_PORT=5432
```

---

### Paso 10: Crear docker-compose.yml

```yaml
version: '3.8'

services:
  # ===== BASE DE DATOS =====
  db:
    image: postgres:15-alpine
    container_name: app-db
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
    restart: unless-stopped
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${DB_USER}']
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend # ¿Para qué? Solo accesible desde la API

  # ===== API (BACKEND) =====
  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    container_name: app-api
    environment:
      DB_HOST: db
      DB_PORT: ${DB_PORT}
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_NAME: ${DB_NAME}
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - backend # ¿Para qué? Comunicarse con la base de datos
      - frontend # ¿Para qué? Recibir peticiones desde Nginx

  # ===== NGINX (REVERSE PROXY + FRONTEND) =====
  nginx:
    image: nginx:alpine
    container_name: app-nginx
    ports:
      - '80:80' # ¿Para qué? Exponer la aplicación al host
    volumes:
      - ./frontend/index.html:/usr/share/nginx/html/index.html:ro
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api
    restart: unless-stopped
    networks:
      - frontend # ¿Para qué? Comunicarse con la API

# ¿Qué? Definir redes personalizadas
networks:
  frontend:
    # ¿Para qué? Red para comunicación Nginx ↔ API
  backend:
    # ¿Para qué? Red para comunicación API ↔ Base de Datos

volumes:
  postgres_data:
```

---

## 🏃 Parte 7: Ejecutar la Aplicación

### Paso 11: Construir y Levantar Servicios

```bash
# ¿Qué? Construir la imagen de la API y levantar todos los servicios
docker compose up --build -d

# Salida esperada:
# [+] Building...
# [+] Running 4/4
#  ✔ Network app-multicapa_frontend    Created
#  ✔ Network app-multicapa_backend     Created
#  ✔ Container app-db                  Started
#  ✔ Container app-api                 Started
#  ✔ Container app-nginx               Started
```

---

### Paso 12: Verificar Servicios

```bash
# ¿Qué? Ver contenedores corriendo
docker compose ps

# ¿Qué? Ver logs de todos los servicios
docker compose logs

# ¿Qué? Ver logs de un servicio específico en tiempo real
docker compose logs -f api
```

---

### Paso 13: Probar la Aplicación

1. **Abrir navegador**: http://localhost

2. **Verificar que carga la lista de estudiantes** automáticamente

3. **Hacer clic en "Ver Estudiantes"** para actualizar

4. **Hacer clic en "Crear Estudiante"** varias veces

5. **Hacer clic en "Verificar Salud API"**

---

## 🔍 Parte 8: Explorar la Arquitectura

### Paso 14: Probar Conectividad entre Contenedores

```bash
# ¿Qué? Desde la API, hacer ping a la base de datos
docker compose exec api ping -c 3 db

# ¿Qué? Desde Nginx, hacer ping a la API
docker compose exec nginx ping -c 3 api

# ¿Qué? Intentar ping desde Nginx a DB (debería FALLAR)
docker compose exec nginx ping -c 3 db
# ❌ Error: No están en la misma red (seguridad)
```

---

### Paso 15: Inspeccionar Redes

```bash
# ¿Qué? Ver redes creadas
docker network ls | grep app-multicapa

# ¿Qué? Inspeccionar red frontend
docker network inspect app-multicapa_frontend

# ¿Qué? Ver qué contenedores están en cada red
docker compose exec api ip addr show
```

---

## 🧪 Ejercicios

### Ejercicio 1: Agregar Endpoint DELETE

1. Agregar endpoint en `api/server.js`:

```javascript
app.delete('/estudiantes/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query(
      'DELETE FROM estudiantes WHERE id = $1 RETURNING *',
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Estudiante no encontrado' });
    }

    res.json({ message: 'Estudiante eliminado', estudiante: result.rows[0] });
  } catch (error) {
    console.error('Error al eliminar estudiante:', error);
    res.status(500).json({ error: 'Error al eliminar estudiante' });
  }
});
```

2. Reconstruir y reiniciar:

```bash
docker compose up --build -d api
```

3. Probar con curl:

```bash
curl -X DELETE http://localhost/api/estudiantes/1
```

---

### Ejercicio 2: Agregar Variables de Entorno

1. Modifica `.env`:

   ```bash
   API_PORT=4000
   ```

2. Modifica `docker-compose.yml`:

   ```yaml
   api:
     environment:
       PORT: ${API_PORT}
   ```

3. Modifica `api/server.js`:

   ```javascript
   const PORT = process.env.PORT || 3000;
   ```

4. Actualiza `nginx.conf`:
   ```nginx
   proxy_pass http://api:4000;
   ```

---

## ✅ Criterios de Éxito

- [ ] ✅ Puedes acceder a http://localhost y ver la aplicación
- [ ] ✅ La lista de estudiantes carga automáticamente
- [ ] ✅ Puedes crear nuevos estudiantes
- [ ] ✅ El health check responde correctamente
- [ ] ✅ Los datos persisten después de `docker compose down` y `up -d`
- [ ] ✅ Nginx no puede hacer ping a `db` (redes separadas)
- [ ] ✅ La API puede comunicarse con `db`

---

## 📌 Próximos Pasos

Excelente! Ahora dominas aplicaciones multicapa. En la siguiente práctica, adaptarás esta arquitectura a tu **dominio asignado** en el proyecto integrador.

**Continuar a**: [03-proyecto-integrador.md](./03-proyecto-integrador.md)
