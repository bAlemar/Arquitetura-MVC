from typing import Dict, List
from src.models.repositories.product_repository import product_repository
import os 

class Product_Search_View():
    def show_all_product(self,products:List) -> None:
        self.__clear()
        
        for product in products:
            message = f"""
            Produto: {product["nome"]}
            Sabor: {product["sabor"]}
            """
            print(message)            
        return
    
    def product_search_view_error(self,error) -> None:
        self.__clear()
        message = f"""
        Não foi possível pesquisar o Produto
        {error}
        """
        print(message)

        return
    def __clear(self):
        os.system('cls||clear')
