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
    return "<p>Hello, World!</p>"
@app.route("/edita-refeicao", methods = ['PUT'])
def edita_refeicao():
    return "<p>Hello, World!</p>"
@app.route("/remove-refeicao", methods = ['DELETE'])
def remove_refeicao():
    return "<p>Hello, World!</p>"
@app.route("/resgata-refeicao", methods = ['GET'])
def resgata_refeicao():
    return "<p>Hello, World!</p>"
@app.route("/lista-refeicoes", methods = ['GET'])
def lista_refeicao():
    return "<p>Hello, World!</p>"