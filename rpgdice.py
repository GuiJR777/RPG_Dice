""" 
Created by: Guilherme J. Ramires
Github: https://github.com/GuiJR777
"""
from random import randint
import re

class  Dice():
    def __init__(self, number_of_sides:int = 6):
        """ 
        Define um dado com quantidade de lados escolhidos, se não definido define um D6. 
        """
        self.sides = int(number_of_sides)
        self.name = f'D{self.sides}'

    def roll(self, amounts:int = 1) -> dict:
        """ 
        Rola dado definido com quantidade de dado passada no parametro,
        por padrão a quantidade é 1. 
        """
        total_result = 0
        results = []
        for i in range(amounts):
            result = randint(1, self.sides)
            print(f'[Dice {i+1} - {self.name}] -> {result} ')
            results.append(result)
            total_result+=result
        if amounts > 1:
            print(f'[Total  - {self.name}] -> {total_result} ')

        return {
            'dice' : self.name,
            'plays' : results,
            'total' : total_result
        }

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