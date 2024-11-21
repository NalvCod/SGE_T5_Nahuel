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
