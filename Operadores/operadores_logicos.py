# OPERADORES LÓGICOS E & OU (AND & OR)

# AND = no operador E, para o resultador ser true, todos o operadores precisam ser verdadeiros.
#print(True and True) # TRUE
#print(True and False) # FALSE 
#print(False and False) # FALSE

# OR = no operador OU, para o resultado ser true, basta apenas um operador ser verdadeiro.
#print(True or True) # TRUE
#print(True or False) # TRUE
#print(False or False) # FALSE


# PARÊNTESES
saldo = 1000
saque = 250
limite = 200
conta_especial = True

teste = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(teste) # TRUE

teste2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) 
print(teste2) # TRUE

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

teste3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(teste3) # TRUE


