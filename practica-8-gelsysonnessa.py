# PRÁCTICA #8 - FÁBRICA DE AUTOPARTES - GELSY SONNESSA:

resultados = []

# Validación de datos ingresados por el usuario:
while True:
    dato = input("\nIngresa el valor de resistencia de cada pieza (en kg): ")
    if dato.replace('.', '').isdigit() == True: # Esta funcion verifica si se ingresó un número decimal
        if float(dato) <= 0:
            print("Por favor, ingresa un dato numérico mayor a cero")
        else:
            resultados.append(float(dato))
            print("Si no desea agregar otro valor de resistencia escriba 'no'")
    elif dato.isdigit() == False and dato != 'no':
        print("Por favor, ingresa un dato numérico válido")
    elif dato.lower() == "no":
        break 
    else:
        print("Por favor, ingresa un dato numérico válido")

# Función para ordenar los valores de resistencias de forma ascendente o descendente:
def ordenar_seleccion(vector, ascendente=True): # El parámetro ascendente=True permite utilizar la función de forma descendente en caso de ser False
  n = len(vector)
  for i in range(n-1):
    # Busca el mínimo o el máximo según el orden deseado
    indice = i
    for j in range(i+1, n):
      if ascendente and vector[j] < vector[indice]:
        indice = j
      elif not ascendente and vector[j] > vector[indice]:
        indice = j
    # Aquí se intercambia el elemento en la posición i con el mínimo o el máximo encontrado
    vector[i], vector[indice] = vector[indice], vector[i]
       
# Acción deseada para el ordenamiento del vector 
while True: 
    accion = input("\nIngrese la forma de ordenamiento que desea: 'a' (ascendente) o 'd' (descendente): ")
    if accion.lower() == 'a':
        ordenar_seleccion(resultados)
    elif accion.lower() == 'd':
        ordenar_seleccion(resultados, ascendente=False)
    if accion.lower() == 'a' or 'd':
        break
    else:
        print("Por favor, ingresa el caracter correcto: 'a' o 'd'")
print("\n✓ Las resitencias de la piezas suministradas son las siguientes:",resultados,"Kg")
   
# Determinación de la pieza con menor resistencia
# Se hace uso del vector ordenado según sea el caso para determinar la pieza con menor resistencia.
if accion.lower() == 'a':
    pieza_defectuosa = resultados[0]
    print("La pieza con menor resistencia es la que tiene",pieza_defectuosa,"Kg de fuerza")
elif accion.lower() == 'd':
    pieza_defectuosa = resultados[-1]
    print("✓ La pieza con menor resistencia es la que tiene",pieza_defectuosa,"Kg de fuerza")

# Piezas que soportaron una carga mayor a 300Kg
cantidad = 0
for pieza in resultados:
  if pieza > 300:
    cantidad += 1
print("✓",cantidad,"piezas son aptas para utilizarse en el modelo de automóvil requerido")

# Función para calcular la media del vector ingresado:
def media(vector):
  n = len(vector)
  suma = 0
  for valor in vector:
    suma += valor
  return suma / n
media_r = media(resultados)
print("✓ La media de la resistencia de las piezas es:",media_r,"Kg")
    
# Función para calcular la mediana de un vector ya ordenado:
def mediana(vector):
  n = len(vector)
  # Si el número de elementos de la lista es PAR, la mediana es el promedio de los dos elementos centrales
  if n % 2 == 0: # este condicional verifica si la cantidad de elementos es par
    i = n // 2
    return (vector[i-1] + vector[i]) / 2
  # Si el número de elementos de la lista es IMPAR, la mediana es el elemento central
  else:
    i = n // 2
    return vector[i]
mediana_r = mediana(resultados)
print("✓ La mediana de la resistencia de las piezas es:",mediana_r,"Kg")

def moda(vector):
  # Se crea un diccionario que almacene la frecuencia de cada elemento.
  # Este dicc. almacena la 'clave' - valor de los elementos, para así determinar cuál se repite más
  frecuencias = {}
  for e in vector:
    if e in frecuencias:
      frecuencias[e] += 1
    else:
      frecuencias[e] = 1
  # Se busca el elemento con mayor frecuencia
  max_fr = 0
  moda = None
  for elemento, frecuencia in frecuencias.items():
    if frecuencia > max_fr:
      max_fr = frecuencia
      moda = elemento
  return moda
moda_r = moda(resultados)
print("✓ La moda de la resistencia de las piezas es:",moda_r,"Kg")
