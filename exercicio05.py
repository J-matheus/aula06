pin = "123456"
erro = 1
while erro<=3:
    senha = int(input("informe a senha do usuario: "))
    if senha==pin:
        print("login feito com sucesso.")
        break
    erro+=1
print("seu login foi bloqueado, tente novamente em alguns minutos.")