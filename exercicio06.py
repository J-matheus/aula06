nota1 = float(input("informe a primeira nota: "))
while nota1 <0 or nota1 >10:
    nota1 = float(input("você digitou um valor invalido, informe a primeira nota novamente: "))
nota2 = float(input("informe a segundo nota:"))
while nota2 <0 or nota2 >10:
    nota2 = float(input("você digitou um valor invalido, informe a segunda nota novamente: "))
media = nota1+nota2%2
print(media)



# #pin = "123456"
# erro = 1
# while erro<=3:
#     senha = int(input("informe a senha do usuario: "))
#     if senha==pin:
#         print("login feito com sucesso.")
#         break
#     erro+=1
# print("seu login foi bloqueado, tente novamente em alguns minutos.")