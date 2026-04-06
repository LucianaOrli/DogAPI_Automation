import requests
import re
from behave import given, when, then

BASE_URL = "https://dog.ceo/api"

@given('que eu acesso o endpoint de listagem de todas as raças')
def step_list_all(context):
    context.response = requests.get(f"{BASE_URL}/breeds/list/all")

@given('que eu busco as imagens da raça "{raca}"')
def step_list_images(context, raca):
    # Ajustado para buscar imagem aleatória da raça (conforme o .feature novo)
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/images/random")

@when('eu envio a requisição GET')
def step_send_get(context):
    # O Behave já executou o GET no Given, mas mantemos para compatibilidade do Gherkin
    pass

@given('que eu solicito uma imagem aleatória de qualquer cão')
def step_random_image(context):
    context.response = requests.get(f"{BASE_URL}/breeds/image/random")

@then('o código de status da resposta deve ser {status:d}')
def step_check_status(context, status):
    assert context.response.status_code == status

@then('o campo "{campo}" deve conter "{valor}"')
def step_check_field_value(context, campo, valor):
    data = context.response.json()
    assert data[campo] == valor, f"Esperava {valor}, mas veio {data[campo]}"

@then('a mensagem de erro deve ser "{msg}"')
def step_check_error_msg(context, msg):
    data = context.response.json()
    assert data["message"] == msg

@then('o corpo da resposta deve conter a lista de raças com status "success"')
def step_check_success(context):
    data = context.response.json()
    assert data["status"] == "success"

@then('a lista de imagens não deve estar vazia')
def step_check_images_not_empty(context):
    data = context.response.json()
    assert len(data["message"]) > 0

# --- CORREÇÃO DO PONTO 3 (SCHEMA, TIPAGEM E REGEX) ---
@then('o campo "message" deve conter uma URL de imagem válida (string e formato seguro)')
def step_check_url_schema(context):
    data = context.response.json()
    url = data["message"]
    
    # 1. Validação de Tipagem (Ponto 3)
    assert isinstance(url, str), "A URL deve ser uma string"
    
    # 2. Validação de Formato Seguro (Ponto 3)
    assert url.startswith("https://"), "A URL deve usar HTTPS"
    
    # 3. Validação de Extensão via REGEX (Ponto 3)
    padrao_imagem = r"\.(jpg|jpeg|png)$"
    assert re.search(padrao_imagem, url.lower()), f"URL {url} não possui formato de imagem válido"
