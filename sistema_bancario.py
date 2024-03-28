menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
'''
saldo = 0
limite = 500
saques = 0
SAQUES_DIARIOS = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = int(input("Digite o valor do deposito: "))
        saldo += valor
    elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            if (valor <= 500) and (saldo > valor):
                saldo-=valor
                saques+=1
                if saques > SAQUES_DIARIOS:
                     print("Limite de saques diarios excedido")
                     break
            else:
                print("Não foi possivel realizar o saque.")
                break  
    elif opcao =="3":
        print(f"Seu saques realizados foram: {saques}, no valor de:R$ {valor}")
        print(f"Seu saldo é de R$: {saldo:.2f}")
    elif opcao == "0":
        break