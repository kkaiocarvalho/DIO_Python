#while True:
#    opcao = int(input("Informe um número: "))

#    if opcao == 10:
#       break

#    print(opcao)
# o código acima só irá para de pedir um número quando a condição (if opcao) for igual a 10
# o break ele corta a execução

#while True:
#    opcao = int(input("Informe um número: "))

#    if opcao == 10:
#        continue  # diferente do código de cima esse continua se o valor for 10

#    print(opcao)

# o continue pula execução
for numero in range(100):

    if numero % 2 == 0:
        continue
    print(numero, end=" \n")
    # o código acima ira retornar o valores impares até 100(continua do 0 de 2 em 2)


while True:
    num = int(input("Informe um número: "))

    if num == 10:
        break   # se esse if viesse depois do (if continue) o código nunca pararia!
                #pois o continue iria continuar rodando msm q o valor fosse 10.
    if num % 2 == 0:
        continue

    print(num)