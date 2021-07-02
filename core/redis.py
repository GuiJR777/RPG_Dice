# Cria Banco de dados Redis e Cache
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

    def include_with_hash(self, value:dict) -> None:
        # Inclui no cache
        value['created_at'] = u.agora()
        key = u.hash_this(str(value))
        self.cache.set(key, str(value))
    
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
            response[f'{i}'] = self.return_db(key)

        return response
        

    def delete(self, key:str) -> None:
        # Consulta Cache, se chave não for encontrada inclui no Redis
        self.cache.delete(key)

    def reset_cache(self):
        for key in self.cache.keys():
            self.cache.delete(key)

if __name__ == '__main__':
    pass