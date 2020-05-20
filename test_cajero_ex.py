from billetes import Billete_100,Billete_1000,Billete_200,Billete_500
from cajero_completo_ex import Cajero
import unittest
from excepciones import MontoError, MontoMayor , CombinacionError, PorcentajeError, MontoNegativo , CajeroVacio

class TestCajero(unittest.TestCase):

    def setUp(self):       

        self.b = Billete_200()
        self.c= Billete_500()
        self.d = Billete_1000()

        #Cajero Vacio

        self.cajero_vacio = Cajero()

        #Set 1 
        lista_billetes = []

        lista_billetes = [self.d for valor in range (0,10)]

        self.cajero1 = Cajero()

        self.cajero1.agregar_billetes(lista_billetes)

        #Set 2

        for i in range (0,20):
            lista_billetes.append(self.c)

        self.cajero2 = Cajero()

        self.cajero2.agregar_billetes(lista_billetes)

        #Set 3

        for i in range (0,15):
            lista_billetes.append(self.b)

        self.cajero3= Cajero()

        self.cajero3.agregar_billetes(lista_billetes)

        
    #SET cajero vacio

    def test_cajero_vacio(self):

        with self.assertRaises(CajeroVacio):
            self.cajero_vacio.extraer_dinero(100)

    # SET 1

    def test_set1_prueba1(self):

        #(cantidad de 100, subtotal de 100,c de 200,s de 200,c de 500, s de 500,c de 1000,s de 1000,total)
        
        self.assertEqual(self.cajero1.contar(), (0,0,0,0,0,0,10,10000,10000))

    def test_set1_prueba2(self):

        extraccion = [self.d for valor in range (0,5)] #5 billetes de $1000

        self.assertEqual(self.cajero1.extraer_dinero(5000),extraccion)

    def test_set1_Error_Cantidad(self):

        with self.assertRaises(MontoMayor):
            self.cajero1.extraer_dinero(12000)
        
    def test_set1_Error_Multiplo100(self):

        with self.assertRaises(MontoError):
            self.cajero1.extraer_dinero(5520)

    def test_set1_Error_Valor_Negativo(self):

        with self.assertRaises(MontoNegativo):
            self.cajero1.extraer_dinero(-1)

    


    #SET 2

    def test_set2_prueba1(self):

        self.assertEqual(self.cajero2.contar(), (0,0,0,0,20,10000,10,10000,20000))

    def test_set2_prueba2(self):

        extraccion = [self.d for valor in range (0,5)] #5 billetes de $1000

        self.assertEqual(self.cajero2.extraer_dinero(5000),extraccion)

    def test_set2_prueba3(self):

        extraccion = [self.d for valor in range (0,10)] #10 billetes de 1000

        for i in range (0,4):
            extraccion.append(self.c) #sumo 4 billetes de 500

        self.assertEqual(self.cajero2.extraer_dinero(12000),extraccion)

    def test_set2_Error_Combinacion(self):

        with self.assertRaises(CombinacionError):
            self.cajero2.extraer_dinero(12100)

    def test_set2_prueba5(self):

        extraccion = [self.c for valor in range (0,2)] #2 billetes de 500

        for i in range (0,6):
            extraccion.append(self.d) #sumo 6 billetes de 1000

        self.assertEqual(self.cajero2.extraer_dinero_cambio(7000,10),extraccion)


    def test_set2_Error_Valor_Negativo(self):

        with self.assertRaises(MontoNegativo):
            self.cajero2.extraer_dinero(-100)

   
    #SET 3

    def test_set3_prueba1(self):

        self.assertEqual(self.cajero3.contar(), (0,0,15,3000,20,10000,10,10000,23000))

    def test_set3_prueba2(self):

        extraccion = [self.d for valor in range (0,5)] #5 billetes de $1000

        self.assertEqual(self.cajero3.extraer_dinero(5000),extraccion)

    def test_set3_prueba3(self):

        extraccion = [self.d for valor in range (0,10)] #10 billetes de 1000

        for i in range (0,4):
            extraccion.append(self.c) #sumo 4 billetes de 500

        self.assertEqual(self.cajero3.extraer_dinero(12000),extraccion)

    def test_set3_Error_Combinacion(self):

        with self.assertRaises(CombinacionError):
            self.cajero3.extraer_dinero(12100)

    def test_set3_prueba5(self):

        extraccion = [self.b for valor in range (0,4)] #4 billetes de 200 por el cambio

        for i in range (0,6):
            extraccion.append(self.d) #sumo 6 billetes de 1000

        extraccion.append(self.b) #billete de 200 para completar

        self.assertEqual(self.cajero3.extraer_dinero_cambio(7000,10),extraccion)

    def test_set3_Error_Valor_Negativo(self):

        with self.assertRaises(MontoNegativo):
            self.cajero3.extraer_dinero(-250)

    #Prueba porpia para el porcentaje de cambio

    def test_porcentaje_mayor(self):

        with self.assertRaises(PorcentajeError):
            self.cajero3.extraer_dinero_cambio(7000,101)

    def test_porcentaje_menor(self):

         with self.assertRaises(PorcentajeError):
            self.cajero3.extraer_dinero_cambio(7000,-1)



if __name__ == "__main__":
    unittest.main()
