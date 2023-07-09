MAIOR_IDADE = 18
IDADE_ESPECIAL = 16 

idade = int(input("Informe sua idade: "))

#Usando apenas if
#if idade >= 18:
#    print("Maior de idade! Você pode tirar CNH.")
#if idade < 18:
#    print("Menor de idade! Ainda não pode tirar CNH.")
#________________________________________________________________

# Usando if else
#if idade >= 18:
#    print("Maior de idade! Você pode tirar CNH.")
#else:
#    print("Menor de idade! Ainda não pode tirar CNH.")
#________________________________________________________________


#Usando if elif else
if idade >= 18:
    print("Maior de idade! Você pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer apenas a aulas teóricas!\nPorém não pode fazer aulas práticas") # simulação(vida real tem isso não rs)
else:
    print("Menor de idade! Ainda não pode tirar CNH.")
#________________________________________________________________
