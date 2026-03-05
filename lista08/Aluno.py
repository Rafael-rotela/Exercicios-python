class Aluno:
    def __init__(self) -> None: ## Metodo construtor
        self.nome = ""
        self.matricula = ""
        self.nota_final = 0

    def  mostrar_dados(self):
        print(f"\n O aluno {self.nome} \n Matricula: {self.matricula} \n Foi com a nota fina de {self.nota_final} \n")
    
    def imprime_nome(self):
        print(f'{self.nome}')

    def imprime_nota(self):
        print(f'{self.matricula}')

aluno = Aluno()
aluno.nome = 'Rafael'
aluno.matricula = 2141
aluno.nota_final =  9
aluno.mostrar_dados()

aluno2 = Aluno()
aluno2.nome = 'MATTEUS'
aluno2.matricula ='1232'
aluno2.nota_final = 8
aluno2.mostrar_dados()

aluno3 = Aluno()
aluno3.nome = 'FABIO'
aluno3.matricula ='21423'
aluno3.nota_final = 10
aluno3.mostrar_dados()

aluno.imprime_nota()
aluno.imprime_nome()