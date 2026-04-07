import requests
from behave import given, then

BASE_URL = "https://dog.ceo/api"

@given('que eu consulto a lista de sub-raças da raça "{raca}"')
def step_list_sub_breeds(context, raca):
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/list")

@given('que eu consulto uma raça chamada "{raca}"')
def step_query_invalid_breed(context, raca):
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/images")

@then('o status code deve ser {code:d}')
def step_check_status_code(context, code):
    assert context.response.status_code == code

@then('a lista de sub-raças não deve estar vazia')
def step_check_sub_breeds_not_empty(context):
    try:
        data = context.response.json()
        sub_breeds = data.get('message', [])
        assert isinstance(sub_breeds, list), "O retorno não é uma lista"
        assert len(sub_breeds) > 0, "A lista de sub-raças está vazia"
    except (ValueError, KeyError):
        assert False, "A API não retornou um JSON válido"

@then('a mensagem de erro deve ser "{mensagem}"')
def step_check_error_message(context, mensagem):
    data = context.response.json()
    mensagem_api = data.get('message', '')
    assert mensagem_api == mensagem, f"Esperado: {mensagem} | Obtido: {mensagem_api}"
