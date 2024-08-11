class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        pass # implementación de la función con la forula de área de un rectángulo
        return self.base*self.altura


class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        pass # inicialización de la variable radio
        self.radio=radio
    
    def area(self):
        pass # implementación de la función con la forula de área de un círculo
        return self.pi*self.radio*self.radio