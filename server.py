from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from datetime import date, datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

tarefa_put_args = reqparse.RequestParser()
tarefa_put_args.add_argument("nome", type=str, help="Nome da tarefa é obrigatório", required=True)
tarefa_put_args.add_argument("descricao", type=str, help="Descrição da tarefa")
tarefa_put_args.add_argument("status", type=str, help="Status da tarefa é obrigatório", required=True)
tarefa_put_args.add_argument("data_vencimento", type=str, help="Data da tarefa no formato YYYY-MM-DD", required=True)

tarefa_update_args = reqparse.RequestParser()
tarefa_update_args.add_argument("nome", type=str, help="Nome da tarefa")
tarefa_update_args.add_argument("descricao", type=str, help="Descrição da tarefa")
tarefa_update_args.add_argument("status", type=str, help="Status da tarefa")
tarefa_update_args.add_argument("data_vencimento", type=str, help="Data da tarefa (YYYY-MM-DD)")


class TarefaModelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)


db.create_all()

resource_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'descricao': fields.String,
    'status': fields.String,
    'data_vencimento': fields.String
}


class Tarefa(Resource):
    @marshal_with(resource_fields)
    def get(self, id_tarefa=None, status=None):
        if id_tarefa is not None:
            result = TarefaModelo.query.filter_by(id=id_tarefa).first()
            if not result:
                abort(404, message='Tarefa não encontrada')
            return result
        elif status is not None:
            result = TarefaModelo.query.filter_by(status=status).all()
            if not result:
                abort(404, message='Tarefa não encontrada')
            return result

        else:
            return TarefaModelo.query.all()

    @marshal_with(resource_fields)
    def post(self):
        args = tarefa_put_args.parse_args()
        if args['status'] not in ["pendente", "realizando", "concluída"]:
            abort(400, message="Status inválido. Use: 'pendente', 'realizando' ou 'concluída'.")
        # Parse data_vencimento to a date object
        try:
            data_vencimento = datetime.strptime(args['data_vencimento'], "%Y-%m-%d").date()
        except ValueError:
            abort(400, message="Formato de data_vencimento inválido. Use YYYY-MM-DD.")

        tarefa = TarefaModelo(
            nome=args['nome'],
            descricao=args['descricao'],
            status=args['status'],
            data_vencimento=data_vencimento
        )
        db.session.add(tarefa)
        db.session.commit()
        return tarefa, 201

    @marshal_with(resource_fields)
    def delete(self, id_tarefa):
        result = TarefaModelo.query.filter_by(id=id_tarefa).first()
        if not result:
            abort(404, message='Tarefa não encontrada')
        db.session.delete(result)
        db.session.commit()
        return '', 204

    @marshal_with(resource_fields)
    def put(self, id_tarefa):
        args = tarefa_update_args.parse_args()
        result = TarefaModelo.query.filter_by(id=id_tarefa).first()
        if not result:
            abort(404, message='Tarefa não encontrada')
        if args['nome']:
            result.nome = args['nome']
        if args['descricao']:
            result.descricao = args['descricao']
        if args['status']:
            if args['status'] not in ["pendente", "realizando", "concluída"]:
                abort(400, message="Status inválido. Use: 'pendente', 'realizando' ou 'concluída'.")
            result.status = args['status']
        if args['data_vencimento']:
            try:
                result.data_vencimento = date.fromisoformat(args['data_vencimento'])
            except ValueError:
                abort(400, message="Data inválida. Use o formato YYYY-MM-DD.")
        db.session.commit()
        return result


api.add_resource(Tarefa, "/tarefas", "/tarefas/<int:id_tarefa>", "/tarefas?<string:status>")

if __name__ == "__main__":
    app.run(debug=True)
