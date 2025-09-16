# Generador de correos

Este repositorio contiene un sencillo programa de consola escrito en Python
que crea direcciones de correo electrónico personalizadas a partir de las
preferencias del usuario.

## Requisitos

* Python 3.8 o superior.

## Uso

Ejecuta el script y responde a las preguntas:

```bash
python email_creator.py
```

El programa solicitará:

1. **Cantidad de letras** que deseas antes del símbolo `@`.
2. **Cantidad de números** que deseas antes del símbolo `@`.
3. **Dominio** del correo (sin incluir el `@`).

Con estos datos, el generador construirá el identificador antes de `@` usando
caracteres aleatorios y mostrará la dirección de correo resultante.
