from typing import List


class __ProductRepository:
    def __init__(self) -> None:
        self.__product_list = []
    
    def insert_product(self,product:any) -> None:
        self.__product_list.append(product)
    
    def all_product(self) -> List:
        return self.__product_list
    
    def search_product(self,name_searched) -> List:
        for product in self.__product_list:
            if product.nome == name_searched:
                return [product]


    def delete_product(self,product_searched:any) -> None:
        lista_produto = [product for product in product_searched]
        for product in self.__product_list:
            if product in lista_produto:
                self.__product_list.remove(product)


product_repository = __ProductRepository()