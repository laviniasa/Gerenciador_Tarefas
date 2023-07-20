import mysql.connector
from datetime import datetime

def adicionar_tarefa():
    tarefa = input("Digite a descrição da tarefa: ")
    data_termino = input("Digite a data da tarefa (formato: YYYY-MM-DD): ")
    status = input("Digite o status da tarefa (Pendente/Em Andamento/Concluída): ")

    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="novo_usuario",
        password="nova_senha",
        database="task_manager"
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Comando SQL para inserir a tarefa na tabela
    query = "INSERT INTO tarefas (descricao, data_termino, status) VALUES (%s, %s, %s)"
    dados = (tarefa, data_termino, status)

    try:
        # Executar o comando SQL
        cursor.execute(query, dados)

        # Confirmar a inserção no banco de dados
        conexao.commit()

        print("Tarefa adicionada com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao adicionar a tarefa: {erro}")

    finally:
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

def listar_tarefas():
    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="novo_usuario",
        password="nova_senha",
        database="task_manager"
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Comando SQL para selecionar todas as tarefas da tabela
    query = "SELECT id, descricao, data_termino, status FROM tarefas"

    try:
        # Executar o comando SQL
        cursor.execute(query)

        # Obter todas as tarefas do banco de dados
        tarefas = cursor.fetchall()

        if not tarefas:
            print("Não há tarefas cadastradas.")
        else:
            print("======= TAREFAS =======")
            for tarefa in tarefas:
                print(f" {tarefa[0]} {tarefa[1]} Data: {tarefa[2]} Status: {tarefa[3]}")

    except mysql.connector.Error as erro:
        print(f"Erro ao listar as tarefas: {erro}")

    finally:
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

# Função para remover uma tarefa pelo ID
def remover_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))

    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="novo_usuario",
        password="nova_senha",
        database="task_manager"
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Comando SQL para deletar a tarefa da tabela
    query = "DELETE FROM tarefas WHERE id = %s"
    dados = (id_tarefa,)

    try:
        # Executar o comando SQL
        cursor.execute(query, dados)

        # Confirmar a remoção no banco de dados
        conexao.commit()

        if cursor.rowcount == 1:
            print("Tarefa removida com sucesso!")
        else:
            print("Nenhuma tarefa encontrada com o ID informado.")

    except mysql.connector.Error as erro:
        print(f"Erro ao remover a tarefa: {erro}")

    finally:
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()
# Função para alterar o status de uma tarefa pelo ID
def alterar_status_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja alterar o status: "))
    novo_status = input("Digite o novo status da tarefa (Pendente/Em Andamento/Concluída): ")

    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="novo_usuario",
        password="nova_senha",
        database="task_manager"
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Comando SQL para atualizar o status da tarefa na tabela
    query = "UPDATE tarefas SET status = %s WHERE id = %s"
    dados = (novo_status, id_tarefa)

    try:
        # Executar o comando SQL
        cursor.execute(query, dados)

        # Confirmar a atualização no banco de dados
        conexao.commit()

        if cursor.rowcount == 1:
            print("Status da tarefa atualizado com sucesso!")
        else:
            print("Nenhuma tarefa encontrada com o ID informado.")

    except mysql.connector.Error as erro:
        print(f"Erro ao alterar o status da tarefa: {erro}")

    finally:
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

# Função para apagar todas as tarefas

def apagar_todas_tarefas():
    
    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="novo_usuario",
        password="nova_senha",
        database="task_manager"
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Comando SQL para deletar todas as tarefas da tabela
    query = "DELETE FROM tarefas"

    try:
        # Executar o comando SQL
        cursor.execute(query)

        # Confirmar a remoção no banco de dados
        conexao.commit()

        print("Todas as tarefas foram apagadas com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao apagar todas as tarefas: {erro}")

    finally:
        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conexao.close()

def menu():
    while True:
        print("\n======= MENU =======")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Listar tarefas")
        print("4 - Alterar status da tarefa")
        print("5 - Apagar todas as tarefas")
        print("0 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            remover_tarefa()
        elif opcao == "3":
            listar_tarefas()
        elif opcao == "4":
            alterar_status_tarefa()
        elif opcao == "5":
            apagar_todas_tarefas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
