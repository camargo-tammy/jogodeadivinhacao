import random
print("////////////////////////////")
print("////   Boas vindas ao   ////")
print("// Jogo de adivinhação🎉  //")
print("////     Tammys💙       ////")
print("////////////////////////////")

numeroSecreto= random.randrange(0,100)
totaldeTentativas = 0
pontos = 100

print("Qual é o nível de dificuldade?")
print("(1)- Fácil (2)- Médio (3)- Difícil ")

nivel= int(input("Escolha um nível "))
if(nivel == 1):
    print("20 tentativas, ih muito frango🐔")
    totaldeTentativas = 20
elif(nivel == 2):
    print("10 tentativas, ta evoluindo já ta virando galo 😉🐓")
    totaldeTentativas = 10
elif(nivel == 3):
    print("5 tentativas, corajoso, rei do galinheiro! ✅💯💥")
    totaldeTentativas = 5