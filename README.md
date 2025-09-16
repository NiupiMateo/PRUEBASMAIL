# Generador de correos

Este repositorio contiene una pequeña aplicación web que genera direcciones de
correo electrónico con letras y números aleatorios según los parámetros que
proporciones.

## Uso

1. Abre el archivo [`email_creator.html`](email_creator.html) en tu navegador
   favorito.
2. Completa los campos del formulario indicando:
   - La cantidad de letras que quieres antes del símbolo `@`.
   - La cantidad de números que quieres antes del símbolo `@`.
   - El dominio del correo (sin incluir el `@`).
   - Cuántas direcciones diferentes deseas generar (hasta 100 por vez).
3. Pulsa **Generar correos** para crear la lista.

El formulario validará los datos introducidos y mostrará cada dirección en una
lista numerada. Si hay algún problema con la entrada, se mostrará un mensaje de
error indicando cómo corregirlo.
