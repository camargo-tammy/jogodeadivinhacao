import random
import time

print("////////////////////////////")
print("////   Boas vindas ao   ////")
print("// Jogo de adivinhação🎉  //")
print("////     Tammys💙       ////")
print("////////////////////////////")

numeroSecreto = random.randrange(1, 101)  
totaldeTentativas = 0
pontos = 100

print("Qual é o nível de dificuldade?")
print("(1)- Fácil (2)- Médio (3)- Difícil ")

nivel = int(input("Escolha um nível "))
if nivel == 1:
    print("20 tentativas, ih muito frango🐔")
    totaldeTentativas = 20
elif nivel == 2:
    print("10 tentativas, ta evoluindo já ta virando galo 😉🐓")
    totaldeTentativas = 10
elif nivel == 3:
    print("5 tentativas, corajoso, rei do galinheiro! ✅💯💥")
    totaldeTentativas = 5

print("\nPreparando o jogo", end="")
for _ in range(3):
    time.sleep(0.5)
    print(".", end="")
print()

for rodada in range(1, totaldeTentativas + 1):
    print("Tentativa {} de {}".format(rodada, totaldeTentativas))
    chute_str = input("Digite um número entre 1 a 100: ")
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Número inválido. O número deve ser entre 1 e 100.")
        continue  

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if acertou:
        print(f"Você acertou e fez {pontos}!")
        break  
    else:
        if maior:
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! Seu chute foi menor que o número secreto.")
    
    pontosPerdidos = abs(numeroSecreto - chute)
    pontos -= pontosPerdidos  
    
print("Fim de jogo! O número era", numeroSecreto)