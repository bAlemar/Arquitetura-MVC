from src.view.client_search_by_estado_view import ClientSearchView
from src.controllers.client_search_by_estado_controller import ClientSearchByEstado

def client_search_by_estado_process():
    client_search_view = ClientSearchView()
    client_search_controller = ClientSearchByEstado()
    
    estado = client_search_view.client_search_by_estado_view()
    response = client_search_controller.search_client(estado)
    if response["success"]:
        return client_search_view.client_search_success(response["attributtes"]["clients"])
    else:
        return client_search_view.client_search_error(response["error"])