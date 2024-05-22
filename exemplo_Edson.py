import os
os.system("cls")

l =["Edson", 12, 1.67, True, 34]
print(f"Exibe a posição 1 da lista: L[1] = {l[1]}")
print(f"Exibe a lista inteira: L = {l}")

l[4] = "Edson"
print(f"L = {l}")

print("------------------------------------------")
print("append")

lista = list()
lista.append(12)
lista.append("Lógica")
print(lista)

print("------------------------------------------")

lista = [22,"lógica"]
print(lista)

lista.insert(1, 57.7)
print(lista)

print("------------------------------------------")

lista = [22, 57.7, "Lógica"]
lista.pop(0)
print(lista)
lista.pop()
print(lista)

print("------------------------------------------")

lista = [22, 57.7, "lógica"]
lista.remove(57.7)
print(lista)

print("------------------------------------------")

print("index")
lista = [22, 57.7, "logica"]
indice = lista.index("logica")
print(f"Índice = {indice}")

print("------------------------------------------")

print("cont")
lista = [22,22,57.7,"logica"]
qtd = lista.count(90)
print(f"Quantidade = {qtd}")

print("------------------------------------------")

print("len")
lista =[22,22,57.7,"logica"]
qtd_elementos = len(lista)
print(f"Quantidade = {qtd_elementos}")

print("------------------------------------------")

print("sum")
lista = [19,4,25,33,-5]
print(sum(lista))

print("------------------------------------------")

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"lista3 = {lista3}")

print("------------------------------------------")

lista1 = [1,2,3]
print(f"Lista1 = {lista1}")
lista2 = [4,5,6]
print(f"Lista2 = {lista2}")
lista2.extend(lista1)
print(f"Lista2 = {lista2}")

print("------------------------------------------")

lista1 = [1,2,3]
lista2 = lista1.copy()
print(f"lista1 = {lista1}")
print(f"Lista2 = {lista2}")

print("------------------------------------------")

lista = [19,4,25,33,-5]
lista.sort()
print(lista)
lista.sort(reverse = True)
print(lista)

print("------------------------------------------")

lista = [19,4,25,33,-5]
lista.reverse()
print(lista)

print("------------------------------------------")

lista = [19,4,25,33,-5]
lista.clear
print(lista)

print("------------------------------------------")

lista = [19,4,25,33,-5]
del(lista)