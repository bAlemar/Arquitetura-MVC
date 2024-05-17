from typing import List


class __ClientRepository:
    def __init__(self) -> None:
        self.__client_list = []
    
    def insert_client(self,client:any) -> None:
        self.__client_list.append(client)
    
    def search_client_by_estado(self,estado_searched:str) -> List:
        clients_searched = []
        for client in self.__client_list:
            if client.estado == estado_searched:
                clients_searched.append(client)
        return clients_searched


client_repository = __ClientRepository()