#Respuestas manejo de excepciones confusas
Problema 1:
1- No podría saberlo porque el except captura todo sin mostrar mensaje ni tipo de excepción 
2- También sería capturado pero sin mostrar información 
3- Hace muy complicada la depuración ya que oculta el tipo y la causa del error, impidiendo así, encontrar el problema real en el código.

Problema 2:
1- FileNotFoundError si el archivo no existe, ValueError si hay un valor no convertible a entero, ZeroDivisionError si la lista está vacía.
2- No, cada tipo de error se debe tratar de manera diferente. Si el archivo no esxiste, mostrar un mensaje claro. Si hay datos inválidos, reportar el dato incorrecto. Si la lista está vacía, avisar que no hay datos.
3- Se pierde la especificidad, es decir que no se sabe qué tipo ocurrió, ni en qué linea, ni su causa.

Problema 3:
1- El programa debería informar al usuario que no se pudo guardar y posiblemente intentar nuevamente o guardar en otra ubicación.
2- Con un mensaje que indique que no se pudo guardar la configuración.
3- no, lo dejaría propagar para detectar el fallo.

Problema 4:
1- El else se ejecuta solo si no ocurre ningún error en el bloque try, el finally se ejecuta siempre así haya o no un error, aún cuando hay un return obreak.
2- else: para un código que solo debe ejecutarse si no hubo un error.
   finally: para cerrar recursos o limpiar.
3-el bloque finally aún se ejecuta antes de que el return devuelva le control.

Problema 5:
1- Dependiendo del contexto: para la edad negativa un ValueError, para la división entre cero un ZeroDivisionError, para nombre vacío FileNotFoundError si se espera un archivo.
2- El mensaje debería explicar qué falló y por qué.
3- Esto permite que el código que usa la función sepa qué tipo de error ocurrió y pueda decidir cómo manejarlo.

Problema 6: 
1- Cuando se puede solucionar o controlar el error localmente.
2- Cuando no se puede resolver pero quiero registrar el error para depurar y dejar que otro nivel superior lo maneje.
3- Cuando el error debe propagarse naturalmente, como errores de programación.

Problema 7: 
1- Depende del contexto: si los datos son críticos, sí. Si se puede puede continuar con los demás elementos es mejor manejar el error y seguir.
2- Guardar los errores en una lista y mostrarlos al final.
3- Se tendría una lista vacía de resultados.