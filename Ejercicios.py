'''
Ejercicio 1. Crea una función que dada una cadena y una letra cuente cuantas veces
aparece dicha letra
'''
def ej1(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador= contador+1

    print(letra)

ej1("palapa", 'p')


'''
Ejercicio 2. Crea una función que dada una cadena determine si es un palíndromo o
si no lo es (sin usar .reversed())
'''
def ej2(cadena):
    cadenaR = cadena[::-1]

    if cadenaR == cadena:
        return True
    else:
        return False


'''
Ejercicio 3. Crea una función que dada un cadena devuelva una lista con las
siguientes cadenas:
• Una con las 5 primeras letras
• Una con las 5 últimas letras
• Una con las letras impares
• Una con la letras pares
• Una con la cadena alrevés (sin usar .reversed())
'''
def ej3(cadena):
    devolver = list
    cadena2 = ''
    contador = 0

    for i in range(0,4):
        cadena2 += cadena[i]

    devolver.append(cadena2)
    cadena2 = ''
    for letra in cadena[::-1]:
        if (contador < 5):
            cadena2 += letra
            contador = contador+1

    devolver.append(cadena2)
    cadena2 = ''
    for letra in cadena[1:cadena.size:2]:
        cadena2 += letra
    devolver.append(cadena2)
    cadena2 = ''
    for letra in cadena[0:cadena.size:2]:
        cadena2 += letra

    cadena2 = ''
    for letra in cadena[::-1]:
            cadena2 += letra
            contador = contador+1
    devolver.append(cadena2)

'''
Ejercicio 4. Crea una función que dada una cadena determine si es un palíndromo o
si no lo es (sin usar .reversed()) y usando slice notation
'''


'''
Ejercicio 5. Crea una función que dada una cadena de texto encuentra la palabra de
mayor longitud y la longitud de la misma
'''
def ej5(cadena):
    cadena.split(' ')
    contador = 0
    mayor = 0
    palabra = ""

    for palabra in cadena:
        for letra in palabra:
            contador = contador+1
        if contador > mayor:
            contador = mayor
            palabra = palabra
        contador = 0

    print(mayor)
    print(contador)


'''
Ejercicio 6. Crea una función que dada una cadena de texto encuentre la palabra más
larga y la más corta de dicha cadena 
'''
def ej6(cadena):
    cadena.split(' ')
    larga = 0
    aux = 0
    corta = 0
    palaralarg = ""
    palabracort = ""

    for palabra in cadena:
        for letra in palabra:
            larga += larga+1
            corta += corta+1
        if larga < corta:
            palabracort = palabra
        else:
            palabralarg = palabra

'''
Ejercicio 7. Crea una función que cuenta cuantas veces aparece una subcadena en
un texto
'''
def ej7(cadena, subcadena):
    longisub = subcadena.size
    contador = 0
    apariciones = 0

    for i in range (0,cadena.size):
        if cadena[i] == subcadena[0]:
            for j in range(0,longisub):
                if subcadena[j] == cadena[i+j]:
                    contador = contador+1

            if contador == longisub:
                apariciones += apariciones+1

print("Numero de apariciones: {apariciones}")


'''
Ejercicio 8 Crea una función que cuenta cuantas veces aparece una subcadena en un
texto y el índice de inicio y fin de cada una de las instancias de la subcadena dentro
del texto.
'''
def ej8(cadena, subcadena):
    palabras = cadena.split(" ")
    aux = ""
    contador = 0

    for palabra in palabras:
        aux = palabra.replace(subcadena, "^")
        if (palabra[0] == '^' and palabra[palabra.size] == '^'):
            contador = contador+1

    print(contador)


ej8("holaho perro hopeho", "ho")
'''
Ejercicio 9. Crea una función que encuentre todas las palabras de un texto que
empiezan y acaban por una misma subcadena dada
'''


'''
Ejercicio 10. Crea una función que reciba como parámetro un número entero y que
devuelva un cadena que contenga la tabla de múltiplicar de dicho número
'''
def ej10(num):
    tabla = ""
    for i in range (1, 11):
        tabla += num+"*"+i+"="+num*i+"\n"


def Pipo():
    while(True):
        res = int(input("MENÚ PRINCIPAL:"
              "\n\t[1] Aprender las tablas"
              "\n\t[2] Practicar las tablas"
              "\n\t[3] Salir\n > "))

        if res == 1:
            aprenderTablas()
        elif res == 2:
            practicarTablas()
        elif res == 3:
            break
        else:
            print("Elige [1] [2] [3]")

def practicarTablas():
    res = input("Elige las tablas para practicar: ")
    tablas = res.split("-")

    numIntentos = int(input("Elige el número de intentos: "))
    fallos = 0
    aciertos = 0

    for it in range(0, numIntentos):
        tabla = int(random.choice(tablas))
        multiplicador = random.randint(0,10)

        intento = int(input(f"¿{tabla} x {multiplicador}?"))
        solucion = int(tabla * multiplicador)

        if intento != solucion:
            print(f"[ERROR] {tabla} x {multiplicador} es {solucion}, no {intento}\n")
            fallos += 1
        else:
            print("[CORRECTO]\n")
            aciertos += 1


    print(f"Has tenido {aciertos} aciertos y {fallos} fallos. Eso te da una tasa de acierto del {numIntentos * 100 / aciertos}%\n")