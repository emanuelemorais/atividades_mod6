# Crie uma classe FormaGeometrica, ela deve possuir os métodos calcularArea e calcularPerimetro. Em seguida, crie duas classes filhas, Retangulo e Circulo, que tenham os atributos largura e altura; raio, respectivamente. Sobrescrever os métodos para calcular a área e o perímetro. Em seguida, crie objetos dessas classes e teste os métodos criados.

class FormaGeometrica():
    def calcularArea(self):
        pass
    
    def calcularPerimetro(self):
        pass
    
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def __repr__(self):
        return f"{self.largura}, {self.altura}"
        
    def calcularArea(self):
        return self.largura * self.altura
    
    def calcularPerimetro(self):
        return 2* self.largura + 2* self.altura
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def __repr__(self):
        return f"{self.raio}"
        
    def calcularArea(self):
        return 3.14 * self.raio**2
    
    def calcularPerimetro(self):
        return 2 * 3.14 * self.raio
    
    
def main():
    r = Retangulo(3, 5)
    print(r.calcularArea())
    print(r.calcularPerimetro())
    
    c = Circulo(8)
    print(c.calcularArea())
    print(c.calcularPerimetro())
    
if __name__ == "__main__":
    main()
        