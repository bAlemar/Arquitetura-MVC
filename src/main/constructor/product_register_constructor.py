#conecta view e controller
from src.view.product_register_view import Product_Register_View
from src.controllers.product_register_controller import ProductRegister

def product_register_process():
    product_register_view = Product_Register_View()
    product_register_controller = ProductRegister()
    
    new_product_information = product_register_view.register_product_view()
    response = product_register_controller.insert(new_product_information)

    if response["sucess"]:
        product_register_view.register_product_sucess(response["attributes"])
    else:
        product_register_view.register_product_error(response["error"])

