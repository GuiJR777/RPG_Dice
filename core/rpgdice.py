""" 
Created by: Guilherme J. Ramires
Github: https://github.com/GuiJR777
"""
from core.cache.redis import Cache
from core.utils import agora
from random import randint
import re

cache = Cache()

class  Dice():
    def __init__(self, number_of_sides:int = 6):
        """ 
        Define um dado com quantidade de lados escolhidos, se não definido define um D6. 
        """
        self.sides = int(number_of_sides)
        self.name = f'D{self.sides}'

    def get_result_in_line(self, plays:list, total_result:int) -> str:
        one_line = '[Dice]:'
        for play in plays:
            one_line+= f' [{play}] '
        one_line += f'-> {total_result}'
        
        return one_line

    def roll(self, amounts:int = 1) -> dict:
        """ 
        Rola dado definido com quantidade de dado passada no parametro,
        por padrão a quantidade é 1. 
        """
        total_result = 0
        plays = []
        for i in range(amounts):
            result = randint(1, self.sides)
            print(f'[Dice {i+1} - {self.name}] -> {result} ')
            plays.append(result)
            total_result+=result
        if amounts > 1:
            print(f'[Total  - {self.name}] -> {total_result} ')
        response = {
            'created_at' : agora(),
            'dice' : self.name,
            'one_line_result' : self.get_result_in_line(plays, total_result),
            'plays' : plays,
            'total' : total_result
        }
        cache.include_with_hash(response)

        return response

    def roll_by_text(self, text:str) -> dict:
        """ 
        Localiza no texto o padrão "roll[numero de dados]d[numero de lados]", 
        exemplo "roll2d20", e executa o comando.
        """
        pattern = r"(roll\d+d\d+)"
        matches = re.findall(pattern, text)
        if matches != []:
            comand = str(matches[0])
            comand = comand.replace('roll','').replace('d', ',')
            amounts, sides = comand.split(',')
            self.sides = int(sides)
            self.name = f'D{self.sides}'

            return self.roll(int(amounts))
        else:
            pass


if __name__ == '__main__':
    # Área de demonstrações
    dado = Dice()
    print(dado.name, dado.roll())
    print(dado.name, dado.roll(3))

    texto = 'Aqui vai ter um comando roll1d20 para rodar um d20'
    resultado = dado.roll_by_text(texto)
    print(dado.name) # O nome do dado mudou pois o ultimo utilizado foi o D20
    print(resultado['total']) #Acesso direto a soma dos resultados