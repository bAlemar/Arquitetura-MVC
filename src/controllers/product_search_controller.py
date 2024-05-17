from src.models.repositories.product_repository import product_repository

class ProductSearch:
    def product_search(self):
        try:
            products = self.__search_product()
            return self.__format_product(products)
        except Exception as e:
            return {"success":False, "error":str(e)}
    
    def __search_product(self):
        products = product_repository.all_product()
        if products == []:
            raise Exception("Produto não encontrado")
        return products    
    
    def __format_product(self,products):
        # Transformando classes em dicionarios
        # formantando para mandar para view
        formatted_products = []
        for product in products:
            formatted_products.append({
                "nome": product.nome,
                "sabor": product.sabor,
                })

        return {
            "success": True,
            "attributes": {
                "count": len(formatted_products),
                "products": formatted_products
            }
        }

