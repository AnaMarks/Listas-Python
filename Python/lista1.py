# 1-
a = int(input('N2: '))
b = int(input('N1: '))
print(b + a)

# 2-
metro = int(input('Metros: '))
print(f'milimetros {metro * 1000}')

# 3-
D = int(input('Dias: '))
H = int(input('Horas: '))
M = int(input('Minutos: '))
S = int(input('Segundos: '))
total = D * 24 * 60 * 60 + H * 60 * 60 + M * 60 + S
print(total)

# 4-
S = float(input('Salario: '))
A = float(input('Aumento%: '))
Aumento = S * A / 100
Novo = S + Aumento
print(f'Aumento: R$: {Aumento:.2f}')
print(f'Salario: R$: {Novo:.2f}')

# 5-
Preco = float(input('Quanto custa esse produto? R$'))
Desconto = (Preco * 10 / 100)
Novo_Preco = Preco - (Preco * 10 / 100)
print(f'O Produto que custa R${Preco} com desconto vai ficar R${Novo_Preco:.2f}')

# 6-
D = float(input('Quantos km é até o local do destino? '))
V = float(input('Qual a velocidade média do carro? '))
Tempo = D / V
print(f'O tempo de viagem até o seu destino é de {Tempo} horas')

# 7-
c = float(input('Por favor, informe a temperatura em C: '))
f = (9 * c / 5) + 32
print(f'A Temperatura é de {c:.2f}°C que corresponde a {f:.2f}°F')

# 8-
f = float(input('Por favor, informe a temperatura em F: '))
c = (f - 32) * 5 / 9
print(f'A temperatura é {f:.2f}°F que é equivalente a {c:.2f}°C')

# 9-
Dias = int(input('Quantos dias alugado? '))
Km = float(input('Quantos Km foram percorridos? '))
Preco = Dias * 60 + Km * 0.15
print(f'O preço a pagar pelo carro é de R${Preco:.2f}')

# 10-
Cigarros = int(input('Cigarros por dia: '))
Anos = int(input('Anos de Fumo: '))
Quantidade_Cigarros = Anos * 365 * Cigarros
Dias = Quantidade_Cigarros / 144
print(f'Você perdeu {Dias:.2f} Dias por fumar, pare de fumar.')

# 11-
print(str(2 * 10000))
