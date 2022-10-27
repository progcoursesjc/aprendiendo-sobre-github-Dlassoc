import collections
from gc import collect
from multiprocessing.resource_sharer import stop
def canciones_letra_dif():
    x = open("canciones.txt")
    hola = x.read().split("==")
    #CANCION 1
    cancion1= hola[0].split()
    palabras_diff = []
    for i in cancion1:
        for j in cancion1:
            if i != j and  i not in palabras_diff:
                palabras_diff.append(i)
    print(f"la cantidad de palabras diferentes de la cancion 1 es {len(palabras_diff)}")

    #CANCION 2
    cancion2= hola[1].split()
    palabras_diff_2 = []
    for i in cancion2:
        for j in cancion2:
            if i != j and  i not in palabras_diff_2:
                palabras_diff_2.append(i)

    print(f"la cantidad de palabras diferentes de la cancion 2 es {len(palabras_diff_2)}")

    #CANCION 3
    cancion3= hola[2].split()
    palabras_diff_3 = []
    for i in cancion3:
        for j in cancion3:
            if i != j and  i not in palabras_diff_3:
                palabras_diff_3.append(i)

    print(f"la cantidad de palabras diferentes de la cancion 3 es {len(palabras_diff_3)}")

def todas_las_canciones_letras_dif():
    x = open("canciones.txt")
    hola = x.read().split()
    palabras_diff = []
    for i in hola:
        for j in hola:
            if i != j and  i not in palabras_diff:
                palabras_diff.append(i)
    print(f"las palabras diferentes son {len(palabras_diff)}")


def palabras_mas_repetidas():
    x = open("canciones.txt")
    hola = x.read().split()
    hola2 = collections.Counter(hola)
    print("\nLas palabras que mas se repiten son:")
    for i, j in hola2.most_common(5):
        print(f"{i} se repite {j}")
    print("***"*4)


def palabras_dif_lista():
    canciones = open("canciones.txt", encoding="utf8")
    stopwords = open("stopwords.txt", encoding="utf8")
    cancion_split = canciones.read().split()
    stopwords_split = stopwords.read().split("\n")
    iguales =[]
    for i in cancion_split:
        for j in stopwords_split:
            if i == j and  i not in iguales:
                iguales.append(i)
                for p in cancion_split:
                    for w in iguales:
                        if p == w:
                            cancion_split.remove(i)
    print(f"se eliminaron {len(iguales)} palabras de stopwords\n")
    print(f"Ahora la lista tiene {len(cancion_split)} palabras\n")
    hola2 = collections.Counter(cancion_split)
    for i, j in hola2.most_common(5):
        print(f"{i} se repite {j} {'veces' if j>1 else 'vez'}.")

                                

                


canciones_letra_dif()
todas_las_canciones_letras_dif()
palabras_mas_repetidas()
palabras_dif_lista()

