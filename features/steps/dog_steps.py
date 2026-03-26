import requests
from behave import given, then

BASE_URL = "https://dog.ceo/api"

@given('que eu acesso o endpoint de listagem de todas as raças')
def step_list_all(context):
    context.response = requests.get(f"{BASE_URL}/breeds/list/all")

@given('que eu busco as imagens da raça "{raca}"')
def step_list_images(context, raca):
    context.response = requests.get(f"{BASE_URL}/breed/{raca}/images")

@given('que eu solicito uma imagem aleatória de qualquer cão')
def step_random_image(context):
    context.response = requests.get(f"{BASE_URL}/breeds/image/random")

@then('o código de status da resposta deve ser 200')
def step_check_status(context):
    assert context.response.status_code == 200

@then('o corpo da resposta deve conter a lista de raças com status "success"')
def step_check_success(context):
    data = context.response.json()
    assert data["status"] == "success"

@then('a lista de imagens não deve estar vazia')
def step_check_images_not_empty(context):
    data = context.response.json()
    assert len(data["message"]) > 0

@then('o campo "message" deve conter uma URL válida de imagem')
def step_check_url(context):
    data = context.response.json()
    assert "https://" in data["message"]
