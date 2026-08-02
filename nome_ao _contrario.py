print("Transforme seu nome ao contrário!")
nome = input("Escreva seu nome: ")
nome_reverso = nome[::-1]
print(f"Seu nome ao contrário é: {nome_reverso}")

for r in nome_reverso:
    print(r)

nome = input("Escreva seu nome: ")
lista_nome = list(nome)
lista_nome.reverse()
nome_invertido = "".join(lista_nome)
print(nome_invertido)