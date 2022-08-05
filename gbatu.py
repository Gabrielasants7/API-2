
from urllib import request
import pandas as pd
import numpy as np
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
app_infos = dict(version='0.1', title='API - Teste Gabi')

rest_app = Api(app, **app_infos)
# codigo-fonte
def pegarVendas():
  df = pd.read_csv('C:/Users/Marztec Tecnologia/Desktop/API/vendas.csv')
  total_vendas = df['Vendas'].sum()
  resposta = {'total_vendas':total_vendas}

  return(resposta)

db_model = rest_app.model('Vendas', 
	{'array': fields.List(cls_or_instance= fields.String ,required = True, 
					 description="Essa API trás a soma do total de vendas", 
					 help="Ex. 1,9,8")})

# Construindo os endpoints
nome_do_endpoint = rest_app.namespace('teste_get', description='Teste GET')
@nome_do_endpoint.route('/pegarVendas')

class test(Resource):
  @rest_app.expect()
  def get(self):
    retorno = pegarVendas()
    return(retorno, 200)

@nome_do_endpoint.route('/teste_POST')
class test_post(Resource):
  @rest_app.expect(db_model)
  def post(self):
    array = request.json['array']
    retorno = array
    return(retorno, 200)


#Rodando a api
if __name__ == "__main__":
    debug = True
    app.run(host = '0.0.0.0', port = 5005, debug = debug)
  