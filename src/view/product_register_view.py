import os
from typing import Dict

class Product_Register_View:
    def register_product_view(self) -> str:
        self.__clear()
        
        print("Registre o Produto")
        nome = input('Digite o nome do Produto: ')
        sabor = input('Digite o Sabor do Produto: ')

        new_product_informations = {
            "nome":nome , "sabor":sabor
        }

        return new_product_informations
    
    def register_product_sucess(self, product_registry: Dict) -> None:
        self.__clear()
        
        message = f"""
        O Produto {product_registry["nome"]}
        com sabor: {product_registry["sabor"]}

        Foi registrado com Sucesso!!    
        """
        print(message)
        return
    
    def register_product_error(self,error:str) -> None:
        self.__clear()
        
        message = f"""
        
        Não foi possível cadastrar esse produto.
        Devido seguinte error:
        {error}
        """
        print(message)

    def __clear(self):
        os.system('cls||clear')