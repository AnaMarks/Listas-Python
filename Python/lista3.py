# 1-
nota = float(input("Digite uma nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    print("Valor inválido")
    nota = float(input("Digite uma nota entre 0 e 10: "))

# 2-
usuario = input("Usuário: ")
senha = input("Senha: ")
while usuario == senha:
    print("A senha deve ser diferente do usuário")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

# 3-
a = 80000
b = 200000
anos = 1
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print(f"Anos: {anos}")

# 4-
n = int(input("Digite o valor de n: "))
a, b = 1, 1
k = 1
while k <= n - 2:
    a, b = b, a + b
    k = k + 1
print(b)

# 5-
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
while a % b != 0:
    a, b = b, a % b
print(f'MDC = {b}')
