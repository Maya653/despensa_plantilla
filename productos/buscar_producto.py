import csv  # Librería para abrir, leer y escribir archivos CSV

class BuscarProducto:

    def __init__(self) -> None:
        pass

    def buscarProducto(self, sku: str) -> bool: # Metodo para buscar un producto
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error buscarProducto() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
