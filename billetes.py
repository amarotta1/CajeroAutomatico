
class Billetes():

    def __init__(self, valor):

        self.denominación = "pesos $"
        self.valor =  valor
        self.representacion =  "$ "+ str(valor)

class Billete_100(Billetes):
    
    def __init__(self):
        Billetes.__init__(self,100)


class Billete_200(Billetes):
    
    def __init__(self):
        Billetes.__init__(self,200)


class Billete_500(Billetes):
    
    def __init__(self):
        Billetes.__init__(self,500)


class Billete_1000(Billetes):
    
    def __init__(self):
        Billetes.__init__(self,1000)

