import os
from typing import Dict

class Client_Register_View:
    def register_client_view(self) -> str:
        self.__clear()
        
        print("Registre o Cliente")
        nome = input('Digite o nome do Cliente: ')
        telefone = input('Digite o telefone do Cliente: ')
        estado = input('Digite o Estado do Cliente: ')

        new_client_informations = {
            "nome":nome , "telefone":telefone , "estado":estado
        }

        return new_client_informations
    
    def register_client_sucess(self, client_registry: Dict) -> None:
        self.__clear()
        message = f"""
        Cliente {client_registry["nome"]}
        que mora no Estado {client_registry["estado"]}
        e possui o telefone {client_registry["telefone"]}

        Registrado com Sucesso!!    
        """
        print(message)
        return
    
    def register_client_error(self,error:str) -> None:
        self.__clear()

        message = f"""
        
        Não foi possível cadastrar esse cliente.
        Devido seguinte error:
        {error}

        """
        print(message)


    def __clear(self):
        os.system('cls||clear')