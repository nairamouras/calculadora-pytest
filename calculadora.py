class Calculadora():
    
    def __init__(self):
        numero1 = int(input("Digite o primeiro número da operação: "))
        print("#"*40)
        numero2 = int(input("Digite o segundo número da operação: "))
        print("#"*40)
        operacao = int(input("Agora escolha a operação desejada: 1 - Soma; 2 - Subtração; 3 - Multiplicação; 4 - Divisão \n"))
        print("#"*90)
        if operacao == 1:
            print("A soma dos números é igual a", self.soma(numero1, numero2))
        elif operacao == 2:
            print("A subtração dos números é igual a", self.subtracao(numero1, numero2))
        elif operacao == 3:
            print("A multiplicação dos números é igual a", self.multiplicacao(numero1, numero2))
        elif operacao == 4:
            print("A divisão dos números é igual a", self.divisao(numero1, numero2))
        else:
            print("Opção inválida.")
            exit()
            
    def soma(self, numero1, numero2):
        return numero1+numero2

    def subtracao(self, numero1, numero2):
        return numero1-numero2

    def multiplicacao(self, numero1, numero2):
        return numero1*numero2

    def divisao(self, numero1, numero2):
        if(numero2 == 0):
            print("Não existe divisão por zero.")
            return None
        else:
            return numero1/numero2
        
if __name__ == '__main__':
    Calculadora()
