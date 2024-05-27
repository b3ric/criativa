# Calcular gorjeta

Voce foi contratado(a) pelo melhor restaurante do Rio de Janeiro para consertar uma calculadora de gorjeta.

A calculadora atual do restaurante nao esta funcionando, segue abaixo o codigo atual:

```python
def main():
    conta = conta_em_float(input("Qual foi o valor da conta? "))
    porcentagem = porcentagem_em_float(input("Qual porcentagem da gorjeta? "))
    gorjeta = conta * porcentagem
    print(f"Valor da gorjeta: ${gorjeta:.2f}")


def conta_em_float(valor):
    # IMPLEMENTAR


def porcentagem_em_float(p):
    # IMPLEMENTAR


main()
```

Como podem ver, duas funcoes nao foram implementadas: `conta_em_decimal` e `porcentagem`.

- `conta_em_decimal`: deve aceitar uma `string` (texto) como input (formatada como `$##.##`). Remova o cifrao da string `$`, e retorne (`return`) o valor como decimal (`float`). Exemplo: um input de `$50.00` deve retornar `50.0`.
- `porcentagem_em_float`: deve aceitar uma `string` (texto) como input (formatado como `##%`). Remova o sinal de porcentagem `%`, e retorne a porcentagem como um decimal (`float`). Exemplo: um input de `15%` deve retornar `0.15`.

Pode-se presumir que os usuarios colocarao dados ja validados. 

## Demo

```
$ python3 gorjeta.py
Qual foi o valor da conta? $50.00
Qual a porcentagem da gorjeta? 15%
Valor da gorjeta: $7.50 
```

## Como testar

- Rode seu programa `python3 gorjeta.py`. Digite `$50.00` e pressione Enter. Depois, digite `15%` e pressione Enter. Seu programa deve imprimir: 
`Valor da gorjeta: $7.50`
- Rode seu programa `python3 gorjeta.py`. Digite `$100.00` e pressione Enter. Depois, digite `18%` e pressione Enter. Seu programa deve imprimir: 
`Valor da gorjeta: $18.00`
- Rode seu programa `python3 gorjeta.py`. Digite `$15.00` e pressione Enter. Depois, digite `25%` e pressione Enter. Seu programa deve imprimir: 
`Valor da gorjeta: $3.75`