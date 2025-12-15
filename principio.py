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
        return "Acesso à área do professor concedido"

    def acessarChat(self):
        return "Acesso ao chat concedido"

    def registrarPresenca(self):
        return "Presença registrada"

class Responsavel(Pessoa):
    def __init__(self, nome, sobrenome, telefone, email, senha):
        super().__init__(nome, sobrenome)
        self.telefone = telefone
        self.email = email
        self.__senha = senha

    def verificarSenha(self, senha):
        return self.__senha == senha
        
    def acessarAreaProf(self):
        return "Acesso à área do professor concedido"

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
        return f"Evento '{evento}' adicionado à turma {self.ano}"

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
        return "Acesso permitido à escola"

    def adicionarEventos(self, evento):
        return f"Evento '{evento}' adicionado à escola"


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

print("SISTEMA ESCOLAR")

print(escola.permitirAcesso()) # Acesso à escola

# Professor
print("Professor")
print(prof.acessarAreaProf())
print(prof.acessarChat())
print(prof.registrarPresenca())

# Responsavel
print("Responsavel")
print(respon.acessarAreaRespon())

# Turma
print("Turma")
print(turma.adicionarEvento("Prova de Matemática"))

# Aluno
print("Aluno")
print(f"Aluno: {aluno.nome} {aluno.sobrenome}")
print(f"Série: {aluno.serie}")
print(f"Matrícula: {aluno.matricula}")

# Notas
print("Notas")
print(f"Disciplina: {nota.disciplina}")
print(f"Nota: {nota.nota}")

# Frequência
print("Frequência")
print(f"Frequência em {freq.disciplina}: {freq.mostrarPercentual()}")

print("FIM DO SISTEMA ESCOLAR PAEDI")
