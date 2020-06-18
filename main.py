from merge_sort import *
from quick_sort import *
import random
import time


lista = random.sample(range(18, 50), 10)
lista2 = lista[:]

print("***********")

print("Caso de teste idade: ")
print(lista)

print("***********")

antes = time.time()
print("Ordenado em decrescente (Quick_Sort):")
quicksort(lista)
depois = time.time()
print("Quick Sort demorou ",  depois-antes)
print(lista)

print("***********")

antes1 = time.time()
print("Ordenado em decrescente (Merge_Sort):")
merge_sort(lista2)
depois1 = time.time()
print("Marge Sort demorou ",depois1-antes1)
print(merge_sort(lista2))

print("***********")
