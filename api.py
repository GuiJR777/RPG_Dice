from flask import Flask, request
from flask_restful import Api, Resource
import json
from rpgdice import Dice

app= Flask(__name__)
api= Api(app)

class Teste(Resource):
    def get(sef):
        message =  'Ok, this is working! \
Please, use the EndPoints:\
[1]/dice/text/{your text hear} method GET to use from command "roll{n}d{n}".\
[2]/dice/text/{your text hear} method POST to send a command "roll{n}d{n}" in a JSON object in the key "text".\
[3]/dice/{number of sides of the desired dice}/{amount of dices desired} to use one especific dice. Enjoy!'
        return {'status':'OK', 'message':f'{message}'}

class RollText(Resource):
    def get(self, comand):
        dado = Dice()
        payload = dado.roll_by_text(comand)
        return payload
    
    def post(self):
        data = json.loads(request.data)
        texto = data['text']
        dado = Dice()
        payload = dado.roll_by_text(texto)
        return payload

class RollDice(Resource):
    def get(self, dado, qtd):
        dado = Dice(int(dado))
        payload = dado.roll(int(qtd))
        return payload


api.add_resource(Teste, '/')
api.add_resource(RollText, '/dice/text/<string:comand>/')
api.add_resource(RollDice, '/dice/<int:dado>/<int:qtd>/')

if __name__==('__main__'):
    app.run(debug = True, host = '0.0.0.0')