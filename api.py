from core.rpgdice import Dice
from core.redis import Cache
from flask import Flask, request
from flask_restful import Api, Resource
import json

app= Flask(__name__)
api= Api(app)

cache = Cache()

class Teste(Resource):
    def get(sef):
        message =  \
'Ok, this is working! \
Please, use the EndPoints:\
[1]/dice/text/{your text hear} method GET to use from command "roll{n}d{n}".\
[2]/dice/text/{your text hear} method POST to send a command "roll{n}d{n}" in a JSON object in the key "text".\
[3]/dice/{number of sides of the desired dice}/{amount of dices desired} to use one especific dice. Enjoy!'

        return {'status':'OK', 'message':f'{message}'}

class RollText(Resource):
    def get(self, comand):
        dado = Dice()
        payload = dado.roll_by_text(comand)
        cache.include_with_hash(payload)

        return json.dumps(payload)
    
    def post(self):
        data = json.loads(request.data)
        texto = data['text']
        dado = Dice()
        payload = dado.roll_by_text(texto)
        cache.include_with_hash(payload)

        return json.dumps(payload)

class RollDice(Resource):
    def get(self, dado, qtd):
        dado = Dice(int(dado))
        payload = dado.roll(int(qtd))
        cache.include_with_hash(payload)

        return json.dumps(payload)

class History(Resource):
    def get(self):
        payload = cache.return_all()

        return json.dump(payload)

class HistoryClear(Resource):
    def get(self):
        cache.reset_cache()
        message =  {
            'message' : 'Ok, history clean'
        }

        return json.dumps(message)

resources = [
    [Teste, '/'],
    [RollText, '/dice/text/<string:comand>/'],
    [RollDice, '/dice/<int:dado>/<int:qtd>/'],
    [History, '/dice/history/'],
    [HistoryClear, '/dice/history/clear/']]

for resource in resources:
    api.add_resource(resource[0], resource[1])


def start():
    return app