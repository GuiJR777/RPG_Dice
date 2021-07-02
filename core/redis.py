# Cria Banco de dados Redis e Cache
import json
import redis
import os
import core.utils as u


class Redis_DB():
    def get_instance() -> redis.Redis:
        try:
            redis_db = redis.from_url(os.environ.get("REDIS_URL"))
            return redis_db
        except Exception as e:
            pass

# Classe que controla o cache
class Cache():
    def __init__(self):
        self.cache = Redis_DB.get_instance()

    def include(self, key:str, value:str) -> None:
        # Inclui no cache
        self.cache.set(key, value)

    def include_with_hash(self, response:dict) -> None:
        # Inclui no cache
        value = {
            'result' : response['one_line_result'],
            'created_at' : u.agora()           
        }
        value = json.dumps(value)
        key = u.hash_this(value)
        self.include(key, value)
    
    def return_db(self,key:str) -> str:
        # Retorna do Cache
        if key in self.cache:
            str = self.cache.get(key)
        else:
            str = None
        return str

    def return_all(self) -> dict:
        response = {}
        i = 0
        for key in self.cache.keys():
            i+=1
            response[f'{i}'] = json.loads(self.return_db(key))

        return response
        

    def delete(self, key:str) -> None:
        # Consulta Cache, se chave não for encontrada inclui no Redis
        self.cache.delete(key)

    def reset_cache(self):
        for key in self.cache.keys():
            self.cache.delete(key)

if __name__ == '__main__':
    pass