print("O TIRANO SMOUG, SER DAS TREVAS E DA GANÂNCIA ESTÁ EM SUA FRENTE, você deverá lançar um feitiço que Gandalf lhe ensinou, o feitiço das ILUSÕES para então acalma-lo, Boa sorte Bilbo...")
rage = 100

while rage >= 5:
    
    numero = int(input("Lance um feitiço inteiro: ")) #feitiço = número inteiro
    
    
    if numero % 2 == 0: 
        print("A magia não funcionou corretamente, Smoug aumenta sua raiva em 20!!")
        rage += 10 
    else:
        print("VOCÊ CONSEGUIU, a magia de gandalf é mais eficaz do que parece, continue até Smoug permaneça quieto em sua tumba de ouro!")
        rage -= 20 
        
    
    print("Ira de Smoug: {}".format(rage))


print("Smoug enfim descansa, e sua jornada pode então continuar")