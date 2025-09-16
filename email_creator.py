"""Creador de correos electrónicos personalizados.

Este programa pregunta al usuario cuántas letras y cuántos números desea
antes del símbolo "@", y el dominio del correo electrónico. Después, genera
un correo con caracteres aleatorios que cumplan esas condiciones.
"""

import random
import string
from typing import Optional


def solicitar_entero(mensaje: str, *, minimo: Optional[int] = None) -> int:
    """Solicita un número entero al usuario y valida que cumpla con un mínimo.

    Args:
        mensaje: Texto que se mostrará al solicitar el número.
        minimo: Valor mínimo aceptado (inclusive). Si es ``None`` no se valida.

    Returns:
        El entero introducido por el usuario.
    """
    while True:
        try:
            respuesta = input(mensaje).strip()
        except EOFError:
            print("\nEntrada finalizada inesperadamente. Inténtalo de nuevo.")
            continue

        if not respuesta:
            print("Por favor, introduce un número entero.")
            continue

        try:
            valor = int(respuesta)
        except ValueError:
            print(f"\"{respuesta}\" no es un número entero válido.")
            continue

        if minimo is not None and valor < minimo:
            if minimo == 0:
                print("El número no puede ser negativo.")
            else:
                print(f"El número debe ser mayor o igual a {minimo}.")
            continue

        return valor


def solicitar_dominio() -> str:
    """Pide al usuario que introduzca un dominio válido y lo devuelve."""
    while True:
        try:
            dominio = input("Introduce el dominio (por ejemplo, gmail.com): ").strip()
        except EOFError:
            print("\nEntrada finalizada inesperadamente. Inténtalo de nuevo.")
            continue

        if not dominio:
            print("El dominio no puede estar vacío.")
            continue

        if "@" in dominio:
            print("No incluyas el símbolo '@' en el dominio.")
            continue

        if dominio.startswith(".") or dominio.endswith("."):
            print("El dominio no puede comenzar ni terminar con un punto.")
            continue

        if " " in dominio:
            print("El dominio no puede contener espacios.")
            continue

        return dominio


def generar_correo(cantidad_letras: int, cantidad_numeros: int, dominio: str) -> str:
    """Genera un correo electrónico con la cantidad de letras y números indicados."""
    letras = [random.choice(string.ascii_lowercase) for _ in range(cantidad_letras)]
    numeros = [random.choice(string.digits) for _ in range(cantidad_numeros)]

    local_partes = letras + numeros
    random.shuffle(local_partes)
    local = "".join(local_partes)

    return f"{local}@{dominio}"


def main() -> None:
    """Función principal que coordina la creación del correo."""
    print("=== Generador de correos electrónicos ===")

    cantidad_letras = solicitar_entero("¿Cuántas letras deseas antes del '@'? ", minimo=0)
    cantidad_numeros = solicitar_entero("¿Cuántos números deseas antes del '@'? ", minimo=0)

    if cantidad_letras == 0 and cantidad_numeros == 0:
        print("Debes elegir al menos una letra o un número para crear el correo.")
        return

    dominio = solicitar_dominio()

    correo = generar_correo(cantidad_letras, cantidad_numeros, dominio)
    print(f"\nTu correo generado es: {correo}")


if __name__ == "__main__":
    main()
