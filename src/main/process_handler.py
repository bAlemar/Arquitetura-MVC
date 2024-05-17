from .constructor.introduction_process import introduction_process
from .constructor.client_register_constructor import client_register_process
from .constructor.product_register_constructor import product_register_process
from .constructor.product_delete_constructor import product_delete_process
from .constructor.product_search_constructor import product_search_process
from .constructor.client_search_by_estado_constructor import client_search_by_estado_process
# importa as funcionalidades do construtor
# Aqui é basicamente o layout do software

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': client_register_process()
        elif command == '2': product_register_process()
        elif command == '3': product_delete_process()
        elif command == '4': product_search_process()
        elif command == '5': client_search_by_estado_process()
        elif command == '6': exit()