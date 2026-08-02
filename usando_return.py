n1 = int(input("Digite o numero 1 para suma: "))
n2 = int(input("Digite o numero 2 para suma: "))

def somar (n1,n2):
    resultado = n1 + n2
    return resultado
somar(n1,n2)

apresenta_resultado = somar(n1,n2)

print(f"O resulta é : {apresenta_resultado}")