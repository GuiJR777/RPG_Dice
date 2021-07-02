""" 
Created by: Guilherme J. Ramires
Github: https:./github.com/GuiJR777
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
            plays.append(result)
            total_result+=result
      
        response = {
            'dice' : self.name,
            'one_line_result' : self.get_result_in_line(plays, total_result),
            'plays' : plays,
            'total' : total_result
        }

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

