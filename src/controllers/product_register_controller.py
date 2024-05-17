from typing import Dict
from src.models.entities.product import Product
from src.models.repositories.product_repository import product_repository

class ProductRegister:
    def insert(self, new_product_informations:Dict) -> Dict:
        try:
            product = self.__create_product_entity(new_product_informations)
            self.__registry_product(product)
            response = self.__format_response(new_product_informations)
            return response
        except:
            return {"sucess":False,"error":"Error in insert client"}

    def __create_product_entity(self,new_product_informations:Dict) -> any:
        nome = new_product_informations['nome']
        sabor = new_product_informations['sabor']
        product = Product(nome,sabor)
        return product

    def __registry_product(self,product:any) -> None:
        product_repository.insert_product(product)

    def __format_response(self, new_product_informations: Dict) -> Dict:
        return {
                "sucess":True,
                "attributes": {
                    "registry":1,
                    "nome":new_product_informations["nome"],
                    "sabor":new_product_informations["sabor"],
                        }
                }

