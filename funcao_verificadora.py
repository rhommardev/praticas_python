ingreso = int(input("Digite um nro para saber se é impar: "))

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
if verificar_par(ingreso):
    print("O numero digitado é par!")
else:
    print("O numero digitado é impar!")
