from src.view.client_register_view import Client_Register_View
from src.controllers.client_register_controller import ClientRegister

def client_register_process():
    client_register_view = Client_Register_View()
    client_register_controller = ClientRegister()

    new_client_informations = client_register_view.register_client_view()
    response = client_register_controller.insert(new_client_informations)

    if response["sucess"]:
        client_register_view.register_client_sucess(response["attributes"])
    else:
        client_register_view.register_client_error(response["error"])
    return