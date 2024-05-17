from typing import Dict
from src.models.entities.client import Client
from src.models.repositories.client_repository import client_repository 

class ClientRegister:
    def insert(self, new_client_informations:Dict) -> Dict:
        try:
            client = self.__create_client_entity(new_client_informations)
            self.__registry_client(client)
            response = self.__format_response(new_client_informations)
            return response
        except:
            return {"sucesso":False,"error":"Error in insert client"}

    def __create_client_entity(self,new_client_informations:Dict) -> any:
        nome = new_client_informations['nome']
        telefone = new_client_informations['telefone']
        estado = new_client_informations['estado']
        client = Client(nome,telefone,estado)
        return client

    def __registry_client(self,client:any) -> None:
        client_repository.insert_client(client)

    def __format_response(self, new_client_informations: Dict) -> Dict:
        return {
                "sucess":True,
                "attributes": {
                    "registry":1,
                    "nome":new_client_informations["nome"],
                    "telefone":new_client_informations["telefone"],
                    "estado": new_client_informations["estado"]
                        }
                }