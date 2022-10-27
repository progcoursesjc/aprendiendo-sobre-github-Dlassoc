x = open("canciones.txt", encoding="utf8")
hola = x.read().split()
palabras_diff = []
for i in hola:
    for j in hola:
        if i != j and  i not in palabras_diff:
            palabras_diff.append(i)
print(f"las palabras diferentes son {len(palabras_diff)}")
