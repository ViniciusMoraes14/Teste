print('~'*50)
print("PARA ENCERRAR O PROGRAMA DIGITE UMA LETRA!")
print('~'*50)
while True:
    try:
        entrada = int(input("Digite o número que deseja verificar:"))

        #Nomeando os termos
        t1, t2 = 0, 1

        #Sequencia
        while t1 < entrada:
            t1, t2 = t2, t1 + t2

        #Verificação e impressão!
        if (t1 == entrada) == True:
            print("ESSE TEM!")
        else:
            print("ESSE NÃO TEM!")
    except:
        break
    
