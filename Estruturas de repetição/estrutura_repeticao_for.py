texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("Final do laço") # add quebra de linha

# exemplo usando a função built-in range 
for numero in range(0, 102, 10):
    print(f"- {numero}", sep=" ")