"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorite #Aqui importar elementos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    #en la variable all_users estoy consultando a la base de datos por todos los registros de la tabla users

    all_users = User.query.get(2)
    #estoy almacenando dentro de una listalist()
    # realizando un map(), donde un map ejecuta una instruccion por cada registro de un usuario en mi base de datos
    #y lambda es lo mismo que una funcion ()=>{} que ejecuta por cada registro de la base de datos (X) y ejecutara su funcion serialize() para devolver los datos que quiero

    all_users = list(map(lambda x: x.serialize(), all_users))
    #retorno todos los usuarios
    return jsonify(all_users), 200
     
#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

# # this only runs if `$ python src/main.py` is executed
# if __name__ == '__main__':
#     PORT = int(os.environ.get('PORT', 3000))
#     app.run(host='0.0.0.0', port=PORT, debug=False)

@app.route('/favoritos', methods=['GET'])
def allFavoritos():
    resultado ={"Mensaje ": "Aca iran todos los favoritos"}
    return jsonify(resultado)

