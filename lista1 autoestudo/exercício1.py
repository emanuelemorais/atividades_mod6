#Crie uma classe “Pessoa” que tenha os atributos nome, idade e profissão. Em seguida, crie uma lista de objetos dessa classe e ordene-os por ordem alfabética pelo atributo nome. Permita que o usuário realize a entrada de dados para cadastrar as pessoas na lista. A quantidade de pessoas pode variar de acordo com quantos dados o usuário desejar informar. A entrada deve ser encerrada quando o usuário não desejar informar mais usuários (pode ser quando o ele digitar um nome em branco)

class Pessoa():
    pessoas = []
    
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
        
    def __repr__(self):
        return f"({self.nome}, {self.idade}, {self.profissao})"
    
    @classmethod
    def adiciona_pessoa_lista(cls, pessoa):
        cls.pessoas.append(pessoa)
        cls.pessoas.sort(key=lambda x: x.nome)
        print(cls.pessoas)
        
    def cria_pessoa():
        numero = input("Quantas pessoas vc deseja adicionar? (Escreva com numeros): ")
        x = 0
        while x < int(numero):
            novo_nome = input("Escreva o nome: ")
            nova_idade = input("Escreva a idade: ")
            nova_profissão = input("Escreva profissão: ")
            p = Pessoa(novo_nome, nova_idade, nova_profissão)
            Pessoa.adiciona_pessoa_lista(p)
            x += 1
        
def main():
    Pessoa.cria_pessoa()
    
    
if __name__ == "__main__":
    main()