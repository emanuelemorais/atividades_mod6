# Crie uma classe ContaBancaria que tenha os atributos numero, titular, saldo e limite. Crie métodos para depositar, sacar e consultar saldo da conta. Em seguida, crie objetos dessa classe e teste os métodos criados.

class ContaBancaria():
    def __init__(self, numero, titular, limite, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def __repr__(self):
        f"numero: {self.numero}, titular: {self.titular}, saldo: {self.saldo}, limite: {self.limite}"
        
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    
        else:
            print(f"Saldo insuficinte: você possui {self.saldo} reais em sua conta")
            
    def consulta_saldo(self):
        print(f"Saldo atual: {self.saldo}")
        
        
def main():
    m = ContaBancaria(numero=123, titular='Manu', limite=1000)
    m.depositar(100)
    m.sacar(60)
    m.consulta_saldo()

    
    
if __name__ == "__main__":
    main()