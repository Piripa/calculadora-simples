class Calculator:
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def soma(valor1, valor2):
        return valor1 + valor2
        
    def subtracao(valor1, valor2):
        return valor1 - valor2

    def divisao(valor1, valor2):
        if(valor1 == 0 ):
            return 0
        elif(valor2 == 0):
            return Exception
        else:
            return valor1 / valor2
    
    def multiplicacao(valor1, valor2):
        return valor1 * valor2