from src.models.repositories.client_repository import client_repository
from typing import List, Dict
class ClientSearchByEstado:
    def search_client(self,estado:str) -> Dict:
        try:   
            clients = self.__get_clients_by_estado(estado)
            return self.__format_response(clients)
        except Exception as e:
            return {"success":False, "error":f"Error {e}"}

    def __get_clients_by_estado(self,estado:str) -> List:
        clients = client_repository.search_client_by_estado(estado)
        if clients == []: raise Exception(f"Nenhum Cliente encontrado no estado {estado}")
        else: return clients
    
    def __format_response(self,clients: List) -> Dict:
        formatted_clients = []
        for client in clients:
            formatted_clients.append({
                "nome": client.nome,
                "telefone": client.telefone,
                "estado": client.estado
            })
        
        return {
            "success": True,
            "attributtes":{
                "quantidade_clientes":len(formatted_clients),
                "clients":formatted_clients
            }
        }