# #conecta view e controller
# from src.view.product_register_view import Product_Register_View
# from src.controllers.product_register_controller import ProductRegister

# def product_register_process():
#     product_register_view = Product_Register_View()
#     product_register_controller = ProductRegister()
    
#     new_product_information = product_register_view.register_product_view()
#     response = product_register_controller.insert(new_product_information)

#     if response["sucess"]:
#         product_register_view.register_product_sucess(response["attributes"])
#     else:
#         product_register_view.register_product_error(response["error"])

from src.view.product_delete_view import Product_Delete_View
from src.controllers.product_delete_controller import ProductDelete

def product_delete_process():
    product_delete_view = Product_Delete_View()
    product_delete_controller = ProductDelete()
    name_product = product_delete_view.product_delete_view()
    response = product_delete_controller.delete(name_product)
    print(response)
    if response["success"]:
        product_delete_view.product_delete_view_suceess(response["attributes"]["produto"])
    else:
        product_delete_view.product_delete_view_error(response["error"])
    return
