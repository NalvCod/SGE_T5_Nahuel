'''
Ejercicio 1. Crea una función que dada una cadena y una letra cuente cuantas veces
aparece dicha letra
'''
def ej1(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador= contador+1
    print(contador)
print("EJERCICIO 1")
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

print("EJERCICIO 2")
print(ej2("ana"))
print(ej2("pipo"))


'''
Ejercicio 3. Crea una función que dada un cadena devuelva una lista con las
siguientes cadenas:
• Una con las 5 primeras letras
• Una con las 5 últimas letras
• Una con las letras impares
• Una con la letras pares
• Una con la cadena alrevés (sin usar .reversed())
'''
def ej3(cadena) -> list:
    devolver = []
    cadena2 = ''
    contador = 0

    for i in range(0,5):
        cadena2 += cadena[i]

    devolver.append(cadena2)
    cadena2 = ''

    for letra in cadena[::-1]:
        if (contador < 5):
            cadena2 += letra
            contador = contador+1

    devolver.append(cadena2)
    cadena2 = ''

    for letra in cadena[1::2]:
        cadena2 += letra
    devolver.append(cadena2)
    cadena2 = ''

    for letra in cadena[::2]:
        cadena2 += letra
    devolver.append(cadena2)
    cadena2 = ''

    for letra in cadena[::-1]:
        cadena2 += letra
        contador = contador+1
    devolver.append(cadena2)

    return devolver

print(ej3("manatí"))

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
    palabras = cadena.split(' ')

    palabracorta = palabras[0]
    palabralarga = palabras[0]

    for palabra in palabras:
        if len(palabra) < len(palabracorta):
            palabracorta = palabra
        if len(palabra) > len(palabralarga):
            palabralarga = palabra

    return palabracorta, palabralarga

cadena = "Estoy bastante desquiciado"
corta, larga = ej6(cadena)
print(f"La palabra más corta es: {corta}")
print(f"La palabra más larga es: {larga}")

'''
Ejercicio 7. Crea una función que cuenta cuantas veces aparece una subcadena en
un texto
'''
def ej7(cadena, subcadena):
    longisub = len(subcadena)
    apariciones = 0

    for i in range(len(cadena) - longisub + 1):
        contador = 0
        for j in range(longisub):
            if subcadena[j] == cadena[i + j]:
                contador += 1
        if contador == longisub:
            apariciones += 1

    return apariciones  # Devolvemos el número de apariciones

cadena = "espa parapa tapa"
subcadena = "pa"
resultado = ej7(cadena, subcadena)
print(f"Numero de apariciones: {resultado}")


'''
Ejercicio 8 Crea una función que cuenta cuantas veces aparece una subcadena en un
texto y el índice de inicio y fin de cada una de las instancias de la subcadena dentro
del texto.
'''
def ej8(cadena, subcadena):
    palabras = cadena.split(" ")
    contador = 0
    indices = []

    for palabra in palabras:
        inicio = 0
        while inicio < len(palabra):
            inicio = palabra.find(subcadena, inicio)
            if inicio == -1:
                break
            final = inicio + len(subcadena) - 1
            indices.append((inicio, final))
            contador += 1
            inicio += 1

    print(f"Numero de apariciones: {contador}")
    for inicio, final in indices:
        print(f"Subcadena encontrada desde el índice {inicio} hasta el índice {final}")

# Ejemplo de uso
ej8("holaho perro hopeho", "ho")

'''
Ejercicio 9. Crea una función que encuentre todas las palabras de un texto que
empiezan y acaban por una misma subcadena dada
'''


def ej9(cadena, subcadena):
    palabras = cadena.split()
    palabras_encontradas = []

    for palabra in palabras:
        if palabra.startswith(subcadena) and palabra.endswith(subcadena):
            palabras_encontradas.append(palabra)

    print(f"Palabras que empiezan y terminan con '{subcadena}':")
    for palabra in palabras_encontradas:
        print(palabra)


ej9("hola hola123 hoho mundo hohoho", "ho")

'''
Ejercicio 10. Crea una función que reciba como parámetro un número entero y que
devuelva un cadena que contenga la tabla de múltiplicar de dicho número
'''
def ej10(num):
    tabla = ""
    for i in range (1, 11):
        tabla += num+"*"+i+"="+num*i+"\n"

def aprenderTablas():
    res = int(input("Que tablas quieres aprender?\n > "))

    for it in range(1,11):
        print(f"{res} x {it} = {(res * it)}")

    print("\n")

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


def pipo():
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


def ahorcado():
    print("EL AHORCADO")
    vidas = 3
    solucion = ""

    dificultad = int(input("Introduce la dificultad:\n\t[1] Normal\n\t[2] Intermedio\n\t[3] Cerebro Galaxia\n > "))

    if dificultad == 1:
        solucion = "pato"
    elif dificultad == 2:
        solucion = "patato"
    elif dificultad == 3:
        solucion = "palpitacion"

    letrasAcertadas = []
    for letra in solucion:
        letrasAcertadas.append(False)


    while vidas > 0:
        mostrar_palabra = ""
        for i in range(len(solucion)):
            if letrasAcertadas[i]:
                mostrar_palabra += solucion[i] + " "
            else:
                mostrar_palabra += "_ "

        print(f"\n{mostrar_palabra.strip()}")

        res = input("\nElige una letra: ").lower()

        if len(res) != 1 or not res.isalpha():
            print("Elige un valor valido")
            continue

        # Verificar si la letra está en la palabra
        letra_incluida = False
        for i in range(len(solucion)):
            if solucion[i] == res:
                letrasAcertadas[i] = True
                letra_incluida = True

        if letra_incluida:
            print("[CORRECTO]")
        else:
            vidas -= 1
            print(f"[INCORRECTO] Tienes [{vidas}] oportunidades más")

        if all(letrasAcertadas):
            print("\nHAS GANADO")
            break

    if vidas == 0:
        print(f"\nHAS PERDIDO. La palabra era: {solucion}")




pipo()
ahorcado()