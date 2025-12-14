class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, matricula, serie):
        super().__init__(nome, sobrenome)
        self.matricula = matricula
        self.serie = serie

class Professor(Pessoa):
    def __init__(self, nome, sobrenome, email, senha):
        super().__init__(nome, sobrenome)
        self.email = email
        self.__senha = senha

    def verificarSenha(self, senha):
        return self.__senha == senha

    def acessarAreaProf(self):
        print("Acesso à área do professor")

    def acessarChat(self):
        print("Acessando chat")

    def registrarPresenca(self):
        print("Presença registrada")

class Responsavel(Pessoa):
    def __init__(self, nome, sobrenome, telefone, email, senha):
        super().__init__(nome, sobrenome)
        self.telefone = telefone
        self.email = email
        self.__senha = senha

    def verificarSenha(self, senha):
        return self.__senha == senha

    def acessarChat(self):
          return True

class Turma:
    def __init__(self, ano, codigo):
        self.ano = ano
        self.codigo = codigo
        self.alunos = []
        self.professores = []

    def adicionarAluno(self, aluno: Aluno):  # classe turma precisa de Aluno
        self.alunos.append(aluno)

    def adicionarProfessor(self, professor: Professor):
        self.professores.append(professor)

    def adicionarEvento(self, evento):
        print(f"Evento '{evento}' adicionado à turma {self.ano}")

class Notas:
    def __init__(self, aluno: Aluno, disciplina):  # classe Nota precisa de Aluno
        self.aluno = aluno
        self.disciplina = disciplina
        self.nota = None

    def registrarNotas(self, nota):
        self.nota = nota

    def relacionarAluno(self, aluno: Aluno):
        self.aluno = aluno

    def relacionarDisciplina(self, disciplina):
        self.disciplina = disciplina

class Frequencia:
    def __init__(self, aluno: Aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina
        self.assiduidade = 0  # percentual

    def registrarFrequencia(self, percentual):
        self.assiduidade = percentual

    def mostrarPercentual(self):
        return f"{self.assiduidade}%"

class Escola:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.usuarios = []

    def cadastrarUsuario(self, pessoa: Pessoa):
        self.usuarios.append(pessoa)

    def permitirAcesso(self):
        print("Acesso permitido")

    def adicionarEventos(self, evento):
        print(f"Evento '{evento}' adicionado à escola")


escola = Escola("E.E.F antonio Mendonça", 101)

aluno = Aluno("João", "Silva", 1234, "9º Ano")
prof = Professor("Ana", "Costa", "ana@email.com", "123")


turma = Turma("9A", 1)
turma.adicionarAluno(aluno)
turma.adicionarProfessor(prof)

nota = Notas(aluno, "Matemática")
nota.registrarNotas(8.5)

freq = Frequencia(aluno, "Matemática")
freq.registrarFrequencia(90)


