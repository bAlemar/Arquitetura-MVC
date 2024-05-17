import os
from typing import List
class Product_Delete_View:
    def product_delete_view(self) -> str:
        product = input('Product: ')
        message = f"""
        Digite o product que deseja deletar
        {product}
        """
        print(message)
        return product

    def product_delete_view_suceess(self,products: List):
        self.__clear()
        
        for product in products:
            message = f"""
            Produto {product["nome"]} com sabor {product["sabor"]} Excluido com Sucesso
            """
            print(message)

    def product_delete_view_error(self,error):
        self.__clear()
        message = f"""
        
        Error ao excluir o produto
        {error}
        
        """
        print(message)
        return
    def __clear(self):
        os.system('cls||clear')