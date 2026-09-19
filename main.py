import json

#tela inicial
print(" seja bem vindo ao Sady task tracker")
print("qual opcao voce deseja acessar?")
print("1 - nova tarefa")
print("2 - excluir tarefas")
print("3 - ver todas tarefas")
input("qual opcao voce deseja?")

def database():
  with open("tasks.json", "r", encoding="utf-8") as arquivo:
    banco = json.load(arquivo)

print(banco)
