# Calculadora Interactiva en Python

## 📋 Descripción

Este es un proyecto de Python que implementa una calculadora interactiva con funcionalidades matemáticas avanzadas. El proyecto está estructurado como un paquete Python con módulos separados para operaciones matemáticas y utilidades de interacción con el usuario.

## 🚀 Características

### ✨ Funcionalidades Principales
- **Operaciones Matemáticas Básicas**: Suma, resta, multiplicación, división
- **Operaciones Avanzadas**: Potencia, raíz cuadrada, factorial
- **Utilidades Matemáticas**: Verificación de números pares/primos, cálculo de porcentajes
- **Interfaz Interactiva**: Menú de opciones con validación de entrada
- **Manejo de Errores**: Validación robusta de entrada y manejo de excepciones
- **Formateo de Salida**: Mensajes con emojis y formato profesional

### 🛠️ Funciones Disponibles

#### Operaciones Matemáticas (`paquete.operaciones`)
- `suma(a, b)` - Suma dos números
- `resta(a, b)` - Resta dos números
- `multiplicacion(a, b)` - Multiplica dos números
- `division(a, b)` - Divide dos números
- `potencia(base, exponente)` - Calcula la potencia
- `raiz_cuadrada(numero)` - Calcula la raíz cuadrada
- `factorial(n)` - Calcula el factorial
- `porcentaje(valor, total)` - Calcula el porcentaje
- `redondear(numero, decimales)` - Redondea un número
- `es_par(numero)` - Verifica si un número es par
- `es_primo(numero)` - Verifica si un número es primo

#### Utilidades (`paquete.utilidades`)
- `imprimir_mensaje(mensaje, tipo)` - Imprime mensajes formateados
- `obtener_nombre_usuario()` - Solicita y valida el nombre del usuario
- `obtener_numero(mensaje, tipo)` - Solicita y valida números
- `limpiar_pantalla()` - Limpia la consola
- `pausar(mensaje)` - Pausa la ejecución
- `validar_email(email)` - Valida formato de email
- `formatear_fecha(fecha, formato)` - Formatea fechas
- `generar_id()` - Genera IDs únicos
- `mostrar_progreso(actual, total, mensaje)` - Muestra barras de progreso
- `esperar(segundos)` - Espera un tiempo específico
- `confirmar(mensaje)` - Solicita confirmación
- `obtener_opcion_menu(opciones, mensaje)` - Muestra menús interactivos
- `formatear_numero(numero, decimales)` - Formatea números

## 📁 Estructura del Proyecto

```
CoursePython/
├── main.py                 # Archivo principal del programa
├── README.md              # Documentación del proyecto
├── datos.txt              # Archivo de datos (si existe)
├── paquete/               # Paquete principal
│   ├── __init__.py        # Inicializador del paquete
│   ├── operaciones.py     # Módulo de operaciones matemáticas
│   └── utilidades.py      # Módulo de utilidades
└── Python/                # Documentación adicional
    └── Python.md          # Notas sobre Python
```

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7 o superior
- No se requieren dependencias externas (solo módulos de la biblioteca estándar)

### Ejecución
1. Clona o descarga el proyecto
2. Navega al directorio del proyecto
3. Ejecuta el programa principal:

```bash
python main.py
```

### Uso del Paquete
También puedes importar y usar las funciones del paquete en tus propios scripts:

```python
from paquete import operaciones, utilidades

# Usar operaciones matemáticas
resultado = operaciones.suma(10, 5)
utilidades.imprimir_mensaje(f"El resultado es: {resultado}")

# Usar utilidades
nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"¡Hola, {nombre}!")
```

## 🎯 Ejemplos de Uso

### Ejemplo 1: Operaciones Básicas
```python
from paquete.operaciones import suma, multiplicacion, potencia

# Suma
resultado_suma = suma(15, 25)
print(f"15 + 25 = {resultado_suma}")

# Multiplicación
resultado_mult = multiplicacion(7, 8)
print(f"7 × 8 = {resultado_mult}")

# Potencia
resultado_pot = potencia(2, 10)
print(f"2^10 = {resultado_pot}")
```

### Ejemplo 2: Utilidades Avanzadas
```python
from paquete.utilidades import imprimir_mensaje, obtener_opcion_menu
from paquete.operaciones import factorial, es_primo

# Menú interactivo
opciones = ["Calcular factorial", "Verificar si es primo", "Salir"]
opcion = obtener_opcion_menu(opciones, "Selecciona una operación")

if opcion == 1:
    numero = int(input("Ingresa un número: "))
    resultado = factorial(numero)
    imprimir_mensaje(f"El factorial de {numero} es {resultado}", "success")
elif opcion == 2:
    numero = int(input("Ingresa un número: "))
    if es_primo(numero):
        imprimir_mensaje(f"{numero} es un número primo", "success")
    else:
        imprimir_mensaje(f"{numero} no es un número primo", "info")
```

## 🔧 Características Técnicas

### Manejo de Errores
- Validación de tipos de entrada
- Manejo de divisiones por cero
- Captura de excepciones de entrada del usuario
- Mensajes de error informativos

### Tipado
- Uso de type hints para mejor documentación
- Soporte para tipos Union[int, float]
- Documentación de parámetros y valores de retorno

### Modularidad
- Código organizado en módulos reutilizables
- Separación clara de responsabilidades
- Fácil extensión y mantenimiento

## 📝 Documentación

Cada función incluye documentación completa con:
- Descripción de la funcionalidad
- Parámetros de entrada
- Valores de retorno
- Excepciones que puede lanzar
- Ejemplos de uso

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre**
- Email: tu.email@ejemplo.com
- GitHub: [@tu-usuario](https://github.com/tu-usuario)

## 🆘 Soporte

Si encuentras algún problema o tienes alguna pregunta:

1. Revisa la documentación de las funciones
2. Verifica que estés usando Python 3.7+
3. Abre un issue en el repositorio

## 🔄 Historial de Versiones

- **v1.0.0** - Versión inicial con operaciones básicas y utilidades
- Funcionalidades principales implementadas
- Documentación completa
- Manejo de errores robusto

---

⭐ ¡Si te gusta este proyecto, dale una estrella en GitHub!
