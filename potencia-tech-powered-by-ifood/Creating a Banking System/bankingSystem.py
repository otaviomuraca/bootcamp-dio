# Potência Tech powered by iFood | Ciência de Dados
# Projeto Criando um Sistema Bancário com Python
# Por Otávio Muraca


menu = ''' \n
============= SISTEMA BANCÁRIO =============

            Para SAQUE digite <S>
          Para DESPÓSITO digite <D>
           Para EXTRATO digite <E>
            Para SAIR digite <Q>

============================================
\n
'''

 # Variáveis
saldo = 0
saque = 0
saque_qnt = 3
count = 0
extrato_historico = []
extrato_historico.append("Operação, Valor \n")
logado = True


# MENU
while logado == True:

    while count == 0:
        menu_press = input(f"{menu} Escolha a função: ").upper()
        count = 1

    while count == 1:
        
        if menu_press == "S": #Saque
            count = 2

        elif menu_press == "D": #Depósito
            count = 3

        elif menu_press == "E": #Extrato
            count = 4

        elif menu_press == "Q": #Sair
            count = 5
        
        else: 
            count = 0


    while count == 2: #Saque
        print(f"O seu saldo é de R$ {saldo:.2f}.")

        if saldo == 0:  
            print("Saldo insuficiente para saque.")
            count = 0 
            break
    
        try:
            saque = float(input("Quantia para saque: R$ "))
        except ValueError:
            print("Valor inválido. Digite um número válido para o saque.")
            continue  


        try:
            if saque <= 500:
                
                if (saque_qnt >=1) and (saque_qnt <=3):

                    try:
                        
                        if (saldo < saque):
                            print("Saldo insuficiente.")

                        elif (saldo >= saque):
                            saldo = saldo - saque
                            saque_qnt -= 1
                            print(f"Você realizou um saque de R${saque:.2f}")
                            print(f"O seu saldo é de R${saldo:.2f}.")
                            extrato_historico.append(f"Saque, {saque:.2f}\n")
                            print(f"Você ainda possui {saque_qnt} saques diários.")


                    except ValueError:
                        print("Valor inválido. Digite um número válido para o saque.")
                        continue


                else:
                    print("Você já realizou 3 saques hoje.") 
                    print("Volte amanhã para realizar novos saques.\n")
                      

            else:
                print(f"""
                    O valor de R${saque:.2f} excede o seu limite de saque
                    Seu limite para saque é de R$500.00.\n""")
                

                
        except ValueError:
            print("Valor inválido. Digite um número válido para o saque.")
            continue  

        count = 0

    while count == 3: #Depósito
        try:
            deposito = float(input(f"Insira a quantia que deseja depositar: R$"))
            saldo = saldo + deposito
            extrato_historico.append(f"Depósito, {deposito:.2f}\n")
            print(f"Seu novo saldo é de R$ {saldo:.2f}.")
            
        except ValueError:
                print("Valor inválido. Digite um número válido para o saque.")
                continue
        count = 0            

    while count == 4: #Extrato
        print("\n============= EXTRATO BANCÁRIO =============")
        for i in extrato_historico:
            print(i)
        print(f"Seu saldo é de R$ {saldo:.2f}.")
        print("\n============================================\n")
        count = 0

    while count == 5: #Sair
        print("\n=======================================")
        print("Você deslogou do sistema. Volte Sempre!")
        print("=======================================\n")
        logado = False
        break

# Fim
