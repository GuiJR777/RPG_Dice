# Cria Banco de dados Redis e Cache
import redis
from core.utils import hash_this
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

    def include(self, key, value):
        # Inclui no cache
        self.cache.set(key, value)
        print(f'Chave {key} salva no cache com sucesso.')

    def include_with_hash(self, value):
        # Inclui no cache
        key = hash_this(str(value))
        self.cache.set(key, value)
        print(f'Chave {key} salva no cache com sucesso.')
    
    def return_db(self,key):
        # Retorna do Cache
        if key in self.cache:
            str = self.cache.get(key)
        else:
            print(f'A Chave {key} não foi encontrada no cache')
            str = None
        return str

    def delete(self, key):
        # Consulta Cache, se chave não for encontrada inclui no Redis
        self.cache.delete(key)
        response = f'Chave {key} deletada do cache com sucesso.'
        print(response)

    def reset_cache(self):
        self.cache.flushall()
        print('Cache resetado com sucesso')

if __name__ == '__main__':
    pass