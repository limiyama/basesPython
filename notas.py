def lernotas():
    nota = float(input('Digite uma nota: '))
    return nota

def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print ("Média: ", media, "Resultado: ", end = "")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resultado(a,b)