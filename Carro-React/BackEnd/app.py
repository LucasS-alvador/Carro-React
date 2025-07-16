#
# IMPORTAÇÕES
#

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

#
# VARIÁVEIS E CONFIGURAÇÕES
#

app = Flask(__name__)

# configurações específicas para o SQLite
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd

db = SQLAlchemy(app)

#
# CLASSES
#

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)

    # expressar a classe em formato texto
    def __str__(self):
        return f'{self.nome}, ' +\
               f'{self.email}, {self.telefone}'

    # expressar a classe em formato json
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }
    
class Carro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.Text)
    marca = db.Column(db.Text)
    ano = db.Column(db.Integer)
    cor = db.Column(db.Text)
    placa = db.Column(db.Text)

    def __str__(self):
        return f'{self.modelo}, {self.marca}, {self.ano}, {self.cor}, {self.placa}'

    def json(self):
        return {
            "modelo": self.modelo,
            "marca": self.marca,
            "ano": self.ano,
            "cor": self.cor,
            "placa": self.placa
        }

#
# ROTAS
#

@app.route("/")
def ola():
    return "backend operante"

# curl localhost:5000/incluir_pessoa -X POST -d '{"nome":"john", "email":"jo@gmail.com", "telefone":"91234567"}' -H "Content-Type:application/json"
@app.route("/incluir_pessoa", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        # cria a pessoa
        nova = Pessoa(**dados)
        # realiza a persistência da nova pessoa
        db.session.add(nova)
        db.session.commit()
        # tudo certo :-) resposta de sucesso
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        # informar mensagem de erro
        return jsonify({"resultado": "erro", "detalhes": str(e)})

@app.route("/listar_pessoas")
def listar_pessoas():
    try:
        # obter as pessoas
        lista = db.session.query(Pessoa).all()
        # converter pessoas pra json
        lista_retorno = [x.json() for x in lista]
        # preparar uma parte da resposta: resultado ok
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        # retornar a lista de pessoas json, com resultado ok
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})
    
# curl localhost:5000/incluir_carro -X POST -d '{"modelo":"Uno", "marca":"Fiat", "ano":2010, "cor":"preto", "placa":"ABC1234"}' -H "Content-Type:application/json"
@app.route("/incluir_carro", methods=['POST'])
def incluir_carro():
    dados = request.get_json()
    try:
        novo = Carro(**dados)
        db.session.add(novo)
        db.session.commit()
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})

@app.route("/listar_carros")
def listar_carros():
    try:
        lista = db.session.query(Carro).all()
        lista_retorno = [x.json() for x in lista]
        return jsonify({"resultado": "ok", "detalhes": lista_retorno})
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})


#
# INICIO DA APLICAÇÃO
#

with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    '''
      iniciar o servidor

      $ flask run

    '''
    app.run(debug=True) # <--- debug=True é importante para o desenvolvimento
    
