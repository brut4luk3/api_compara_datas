# Bibliotecas importadas
from flask import Flask # Flask API, precisa ser importado via pip ou Python Packages (no Pycharm)
from flask import request, jsonify # Flask API, precisa ser importado via pip ou Python Packages (no Pycharm)
from datetime import datetime # Datetime, biblioteca nativa do Python

app = Flask(__name__) # --> Instância da aplicação Flask, obrigatório

@app.route('/api/compara_datas', methods=['POST']) # ROTA (endpoint) e Método (POST)

def compara_datas(): # Função principal do código, controla o campo "modo"
    dados = request.get_json() # Obrigatório, criará o body da API
    data1 = datetime.strptime(dados['data1'], '%d/%m/%Y').date() # strptime - Função do datetime que converte as strings data1 e data2 em formato "date"
    data2 = datetime.strptime(dados['data2'], '%d/%m/%Y').date()
    modo = dados['modo'] # Modo de operação da API, pode ser "diferenca" ou "comparacao"

    if modo == 'diferenca': # Faz o cálculo de dias entre as datas
        dias_entre_datas = abs((data1 - data2).days) # Função "abs" garante que o resulta sempre será positivo

        response = {
            'result': dias_entre_datas
        }

    elif modo == 'comparacao': # Usando a data1 como parâmetro, mostrará "1" para maior, "-1" para menor e "0" para igual
        if data1 > data2:
            maior_ou_menor = '1'
        elif data1 < data2:
            maior_ou_menor = '-1'
        else:
            maior_ou_menor = '0'

        response = {
            'result': maior_ou_menor
        }

    else: # Cenário de erro para o caso do usuário escrever algo errado no campo "modo".
        response = {
            'Erro': 'Modo de operação inválido! Modos aceitos: diferenca ou comparacao'
        }

    return jsonify(response) # Mostra o resultado da operação no retorno


if __name__ == '__main__': # Roda a aplicação
    app.run()