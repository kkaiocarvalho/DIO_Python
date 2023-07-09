# --------- MAIÚSCULA, MINÚSCULA E TÍTULO ---------
nome = "kAiOeLiViA"

print(nome.upper()) # deixa tudo maiusculo
print() #   QUEBRA DE LINHA
print(nome.lower()) # deixa tudo minusculo
print() #   QUEBRA DE LINHA
print(nome.title()) # deixa apenas a primeira letra em maiusculo
print() #   QUEBRA DE LINHA
nome_novo = "  Daiki "

# --------- REMOVENDO ESPAÇOS EM BRANCO ----------
print(nome_novo.strip()) # remove todo espaço em branco
print() #   QUEBRA DE LINHA
print(nome_novo.rstrip()) # remove espaço em branco da direita
print() #   QUEBRA DE LINHA
print(nome_novo.lstrip()) # remove espaço em branco da esquerda

# --------- JUNÇÕES E CENTRALIZAÇÃO ------------ 
texto = 'DragonBallZ'

print(texto.center(15,'-')) # o 1º parametro serve para definir o número de caracteres q a messagem deve apresentar! a string texto já tem 11 e irá add + 4 para dar 15! e ira ser completa pelo 2º paramentro que é '-'.

print(texto.center(15)) #aqui não tem o segundo parametro ett sera preenchida com espaços em branco

print(".".join(texto))# serve para add um caracter em cada caracter da string 