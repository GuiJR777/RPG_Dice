from core.rpgdice import Dice
from core.redis import Cache
from core.constants import USE_CACHE
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
        if USE_CACHE:
            cache.include_with_hash(payload)

        return payload
    
    def post(self):
        data = json.loads(request.data)
        texto = data['text']
        dado = Dice()
        payload = dado.roll_by_text(texto)
        if USE_CACHE:
            cache.include_with_hash(payload)

        return payload

class RollDice(Resource):
    def get(self, dado, qtd):
        dado = Dice(int(dado))
        payload = dado.roll(int(qtd))
        if USE_CACHE:
            cache.include_with_hash(payload)

        return payload

class History(Resource):
    def get(self):
        
        return cache.return_all()

class HistoryClear(Resource):
    def get(self):
        cache.reset_cache()
        message =  'Ok, history clean'

        return {
            'message' : message
        }

resources = [
    [Teste, '/'],
    [RollText, '/dice/text/<string:comand>/'],
    [RollDice, '/dice/<int:dado>/<int:qtd>/'],
    [History, '/dice/history/'],
    [HistoryClear, '/dice/history/clear/']]

for resource in resources:
    api.add_resource(resource[0], resource[1])


if __name__==('__main__'):
    app.run(debug = True, host = '0.0.0.0')