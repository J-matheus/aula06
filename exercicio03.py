# aluno = input("informe o nome do aluno: ")
#
# nota01 = 0
# nota02 = 0
# x= 0
# while x <= aluno:
#     num=int(input("informe a nota: "))
#     nota01 = nota01+num
#     x += 1
#     num02=int(input("informe a nota: "))
#     nota02 = nota02+num02
#     x+=1
# media=nota01/2
# media2=nota02/2
# print(media)
# print(media2)

nota = 0
x = 0
alunos = int (input("informe o nome do aluno: "))
while x <= alunos:
    num=int(input("informe a nota: "))
    nota = nota+num
    x += 1
media=nota/alunos
print(media)