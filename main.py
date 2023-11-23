from datetime import datetime
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# route -> site
# função -> o que você quer



app = flask.Flask("__name__")

# Rota para a página inicial
@app.route('/')
def homepage.html
    return render_template(homepage.html)


# Função auxiliar para calcular desconto de IRRF
def calcular_desconto_irrf(salario_dependente):
    if salario_dependente <= 2112.00:
        desconto = 0
    elif 2112.01 <= salario_dependente <= 2826.65:
        desconto = 0.075
    elif 2826.66 <= salario_dependente <= 3751.05:
        desconto = 0.15
    elif 3751.06 <= salario_dependente <= 4664.68:
        desconto = 0.225
    else:  # Acima de R$ 4.664.69
        desconto = 0.275
    return salario_dependente * desconto
assert isinstance(app.route, object)

# Função para calcular a rescisão
def calcular_rescisao(salario, data_inicio, data_final, motivo_rescisao, meses_ferias_vencidas, numero_dependentes):
    try:
        # Obter dados do formulário
        salario = float(request.form.get('salario', 0))
        data_inicio = request.form.get('dataInicio')
        data_final = request.form.get('dataFinal')
        motivo_rescisao = request.form.get('motivoRescisao')
        meses_ferias_vencidas = int(request.form.get('mesesFeriasVencidas', 0))
        numero_dependentes = int(request.form.get('numeroDependentes', 0))

        # Chamar a função calcular_rescisao
        resultado = calcular_rescisao(salario, data_inicio, data_final, motivo_rescisao, meses_ferias_vencidas, numero_dependentes)

        # Enviar o resultado
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"erro": str(e)})


# Rota para a página inicial

# Rota para calcular a rescisão
@app.route('/calcular_rescisao', methods=['POST'])
def calcular():
    try:
    # Obtenção de dados do formulário
        salario = float(request.form.get('salario', 0))
        data_inicio = request.form.get('dataInicio')
        data_final = request.form.get('dataFinal')
        motivo_rescisao = request.form.get('motivoRescisao')
        meses_ferias_vencidas = int(request.form.get('mesesFeriasVencidas', 0))
        numero_dependentes = int(request.form.get('numeroDependentes', 0))

    # Conversão das datas
        data_inicio_obj = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_final_obj = datetime.strptime(data_final, "%d/%m/%Y")

    # Cálculos comuns
        salario_dia = salario / 30
        salario_proporcional = salario_dia * data_final_obj.day
        ferias_vencidas = salario * meses_ferias_vencidas * 0.033
        salario_ferias = salario * 0.033
        ferias_proporcional = salario_ferias * data_final_obj.month
        total_meses = (data_final_obj.year - data_inicio_obj.year) * 12 + data_final_obj.month - data_inicio_obj.month
        decimo_terceiro_proporcional = salario * total_meses / 12
        percentual_fgts = 0.08
        fgts = salario * percentual_fgts * total_meses
        multa_fgts = fgts * 0.4  # A multa de 40% sobre o FGTS

    # Ajuste do salário com base no número de dependentes
        valor_por_dependente = 189.59
        salario_ajustado = salario - (numero_dependentes * valor_por_dependente)

    # Calculando o desconto do IRRF
        desconto_irrf = calcular_desconto_irrf(salario_ajustado)

    # Cálculo baseado no motivo da rescisão
        if motivo_rescisao == "pedido de demissão":
            total_rescisao = salario_proporcional + ferias_vencidas + ferias_proporcional + decimo_terceiro_proporcional
        elif motivo_rescisao == "demissão sem justa causa":
            total_rescisao = salario_proporcional + ferias_vencidas + ferias_proporcional + decimo_terceiro_proporcional + fgts + multa_fgts
        elif motivo_rescisao == "demissão com justa causa":
            total_rescisao = salario_proporcional + ferias_vencidas + ferias_proporcional
        elif motivo_rescisao == "término do contrato de trabalho":
            total_rescisao = salario_proporcional + ferias_proporcional + decimo_terceiro_proporcional
        else:
            return jsonify({"erro": "Motivo de rescisão inválido."})

        total_rescisao -= desconto_irrf  # Subtraindo o desconto do IRRF do total

    # Preparando os dados para a tabela
        dados_rescisao = {
        "Salário Proporcional": salario_proporcional,
        "Férias Vencidas": ferias_vencidas,
        "Férias Proporcionais": ferias_proporcional,
        "Décimo Terceiro Proporcional": decimo_terceiro_proporcional,
        "FGTS": fgts,
        "Multa FGTS": multa_fgts,
        "Desconto IRRF": desconto_irrf,
        "Total Rescisão": total_rescisao
    }

    # Criando um DataFrame com os dados
        df_rescisao = pd.DataFrame(dados_rescisao)

    # Convertendo o DataFrame para JSON
        return jsonify(df_rescisao.to_dict('records'))
    except Exception as e:
        return jsonify({"erro": str(e)})

    # Preparando os dados para a tabela
        dados_rescisao = {
        "Salário Proporcional": salario_proporcional,
        "Férias Vencidas": ferias_vencidas,
        "Férias Proporcionais": ferias_proporcional,
        "Décimo Terceiro Proporcional": decimo_terceiro_proporcional,
        "FGTS": fgts,
        "Multa FGTS": multa_fgts,
        "Desconto INSS": calcular_desconto_irrf(salario_ajustado),
        "Total Rescisão": total_rescisao
    }
    # Criando um DataFrame com os dados
        df_rescisao = pd.DataFrame(dados_rescisao)

    # Convertendo o DataFrame para JSON
        return jsonify(df_rescisao.to_dict('records'))
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

    #servidor heroku
