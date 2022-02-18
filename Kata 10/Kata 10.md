# Kata del módulo 10

## Uso de tracebacks para buscar errores

### Tracebacks

Intenta crear un archivo de Python y asígnale el nombre *open.py*, con el contenido siguiente:

```
def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()
```

![1](Kata 10.assets/1.png)

![2](Kata 10.assets/2-5155170.png)

## Controlando las excepciones
### Try y Except de los bloques

Vamos a crear un archivo de Python denominado config.py. El archivo tiene código que busca y lee el archivo de configuración del sistema de navegación:

![3](Kata 10.assets/3.png)

![4](Kata 10.assets/4.png)

A continuación, quitamos el archivo *config.txt* y creamos un directorio denominado *config.txt*. Intentaremos llamar al archivo *config.py* para ver un error nuevo.

![5](Kata 10.assets/5.png)

Una manera poco útil de controlar este error sería detectando todas las excepciones para evitar un Traceback. Para comprenderlo mejor probaremos actualizando la función `main()`

![6](Kata 10.assets/6.png)

Que, ejecutando en consola, nos aparece lo siguiente:

![7](Kata 10.assets/7.png)

Vamos a corregir este fragmento de código para abordar todas estas frustraciones. Revertiremos la detección de `FileNotFoundError` y luego agregamos otro bloque `except` para detectar `PermissionError`:

```python
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
```

![8](Kata 10.assets/8.png)

Y al ejecutarlo, nos produce el siguiente resultado en consola:

![9](Kata 10.assets/9.png)

Eliminamos el archivo config.txt para asegurarnos de que se alcanza el primer bloque `except` en su lugar:

![10](Kata 10.assets/10.png)

Podemos agrupar las excepciones como si fuera una, usando paréntesis en la línea `except`, por ejemplo, si el sistema está bajo cargas pesadas y el sistema de archivos está demasiado ocupado, tiene sentido detectar `BlockingIOError` y `TimeOutError` juntos:

![11](Kata 10.assets/11.png)

Si necesitas acceder al error asociado a la excepción, debes actualizar la línea `except` para incluir la palabra clave `as`. Esta técnica es práctica si una excepción es demasiado genérica y el mensaje de error puede ser útil:

![12](Kata 10.assets/12.png)

Y en consola nos produce lo siguiente:

![13](Kata 10.assets/13.png)

En este caso, `as err` significa que `err` se convierte en una variable con el objeto de excepción como valor; después, usa este valor para imprimir el mensaje de error asociado a la excepción. Otra razón para utilizar esta técnica es acceder directamente a los atributos del error. Por ejemplo, si detecta una excepción `OSError` más genérica, que es la excepción primaria de `FilenotFoundError` y `PermissionError`, podemos diferenciarla mediante el atributo `.errno`:

![14](Kata 10.assets/14.png)

Y en consola nos produce lo siguiente:

![15](Kata 10.assets/15.png)

## Generación de excepciones

Si conocemos una situación que podría provocar una condición de error al escribir código, resulta útil generar excepciones que permitan que otro código comprenda cuál es el problema.

En este ejemplo, tenemos que los astronautas limitan el uso de agua a 11 litros diarios; crearemos una función que, con base al número de astronautas, pueda calcular la cantidad de agua que quedará después de un día o más:

![15](Kata 10.assets/15-5159314.png)

Probemos con 5 astronautas, 100 litros de agua y 2 días:

![16](Kata 10.assets/16.png)

Esto no es muy útil ya que una carencia en los litros sería un error; para ello generaremos una excepción en la función `water_left()` para alertar de la condición del error:

![17](Kata 10.assets/17.png)

Y al volverlo a ejecutar, tenemos:

![18](Kata 10.assets/18.png)

Actualizamos la función `water_left()`para evitar el paso de tipos no admitidos

![19](Kata 10.assets/19.png)

Y al pasar los argumentos, comprobamos el error `TypeError`:

![20](Kata 10.assets/20.png)

Este error no es muy descriptivo en el contexto de la función, por lo que acutalizaremos la función para que use `TypeError` pero con un mensaje:

![21](Kata 10.assets/21.png)

Y al volver a intentarlo, obtenemos:

![22](Kata 10.assets/22.png)

**Fin del ejercicio**

---

- Github: [Rene-Bedolla](https://github.com/Rene-Bedolla)
