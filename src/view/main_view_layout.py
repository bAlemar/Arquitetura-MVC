def introduction_page():
    message = """
    Sistema do Padeiro
    Selecione o campo que deseja acessar:
    
    * Cadastrar Cliente - 1
    * Cadastrar Produto - 2
    * Deletar Produto - 3
    * Ver Produtos Cadastrados - 4
    * Ver Cliente por Estado - 5
    * Sair - 6
    """
    print(message)
    command = input('Comando: ')
    
    return command