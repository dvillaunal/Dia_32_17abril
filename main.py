# Uso de *args y **kwargs
'''
En Python, podemos pasar un número variable de argumentos a una función usando
símbolos especiales. Hay dos símbolos especiales:

-> Símbolos especiales utilizados para pasar argumentos:
    1. * Args (argumentos sin palabras clave)
    
    2. ** kwargs (argumentos de palabras clave)
'''

# *args:
'Definimos una función que itera según los valores ingresados en myFun(), para al final imprimirlos'
def myFun(*argv):
  '''
  esta función esta definida con *args
  '''
  for i in argv:
    print(i)

myFun('Hola', 'Soy una función', 'Definida con', '*args')

# Podemos definir una función 'Normal' y con *args:
'''
Recordemos que para definir funciones en python
es con la palabra def......
después se efine el nombre y dentro del parentesís van
las variables que se utilizaran, es decir,
def f(x,y) <= esta funcion llamada f depende de dos varibles
independientes las cuales son 'x & y'
(Nota: f puede depender de infinitas variables ya depende del programador)


en el caso de hoy haremos algo muy similar utilizaremos x := varible definida
dentro de la funcón & y:= *argv (puedes ingresar más de un valor dentro de myFun)
por "ende no tenemos  limite" en  poner algo logico dentro de f(x, y:= *argv)
'''
# Ejemplo:
'''
*args en una función entra como una tupla de todos los elementos
que toma, es decir, como vemos el lo que imprime:
"print('Imprimiremos letra por letra de {}'.format(argv))"
es una tupla en los {}, asi dejando claro que no itera,
entra los valores de tuple[0] a tuple[n], si ingresamos n valores
'''


def f(x, *argv):
  '''
  Esta función Recibe Numeros Enteros
  para hacer las siguientes operaciones:
  1er termino =>  Intacto
  '''
  print("1er Termino :", x)
  c = 1
  print('---------------------------')
  print('Imprimiremos letra por letra de {}'.format(argv))
  for i in argv:
    for x in i:
      print('---------------------------')
      print(x)
      print('---------------------------')
      c += 1
      if c == 50:
        break


f('Hola', 'Soy una función', 'Definida con', '*args')

# 2. ** kwargs:
'''
Utilizamos *args y **kwargs como argumento cuando tenemos dudas
sobre el número de argumentos que debemos pasar en una función
'''

def nom(**kwargs): 
  for key, value in kwargs.items():
    print("%s == %s" %(key, value))
  
nombre = input('Ingrese su primer o uníco nombre: ')
apellido = input('Ingrese su primer o uníco apellido: ')

print('Mi nombre es: ')
nom(name = 'Daniel', last = 'Villa') 

print('Tu nombre es: ')
nom(name = nombre, last = apellido) 


# usando *args & **kwargs para llamar una función:


def COOR(x, y, z):
  '''
  Recibe coordenadas en R3
  '''
  print("Coordenada x:", x)
  print("Coordenada y:", y)
  print("Coordenada z:", z)
      
# Ahora usaremos *args or **kwargs para
# pasar argumentos a COOR(x,y,z): 
coordenada = ("Cos(alpha)", "Cos(Beta)", "Cos(theta)")

COOR(*coordenada)

vector = {"x" : "1", "y" : "2", "z" : "3"}
print('Vector de Coordenadas: ')
COOR(**vector)