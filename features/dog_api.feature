Funcionalidade: Validação da Dog API

Cenário: Listar sub-raças de um Terrier
    Dado que eu consulto a lista de sub-raças da raça "terrier"
    Então o status code deve ser 200
    E a lista de sub-raças não deve estar vazia

Cenário: Consultar raça inexistente
    Dado que eu consulto uma raça chamada "dragao"
    Então o status code deve ser 404
    E a mensagem de erro deve ser "Breed not found (master breed does not exist)"
