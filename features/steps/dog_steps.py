import requests
from behave import given, then

BASE_URL = "https://dog.ceo/api"

@given('que eu consulto a lista de sub-raças da raça "{raca}"')
def step_list_sub_breeds(context, raca):
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/list")

@given('que eu consulto uma raça chamada "{raca}"')
def step_query_invalid_breed(context, raca):
    # Usando o endpoint de imagens para garantir o retorno de erro da API
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/images")

@then('o status code deve ser {code:d}')
def step_check_status_code(context, code):
    assert context.response.status_code == code

@then('a lista de sub-raças não deve estar vazia')
def step_check_sub_breeds_not_empty(context):
    data = context.response.json()
    assert len(data['message']) > 0

@then('a mensagem de erro deve ser "{mensagem}"')
def step_check_error_message(context, mensagem):
    data = context.response.json()
    # Pegamos a mensagem da API e removemos espaços extras para comparar
    mensagem_api = str(data.get('message', '')).strip()
    mensagem_esperada = mensagem.strip()
    
    assert mensagem_api == mensagem_esperada, f"Erro: Esperava '{mensagem_esperada}', mas a API retornou '{mensagem_api}'"
