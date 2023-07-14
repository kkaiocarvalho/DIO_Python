nome = "Kaio"
idade = 20
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Kaio", "idade": 20}

# OLD STYLE %
print("Nome: %s \nIdade: %d" % (nome, idade))

print()
# MÉTODO FORMAT
print("Nome: {} \nIdade: {}".format(nome, idade))

print()
# MÉTODO FORMAT
print("Nome: {1} \nIdade: {0}".format(idade, nome))

print()
# MÉTODO FORMAT
print("Nome: {nome} \nIdade: {idade}".format(nome = nome, idade = idade))
print("Nome: {name} \nIdade: {age}".format(name = nome, age = idade))

print()
# MÉTODO FORMAT
print("Nome: {nome} \nIdade: {idade}".format(**dados))

print()
# MÉTODO f-strings
print(f"Nome: {nome} \nIdade: {idade} \nLinguagem: {linguagem}")

# Formatando strings com f-strings
PI = 3.14159
print(f"Valor de PI: {PI:.2f}\n")
print(f"PI: {PI:10.2f}\n")
print(f"PI: {PI:5.2f}")