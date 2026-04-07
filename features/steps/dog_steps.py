@then('a mensagem de erro deve ser "{mensagem}"')
def step_check_error_message(context, mensagem):
    data = context.response.json()
    # Usamos o .strip() para evitar erros com espaços invisíveis
    mensagem_api = data.get('message', '').strip()
    mensagem_esperada = mensagem.strip()
    
    assert mensagem_api == mensagem_esperada, \
        f"Esperado: {mensagem_esperada} | Obtido: {mensagem_api}"
