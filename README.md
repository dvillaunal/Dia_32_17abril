# Uso de ``*args`` y ``**kwargs``:

## 1. ``*args``:

La sintaxis especial * args en las definiciones de funciones en Python se usa para pasar un número variable de argumentos a una función. Se utiliza para pasar una lista de argumentos de longitud variable sin palabras clave.

 * La sintaxis es usar el símbolo ``*`` para tomar un número      variable de argumentos; por convención, se usa a menudo    con la palabra ``args`` _(puede ser otro)_.
 
 *  Lo que ``* args`` le permite hacer es aceptar más argumentos que el número de argumentos formales que definió anteriormente. Con `*args` , se puede agregar        cualquier número de argumentos adicionales a sus           parámetros formales actuales (incluidos cero argumentos    adicionales).

 * **Por ejemplo:** queremos hacer una función de                 multiplicación que tome cualquier número de argumentos y   sea capaz de multiplicarlos todos juntos. Se puede hacer   usando ``*args``.

 * Al usar ``*``, la variable que asociamos con ``*`` se convierte en un iterable, lo que significa que puede hacer cosas como iterar sobre ella, ejecutar algunas funciones de orden superior como mapa y filtro, etc.

## 2. ``**kwargs``:

La sintaxis especial ``** kwargs`` en las definiciones de funciones en Python se usa para pasar una lista de argumentos de longitud variable con palabras clave. __Usamos el nombre kwargs con la estrella doble. La razón es porque la estrella doble nos permite pasar a través de argumentos de palabras clave (y cualquier número de ellos).__

 *  Un argumento de palabra clave es donde proporciona un nombre a la variable a medida que la pasa a la función.

 * Uno puede pensar en los kwargs como un diccionario que asigna cada palabra clave al valor que le pasamos junto a ella. Es por eso que cuando iteramos sobre los kwargs no parece haber ningún orden en el que se imprimieron.

 
