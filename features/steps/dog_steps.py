import requests
from behave import given, then

BASE_URL = "https://dog.ceo/api"

@given('que eu consulto a lista de sub-raças da raça "{raca}"')
def step_list_sub_breeds(context, raca):
    # Endpoint para listar sub-raças
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/list")

@given('que eu consulto uma raça chamada "{raca}"')
def step_query_invalid_breed(context, raca):
    # Usamos o endpoint de imagens para validar o erro 404 de raça inexistente
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/images")

@then('o status code deve ser {code:d}')
def step_check_status_code(context, code):
    # O ':d' no decorator garante que o 'code' chegue como um número inteiro
    assert context.response.status_code == code

@then('a lista de sub-raças não deve estar vazia')
def step_check_sub_breeds_not_empty(context):
    data = context.response.json()
    # Verifica se a lista dentro da chave 'message' contém itens
    assert len(data['message']) > 0

@then('a mensagem de erro deve ser "{mensagem}"')
def step_check_error_message(context, mensagem):
    data = context.response.json()
    mensagem_api = data.get('message', '')
    # Comparação exata da mensagem retornada pela API
    assert mensagem_api == mensagem, f"Esperado: {mensagem} | Obtido: {mensagem_api}"
