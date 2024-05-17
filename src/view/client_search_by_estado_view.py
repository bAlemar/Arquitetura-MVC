from typing import Dict,List
import os

class ClientSearchView:
    def client_search_by_estado_view(self):
        self.__clear()
        message = f"""
        Procure o Cliente por Estado
        """
        print(message)
        estado = input('Insira Estado: ')
        return estado
    
    def client_search_success(self,clients_by_estado:List):
        self.__clear()
        for client in clients_by_estado:
            message = f"""
            Cliente: {client["nome"]}
            Telefone: {client["telefone"]}
            Estado: {client["estado"]}
            """
            print(message)
        return
    

    def client_search_error(self,error):
        self.__clear()

        message = f"""    
        Não foi possível achar esse cliente
        {error}
        """
        
        print(message)
        return
    
    def __clear(self):
        os.system('cls||clear')