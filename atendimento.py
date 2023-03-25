nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
covid = input("Tem suspeita de COVID? ").upper()

if covid == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
    
elif covid == "NAO":
    print("Encaminhe o paciente para sala BRANCA")
    
else:
    print("Responda se há suspeita de COVID com SIM ou NAO")
    
if idade >= 65:
    print("Paciente COM prioridade")
else:
    print("Paciente SEM prioridade")