from menus.models import Menu


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, menu, ingredientes):
        id = str(menu.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "menu_id": menu.id,
                "nombre": menu.nombre_menu,
                "acumulado": menu.precio,
                "cantidad": 1,
                "ingredientes": ingredientes,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += menu.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, menu_id):
        id = str(menu_id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, menu_id):
        id = str(menu_id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(menu_id)
            else:
                menu = Menu.objects.get(id=self.carrito[id]["menu_id"])
                self.carrito[id]["acumulado"] -= menu.precio
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
    
    