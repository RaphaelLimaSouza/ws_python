class Aluno:
    def __init__(self, nome, visitante=False):
        self.nome = nome
        self.visitante = visitante
        self.faltas = 0

class SalaDeAula:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, nome, visitante=False):
        aluno = Aluno(nome, visitante)
        self.alunos.append(aluno)

    def validar_presenca(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                aluno.faltas = 0
            else:
                aluno.faltas += 1

            if aluno.faltas > 2 and not aluno.visitante:
                self.alunos.remove(aluno)
                print(f'O aluno {aluno.nome} foi desmatriculado por excesso de faltas.')

sala = SalaDeAula()
sala.adicionar_aluno('João')
sala.adicionar_aluno('Maria', visitante=True)

sala.validar_presenca('João')
