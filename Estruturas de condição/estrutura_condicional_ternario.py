saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

saldo2 = 2000
saque2 = 2500

status2 = "Sucesso" if saldo2 >= saque2 else "Falha"

print(f"Status2: {status2} ao realizar o saque!")