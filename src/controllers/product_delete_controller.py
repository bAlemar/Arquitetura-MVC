from typing import Dict, List
from src.models.repositories.product_repository import product_repository

class ProductDelete:
    def delete(self,name:str):
        try:
            product = self.__get_product(name)
            product_repository.delete_product(product) 
            response = self.__format_response(product)
            return response
        except Exception as e:
            return {"success":False, "error":str(e)}

    def __get_product(self, name:str) -> any:
        product = product_repository.search_product(name)
        if not product:
            raise Exception("Esse Produto Não Existe na Base de Dados")
        return product
    
    def __format_response(self, products: List) -> Dict:      
        #Abrindo o objeto e armazenando ele em um dicionario. Ou seja
        #Extraindo os valores de cada objeto da lista products
        lista_produtos = []
        for product in products:
            lista_produtos.append({
                "nome":product.nome,
                "sabor":product.sabor
            })

        return {
            "success":True,
            "attributes":{
                "status": "Deletado",
                "produto": lista_produtos,
                
            }
        }