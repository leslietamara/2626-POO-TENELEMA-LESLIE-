# INSTRUCCIONES PARA SUBIR A GITHUB

## Pasos para Crear el Repositorio en GitHub

### 1. Crear un nuevo repositorio en GitHub

1. Ir a https://github.com/new
2. Nombre del repositorio: `restaurante-app` o `sistema-restaurante`
3. Descripción: "Sistema de gestión de restaurante con POO en Python - Semana 7"
4. Seleccionar: **Public** (para que sea accesible)
5. **NO** inicializar con README (ya tenemos uno)
6. Hacer clic en "Create repository"

### 2. Inicializar Git en la carpeta del proyecto

En PowerShell, navega a la carpeta padre:

```powershell
cd C:\Users\TAMARA\PycharmProjects\Clase-Semana-7-POO

# Inicializar repositorio Git
git init

# Configurar datos (si no están configurados)
git config user.name "Tu Nombre"
git config user.email "tu.email@example.com"

# Agregar archivos
git add .

# Primer commit
git commit -m "Initialcommit: Sistema de restaurante con POO"

# Agregar origen remoto (reemplaze con tu URL)
git remote add origin https://github.com/TU_USUARIO/restaurante-app.git

# Subir a main
git branch -M main
git push -u origin main
```

### 3. Alternativa: Clonar y Trabajar

Si prefieres clonar el repositorio primero:

```powershell
# Clonar repositorio vacío
git clone https://github.com/TU_USUARIO/restaurante-app.git

# Copiar archivos de restaurante_app a la carpeta clonada

# Dentro de la carpeta
git add .
git commit -m "Initial commit: Sistema de restaurante con POO"
git push
```

---

## Estructura que se Subirá

```
restaurante-app/
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── cliente.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   ├── main.py
│   ├── prueba.py
│   ├── README.md
│   ├── GUIA_COMPLETA.md
│   └── VALIDACION_REQUISITOS.md
└── .gitignore (opcional)
```

### Archivo .gitignore Recomendado

Crear archivo `.gitignore` en la raíz con:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

---

## Verificación Pre-Push

Antes de subir a GitHub, verificar:

### 1. Estructura correcta
```powershell
tree restaurante_app /F
```
✅ Debe mostrar la estructura correcta

### 2. Código funciona
```powershell
cd restaurante_app
python prueba.py
```
✅ Todas las pruebas deben pasar

### 3. Archivos principales
- ✅ `modelos/producto.py` existe
- ✅ `modelos/cliente.py` existe
- ✅ `servicios/restaurante.py` existe
- ✅ `main.py` existe
- ✅ `README.md` existe

### 4. Sin errores de Python
```powershell
python -m py_compile restaurante_app/modelos/producto.py
python -m py_compile restaurante_app/modelos/cliente.py
python -m py_compile restaurante_app/servicios/restaurante.py
python -m py_compile restaurante_app/main.py
```

---

## Comando Git Rápido (Resumen)

Si ya tienes Git configurado:

```powershell
cd C:\Users\TAMARA\PycharmProjects\Clase-Semana-7-POO

git init
git config user.name "Tu Nombre"
git config user.email "tu.email@example.com"
git add .
git commit -m "Initial commit: Sistema de restaurante con POO"
git remote add origin https://github.com/TU_USUARIO/restaurante-app.git
git branch -M main
git push -u origin main
```

---

## Verificación en GitHub

Una vez subido:

1. Ir a tu repositorio en GitHub
2. Verificar que aparezcan todos los archivos
3. Ver que el README.md se muestre formateado
4. Copiar URL del repositorio: `https://github.com/TU_USUARIO/restaurante-app`

---

## Enlace para Entregar

Copiará esta URL completa:

```
https://github.com/TU_USUARIO/restaurante-app
```

Y la entreguetas según las instrucciones del curso.

---

## Cambios Posteriores

Si necesitas hacer cambios después de subir:

```powershell
# Realizar cambios en los archivos

# Verificar cambios
git status

# Preparar cambios
git add .

# Confirmar cambios
git commit -m "Descripción del cambio"

# Subir
git push
```

---

## Verificación Final del Repositorio

Checklist antes de entregar:

- ✅ Repositorio es **PUBLIC** (no private)
- ✅ Contiene carpeta `restaurante_app/`
- ✅ Contiene carpeta `modelos/` con archivos correctos
- ✅ Contiene carpeta `servicios/` con archivos correctos
- ✅ Contiene `main.py` en la raíz del proyecto
- ✅ Contiene `README.md` visible
- ✅ README tiene: autor, descripción, estructura, conceptos POO
- ✅ Código es ejecutable sin erros
- ✅ Menú funciona correctamente
- ✅ Validaciones funcionan
- ✅ NO contiene archivos `.pyc` o `__pycache__` innecesarios

---

## Ejemplo de README en GitHub

Cuando se visualiza el repositorio, el README debería verse así:

```
# Sistema de Restaurante - Programación Orientada a Objetos

**Autor:** Tamara  
**Fecha:** Semana 7 - Parcial 1  

## Descripción del Sistema
El **Sistema de Restaurante** es una aplicación de consola...

## Estructura del Proyecto
...
```

---

## Ventajas de GitHub

- Historial de cambios
- Control de versiones
- Pruebas colaborativas
- Portfolio profesional
- Compartir código fácilmente

---

## Soporte

Si tienes problemas:

1. Verificar que tengas Git instalado: `git --version`
2. Verificar credenciales de GitHub
3. Usar HTTPS en lugar de SSH si hay problemas
4. Revisar que el repositorio sea PUBLIC

---

## Próximos Pasos

1. ✅ Crear proyecto localmente (YA HECHO)
2. ✅ Probar que funciona (YA HECHO)
3. → Crear repositorio GitHub
4. → Subir archivos
5. → Copiar URL
6. → Entregar URL del repositorio

---

¡El proyecto está listo para GitHub!

Instrucciones creadas: 2025-07-10

