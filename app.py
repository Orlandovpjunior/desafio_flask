from flask import Flask, request, jsonify
from database import db
from models.refeicao import Refeicao

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:admin123@127.0.0.1:3307/flask-refeicao-crud'
app.secret_key = "chave-secreta-muito-segura"
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/adiciona-refeicao", methods = ['POST'])
def adiciona_refeicao():
    data = request.get_json()

    nome = data.get('nome')
    descricao = data.get('descricao')
    horario = data.get('horario')
    dentro_dieta = data.get('dentro_dieta')

    if nome and descricao and horario and dentro_dieta:
        refeicao = Refeicao(nome=nome, descricao=descricao, horario=horario,dentro_dieta=dentro_dieta)
        db.session.add(refeicao)
        db.session.commit()
        return jsonify({'message': 'Refeição cadastrada com sucesso'})
    return jsonify({'message': 'Erro ao cadastrar refeição'}), 400

@app.route("/edita-refeicao/<int:id_refeicao>", methods = ['PUT'])
def edita_refeicao(id_refeicao):
    data = request.get_json()
    refeicao = Refeicao.query.get(id_refeicao)

    refeicao.nome = data.get("nome")
    refeicao.descricao = data.get("descricao")
    refeicao.horario = data.get("horario")
    refeicao.dentro_dieta = data.get("dentro_dieta")

    db.session.commit()

    return jsonify({"mensagem": "Refeição atualizada com sucesso!"})
    

@app.route("/remove-refeicao/<int:id_refeicao>", methods = ['DELETE'])
def remove_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()

        return jsonify({"mensagem": "Refeição excluída com sucesso!"})
    return jsonify({"mensagem": "Erro ao excluir a refeição"}), 400

@app.route("/resgata-refeicao/<int:id_refeicao>", methods = ['GET'])
def resgata_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)

    if refeicao:
        return jsonify({'message': refeicao.nome})
    return jsonify({'message': 'Refeição não encontrada'}), 400

@app.route("/lista-refeicoes", methods = ['GET'])
def lista_refeicao():
    refeicoes = Refeicao.query.all()

    resultado = []

    for r in refeicoes:
        resultado.append({
            'id': r.id,
            'nome': r.nome,
            'descricao': r.descricao,
            'horario': r.horario.strftime("%H:%M:%S"),
            'dentro_dieta': r.dentro_dieta
        })

    return jsonify(resultado)

