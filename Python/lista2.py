#1-
a = int(input('lado a:' ))
b = int(input('lado b:' ))
c = int(input('lado c:' ))

if a > b + c or b > a + c or c > a + b:
    print ('nao pode ser um triângulo')
elif a == b ==c:
    print ('Equilátero')
elif a == b or b == c or a == c:
    print ('Isósceles')
else:
    print ('Escaleno')

#2-
 
#3-
peso = float(input('peso:'))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = excesso = 0
print (f'Multa: R$ {multa:.2f}')
print (f'Excesso: {excesso:.2f}')

#4-
a = int(input('N 1:'))
b = int(input('N 2:'))
c = int(input('N 3:'))

if a>=b and a>=c:
    print (f'maior: {a}')
elif b>= c:
    print (f'maior: {b}')
else:
    print (f'maior: {c}')

#5-
a = int(input('N 1:'))
b = int(input('N 2:'))
c = int(input('N 3:'))

if a>=b and a>=c:
    print (f'maior: {a}')
elif b>= c:
    print (f'maior: {b}')
else:
    print (f'maior: {c}')

if a <=b and a<=c:
    print (f'menor: {a}')
elif b<=c:
    print (f'menor: {b}')
else:
    print (f'menor: [c]')

#6-
valor = int(input('valor por horas:'))
horas = int(input('horas trabalhadas no mês:'))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
sl = bruto - ir - inss - sindicato
print (f'salário bruto: R${bruto:.2f}')
print (f'ir: R${ir:.2f}')
print (f'inss: R${inss:.2f}')
print (f'sindicato: R${sindicato:.2f}')
print (f'salário liquido: R${sl:.2f}')

#7- 
metros = int(input('metros quadrados:'))
if metros % 54 == 0:
    latas = metros / 54
else:
    latas= int(metros/54)+1
valor = latas * 80
print (f'{latas} latas')
print (f'total: {valor:.2f}')

