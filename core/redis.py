# Cria Banco de dados Redis e Cache
import redis
import core.utils as u
from core.constants import REDIS_PASS, REDIS_PORT, REDIS_URL


class Redis_DB():
    def get_instance() -> redis.Redis:
        try:
            redis_db = redis.StrictRedis(host=REDIS_URL, port=REDIS_PORT, password=REDIS_PASS, decode_responses=True)
            redis_db.ping()
            return redis_db
        except Exception as e:
            print(e)

        redis_db = redis.StrictRedis(host="redis", port=REDIS_PORT, password=REDIS_PASS, decode_responses=True)
        redis_db.ping()

        return redis_db

# Classe que controla o cache
class Cache():
    def __init__(self):
        self.cache = Redis_DB.get_instance()

    def include(self, key:str, value:str) -> None:
        # Inclui no cache
        self.cache.set(key, value)
        print(f'Chave {key} salva no cache com sucesso.')

    def include_with_hash(self, value:dict) -> None:
        # Inclui no cache
        value['created_at'] = u.agora()
        key = u.hash_this(str(value))
        self.cache.set(key, str(value))
        print(f'Chave {key} salva no cache com sucesso.')
    
    def return_db(self,key:str) -> str:
        # Retorna do Cache
        if key in self.cache:
            str = self.cache.get(key)
        else:
            print(f'A Chave {key} não foi encontrada no cache')
            str = None
        return str

    def return_all(self) -> dict:
        response = {}
        i = 0
        for key in self.cache.keys():
            i+=1
            response[i] = self.cache.get(key)
        return response
        

    def delete(self, key:str) -> None:
        # Consulta Cache, se chave não for encontrada inclui no Redis
        self.cache.delete(key)
        response = f'Chave {key} deletada do cache com sucesso.'
        print(response)

    def reset_cache(self):
        for key in self.cache.keys():
            self.cache.delete(key)
        print('Cache resetado com sucesso')

if __name__ == '__main__':
    pass