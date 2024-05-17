from src.view.product_search_view import Product_Search_View
from src.controllers.product_search_controller import ProductSearch
def product_search_process():
    product_search_view = Product_Search_View()
    product_search_controller = ProductSearch()
    products = product_search_controller.product_search()
    if products["success"]:
        product_search_view.show_all_product(products["attributes"]["products"])
    else:
        product_search_view.product_search_view_error(products["error"])
    return 