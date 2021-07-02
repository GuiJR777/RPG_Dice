## RPG Dice

Uma simples classe que imita o comportamento de dados de RPG, podendo ser utilizado para lançar um ou mais dados do tipo **D4**, **D6**, **D8**, **D10**, **D12**, **D20** e **D100** ou outros tipos de dados que o usuario quiser.

### Como Funciona:

A classe pode ser atribuida a uma variavel para que o dado seja lançado mais de uma vez com o método **_roll_**, tambem se pode definir o número de lados que o dado terá no construtor da classe. As informações do dado podem ser acessadas nos parâmetros **_sides_**: Quantidade de lados do dado e **_name_**: Nome do dado.
_Exemplo_:

```python
d20 = Dice(20) # Cria um dado chamdo D20 de 20 lados.
d20.roll() # Rola 1 vez.
d20.roll(3) # Rola 3 vezes.
```

O retorno de **_roll_** será um dicionário python contendo uma lista das jogadas na chave "plays" e a soma dos dados na chave "result".

Tambem é possivel passar um texto contendo uma instrução de rolagem no seguinte padrão "roll"+"numero de dados"+"d"+"numero de lados dos dados" para o método **_roll_by_text_** que definirá então o dado a ser usado e rolará a quantidade de vezes que foi solicitado.
_Exemplo_:

```python
texto = 'O comando roll2d20 ira solicitar a rolagem de 2 dados D20'
dado = Dice()
dado.roll_by_text(texto)
```

O retorno de **_roll_by_text_** será um dicionário python contendo uma lista das jogadas na chave "plays" e a soma dos dados na chave "result". O método alterará os parâmetros **_name_** e **_sides_** para o valor do dado solicitado no texto.

Sugiro utilizar diferentes váriaveis para diferentes dados e um geral para executar os textos.
_Exemplo_:

```python
d10 = Dice(10)
d20 = Dice(20)
d100 = Dice(100)
dado = Dice()
```

### API:

A classe pode ser usada atravéz de uma simples API **Flask**
Por favor, use os EndPoints:

- **/dice/text/{ _your text hear_ }** método GET para usar a partir do comando "roll {n} d {n}".
- **/dice/text/** método POST para enviar um comando "roll {n} d {n}" em um objeto JSON na chave "text".
- **/dice/{ _número de lados do dado desejado_ }/{ _quantidade de dados desejados_ }** para usar um dado específico.

Essa classe será utilizada futuramente em projetos que envolvem RPG, fique a vontade para utiliza-lá em seus projetos também.

![Lets Do It!!](https://media1.tenor.com/images/d8d7b003cc98b44d2a4ca87e27f0c304/tenor.gif "Lets Do It!!")
