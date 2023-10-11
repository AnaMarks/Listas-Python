# A. fim_igual
# Dada uma lista de strings, retorna o número de strings
# com tamanho >= 2 onde o primeiro e o último caracteres são iguais
def fim_igual(words):
  return len([w for w in words
         if len(w) >= 2 and w[0] == w[-1]])
  k = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      k = k + 1
  return k

# B. x_antes
# Dada uma lista de strings retorna uma lista onde todos os elementos
# que começam com x ficam sorteados antes 
# Exemplo ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final
def x_antes(words):
  x = []
  outros = []
  for w in words:
    if w.startswith('x'): #w[0] == 'x'
      x.append(w)
    else:
      outros.append(w)
  return sorted(x) + sorted(outros)

# LAB(begin solution)
# Extract the last element from a tuple -- used for custom sorting below.
def last(a):  return a[-1]
# LAB(end solution)

# C. sort_last
# Dada uma lista de tuplas não vazias retorna uma tupla ordenada
# por ordem crescente do último elemento 
# Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retorna
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use key=função que você definiu e que retorna o último elemento
def sort_last(tuples):
  return sorted(tuples, key=last)

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('fim_igual')
  test(fim_igual(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(fim_igual(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(fim_igual(['aaa', 'be', 'abc', 'hello']), 1)

  print ()
  print ('x_antes')
  test(x_antes(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(x_antes(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print ()
  print ('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()

#lista 14

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
  return list(set(nums))

# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto, depois tente sortear
# as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
  return ' '.join([''.join(
            sorted(set(p)))
            for p in frase.split()])

# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2
def derivada(coef):
  return [c*grau for c,grau in enumerate (coef)][1:]

# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
  r = []
  v1 = 0
  for x, y in zip(n1, n2):
    n = (x + y) % 10 + v1
    v1 = (x + y) // 10
    r.append(n)
  if v1 != 0: r.append(v1)
  return r

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
  return sorted(s1) == sorted(s2)

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('remove_iguais')
  test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
  test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
  test(remove_iguais([]), [])

  print ()
  print ('cripto')
  test(cripto('ana e mariana gostam de banana'),
       'an e aimnr agmost de abn')
  test(cripto('Batatinha quando nasce esparrama pelo chão'),
       'Bahint adnoqu acens aemprs elop choã')

  print ()
  print ('derivada de polinômio')
  test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
  test(derivada([4, 16, 1]), [16, 2])

  print ()
  print ('soma em listas invertidas')
  test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
  test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])

  print ()
  print ('anagrama')
  test(anagrama('sim', 'siiimmmmm'), False)
  test(anagrama('iracema', 'america'), True)
  test(anagrama('ator', 'rota'), True)
  test(anagrama('aberto', 'rebato'), True)
  test(anagrama('amor', 'roma'), True)
  test(anagrama('ramo', 'amor'), True)
  test(anagrama('baba', 'aba'), False)
  test(anagrama('casa', 'cassa'), False)
  test(anagrama('palmeiras', 'abacate'), False)


if __name__ == '__main__':
  main()
