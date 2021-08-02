from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/respostas.db'
db = SQLAlchemy(app)


class Textos(db.Model):
    __tablename__ = "textos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=False, nullable=False)
    # respostas = db.relationship('Respostas', backref='texto', lazy=True)

    def __repr__(self):
        return f'<Texto {self.id} - {self.nome}>'


class Estudantes(db.Model):
    __tablename__ = "estudantes"

    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.String(20), unique=False, nullable=False)
    # respostas = db.relationship('Respostas', backref='estudante', lazy=True)

    def __repr__(self):
        return f'<Estudante {self.id} - {self.ano}>'


class Perguntas(db.Model):
    __tablename__ = "perguntas"

    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.Text(), unique=False, nullable=False)
    # respostas = db.relationship('Respostas', backref='pergunta', lazy=True)

    def __repr__(self):
        return f'<Texto {self.id} - {self.nome}>'


class Respostas(db.Model):
    __tablename__ = "respostas"

    id = db.Column(db.Integer, primary_key=True)
    texto_id = db.Column(db.Integer, db.ForeignKey('textos.id'), nullable=False)
    estudante_id = db.Column(db.Integer, db.ForeignKey('estudantes.id'), nullable=False)
    pergunta_id = db.Column(db.Integer, db.ForeignKey('perguntas.id'), nullable=False)
    data_hora = db.Column(db.String(50), nullable=False, unique=False)
    resposta = db.Column(db.Text(), unique=False, nullable=False)

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'texto_id': self.texto_id,
            'estudante_id': self.estudante_id,
            'pergunta_id': self.pergunta_id,
            'data_hora': self.data_hora,
            'resposta': self.resposta
        }
