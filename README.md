# Sistema Administrativo - Flask

Un sistema administrativo elegante y moderno desarrollado con Flask y Tailwind CSS para la gestión de empleados y departamentos.

## 🚀 Características

- **Dashboard interactivo** con estadísticas en tiempo real
- **Gestión completa de empleados** (crear, editar, desactivar)
- **Administración de departamentos** con descripciones detalladas
- **Interfaz moderna y responsiva** con Tailwind CSS
- **Base de datos SQLite** para almacenamiento local
- **Diseño limpio y elegante** con iconos Font Awesome

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de Datos**: SQLite con SQLAlchemy
- **Frontend**: Tailwind CSS
- **Iconos**: Font Awesome
- **Estructura**: MVC (Model-View-Controller)

## 📋 Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. **Clona o descarga el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd sistema-administrativo
   ```

2. **Crea un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

5. **Abre tu navegador**
   - Ve a `http://localhost:5000`
   - ¡El sistema está listo para usar!

## 📊 Funcionalidades

### Dashboard
- Vista general con estadísticas
- Contadores de empleados y departamentos
- Accesos rápidos a funciones principales

### Gestión de Empleados
- **Listar empleados** con información detallada
- **Agregar nuevos empleados** con formulario completo
- **Editar información** de empleados existentes
- **Desactivar empleados** (soft delete)
- **Búsqueda y filtros** por departamento

### Gestión de Departamentos
- **Crear departamentos** con descripciones
- **Ver estadísticas** por departamento
- **Contar empleados** por departamento
- **Información organizacional** completa

## 🗄️ Estructura de la Base de Datos

### Tabla: Empleado
- `id`: Identificador único
- `nombre`: Nombre del empleado
- `apellido`: Apellido del empleado
- `email`: Correo electrónico (único)
- `telefono`: Número de teléfono
- `departamento`: Departamento asignado
- `cargo`: Cargo o puesto
- `salario`: Salario del empleado
- `fecha_contratacion`: Fecha de contratación
- `activo`: Estado activo/inactivo

### Tabla: Departamento
- `id`: Identificador único
- `nombre`: Nombre del departamento (único)
- `descripcion`: Descripción del departamento

## 🎨 Diseño y UI/UX

- **Paleta de colores moderna**: Azul primario, verde de acento
- **Diseño responsivo**: Funciona en móviles y escritorio
- **Componentes reutilizables**: Tarjetas, botones, formularios
- **Iconografía consistente**: Font Awesome para mejor UX
- **Transiciones suaves**: Efectos hover y focus

## 🔒 Seguridad

- **Validación de formularios** en frontend y backend
- **Sanitización de datos** de entrada
- **Manejo de errores** con mensajes informativos
- **Soft delete** para preservar datos históricos

## 🚀 Despliegue

### Desarrollo Local
```bash
python app.py
```

### Producción (recomendado)
```bash
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📝 API Endpoints

- `GET /` - Dashboard principal
- `GET /empleados` - Lista de empleados
- `GET /empleados/nuevo` - Formulario nuevo empleado
- `POST /empleados/nuevo` - Crear empleado
- `GET /empleados/<id>/editar` - Formulario editar empleado
- `POST /empleados/<id>/editar` - Actualizar empleado
- `POST /empleados/<id>/eliminar` - Desactivar empleado
- `GET /departamentos` - Lista de departamentos
- `GET /departamentos/nuevo` - Formulario nuevo departamento
- `POST /departamentos/nuevo` - Crear departamento
- `GET /api/empleados` - API JSON de empleados

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado con ❤️ usando Flask y Tailwind CSS

---

**¡Disfruta usando el Sistema Administrativo!** 🎉 