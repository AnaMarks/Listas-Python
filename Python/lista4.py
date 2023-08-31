# 1-
import random

a = random.sample(range(1, 100), 10)
maior = menor = a[0]

for x in a[1:]:
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(a)
print(f'menor valor: {menor}')
print(f'maior valor: {maior}')

# 2-
import random

lista = []
lista = random.sample(range(100), 20)
impar, par = [], []

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print('lista', lista)
print('pares', par)
print('impar', impar)

# 3-
import random

lista1, lista2, lista3 = [], [], []
lista1, lista2 = random.sample(range(100), 10), random.sample(range(100), 10)

for n in range(10):
    lista3.append(lista1[n])
    lista3.append(lista2[n])

print('lista 1', lista1)
print('lista 2', lista2)
print('lista mesclada', lista3)

# 4-
texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto = texto.lower()
texto = texto.split()
lista = []

for n in texto:
    n = n.rstrip(',.:')
    if n.startswith(tuple('python')) or n.endswith(tuple('python')):
        lista.append(n)

print(lista)

# 5-
texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
texto = texto.lower()
texto = texto.lstrip(',.')
texto = texto.split()
python = list('python')
x = 0

for n in texto:
    if len(n) > 4 and n != n.strip('python'):
        x = x + 1

print(x)
