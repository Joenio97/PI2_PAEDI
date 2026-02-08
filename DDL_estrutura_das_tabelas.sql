DROP TABLE IF EXISTS mensagem CASCADE;
DROP TABLE IF EXISTS evento CASCADE;
DROP TABLE IF EXISTS cronograma CASCADE;
DROP TABLE IF EXISTS frequencia CASCADE;
DROP TABLE IF EXISTS nota CASCADE;
DROP TABLE IF EXISTS prof_turm_disci CASCADE;
DROP TABLE IF EXISTS disciplina CASCADE;
DROP TABLE IF EXISTS responsavel_aluno CASCADE;
DROP TABLE IF EXISTS aluno CASCADE;
DROP TABLE IF EXISTS turma CASCADE;
DROP TABLE IF EXISTS professor CASCADE;
DROP TABLE IF EXISTS funcionario CASCADE;
DROP TABLE IF EXISTS responsavel CASCADE;
DROP TABLE IF EXISTS instituicao CASCADE;
DROP TABLE IF EXISTS usuario CASCADE;


CREATE TABLE usuario (
    id_usuario integer PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    tipo_usuario VARCHAR(20) CHECK (tipo_usuario IN ('RESPONSAVEL','PROFESSOR'))
);

CREATE TABLE instituicao (
    id_instituicao integer PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE responsavel (
    id_responsavel integer PRIMARY KEY,
    id_usuario integer UNIQUE REFERENCES usuario(id_usuario)
);

CREATE TABLE funcionario (
    id_funcionario integer PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    funcao VARCHAR(50),
    telefone VARCHAR(20),
    id_instituicao integer references instituicao(id_instituicao)
);

CREATE TABLE professor (
    id_professor SERIAL PRIMARY KEY,
    id_usuario integer UNIQUE REFERENCES usuario(id_usuario),
    id_funcionario integer UNIQUE REFERENCES funcionario(id_funcionario)
);

CREATE TABLE turma (
    id_turma integer PRIMARY KEY,
    ano integer NOT NULL,
    semestre smallint,
    id_instituicao INT REFERENCES instituicao(id_instituicao)
);

CREATE TABLE aluno (
    id_aluno integer PRIMARY KEY,
    matricula VARCHAR(20) UNIQUE,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    id_turma integer REFERENCES turma(id_turma)
);

CREATE TABLE responsavel_aluno (
    id_responsavel integer REFERENCES responsavel(id_responsavel),
    id_aluno integer REFERENCES aluno(id_aluno),
    PRIMARY KEY (id_responsavel, id_aluno)
);

CREATE TABLE disciplina (
    id_disciplina integer PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE prof_turm_disci (
    id_professor INT REFERENCES professor(id_professor),
    id_turma INT REFERENCES turma(id_turma),
    id_disciplina INT REFERENCES disciplina(id_disciplina),
    PRIMARY KEY (id_professor, id_turma, id_disciplina)
);

CREATE TABLE nota (
    id_nota integer PRIMARY KEY,
    id_aluno integer REFERENCES aluno(id_aluno),
    id_disciplina integer REFERENCES disciplina(id_disciplina),
    valor NUMERIC(4,2)
);

CREATE TABLE frequencia (
    id_frequencia integer PRIMARY KEY,
    id_aluno integer REFERENCES aluno(id_aluno),
    id_disciplina integer REFERENCES disciplina(id_disciplina),
    data DATE,
    presenca BOOLEAN
);

CREATE TABLE cronograma (
    id_cronograma integer PRIMARY KEY,
    data DATE,
    conteudo TEXT,
    tipo VARCHAR(20),
    id_professor integer REFERENCES professor(id_professor),
    id_turma integer REFERENCES turma(id_turma),
    id_disciplina integer REFERENCES disciplina(id_disciplina)
);

CREATE TABLE evento (
    id_evento integer PRIMARY KEY,
    tema VARCHAR(100),
    data DATE,
    id_instituicao integer REFERENCES instituicao(id_instituicao)
);

CREATE TABLE mensagem (
    id_mensagem integer PRIMARY KEY,
    texto TEXT,
    data_envio TIMESTAMP,
    id_usuario_origem integer REFERENCES usuario(id_usuario),
    id_usuario_destino integer REFERENCES usuario(id_usuario)
);
