import json
def carregar_dados():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as f: 
            return json.load(f)

    except FileNotFoundError:
        return {"usuarios": []}

def salvar_dados(dados):
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def cadastrar_usuario(nome, idade):
    dados = carregar_dados()
    novo_id = len(dados["usuarios"]) + 1

    dados["usuarios"].append({
        "id": novo_id,
        "nome": nome,
        "idade": idade
    })

    salvar_dados(dados)
    print(f"Usuario {nome}, cadastrado com o id {novo_id}")
    
     
def listar():
    dados = carregar_dados()
    for u in dados["usuarios"]:
        print(f"ID: {u['id']} | Nome: {u['nome']} | Idade: {u['idade']}")


def editar(id_alvo, novo_nome, nova_idade):
    dados = carregar_dados()
    for u in dados["usuarios"]:
        if u["id"] == id_alvo:
            u["nome"] = novo_nome
            u["idade"] = nova_idade
            salvar_dados(dados)
            print("Usuario atualizado com sucesso!")
            return
    print("Usuario não encontrado!.")

def deletar(id_alvo):
    dados = carregar_dados()
    for u in dados["usuarios"]:
        if u["id"] == id_alvo:
            dados["usuarios"].remove(u)
            salvar_dados(dados)
            print("Usuarios deletado!")
            return
        
    print("Usuario não encontrado")

while True:
    print("1- Cadastrar")
    print("2- Listar")
    print("3- Editar")
    print("4- Deletar")
    print("5- Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cadastrar_usuario(nome, idade)

    elif op == "2":
        listar()

    elif op == "3":
        listar()
        try:
            id_alvo = int(input("Digite o ID que gostaria de editar: "))
            novo_nome = input("Novo nome: ")
            nova_idade = int(input("Nova idade: "))
            editar(id_alvo, novo_nome, nova_idade)

        except ValueError:
            print("Dados invalidos!")

    elif op == "4":
        listar()
        try:
            id_alvo = int(input("Digite o ID que gostaria de deletar: "))
            deletar(id_alvo)

        except ValueError:
            print("ID invalido!")

    else:
        break
